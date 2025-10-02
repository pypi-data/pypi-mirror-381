"""
Utility functions for camera-master package
"""
import cv2
import numpy as np
import os
import json
from datetime import datetime
from pathlib import Path


def get_data_dir():
    """Get or create data directory for storing models and data"""
    data_dir = Path.home() / ".camera_master"
    data_dir.mkdir(exist_ok=True)
    return data_dir


def get_faces_db_dir():
    """Get or create directory for face database"""
    faces_dir = get_data_dir() / "faces_db"
    faces_dir.mkdir(exist_ok=True)
    return faces_dir


def get_reports_dir():
    """Get or create directory for reports"""
    reports_dir = get_data_dir() / "reports"
    reports_dir.mkdir(exist_ok=True)
    return reports_dir


def get_logs_dir():
    """Get or create directory for logs"""
    logs_dir = get_data_dir() / "logs"
    logs_dir.mkdir(exist_ok=True)
    return logs_dir


def save_json(data, filepath):
    """Save data to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4, default=str)


def load_json(filepath):
    """Load data from JSON file"""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return json.load(f)


def calculate_eye_aspect_ratio(eye_landmarks):
    """
    Calculate Eye Aspect Ratio (EAR) for drowsiness/attention detection
    
    Args:
        eye_landmarks: List of eye landmark coordinates
        
    Returns:
        float: Eye aspect ratio value
    """
    if len(eye_landmarks) < 6:
        return 0.0
    
    # Compute vertical distances
    v1 = np.linalg.norm(np.array(eye_landmarks[1]) - np.array(eye_landmarks[5]))
    v2 = np.linalg.norm(np.array(eye_landmarks[2]) - np.array(eye_landmarks[4]))
    
    # Compute horizontal distance
    h = np.linalg.norm(np.array(eye_landmarks[0]) - np.array(eye_landmarks[3]))
    
    # Calculate EAR
    if h == 0:
        return 0.0
    ear = (v1 + v2) / (2.0 * h)
    return ear


def resize_with_aspect_ratio(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Resize image while maintaining aspect ratio
    
    Args:
        image: Input image
        width: Target width
        height: Target height
        inter: Interpolation method
        
    Returns:
        Resized image
    """
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def draw_text_with_background(img, text, position, font_scale=0.6, 
                              font_thickness=2, text_color=(255, 255, 255),
                              bg_color=(0, 0, 0), padding=5):
    """
    Draw text with background rectangle
    
    Args:
        img: Image to draw on
        text: Text to draw
        position: (x, y) position
        font_scale: Font scale
        font_thickness: Font thickness
        text_color: Text color (BGR)
        bg_color: Background color (BGR)
        padding: Padding around text
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    
    x, y = position
    text_w, text_h = text_size
    
    # Draw background rectangle
    cv2.rectangle(img, 
                 (x - padding, y - text_h - padding),
                 (x + text_w + padding, y + padding),
                 bg_color, -1)
    
    # Draw text
    cv2.putText(img, text, (x, y), font, font_scale, text_color, font_thickness)


def create_color_from_name(name):
    """
    Generate consistent color from name for visualization
    
    Args:
        name: String name
        
    Returns:
        tuple: BGR color tuple
    """
    # Generate hash from name
    hash_value = hash(name)
    
    # Convert to BGR color
    r = (hash_value & 0xFF0000) >> 16
    g = (hash_value & 0x00FF00) >> 8
    b = hash_value & 0x0000FF
    
    return (b, g, r)


def timestamp_to_string(timestamp=None):
    """
    Convert timestamp to formatted string
    
    Args:
        timestamp: datetime object or None for current time
        
    Returns:
        str: Formatted timestamp string
    """
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def get_timestamp_filename(prefix="", extension="csv"):
    """
    Generate filename with timestamp
    
    Args:
        prefix: Filename prefix
        extension: File extension
        
    Returns:
        str: Filename with timestamp
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if prefix:
        return f"{prefix}_{timestamp}.{extension}"
    return f"{timestamp}.{extension}"


def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def calculate_angle(point1, point2, point3):
    """
    Calculate angle between three points
    
    Args:
        point1, point2, point3: Points as tuples (x, y)
        
    Returns:
        float: Angle in degrees
    """
    radians = np.arctan2(point3[1] - point2[1], point3[0] - point2[0]) - \
              np.arctan2(point1[1] - point2[1], point1[0] - point2[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle


def is_hand_open(landmarks):
    """
    Check if hand is open based on landmarks
    
    Args:
        landmarks: Hand landmarks from mediapipe
        
    Returns:
        bool: True if hand is open
    """
    # Compare fingertip y-coordinates with corresponding pip joints
    fingers_open = []
    
    # Thumb (special case - compare x-coordinates)
    thumb_tip = landmarks[4]
    thumb_ip = landmarks[3]
    fingers_open.append(abs(thumb_tip.x - thumb_ip.x) > 0.05)
    
    # Other fingers
    finger_tips = [8, 12, 16, 20]
    finger_pips = [6, 10, 14, 18]
    
    for tip, pip in zip(finger_tips, finger_pips):
        tip_y = landmarks[tip].y
        pip_y = landmarks[pip].y
        fingers_open.append(tip_y < pip_y)
    
    return sum(fingers_open) >= 4


class VideoStreamHandler:
    """Handle video stream from camera or file"""
    
    def __init__(self, source=0):
        """
        Initialize video stream
        
        Args:
            source: Camera index or video file path
        """
        self.source = source
        self.cap = None
        
    def __enter__(self):
        """Start video stream"""
        self.cap = cv2.VideoCapture(self.source)
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open video source: {self.source}")
        return self.cap
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Release video stream"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
