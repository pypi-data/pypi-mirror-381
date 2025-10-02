"""
Attention tracking using eye aspect ratio and head pose
"""
import cv2
import mediapipe as mp
import numpy as np
from collections import deque
from datetime import datetime
import pandas as pd
from camera_master.utils import (
    calculate_eye_aspect_ratio, draw_text_with_background,
    get_reports_dir, VideoStreamHandler
)


class AttentionTracker:
    """
    Track attention and engagement using eye tracking and head pose
    """
    
    def __init__(self, ear_threshold=0.25, attention_threshold=0.5):
        """
        Initialize Attention Tracker
        
        Args:
            ear_threshold: Eye aspect ratio threshold for drowsiness
            attention_threshold: Attention score threshold
        """
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing = mp.solutions.drawing_utils
        
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        self.ear_threshold = ear_threshold
        self.attention_threshold = attention_threshold
        
        # Eye landmarks indices
        self.left_eye_indices = [33, 160, 158, 133, 153, 144]
        self.right_eye_indices = [362, 385, 387, 263, 373, 380]
        
        # Tracking history
        self.attention_history = deque(maxlen=100)
        self.session_data = []
        
        self.reports_dir = get_reports_dir()
    
    def calculate_ear(self, eye_landmarks):
        """
        Calculate Eye Aspect Ratio
        
        Args:
            eye_landmarks: Eye landmark coordinates
            
        Returns:
            float: EAR value
        """
        if len(eye_landmarks) < 6:
            return 0.0
        
        # Vertical distances
        v1 = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
        v2 = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
        
        # Horizontal distance
        h = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
        
        if h == 0:
            return 0.0
        
        ear = (v1 + v2) / (2.0 * h)
        return ear
    
    def estimate_head_pose(self, landmarks, frame_shape):
        """
        Estimate head pose angles
        
        Args:
            landmarks: Face landmarks
            frame_shape: Frame dimensions
            
        Returns:
            tuple: (pitch, yaw, roll) angles in degrees
        """
        h, w = frame_shape[:2]
        
        # 3D model points
        model_points = np.array([
            (0.0, 0.0, 0.0),             # Nose tip
            (0.0, -330.0, -65.0),        # Chin
            (-225.0, 170.0, -135.0),     # Left eye left corner
            (225.0, 170.0, -135.0),      # Right eye right corner
            (-150.0, -150.0, -125.0),    # Left mouth corner
            (150.0, -150.0, -125.0)      # Right mouth corner
        ])
        
        # 2D image points
        image_points = np.array([
            (landmarks[1].x * w, landmarks[1].y * h),      # Nose tip
            (landmarks[152].x * w, landmarks[152].y * h),  # Chin
            (landmarks[33].x * w, landmarks[33].y * h),    # Left eye
            (landmarks[263].x * w, landmarks[263].y * h),  # Right eye
            (landmarks[61].x * w, landmarks[61].y * h),    # Left mouth
            (landmarks[291].x * w, landmarks[291].y * h)   # Right mouth
        ], dtype="double")
        
        # Camera internals
        focal_length = w
        center = (w / 2, h / 2)
        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ], dtype="double")
        
        dist_coeffs = np.zeros((4, 1))
        
        # Solve PnP
        success, rotation_vector, translation_vector = cv2.solvePnP(
            model_points, image_points, camera_matrix, dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE
        )
        
        # Convert rotation vector to rotation matrix
        rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
        
        # Calculate Euler angles
        sy = np.sqrt(rotation_matrix[0, 0]**2 + rotation_matrix[1, 0]**2)
        
        singular = sy < 1e-6
        
        if not singular:
            pitch = np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2])
            yaw = np.arctan2(-rotation_matrix[2, 0], sy)
            roll = np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
        else:
            pitch = np.arctan2(-rotation_matrix[1, 2], rotation_matrix[1, 1])
            yaw = np.arctan2(-rotation_matrix[2, 0], sy)
            roll = 0
        
        # Convert to degrees
        pitch = np.degrees(pitch)
        yaw = np.degrees(yaw)
        roll = np.degrees(roll)
        
        return pitch, yaw, roll
    
    def calculate_attention_score(self, ear, pitch, yaw, roll):
        """
        Calculate attention score based on eye openness and head pose
        
        Args:
            ear: Eye aspect ratio
            pitch: Head pitch angle
            yaw: Head yaw angle
            roll: Head roll angle
            
        Returns:
            float: Attention score (0-1)
        """
        # Eye openness score (0-1)
        eye_score = min(ear / 0.3, 1.0) if ear > self.ear_threshold else 0.0
        
        # Head pose score (0-1)
        # Good attention: looking straight (yaw ~0, pitch ~0)
        yaw_score = max(0, 1 - abs(yaw) / 30)  # Penalize turning head
        pitch_score = max(0, 1 - abs(pitch) / 20)  # Penalize looking up/down
        
        head_pose_score = (yaw_score + pitch_score) / 2
        
        # Combined attention score
        attention_score = (eye_score * 0.6 + head_pose_score * 0.4)
        
        return attention_score
    
    def process_frame(self, frame):
        """
        Process frame and calculate attention metrics
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, attention_data)
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        attention_data = None
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                
                # Extract eye landmarks
                left_eye = np.array([
                    [face_landmarks.landmark[i].x * w,
                     face_landmarks.landmark[i].y * h]
                    for i in self.left_eye_indices
                ])
                
                right_eye = np.array([
                    [face_landmarks.landmark[i].x * w,
                     face_landmarks.landmark[i].y * h]
                    for i in self.right_eye_indices
                ])
                
                # Calculate EAR
                left_ear = self.calculate_ear(left_eye)
                right_ear = self.calculate_ear(right_eye)
                avg_ear = (left_ear + right_ear) / 2
                
                # Estimate head pose
                pitch, yaw, roll = self.estimate_head_pose(
                    face_landmarks.landmark, frame.shape
                )
                
                # Calculate attention score
                attention_score = self.calculate_attention_score(
                    avg_ear, pitch, yaw, roll
                )
                
                # Determine status
                is_attentive = attention_score >= self.attention_threshold
                is_drowsy = avg_ear < self.ear_threshold
                
                attention_data = {
                    'timestamp': datetime.now(),
                    'eye_aspect_ratio': avg_ear,
                    'pitch': pitch,
                    'yaw': yaw,
                    'roll': roll,
                    'attention_score': attention_score,
                    'is_attentive': is_attentive,
                    'is_drowsy': is_drowsy
                }
                
                # Store in history
                self.attention_history.append(attention_data)
                self.session_data.append(attention_data)
                
                # Draw visualization
                # Attention status
                status_color = (0, 255, 0) if is_attentive else (0, 0, 255)
                status_text = "Attentive" if is_attentive else "Distracted"
                
                if is_drowsy:
                    status_text = "Drowsy"
                    status_color = (0, 165, 255)
                
                draw_text_with_background(frame, status_text, (10, 30),
                                         font_scale=0.8, bg_color=status_color)
                
                # Display metrics
                y_pos = 70
                metrics = [
                    f"Attention: {attention_score:.2f}",
                    f"EAR: {avg_ear:.2f}",
                    f"Yaw: {yaw:.1f}°",
                    f"Pitch: {pitch:.1f}°"
                ]
                
                for metric in metrics:
                    cv2.putText(frame, metric, (10, y_pos),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    y_pos += 25
        
        return frame, attention_data
    
    def track_attention_frame(self, frame):
        """
        Track attention for a single frame (for CameraManager integration)
        
        Args:
            frame: Input frame
            
        Returns:
            dict: Attention data
        """
        _, attention_data = self.process_frame(frame)
        return attention_data
    
    def start_tracking(self, camera_index=0, callback=None):
        """
        Start real-time attention tracking
        
        Args:
            camera_index: Camera index
            callback: Callback function for attention events
        """
        print("Starting attention tracking. Press 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, attention_data = self.process_frame(frame)
                
                # Call callback if provided
                if callback and attention_data:
                    callback(attention_data)
                
                cv2.imshow('Attention Tracking', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    def get_attention_report(self):
        """
        Get attention tracking report as DataFrame
        
        Returns:
            pd.DataFrame: Attention records
        """
        if not self.session_data:
            return pd.DataFrame()
        
        df = pd.DataFrame(self.session_data)
        return df
    
    def get_statistics(self):
        """
        Get attention statistics
        
        Returns:
            dict: Statistics
        """
        if not self.session_data:
            return {
                'average_attention': 0,
                'attention_rate': 0,
                'drowsiness_rate': 0
            }
        
        df = pd.DataFrame(self.session_data)
        
        return {
            'average_attention': df['attention_score'].mean(),
            'attention_rate': (df['is_attentive'].sum() / len(df) * 100),
            'drowsiness_rate': (df['is_drowsy'].sum() / len(df) * 100),
            'total_measurements': len(df)
        }
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()
