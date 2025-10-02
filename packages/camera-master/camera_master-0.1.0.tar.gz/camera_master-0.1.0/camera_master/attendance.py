"""
Face recognition based attendance system using DeepFace
"""
import cv2
import os
import pandas as pd
from datetime import datetime
from pathlib import Path
from deepface import DeepFace
import numpy as np
from camera_master.utils import (
    get_faces_db_dir, get_reports_dir, draw_text_with_background,
    timestamp_to_string, VideoStreamHandler
)


class Attendance:
    """
    Face recognition based attendance tracking system
    """
    
    def __init__(self, model_name="VGG-Face", detector_backend="opencv", 
                 distance_metric="cosine", threshold=0.6):
        """
        Initialize Attendance system
        
        Args:
            model_name: Face recognition model (VGG-Face, Facenet, OpenFace, DeepFace, ArcFace)
            detector_backend: Face detection backend (opencv, ssd, mtcnn, retinaface)
            distance_metric: Distance metric (cosine, euclidean, euclidean_l2)
            threshold: Recognition threshold
        """
        self.model_name = model_name
        self.detector_backend = detector_backend
        self.distance_metric = distance_metric
        self.threshold = threshold
        
        self.faces_db_dir = get_faces_db_dir()
        self.reports_dir = get_reports_dir()
        
        self.attendance_log = []
        self.session_start = datetime.now()
        
    def register_face(self, name, image=None, camera_index=0):
        """
        Register a new face for attendance
        
        Args:
            name: Person's name
            image: Image array or None to capture from camera
            camera_index: Camera index if capturing
            
        Returns:
            bool: Success status
        """
        person_dir = self.faces_db_dir / name
        person_dir.mkdir(exist_ok=True)
        
        if image is None:
            # Capture from camera
            print(f"Capturing face for {name}. Press 's' to save, 'q' to quit.")
            with VideoStreamHandler(camera_index) as cap:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    # Detect faces
                    try:
                        faces = DeepFace.extract_faces(frame, 
                                                       detector_backend=self.detector_backend,
                                                       enforce_detection=False)
                        
                        for face_obj in faces:
                            facial_area = face_obj['facial_area']
                            x, y, w, h = facial_area['x'], facial_area['y'], \
                                       facial_area['w'], facial_area['h']
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    except:
                        pass
                    
                    cv2.putText(frame, f"Registering: {name}", (10, 30),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('Register Face', frame)
                    
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
        image_path = person_dir / f"{name}_{timestamp}.jpg"
        cv2.imwrite(str(image_path), image)
        
        print(f"Face registered for {name}: {image_path}")
        return True
    
    def recognize_face(self, frame):
        """
        Recognize faces in frame
        
        Args:
            frame: Image frame
            
        Returns:
            list: List of recognized persons with details
        """
        if not any(self.faces_db_dir.iterdir()):
            return []
        
        recognized = []
        
        try:
            # Find faces in database
            dfs = DeepFace.find(frame, 
                               db_path=str(self.faces_db_dir),
                               model_name=self.model_name,
                               detector_backend=self.detector_backend,
                               distance_metric=self.distance_metric,
                               enforce_detection=False,
                               silent=True)
            
            if dfs and len(dfs) > 0:
                for df in dfs:
                    if len(df) > 0:
                        # Get best match
                        best_match = df.iloc[0]
                        distance = best_match[self.distance_metric]
                        
                        if distance < self.threshold:
                            identity_path = best_match['identity']
                            name = Path(identity_path).parent.name
                            
                            recognized.append({
                                'name': name,
                                'confidence': 1 - distance,
                                'distance': distance
                            })
        except Exception as e:
            print(f"Recognition error: {e}")
        
        return recognized
    
    def mark_attendance(self, name):
        """
        Mark attendance for a person
        
        Args:
            name: Person's name
        """
        timestamp = datetime.now()
        
        # Check if already marked today
        today = timestamp.date()
        for record in self.attendance_log:
            if record['name'] == name and record['timestamp'].date() == today:
                return  # Already marked
        
        self.attendance_log.append({
            'name': name,
            'timestamp': timestamp,
            'status': 'Present'
        })
        
        print(f"Attendance marked for {name} at {timestamp_to_string(timestamp)}")
    
    def start_monitoring(self, camera_index=0, duration=None):
        """
        Start real-time attendance monitoring
        
        Args:
            camera_index: Camera index
            duration: Monitoring duration in seconds (None for infinite)
            
        Returns:
            pd.DataFrame: Attendance records
        """
        print("Starting attendance monitoring. Press 'q' to quit.")
        
        start_time = datetime.now()
        last_recognition_time = {}
        recognition_cooldown = 10  # seconds
        
        with VideoStreamHandler(camera_index) as cap:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Check duration
                if duration and (datetime.now() - start_time).seconds > duration:
                    break
                
                # Recognize faces every few frames for performance
                current_time = datetime.now()
                
                # Detect and draw faces
                try:
                    faces = DeepFace.extract_faces(frame,
                                                   detector_backend=self.detector_backend,
                                                   enforce_detection=False)
                    
                    for face_obj in faces:
                        facial_area = face_obj['facial_area']
                        x, y, w, h = facial_area['x'], facial_area['y'], \
                                   facial_area['w'], facial_area['h']
                        
                        # Extract face region
                        face_img = frame[y:y+h, x:x+w]
                        
                        # Recognize
                        recognized = self.recognize_face(face_img)
                        
                        if recognized:
                            person = recognized[0]
                            name = person['name']
                            confidence = person['confidence']
                            
                            # Check cooldown
                            if name not in last_recognition_time or \
                               (current_time - last_recognition_time[name]).seconds > recognition_cooldown:
                                self.mark_attendance(name)
                                last_recognition_time[name] = current_time
                            
                            # Draw rectangle and name
                            color = (0, 255, 0)
                            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                            text = f"{name} ({confidence:.2f})"
                            draw_text_with_background(frame, text, (x, y-10))
                        else:
                            # Unknown face
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                            draw_text_with_background(frame, "Unknown", (x, y-10))
                
                except Exception as e:
                    pass
                
                # Display info
                info_text = f"Monitoring | Present: {len(self.attendance_log)}"
                cv2.putText(frame, info_text, (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('Attendance Monitoring', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        return self.get_attendance_report()
    
    def get_attendance_report(self):
        """
        Get attendance report as DataFrame
        
        Returns:
            pd.DataFrame: Attendance records
        """
        if not self.attendance_log:
            return pd.DataFrame(columns=['name', 'timestamp', 'status'])
        
        df = pd.DataFrame(self.attendance_log)
        return df
    
    def save_report(self, filename=None):
        """
        Save attendance report to CSV
        
        Args:
            filename: Output filename (auto-generated if None)
            
        Returns:
            str: Path to saved report
        """
        df = self.get_attendance_report()
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"attendance_{timestamp}.csv"
        
        filepath = self.reports_dir / filename
        df.to_csv(filepath, index=False)
        
        print(f"Attendance report saved: {filepath}")
        return str(filepath)
    
    def get_statistics(self):
        """
        Get attendance statistics
        
        Returns:
            dict: Statistics
        """
        df = self.get_attendance_report()
        
        if df.empty:
            return {
                'total_present': 0,
                'total_registered': len(list(self.faces_db_dir.iterdir())),
                'attendance_rate': 0.0
            }
        
        total_present = len(df)
        total_registered = len(list(self.faces_db_dir.iterdir()))
        
        return {
            'total_present': total_present,
            'total_registered': total_registered,
            'attendance_rate': (total_present / total_registered * 100) if total_registered > 0 else 0,
            'session_duration': (datetime.now() - self.session_start).seconds / 60,  # minutes
        }
