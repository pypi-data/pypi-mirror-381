"""
Fatigue detection using eye aspect ratio and yawning detection
"""
import cv2
import mediapipe as mp
import numpy as np
from collections import deque
from datetime import datetime
import pandas as pd
from camera_master.utils import draw_text_with_background, VideoStreamHandler, get_reports_dir


class FatigueDetector:
    """
    Detect fatigue and drowsiness using eye closure and yawning
    """
    
    def __init__(self, ear_threshold=0.25, ear_consec_frames=20,
                 mar_threshold=0.6, yawn_consec_frames=15):
        """
        Initialize Fatigue Detector
        
        Args:
            ear_threshold: Eye aspect ratio threshold
            ear_consec_frames: Consecutive frames for drowsiness alert
            mar_threshold: Mouth aspect ratio threshold for yawning
            yawn_consec_frames: Consecutive frames for yawn detection
        """
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        self.ear_threshold = ear_threshold
        self.ear_consec_frames = ear_consec_frames
        self.mar_threshold = mar_threshold
        self.yawn_consec_frames = yawn_consec_frames
        
        # Eye landmarks
        self.left_eye_indices = [33, 160, 158, 133, 153, 144]
        self.right_eye_indices = [362, 385, 387, 263, 373, 380]
        
        # Mouth landmarks
        self.mouth_indices = [61, 291, 0, 17, 269, 405]
        
        # Counters
        self.ear_counter = 0
        self.yawn_counter = 0
        self.total_drowsy_events = 0
        self.total_yawns = 0
        
        # History
        self.fatigue_history = deque(maxlen=100)
        self.session_data = []
        self.reports_dir = get_reports_dir()
    
    def calculate_ear(self, eye_landmarks):
        """Calculate Eye Aspect Ratio"""
        if len(eye_landmarks) < 6:
            return 0.0
        
        v1 = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
        v2 = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
        h = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
        
        if h == 0:
            return 0.0
        
        return (v1 + v2) / (2.0 * h)
    
    def calculate_mar(self, mouth_landmarks):
        """
        Calculate Mouth Aspect Ratio for yawn detection
        
        Args:
            mouth_landmarks: Mouth landmark coordinates
            
        Returns:
            float: MAR value
        """
        if len(mouth_landmarks) < 6:
            return 0.0
        
        # Vertical distances
        v1 = np.linalg.norm(mouth_landmarks[1] - mouth_landmarks[5])
        v2 = np.linalg.norm(mouth_landmarks[2] - mouth_landmarks[4])
        
        # Horizontal distance
        h = np.linalg.norm(mouth_landmarks[0] - mouth_landmarks[3])
        
        if h == 0:
            return 0.0
        
        return (v1 + v2) / (2.0 * h)
    
    def detect_fatigue(self, frame):
        """
        Detect fatigue indicators
        
        Args:
            frame: Input image frame
            
        Returns:
            dict: Fatigue detection results
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        fatigue_data = {
            'timestamp': datetime.now(),
            'ear': 0.0,
            'mar': 0.0,
            'is_drowsy': False,
            'is_yawning': False,
            'fatigue_level': 'Normal'
        }
        
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
                
                # Extract mouth landmarks
                mouth = np.array([
                    [face_landmarks.landmark[i].x * w,
                     face_landmarks.landmark[i].y * h]
                    for i in self.mouth_indices
                ])
                
                # Calculate MAR
                mar = self.calculate_mar(mouth)
                
                # Check for drowsiness
                if avg_ear < self.ear_threshold:
                    self.ear_counter += 1
                else:
                    if self.ear_counter >= self.ear_consec_frames:
                        self.total_drowsy_events += 1
                    self.ear_counter = 0
                
                is_drowsy = self.ear_counter >= self.ear_consec_frames
                
                # Check for yawning
                if mar > self.mar_threshold:
                    self.yawn_counter += 1
                else:
                    if self.yawn_counter >= self.yawn_consec_frames:
                        self.total_yawns += 1
                    self.yawn_counter = 0
                
                is_yawning = self.yawn_counter >= self.yawn_consec_frames
                
                # Determine fatigue level
                fatigue_level = 'Normal'
                if is_drowsy and is_yawning:
                    fatigue_level = 'Critical'
                elif is_drowsy or is_yawning:
                    fatigue_level = 'Warning'
                elif avg_ear < self.ear_threshold * 1.2:
                    fatigue_level = 'Mild'
                
                fatigue_data.update({
                    'ear': avg_ear,
                    'mar': mar,
                    'is_drowsy': is_drowsy,
                    'is_yawning': is_yawning,
                    'fatigue_level': fatigue_level
                })
        
        self.fatigue_history.append(fatigue_data)
        self.session_data.append(fatigue_data)
        
        return fatigue_data
    
    def process_frame(self, frame):
        """
        Process frame and detect fatigue
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, fatigue_data)
        """
        fatigue_data = self.detect_fatigue(frame)
        
        # Draw visualization
        fatigue_level = fatigue_data['fatigue_level']
        
        # Color coding
        colors = {
            'Normal': (0, 255, 0),
            'Mild': (0, 255, 255),
            'Warning': (0, 165, 255),
            'Critical': (0, 0, 255)
        }
        
        color = colors.get(fatigue_level, (255, 255, 255))
        
        # Main status
        status_text = f"Fatigue: {fatigue_level}"
        draw_text_with_background(frame, status_text, (10, 30),
                                 font_scale=0.8, bg_color=color)
        
        # Detailed info
        y_pos = 70
        info = [
            f"EAR: {fatigue_data['ear']:.3f} ({'LOW' if fatigue_data['ear'] < self.ear_threshold else 'OK'})",
            f"MAR: {fatigue_data['mar']:.3f}",
            f"Drowsy: {'YES' if fatigue_data['is_drowsy'] else 'NO'}",
            f"Yawning: {'YES' if fatigue_data['is_yawning'] else 'NO'}"
        ]
        
        for text in info:
            cv2.putText(frame, text, (10, y_pos),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            y_pos += 25
        
        # Statistics
        stats_text = f"Drowsy Events: {self.total_drowsy_events} | Yawns: {self.total_yawns}"
        cv2.putText(frame, stats_text, (10, frame.shape[0] - 20),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        
        # Alert for critical fatigue
        if fatigue_level == 'Critical':
            alert_text = "!!! TAKE A BREAK !!!"
            text_size = cv2.getTextSize(alert_text, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)[0]
            x_center = (frame.shape[1] - text_size[0]) // 2
            draw_text_with_background(frame, alert_text, (x_center, frame.shape[0] - 60),
                                     font_scale=1.2, font_thickness=3,
                                     bg_color=(0, 0, 255), text_color=(255, 255, 255))
        
        return frame, fatigue_data
    
    def detect_fatigue_frame(self, frame):
        """
        Detect fatigue for a single frame (for CameraManager integration)
        
        Args:
            frame: Input frame
            
        Returns:
            dict: Fatigue data
        """
        fatigue_data = self.detect_fatigue(frame)
        return fatigue_data
    
    def start_detection(self, camera_index=0, callback=None):
        """
        Start real-time fatigue detection
        
        Args:
            camera_index: Camera index
            callback: Callback function for fatigue events
        """
        print("Starting fatigue detection. Press 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, fatigue_data = self.process_frame(frame)
                
                # Call callback if provided
                if callback:
                    callback(fatigue_data)
                
                cv2.imshow('Fatigue Detection', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    def get_fatigue_report(self):
        """Get fatigue report as DataFrame"""
        if not self.session_data:
            return pd.DataFrame()
        
        return pd.DataFrame(self.session_data)
    
    def get_statistics(self):
        """Get fatigue statistics"""
        if not self.session_data:
            return {
                'total_drowsy_events': 0,
                'total_yawns': 0,
                'average_ear': 0,
                'fatigue_risk': 'Low'
            }
        
        df = pd.DataFrame(self.session_data)
        
        # Calculate risk level
        critical_count = len(df[df['fatigue_level'] == 'Critical'])
        warning_count = len(df[df['fatigue_level'] == 'Warning'])
        
        if critical_count > len(df) * 0.1:
            risk = 'High'
        elif warning_count > len(df) * 0.2:
            risk = 'Medium'
        else:
            risk = 'Low'
        
        return {
            'total_drowsy_events': self.total_drowsy_events,
            'total_yawns': self.total_yawns,
            'average_ear': df['ear'].mean(),
            'average_mar': df['mar'].mean(),
            'fatigue_risk': risk,
            'critical_moments': critical_count,
            'warning_moments': warning_count
        }
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()
