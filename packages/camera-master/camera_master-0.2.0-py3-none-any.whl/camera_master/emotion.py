"""
Emotion analysis using DeepFace
"""
import cv2
import numpy as np
from deepface import DeepFace
from collections import deque
from datetime import datetime
import pandas as pd
from camera_master.utils import (
    draw_text_with_background, get_reports_dir, VideoStreamHandler
)


class EmotionAnalyzer:
    """
    Real-time emotion detection and analysis
    """
    
    def __init__(self, detector_backend="opencv", enforce_detection=False):
        """
        Initialize Emotion Analyzer
        
        Args:
            detector_backend: Face detection backend
            enforce_detection: Whether to enforce face detection
        """
        self.detector_backend = detector_backend
        self.enforce_detection = enforce_detection
        
        self.emotion_history = deque(maxlen=100)
        self.emotion_counts = {
            'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0,
            'sad': 0, 'surprise': 0, 'neutral': 0
        }
        
        self.reports_dir = get_reports_dir()
        self.session_data = []
        
        # Color mapping for emotions
        self.emotion_colors = {
            'angry': (0, 0, 255),      # Red
            'disgust': (128, 0, 128),  # Purple
            'fear': (255, 0, 255),     # Magenta
            'happy': (0, 255, 0),      # Green
            'sad': (255, 0, 0),        # Blue
            'surprise': (0, 255, 255), # Yellow
            'neutral': (128, 128, 128) # Gray
        }
    
    def analyze_emotion(self, frame):
        """
        Analyze emotions in frame
        
        Args:
            frame: Input image frame
            
        Returns:
            list: List of detected emotions with details
        """
        emotions_detected = []
        
        try:
            # Analyze with DeepFace
            analysis = DeepFace.analyze(
                frame,
                actions=['emotion'],
                detector_backend=self.detector_backend,
                enforce_detection=self.enforce_detection,
                silent=True
            )
            
            # Handle both single face and multiple faces
            if not isinstance(analysis, list):
                analysis = [analysis]
            
            for face_analysis in analysis:
                emotion_scores = face_analysis['emotion']
                dominant_emotion = face_analysis['dominant_emotion']
                region = face_analysis['region']
                
                emotions_detected.append({
                    'dominant_emotion': dominant_emotion,
                    'emotion_scores': emotion_scores,
                    'region': region,
                    'timestamp': datetime.now()
                })
                
                # Update counts
                self.emotion_counts[dominant_emotion] += 1
                self.emotion_history.append({
                    'emotion': dominant_emotion,
                    'timestamp': datetime.now()
                })
                
        except Exception as e:
            pass
        
        return emotions_detected
    
    def process_frame(self, frame):
        """
        Process frame and detect emotions
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, emotions_detected)
        """
        emotions = self.analyze_emotion(frame)
        
        for emotion_data in emotions:
            region = emotion_data['region']
            dominant_emotion = emotion_data['dominant_emotion']
            emotion_scores = emotion_data['emotion_scores']
            
            x, y, w, h = region['x'], region['y'], region['w'], region['h']
            
            # Draw rectangle with emotion color
            color = self.emotion_colors.get(dominant_emotion, (255, 255, 255))
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            # Draw emotion label
            confidence = emotion_scores[dominant_emotion]
            text = f"{dominant_emotion}: {confidence:.1f}%"
            draw_text_with_background(frame, text, (x, y-10), 
                                     bg_color=color, text_color=(255, 255, 255))
            
            # Draw top 3 emotions
            sorted_emotions = sorted(emotion_scores.items(), 
                                   key=lambda x: x[1], reverse=True)[:3]
            
            y_offset = y + h + 20
            for i, (emotion, score) in enumerate(sorted_emotions):
                text = f"{emotion}: {score:.1f}%"
                cv2.putText(frame, text, (x, y_offset + i*20),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
            
            # Log session data
            self.session_data.append({
                'timestamp': emotion_data['timestamp'],
                'dominant_emotion': dominant_emotion,
                'confidence': confidence,
                **emotion_scores
            })
        
        return frame, emotions
    
    def start_analysis(self, camera_index=0, callback=None):
        """
        Start real-time emotion analysis
        
        Args:
            camera_index: Camera index
            callback: Callback function for emotion events
        """
        print("Starting emotion analysis. Press 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            frame_count = 0
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                
                # Process every 5th frame for performance
                if frame_count % 5 == 0:
                    processed_frame, emotions = self.process_frame(frame)
                    
                    # Call callback if provided
                    if callback and emotions:
                        for emotion in emotions:
                            callback(emotion)
                else:
                    processed_frame = frame
                
                # Display statistics
                y_pos = 30
                cv2.putText(processed_frame, "Emotion Statistics:", (10, y_pos),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                y_pos += 25
                for emotion, count in self.emotion_counts.items():
                    if count > 0:
                        color = self.emotion_colors[emotion]
                        text = f"{emotion}: {count}"
                        cv2.putText(processed_frame, text, (10, y_pos),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
                        y_pos += 20
                
                cv2.imshow('Emotion Analysis', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    def get_emotion_statistics(self):
        """
        Get emotion statistics
        
        Returns:
            dict: Emotion statistics
        """
        total = sum(self.emotion_counts.values())
        
        if total == 0:
            return {
                'total_detections': 0,
                'emotion_percentages': {},
                'dominant_emotion': None
            }
        
        percentages = {
            emotion: (count / total * 100) 
            for emotion, count in self.emotion_counts.items()
        }
        
        dominant = max(self.emotion_counts.items(), key=lambda x: x[1])[0]
        
        return {
            'total_detections': total,
            'emotion_percentages': percentages,
            'dominant_emotion': dominant,
            'emotion_counts': self.emotion_counts.copy()
        }
    
    def get_emotion_report(self):
        """
        Get emotion analysis report as DataFrame
        
        Returns:
            pd.DataFrame: Emotion records
        """
        if not self.session_data:
            return pd.DataFrame()
        
        df = pd.DataFrame(self.session_data)
        return df
    
    def save_report(self, filename=None):
        """
        Save emotion report to CSV
        
        Args:
            filename: Output filename
            
        Returns:
            str: Path to saved report
        """
        df = self.get_emotion_report()
        
        if df.empty:
            print("No emotion data to save")
            return None
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"emotion_analysis_{timestamp}.csv"
        
        filepath = self.reports_dir / filename
        df.to_csv(filepath, index=False)
        
        print(f"Emotion report saved: {filepath}")
        return str(filepath)
    
    def get_mood_trend(self, window_size=10):
        """
        Get mood trend over recent detections
        
        Args:
            window_size: Number of recent detections to analyze
            
        Returns:
            str: Trend description
        """
        if len(self.emotion_history) < window_size:
            return "Insufficient data"
        
        recent = list(self.emotion_history)[-window_size:]
        emotion_list = [e['emotion'] for e in recent]
        
        positive_count = sum(1 for e in emotion_list if e in ['happy', 'surprise'])
        negative_count = sum(1 for e in emotion_list if e in ['sad', 'angry', 'fear', 'disgust'])
        
        if positive_count > negative_count * 1.5:
            return "Positive trend"
        elif negative_count > positive_count * 1.5:
            return "Negative trend"
        else:
            return "Neutral trend"
