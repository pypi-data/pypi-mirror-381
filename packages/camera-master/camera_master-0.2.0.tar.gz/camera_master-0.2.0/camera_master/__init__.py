"""
Camera Master - AI-Powered Education Monitoring System
=====================================================

A comprehensive package for education monitoring with:
- Face recognition attendance
- Gesture recognition
- Emotion analysis
- Attention tracking
- Automated reporting
- Dashboards and visualization

Note: Some features require TensorFlow which currently supports Python 3.8-3.11
"""

__version__ = "0.1.0"
__author__ = "RNS"

# Lazy imports to handle TensorFlow compatibility issues
def __getattr__(name):
    """Lazy import for better compatibility."""
    if name == "Attendance":
        from camera_master.attendance import Attendance
        return Attendance
    elif name == "GestureRecognizer":
        from camera_master.gesture import GestureRecognizer
        return GestureRecognizer
    elif name == "EmotionAnalyzer":
        from camera_master.emotion import EmotionAnalyzer
        return EmotionAnalyzer
    elif name == "Visualizer":
        from camera_master.visualization import Visualizer
        return Visualizer
    elif name == "ReportGenerator":
        from camera_master.reports import ReportGenerator
        return ReportGenerator
    elif name == "AttentionTracker":
        from camera_master.attention import AttentionTracker
        return AttentionTracker
    elif name == "MaskDetector":
        from camera_master.mask_detection import MaskDetector
        return MaskDetector
    elif name == "AgeGenderEstimator":
        from camera_master.age_gender import AgeGenderEstimator
        return AgeGenderEstimator
    elif name == "FatigueDetector":
        from camera_master.fatigue import FatigueDetector
        return FatigueDetector
    elif name == "SpoofDetector":
        from camera_master.spoof import SpoofDetector
        return SpoofDetector
    elif name == "MoodTracker":
        from camera_master.mood_tracker import MoodTracker
        return MoodTracker
    elif name == "AccessControl":
        from camera_master.access_control import AccessControl
        return AccessControl
    elif name == "GamificationEngine":
        from camera_master.gamification import GamificationEngine
        return GamificationEngine
    elif name == "CameraManager":
        from camera_master.camera_manager import CameraManager
        return CameraManager
    elif name == "UnifiedMonitoringSession":
        from camera_master.camera_manager import UnifiedMonitoringSession
        return UnifiedMonitoringSession
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

__all__ = [
    "Attendance",
    "GestureRecognizer",
    "EmotionAnalyzer",
    "Visualizer",
    "ReportGenerator",
    "AttentionTracker",
    "MaskDetector",
    "AgeGenderEstimator",
    "FatigueDetector",
    "SpoofDetector",
    "MoodTracker",
    "AccessControl",
    "GamificationEngine",
    "CameraManager",
    "UnifiedMonitoringSession"
]
