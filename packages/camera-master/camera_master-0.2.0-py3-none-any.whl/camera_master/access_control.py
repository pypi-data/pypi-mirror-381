"""
Face-based access control system
"""
import cv2
from pathlib import Path
from datetime import datetime
from deepface import DeepFace
import json
import pandas as pd
from camera_master.utils import (
    get_data_dir, draw_text_with_background, VideoStreamHandler, save_json, load_json
)


class AccessControl:
    """
    Face-based access control with authorization levels
    """
    
    def __init__(self, model_name="VGG-Face", detector_backend="opencv",
                 distance_metric="cosine", threshold=0.5):
        """
        Initialize Access Control
        
        Args:
            model_name: Face recognition model
            detector_backend: Face detection backend
            distance_metric: Distance metric
            threshold: Recognition threshold
        """
        self.model_name = model_name
        self.detector_backend = detector_backend
        self.distance_metric = distance_metric
        self.threshold = threshold
        
        self.data_dir = get_data_dir()
        self.authorized_dir = self.data_dir / "authorized_users"
        self.authorized_dir.mkdir(exist_ok=True)
        
        self.access_log_file = self.data_dir / "access_log.json"
        self.users_db_file = self.data_dir / "users_database.json"
        
        self.users_db = self._load_users_db()
        self.access_log = self._load_access_log()
    
    def _load_users_db(self):
        """Load users database"""
        return load_json(self.users_db_file)
    
    def _save_users_db(self):
        """Save users database"""
        save_json(self.users_db, self.users_db_file)
    
    def _load_access_log(self):
        """Load access log"""
        data = load_json(self.access_log_file)
        return data.get('log', [])
    
    def _save_access_log(self):
        """Save access log"""
        save_json({'log': self.access_log}, self.access_log_file)
    
    def register_user(self, name, role="user", access_level=1, image=None, camera_index=0):
        """
        Register authorized user
        
        Args:
            name: User name
            role: User role (admin, teacher, student, etc.)
            access_level: Access level (1-5)
            image: Face image or None to capture
            camera_index: Camera index for capture
            
        Returns:
            bool: Success status
        """
        user_dir = self.authorized_dir / name
        user_dir.mkdir(exist_ok=True)
        
        if image is None:
            # Capture from camera
            print(f"Capturing face for {name}. Press 's' to save, 'q' to quit.")
            with VideoStreamHandler(camera_index) as cap:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    cv2.putText(frame, f"Registering: {name} ({role})", (10, 30),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('Register User', frame)
                    
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('s'):
                        image = frame.copy()
                        break
                    elif key == ord('q'):
                        return False
        
        if image is None:
            return False
        
        # Save face image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = user_dir / f"{name}_{timestamp}.jpg"
        cv2.imwrite(str(image_path), image)
        
        # Add to users database
        self.users_db[name] = {
            'role': role,
            'access_level': access_level,
            'registered_date': datetime.now().isoformat(),
            'image_path': str(image_path)
        }
        
        self._save_users_db()
        print(f"User registered: {name} ({role}, Level {access_level})")
        return True
    
    def verify_access(self, frame, required_level=1):
        """
        Verify access from face in frame
        
        Args:
            frame: Input image frame
            required_level: Minimum required access level
            
        Returns:
            dict: Verification result
        """
        result = {
            'granted': False,
            'user': None,
            'role': None,
            'access_level': 0,
            'message': 'Access Denied',
            'confidence': 0.0
        }
        
        if not any(self.authorized_dir.iterdir()):
            result['message'] = 'No authorized users registered'
            return result
        
        try:
            # Find matching face
            dfs = DeepFace.find(frame,
                               db_path=str(self.authorized_dir),
                               model_name=self.model_name,
                               detector_backend=self.detector_backend,
                               distance_metric=self.distance_metric,
                               enforce_detection=False,
                               silent=True)
            
            if dfs and len(dfs) > 0:
                for df in dfs:
                    if len(df) > 0:
                        best_match = df.iloc[0]
                        distance = best_match[self.distance_metric]
                        
                        if distance < self.threshold:
                            identity_path = best_match['identity']
                            name = Path(identity_path).parent.name
                            
                            # Get user info
                            user_info = self.users_db.get(name, {})
                            access_level = user_info.get('access_level', 0)
                            role = user_info.get('role', 'unknown')
                            
                            # Check access level
                            if access_level >= required_level:
                                result = {
                                    'granted': True,
                                    'user': name,
                                    'role': role,
                                    'access_level': access_level,
                                    'message': f'Access Granted - Welcome {name}',
                                    'confidence': 1 - distance
                                }
                            else:
                                result = {
                                    'granted': False,
                                    'user': name,
                                    'role': role,
                                    'access_level': access_level,
                                    'message': f'Insufficient Access Level (Have: {access_level}, Need: {required_level})',
                                    'confidence': 1 - distance
                                }
        
        except Exception as e:
            result['message'] = f'Verification Error: {str(e)}'
        
        # Log access attempt
        self._log_access_attempt(result)
        
        return result
    
    def _log_access_attempt(self, result):
        """Log access attempt"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'granted': result['granted'],
            'user': result['user'],
            'role': result['role'],
            'access_level': result['access_level'],
            'message': result['message']
        }
        
        self.access_log.append(log_entry)
        
        # Save log periodically (every 10 entries)
        if len(self.access_log) % 10 == 0:
            self._save_access_log()
    
    def verify_access_frame(self, frame, required_level=1):
        """
        Verify access for a single frame (for CameraManager integration)
        
        Args:
            frame: Input frame
            required_level: Required access level
            
        Returns:
            dict: Access verification result
        """
        return self.verify_access(frame, required_level)
    
    def start_access_control(self, camera_index=0, required_level=1):
        """
        Start real-time access control monitoring
        
        Args:
            camera_index: Camera index
            required_level: Required access level
        """
        print(f"Starting access control (Required Level: {required_level}). Press 'q' to quit.")
        
        last_check_time = datetime.now()
        check_interval = 2  # Check every 2 seconds
        
        with VideoStreamHandler(camera_index) as cap:
            current_result = None
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Check access periodically
                if (datetime.now() - last_check_time).seconds >= check_interval:
                    current_result = self.verify_access(frame, required_level)
                    last_check_time = datetime.now()
                
                # Display result
                if current_result:
                    color = (0, 255, 0) if current_result['granted'] else (0, 0, 255)
                    
                    draw_text_with_background(
                        frame, current_result['message'], (10, 30),
                        font_scale=0.8, bg_color=color, text_color=(255, 255, 255)
                    )
                    
                    if current_result['user']:
                        info_text = f"User: {current_result['user']} | Role: {current_result['role']} | Level: {current_result['access_level']}"
                        cv2.putText(frame, info_text, (10, 70),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                cv2.imshow('Access Control', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        # Save log on exit
        self._save_access_log()
    
    def get_access_log(self, hours=24):
        """
        Get recent access log
        
        Args:
            hours: Number of hours to retrieve
            
        Returns:
            list: Access log entries
        """
        cutoff_time = datetime.now() - pd.Timedelta(hours=hours)
        
        recent_log = [
            entry for entry in self.access_log
            if pd.to_datetime(entry['timestamp']) > cutoff_time
        ]
        
        return recent_log
    
    def get_statistics(self, hours=24):
        """
        Get access control statistics
        
        Args:
            hours: Number of hours to analyze
            
        Returns:
            dict: Statistics
        """
        recent_log = self.get_access_log(hours)
        
        if not recent_log:
            return {
                'total_attempts': 0,
                'granted': 0,
                'denied': 0,
                'success_rate': 0.0
            }
        
        granted = sum(1 for entry in recent_log if entry['granted'])
        denied = len(recent_log) - granted
        
        return {
            'total_attempts': len(recent_log),
            'granted': granted,
            'denied': denied,
            'success_rate': (granted / len(recent_log) * 100),
            'unique_users': len(set(entry['user'] for entry in recent_log if entry['user']))
        }
    
    def remove_user(self, name):
        """
        Remove user from access control
        
        Args:
            name: User name
        """
        if name in self.users_db:
            del self.users_db[name]
            self._save_users_db()
            
            # Remove user directory
            user_dir = self.authorized_dir / name
            if user_dir.exists():
                import shutil
                shutil.rmtree(user_dir)
            
            print(f"User removed: {name}")
            return True
        
        print(f"User not found: {name}")
        return False
