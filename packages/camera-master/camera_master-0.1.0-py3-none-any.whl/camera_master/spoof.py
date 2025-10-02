"""
Spoof detection using blink detection and liveness checks
"""
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from collections import deque
from datetime import datetime
from camera_master.utils import draw_text_with_background, VideoStreamHandler


class SpoofDetector:
    """
    Detect spoofing attempts using liveness detection (blink detection)
    """
    
    def __init__(self, ear_blink_threshold=0.21, blink_consec_frames=3,
                 liveness_check_duration=5):
        """
        Initialize Spoof Detector
        
        Args:
            ear_blink_threshold: EAR threshold for blink detection
            blink_consec_frames: Consecutive frames for blink
            liveness_check_duration: Duration for liveness check (seconds)
        """
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        
        self.ear_blink_threshold = ear_blink_threshold
        self.blink_consec_frames = blink_consec_frames
        self.liveness_check_duration = liveness_check_duration
        
        # Eye landmarks
        self.left_eye_indices = [33, 160, 158, 133, 153, 144]
        self.right_eye_indices = [362, 385, 387, 263, 373, 380]
        
        # Blink detection
        self.blink_counter = 0
        self.total_blinks = 0
        self.blink_history = deque(maxlen=100)
        
        # Liveness check
        self.liveness_start_time = None
        self.liveness_blinks_required = 2
        self.liveness_blinks_detected = 0
        self.is_live = False
    
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
    
    def detect_blink(self, frame):
        """
        Detect eye blinks
        
        Args:
            frame: Input image frame
            
        Returns:
            dict: Blink detection results
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)
        
        blink_data = {
            'timestamp': datetime.now(),
            'ear': 0.0,
            'blink_detected': False,
            'total_blinks': self.total_blinks
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
                
                # Blink detection
                if avg_ear < self.ear_blink_threshold:
                    self.blink_counter += 1
                else:
                    if self.blink_counter >= self.blink_consec_frames:
                        self.total_blinks += 1
                        blink_data['blink_detected'] = True
                        self.blink_history.append(datetime.now())
                        
                        # Update liveness check
                        if self.liveness_start_time is not None:
                            self.liveness_blinks_detected += 1
                    
                    self.blink_counter = 0
                
                blink_data.update({
                    'ear': avg_ear,
                    'total_blinks': self.total_blinks
                })
        
        return blink_data
    
    def start_liveness_check(self):
        """Start a new liveness check"""
        self.liveness_start_time = datetime.now()
        self.liveness_blinks_detected = 0
        self.is_live = False
        print("Liveness check started. Please blink naturally.")
    
    def check_liveness(self):
        """
        Check if liveness test is passed
        
        Returns:
            tuple: (is_complete, is_live, message)
        """
        if self.liveness_start_time is None:
            return False, False, "Liveness check not started"
        
        elapsed = (datetime.now() - self.liveness_start_time).seconds
        
        if elapsed >= self.liveness_check_duration:
            # Check passed
            if self.liveness_blinks_detected >= self.liveness_blinks_required:
                self.is_live = True
                message = f"LIVE - {self.liveness_blinks_detected} blinks detected"
            else:
                self.is_live = False
                message = f"SPOOF DETECTED - Only {self.liveness_blinks_detected} blinks"
            
            return True, self.is_live, message
        
        # Still checking
        remaining = self.liveness_check_duration - elapsed
        message = f"Checking... {self.liveness_blinks_detected}/{self.liveness_blinks_required} blinks ({remaining}s left)"
        return False, False, message
    
    def process_frame(self, frame):
        """
        Process frame for spoof detection
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, blink_data)
        """
        blink_data = self.detect_blink(frame)
        
        # Display blink information
        blink_text = f"Blinks: {self.total_blinks}"
        ear_text = f"EAR: {blink_data['ear']:.3f}"
        
        cv2.putText(frame, blink_text, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, ear_text, (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        # Show blink indicator
        if blink_data['blink_detected']:
            cv2.circle(frame, (frame.shape[1] - 50, 30), 20, (0, 255, 0), -1)
            cv2.putText(frame, "BLINK", (frame.shape[1] - 80, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Liveness check display
        if self.liveness_start_time is not None:
            is_complete, is_live, message = self.check_liveness()
            
            if is_complete:
                color = (0, 255, 0) if is_live else (0, 0, 255)
                draw_text_with_background(frame, message, (10, 100),
                                         font_scale=0.8, bg_color=color)
            else:
                draw_text_with_background(frame, message, (10, 100),
                                         font_scale=0.7, bg_color=(0, 165, 255))
        
        return frame, blink_data
    
    def detect_frame(self, frame):
        """
        Detect spoof for a single frame (for CameraManager integration)
        
        Args:
            frame: Input frame
            
        Returns:
            dict: Spoof detection result
        """
        blink_data = self.detect_blink(frame)
        if blink_data['face_detected']:
            is_complete, is_live, message = self.check_liveness()
            return {
                'status': 'live' if is_live else 'checking',
                'blink_detected': blink_data['blink_detected'],
                'total_blinks': self.total_blinks,
                'ear': blink_data['ear'],
                'is_live': is_live if is_complete else None,
                'message': message
            }
        return {'status': 'no_face', 'blink_detected': False, 'total_blinks': 0, 'ear': 0.0, 'is_live': None, 'message': 'No face detected'}
    
    def start_detection(self, camera_index=0, auto_liveness_check=False):
        """
        Start real-time spoof detection
        
        Args:
            camera_index: Camera index
            auto_liveness_check: Automatically start liveness checks
        """
        print("Starting spoof detection. Press 'l' for liveness check, 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            if auto_liveness_check:
                self.start_liveness_check()
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, blink_data = self.process_frame(frame)
                
                # Check if liveness test is complete
                if self.liveness_start_time is not None:
                    is_complete, is_live, message = self.check_liveness()
                    if is_complete and auto_liveness_check:
                        # Restart liveness check
                        self.start_liveness_check()
                
                cv2.imshow('Spoof Detection', processed_frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('l'):
                    self.start_liveness_check()
    
    def get_blink_rate(self, window_seconds=60):
        """
        Calculate blink rate (blinks per minute)
        
        Args:
            window_seconds: Time window in seconds
            
        Returns:
            float: Blinks per minute
        """
        if not self.blink_history:
            return 0.0
        
        # Get blinks in recent window
        cutoff_time = datetime.now() - pd.Timedelta(seconds=window_seconds)
        recent_blinks = [t for t in self.blink_history if t > cutoff_time]
        
        if not recent_blinks:
            return 0.0
        
        # Calculate rate
        blinks_per_minute = len(recent_blinks) / (window_seconds / 60)
        return blinks_per_minute
    
    def is_blink_rate_normal(self):
        """
        Check if blink rate is within normal human range (10-20 bpm)
        
        Returns:
            bool: True if blink rate is normal
        """
        rate = self.get_blink_rate()
        return 10 <= rate <= 30  # Slightly wider range to account for variations
    
    def get_statistics(self):
        """Get spoof detection statistics"""
        return {
            'total_blinks': self.total_blinks,
            'blink_rate_bpm': self.get_blink_rate(),
            'is_blink_rate_normal': self.is_blink_rate_normal(),
            'liveness_status': 'Live' if self.is_live else 'Unknown',
            'recent_blinks': len(self.blink_history)
        }
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()
