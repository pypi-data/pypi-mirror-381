"""
Mask detection using MediaPipe Face Detection
"""
import cv2
import mediapipe as mp
import numpy as np
from camera_master.utils import draw_text_with_background, VideoStreamHandler


class MaskDetector:
    """
    Detect face masks using face landmarks and heuristics
    """
    
    def __init__(self, min_detection_confidence=0.7):
        """
        Initialize Mask Detector
        
        Args:
            min_detection_confidence: Minimum detection confidence
        """
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        
        self.face_detection = self.mp_face_detection.FaceDetection(
            min_detection_confidence=min_detection_confidence
        )
        
        self.mask_count = 0
        self.no_mask_count = 0
    
    def detect_mask(self, frame):
        """
        Detect if person is wearing a mask
        
        Args:
            frame: Input image frame
            
        Returns:
            list: List of detections with mask status
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(rgb_frame)
        
        detections = []
        
        if results.detections:
            h, w, _ = frame.shape
            
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                bbox = (
                    int(bboxC.xmin * w),
                    int(bboxC.ymin * h),
                    int(bboxC.width * w),
                    int(bboxC.height * h)
                )
                
                # Extract face region
                x, y, w_box, h_box = bbox
                face_region = frame[max(0, y):min(h, y+h_box), 
                                  max(0, x):min(w, x+w_box)]
                
                # Simple heuristic: check lower half of face for mask
                # A more sophisticated approach would use a trained model
                has_mask = self._check_mask_heuristic(face_region)
                
                if has_mask:
                    self.mask_count += 1
                else:
                    self.no_mask_count += 1
                
                detections.append({
                    'bbox': bbox,
                    'has_mask': has_mask,
                    'confidence': detection.score[0]
                })
        
        return detections
    
    def _check_mask_heuristic(self, face_region):
        """
        Simple heuristic to check for mask presence
        Note: This is a simplified approach. For production, use a trained model.
        
        Args:
            face_region: Cropped face image
            
        Returns:
            bool: True if mask detected
        """
        if face_region.size == 0:
            return False
        
        # Get lower half of face
        h, w = face_region.shape[:2]
        lower_face = face_region[h//2:, :]
        
        # Convert to HSV
        hsv = cv2.cvtColor(lower_face, cv2.COLOR_BGR2HSV)
        
        # Check for typical mask colors (white, blue, black)
        # This is a very simple heuristic
        mask_ranges = [
            # White mask
            (np.array([0, 0, 200]), np.array([180, 30, 255])),
            # Blue mask
            (np.array([90, 50, 50]), np.array([130, 255, 255])),
            # Black mask
            (np.array([0, 0, 0]), np.array([180, 255, 50]))
        ]
        
        total_pixels = lower_face.shape[0] * lower_face.shape[1]
        mask_pixels = 0
        
        for lower, upper in mask_ranges:
            mask = cv2.inRange(hsv, lower, upper)
            mask_pixels += cv2.countNonZero(mask)
        
        # If more than 40% of lower face matches mask colors
        return (mask_pixels / total_pixels) > 0.4
    
    def process_frame(self, frame):
        """
        Process frame and detect masks
        
        Args:
            frame: Input image frame
            
        Returns:
            tuple: (processed_frame, detections)
        """
        detections = self.detect_mask(frame)
        
        for detection in detections:
            bbox = detection['bbox']
            has_mask = detection['has_mask']
            confidence = detection['confidence']
            
            x, y, w, h = bbox
            
            # Draw bounding box
            color = (0, 255, 0) if has_mask else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            
            # Draw label
            label = f"Mask: {'Yes' if has_mask else 'No'} ({confidence:.2f})"
            draw_text_with_background(frame, label, (x, y-10), 
                                     bg_color=color, text_color=(255, 255, 255))
        
        return frame, detections
    
    def detect_mask_frame(self, frame):
        """
        Detect mask for a single frame (for CameraManager integration)
        
        Args:
            frame: Input frame
            
        Returns:
            dict: Mask detection result
        """
        detections = self.detect_mask(frame)
        if detections:
            return {
                'status': 'wearing_mask' if detections[0]['has_mask'] else 'no_mask',
                'has_mask': detections[0]['has_mask'],
                'confidence': detections[0]['confidence']
            }
        return {'status': 'no_face', 'has_mask': None, 'confidence': 0.0}
    
    def start_detection(self, camera_index=0, callback=None):
        """
        Start real-time mask detection
        
        Args:
            camera_index: Camera index
            callback: Callback function for detection events
        """
        print("Starting mask detection. Press 'q' to quit.")
        
        with VideoStreamHandler(camera_index) as cap:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, detections = self.process_frame(frame)
                
                # Call callback if provided
                if callback and detections:
                    for detection in detections:
                        callback(detection)
                
                # Display statistics
                total = self.mask_count + self.no_mask_count
                mask_rate = (self.mask_count / total * 100) if total > 0 else 0
                
                info_text = f"Mask: {self.mask_count} | No Mask: {self.no_mask_count} | Rate: {mask_rate:.1f}%"
                cv2.putText(processed_frame, info_text, (10, 30),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                cv2.imshow('Mask Detection', processed_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    
    def get_statistics(self):
        """
        Get mask detection statistics
        
        Returns:
            dict: Statistics
        """
        total = self.mask_count + self.no_mask_count
        
        return {
            'mask_count': self.mask_count,
            'no_mask_count': self.no_mask_count,
            'total_detections': total,
            'mask_compliance_rate': (self.mask_count / total * 100) if total > 0 else 0
        }
    
    def __del__(self):
        """Cleanup"""
        if hasattr(self, 'face_detection'):
            self.face_detection.close()
