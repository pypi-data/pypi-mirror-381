"""
Gesture recognition using MediaPipe Hands
"""
import cv2
import mediapipe as mp
import numpy as np
from collections import deque
from camera_master.utils import draw_text_with_background, VideoStreamHandler


class GestureRecognizer:
    """
    Hand gesture recognition for numbers and signs
    """
    
    def __init__(self, max_num_hands=2, min_detection_confidence=0.7, 
                 min_tracking_confidence=0.5):
        """
        Initialize Gesture Recognizer
        
        Args:
            max_num_hands: Maximum number of hands to detect
            min_detection_confidence: Minimum detection confidence
            min_tracking_confidence: Minimum tracking confidence
        """
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        
        self.gesture_history = deque(maxlen=10)
        self.gesture_to_text = {}
        
    def count_fingers(self, landmarks, handedness):
        """
        Count extended fingers
        
        Args:
            landmarks: Hand landmarks
            handedness: Hand label (Left/Right)
            
        Returns:
            int: Number of extended fingers
        """
        fingers = []
        
        # Thumb
        if handedness == "Right":
            if landmarks[4].x < landmarks[3].x:
                fingers.append(1)
            else:
                fingers.append(0)
        else:
            if landmarks[4].x > landmarks[3].x:
                fingers.append(1)
            else:
                fingers.append(0)
        
        # Other fingers
        finger_tips = [8, 12, 16, 20]
        finger_pips = [6, 10, 14, 18]
        
        for tip, pip in zip(finger_tips, finger_pips):
            if landmarks[tip].y < landmarks[pip].y:
                fingers.append(1)
            else:
                fingers.append(0)
        
        return sum(fingers)
    
    def recognize_gesture(self, landmarks, handedness):
        """
        Recognize hand gesture
        
        Args:
            landmarks: Hand landmarks
            handedness: Hand label
            
        Returns:
            dict: Gesture information
        """
        finger_count = self.count_fingers(landmarks, handedness)
        
        # Basic number gestures
        gestures = {
            0: "Zero / Fist",
            1: "One",
            2: "Two / Peace",
            3: "Three",
            4: "Four",
            5: "Five / Open Hand"
        }
        
        gesture_name = gestures.get(finger_count, "Unknown")
        
        # Additional gesture patterns
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        
        # Calculate distances for special gestures
        thumb_index_dist = np.sqrt(
            (thumb_tip.x - index_tip.x)**2 + 
            (thumb_tip.y - index_tip.y)**2
        )
        
        # OK sign (thumb and index touching)
        if thumb_index_dist < 0.05 and finger_count == 3:
            gesture_name = "OK"
        
        # Thumbs up
        if finger_count == 1 and landmarks[4].y < landmarks[3].y:
            gesture_name = "Thumbs Up"
        
        # Thumbs down
        if finger_count == 1 and landmarks[4].y > landmarks[3].y:
            gesture_name = "Thumbs Down"
        
        return {
            'gesture': gesture_name,
            'finger_count': finger_count,
            'handedness': handedness,
            'confidence': 1.0
        }
    
    def process_frame(self, frame):
        """
        Process frame and detect gestures
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, gestures_detected)
        """
        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        gestures_detected = []
        
        if results.multi_hand_landmarks:
            for hand_landmarks, hand_handedness in zip(
                results.multi_hand_landmarks, 
                results.multi_handedness
            ):
                # Draw hand landmarks
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
                
                # Recognize gesture
                handedness = hand_handedness.classification[0].label
                gesture_info = self.recognize_gesture(
                    hand_landmarks.landmark, 
                    handedness
                )
                
                gestures_detected.append(gesture_info)
                
                # Draw gesture name
                h, w, _ = frame.shape
                x = int(hand_landmarks.landmark[0].x * w)
                y = int(hand_landmarks.landmark[0].y * h)
                
                text = f"{gesture_info['gesture']} ({handedness})"
                draw_text_with_background(frame, text, (x, y - 30))
        
        return frame, gestures_detected
    
    def start_recognition(self, camera_index=0, callback=None):
        """
        Start real-time gesture recognition
        
        Args:
            camera_index: Camera index
            callback: Callback function for gesture events
        """
        print("Starting gesture recognition. Press 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                # Flip frame horizontally for mirror view
                frame = cv2.flip(frame, 1)
                
                # Process frame
                processed_frame, gestures = self.process_frame(frame)
                
                # Call callback if provided
                if callback and gestures:
                    for gesture in gestures:
                        callback(gesture)
                
                # Display info
                info_text = f"Gestures: {len(gestures)}"
                cv2.putText(processed_frame, info_text, (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('Gesture Recognition', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    def gesture_to_number(self, gesture_info):
        """
        Convert gesture to number
        
        Args:
            gesture_info: Gesture information dict
            
        Returns:
            int or None: Number represented by gesture
        """
        finger_count = gesture_info.get('finger_count', -1)
        if 0 <= finger_count <= 5:
            return finger_count
        return None
    
    def train_custom_gesture(self, gesture_name, sample_count=10, camera_index=0):
        """
        Train custom gesture (placeholder for future ML implementation)
        
        Args:
            gesture_name: Name of custom gesture
            sample_count: Number of samples to collect
            camera_index: Camera index
        """
        print(f"Training custom gesture: {gesture_name}")
        print(f"Please perform the gesture {sample_count} times")
        
        samples = []
        
        with VideoStreamHandler(camera_index) as cap:
            count = 0
            while count < sample_count:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(rgb_frame)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        # Draw landmarks
                        self.mp_drawing.draw_landmarks(
                            frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                        )
                
                cv2.putText(frame, f"Training: {gesture_name} ({count}/{sample_count})",
                          (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, "Press 's' to capture sample",
                          (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
                cv2.imshow('Train Custom Gesture', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('s') and results.multi_hand_landmarks:
                    # Save landmark data
                    landmarks_data = []
                    for landmark in results.multi_hand_landmarks[0].landmark:
                        landmarks_data.extend([landmark.x, landmark.y, landmark.z])
                    samples.append(landmarks_data)
                    count += 1
                    print(f"Sample {count} captured")
                elif key == ord('q'):
                    break
        
        self.gesture_to_text[gesture_name] = samples
        print(f"Custom gesture '{gesture_name}' trained with {len(samples)} samples")
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'hands'):
            self.hands.close()
