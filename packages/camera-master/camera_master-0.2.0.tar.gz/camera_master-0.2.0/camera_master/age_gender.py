"""
Age and gender estimation using DeepFace
"""
import cv2
from deepface import DeepFace
import numpy as np
from camera_master.utils import draw_text_with_background, VideoStreamHandler


class AgeGenderEstimator:
    """
    Estimate age and gender using DeepFace
    """
    
    def __init__(self, detector_backend="opencv", enforce_detection=False):
        """
        Initialize Age/Gender Estimator
        
        Args:
            detector_backend: Face detection backend
            enforce_detection: Whether to enforce face detection
        """
        self.detector_backend = detector_backend
        self.enforce_detection = enforce_detection
        
        self.age_groups = {
            (0, 12): 'Child',
            (13, 19): 'Teenager',
            (20, 35): 'Young Adult',
            (36, 55): 'Adult',
            (56, 100): 'Senior'
        }
    
    def estimate(self, frame):
        """
        Estimate age and gender from frame
        
        Args:
            frame: Input image frame
            
        Returns:
            list: List of estimations with details
        """
        estimations = []
        
        try:
            analysis = DeepFace.analyze(
                frame,
                actions=['age', 'gender'],
                detector_backend=self.detector_backend,
                enforce_detection=self.enforce_detection,
                silent=True
            )
            
            # Handle both single face and multiple faces
            if not isinstance(analysis, list):
                analysis = [analysis]
            
            for face_analysis in analysis:
                age = face_analysis['age']
                gender = face_analysis['dominant_gender']
                gender_confidence = face_analysis['gender'][gender]
                region = face_analysis['region']
                
                # Determine age group
                age_group = 'Unknown'
                for (min_age, max_age), group in self.age_groups.items():
                    if min_age <= age <= max_age:
                        age_group = group
                        break
                
                estimations.append({
                    'age': age,
                    'age_group': age_group,
                    'gender': gender,
                    'gender_confidence': gender_confidence,
                    'region': region
                })
        
        except Exception as e:
            pass
        
        return estimations
    
    def process_frame(self, frame):
        """
        Process frame and estimate age/gender
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, estimations)
        """
        estimations = self.estimate(frame)
        
        for estimation in estimations:
            region = estimation['region']
            age = estimation['age']
            age_group = estimation['age_group']
            gender = estimation['gender']
            gender_conf = estimation['gender_confidence']
            
            x, y, w, h = region['x'], region['y'], region['w'], region['h']
            
            # Draw rectangle
            color = (255, 0, 255) if gender == 'Woman' else (0, 255, 255)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            # Draw labels
            age_text = f"Age: {age} ({age_group})"
            gender_text = f"Gender: {gender} ({gender_conf:.1f}%)"
            
            draw_text_with_background(frame, age_text, (x, y-30),
                                     bg_color=color, text_color=(255, 255, 255))
            draw_text_with_background(frame, gender_text, (x, y-10),
                                     bg_color=color, text_color=(255, 255, 255))
        
        return frame, estimations
    
    def estimate_frame(self, frame):
        """
        Estimate age/gender for a single frame (for CameraManager integration)
        
        Args:
            frame: Input frame
            
        Returns:
            dict: Age/gender estimation result
        """
        estimations = self.estimate(frame)
        if estimations:
            return {
                'age': estimations[0]['age'],
                'age_group': estimations[0]['age_group'],
                'gender': estimations[0]['gender'],
                'gender_confidence': estimations[0]['gender_confidence']
            }
        return {'age': None, 'age_group': None, 'gender': None, 'gender_confidence': 0.0}
    
    def start_estimation(self, camera_index=0, callback=None):
        """
        Start real-time age/gender estimation
        
        Args:
            camera_index: Camera index
            callback: Callback function for estimation events
        """
        print("Starting age/gender estimation. Press 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            frame_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                
                # Process every 10th frame for performance
                if frame_count % 10 == 0:
                    processed_frame, estimations = self.process_frame(frame)
                    
                    # Call callback if provided
                    if callback and estimations:
                        for estimation in estimations:
                            callback(estimation)
                else:
                    processed_frame = frame
                
                # Display info
                info_text = "Age/Gender Estimation"
                cv2.putText(processed_frame, info_text, (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('Age/Gender Estimation', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    def get_demographics_summary(self, estimations_list):
        """
        Get demographic summary from list of estimations
        
        Args:
            estimations_list: List of estimation dictionaries
            
        Returns:
            dict: Demographics summary
        """
        if not estimations_list:
            return {
                'total_faces': 0,
                'average_age': 0,
                'age_distribution': {},
                'gender_distribution': {}
            }
        
        ages = [e['age'] for e in estimations_list]
        age_groups = [e['age_group'] for e in estimations_list]
        genders = [e['gender'] for e in estimations_list]
        
        # Count age groups
        age_group_counts = {}
        for group in age_groups:
            age_group_counts[group] = age_group_counts.get(group, 0) + 1
        
        # Count genders
        gender_counts = {}
        for gender in genders:
            gender_counts[gender] = gender_counts.get(gender, 0) + 1
        
        return {
            'total_faces': len(estimations_list),
            'average_age': np.mean(ages),
            'age_range': (min(ages), max(ages)),
            'age_distribution': age_group_counts,
            'gender_distribution': gender_counts
        }
