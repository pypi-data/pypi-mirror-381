# Camera Integration Guide

## Overview

**Camera Master** now has **unified camera integration** across all modules! Every camera-based feature can work independently or together in a single session.

---

## Key Features

### [OK] Integrated Features
All features use camera and can work together:

| Feature | Module | Camera Method | Description |
|---------|--------|---------------|-------------|
| **Attendance** | `attendance.py` | `recognize_face()` | Face recognition attendance |
| **Gesture** | `gesture.py` | `recognize_gesture()` | Hand gesture recognition |
| **Emotion** | `emotion.py` | `analyze_emotion()` | Emotion detection |
| **Attention** | `attention.py` | `track_attention_frame()` | Attention tracking |
| **Fatigue** | `fatigue.py` | `detect_fatigue_frame()` | Drowsiness detection |
| **Mask** | `mask_detection.py` | `detect_mask_frame()` | Mask compliance |
| **Age/Gender** | `age_gender.py` | `estimate_frame()` | Age/gender estimation |
| **Spoof** | `spoof.py` | `detect_frame()` | Liveness detection |
| **Access Control** | `access_control.py` | `verify_access_frame()` | Face-based access |

### Support Features
These work with data from camera features:

| Feature | Module | Purpose |
|---------|--------|---------|
| **Visualization** | `visualization.py` | Charts and graphs |
| **Reports** | `reports.py` | Report generation |
| **Gamification** | `gamification.py` | Points and badges |
| **Mood Tracker** | `mood_tracker.py` | Emotion trends |

---

## New: Unified Camera Integration

### CameraManager Class

The `CameraManager` centralizes camera access for all features:

```python
from camera_master import CameraManager

# Create manager
manager = CameraManager(camera_index=0)

# Register features
from camera_master import GestureRecognizer, AttentionTracker, FatigueDetector

manager.register_feature('gesture', GestureRecognizer())
manager.register_feature('attention', AttentionTracker())
manager.register_feature('fatigue', FatigueDetector())

# Start integrated session (all features running simultaneously)
results = manager.start_integrated_session(duration=60, show_video=True)

# View session summary
print(manager.get_session_summary())
```

### UnifiedMonitoringSession Class

Pre-configured comprehensive monitoring:

```python
from camera_master import UnifiedMonitoringSession

# Create session
session = UnifiedMonitoringSession(camera_index=0)

# Start comprehensive monitoring with all features
results = session.start_comprehensive_monitoring(
 enable_attendance=True,
 enable_emotion=True,
 enable_gesture=True,
 enable_attention=True,
 enable_fatigue=True,
 enable_mask=True,
 duration=120 # 2 minutes
)
```

---

## Usage Examples

### Example 1: Multiple Features Together

```python
from camera_master import CameraManager
from camera_master import GestureRecognizer, AttentionTracker

# Setup
manager = CameraManager(camera_index=0)
manager.register_feature('gesture', GestureRecognizer())
manager.register_feature('attention', AttentionTracker())

# Run for 30 seconds
results = manager.start_integrated_session(duration=30)

# Access results
gesture_data = results['feature_results']['gesture']
attention_data = results['feature_results']['attention']
```

### Example 2: Classroom Monitoring

```python
from camera_master import CameraManager
from camera_master import Attendance, EmotionAnalyzer, AttentionTracker

# Setup classroom monitoring
manager = CameraManager(camera_index=0)

manager.register_feature('attendance', Attendance())
manager.register_feature('emotion', EmotionAnalyzer())
manager.register_feature('attention', AttentionTracker())

# Monitor for 1 hour
results = manager.start_integrated_session(duration=3600)

# Generate reports
from camera_master import ReportGenerator, Visualizer

report_gen = ReportGenerator()
visualizer = Visualizer()

# Create attendance report
report_gen.generate_attendance_report(
 results['feature_results']['attendance']
)

# Visualize emotions
visualizer.plot_emotion_distribution(
 results['feature_results']['emotion']
)
```

### Example 3: Driver Monitoring

```python
from camera_master import CameraManager
from camera_master import AttentionTracker, FatigueDetector

# Setup driver safety monitoring
manager = CameraManager(camera_index=0)

manager.register_feature('attention', AttentionTracker())
manager.register_feature('fatigue', FatigueDetector())

# Continuous monitoring
results = manager.start_integrated_session(duration=None) # Unlimited

# Alert on fatigue
if results['statistics']['fatigue']['successful_detections'] > 0:
 print("WARNING: DRIVER FATIGUE DETECTED - TAKE A BREAK!")
```

### Example 4: Security Access Control

```python
from camera_master import CameraManager
from camera_master import AccessControl, SpoofDetector, MaskDetector

# Setup security monitoring
manager = CameraManager(camera_index=0)

access_control = AccessControl()
spoof_detector = SpoofDetector()
spoof_detector.start_liveness_check()

manager.register_feature('access_control', access_control)
manager.register_feature('spoof', spoof_detector)
manager.register_feature('mask', MaskDetector())

# Monitor access points
results = manager.start_integrated_session(duration=None)

# Check access attempts
for detection in results['detections']:
 if 'access_control' in detection['results']:
 access_result = detection['results']['access_control']
 if access_result['granted']:
 print(f"[OK] Access GRANTED: {access_result['user']}")
 else:
 print(f"[X] Access DENIED: {access_result['message']}")
```

### Example 5: Custom Feature Combination

```python
from camera_master import CameraManager

# Create custom monitoring system
manager = CameraManager(camera_index=0)

# Only register features you need
from camera_master import GestureRecognizer, EmotionAnalyzer

manager.register_feature('gesture', GestureRecognizer())
manager.register_feature('emotion', EmotionAnalyzer())

# Add callback for real-time processing
def on_gesture_detected(result):
 if result.get('gesture') == 'thumbs_up':
 print(" User gave thumbs up!")

# Run with custom duration
results = manager.start_integrated_session(
 duration=45,
 show_video=True
)
```

---

## Individual Module Usage

Each module can still be used independently:

### Attendance

```python
from camera_master import Attendance

attendance = Attendance()
attendance.register_face("Student Name")
attendance.start_monitoring(camera_index=0)
attendance.save_report()
```

### Gesture Recognition

```python
from camera_master import GestureRecognizer

recognizer = GestureRecognizer()
recognizer.start_recognition(camera_index=0)
stats = recognizer.get_statistics()
```

### Emotion Analysis

```python
from camera_master import EmotionAnalyzer

analyzer = EmotionAnalyzer()
analyzer.start_analysis(camera_index=0)
emotions = analyzer.get_emotion_statistics()
```

### Attention Tracking

```python
from camera_master import AttentionTracker

tracker = AttentionTracker()
tracker.start_tracking(camera_index=0)
report = tracker.generate_attention_report()
```

### Fatigue Detection

```python
from camera_master import FatigueDetector

detector = FatigueDetector()
detector.start_detection(camera_index=0)
summary = detector.get_fatigue_summary()
```

---

## Working with Results

### Session Results Structure

```python
results = {
 'session_info': {
 'start_time': '2025-10-01T10:00:00',
 'end_time': '2025-10-01T10:30:00',
 'duration_seconds': 1800,
 'frames_processed': 54000,
 'fps': 30.0
 },
 'active_features': ['gesture', 'attention', 'emotion'],
 'feature_results': {
 'gesture': [...], # List of gesture detections
 'attention': [...], # List of attention measurements
 'emotion': [...] # List of emotion detections
 },
 'statistics': {
 'gesture': {
 'total_detections': 500,
 'successful_detections': 450,
 'gesture_distribution': {'thumbs_up': 100, 'peace': 50, ...}
 },
 'attention': {...},
 'emotion': {...}
 }
}
```

### Processing Results

```python
# Get all gesture detections
gestures = results['feature_results']['gesture']

# Count specific gesture
thumbs_up_count = len([
 g for g in gestures 
 if g and g.get('gesture') == 'thumbs_up'
])

# Get statistics
stats = results['statistics']
print(f"Total frames: {stats['gesture']['total_detections']}")
print(f"Success rate: {stats['gesture']['successful_detections'] / stats['gesture']['total_detections'] * 100:.1f}%")
```

---

## Integration with Data Processing Modules

### Generate Reports from Session

```python
from camera_master import CameraManager, ReportGenerator

# Run session
manager = CameraManager(camera_index=0)
# ... register features ...
results = manager.start_integrated_session(duration=60)

# Generate reports
report_gen = ReportGenerator()

# Attendance report
if 'attendance' in results['feature_results']:
 report_gen.generate_attendance_report(
 results['feature_results']['attendance'],
 output_format='html'
 )

# Emotion report
if 'emotion' in results['feature_results']:
 report_gen.generate_emotion_report(
 results['feature_results']['emotion'],
 output_format='json'
 )
```

### Create Visualizations

```python
from camera_master import Visualizer
import pandas as pd

visualizer = Visualizer()

# Convert results to DataFrame
attendance_df = pd.DataFrame(results['feature_results']['attendance'])

# Create visualizations
visualizer.plot_attendance_over_time(attendance_df)
visualizer.plot_attention_heatmap(results['feature_results']['attention'])
```

### Update Gamification

```python
from camera_master import GamificationEngine

game = GamificationEngine()

# Award points for session participation
for detection in results['detections']:
 if 'attendance' in detection['results']:
 user = detection['results']['attendance'].get('name')
 if user:
 game.record_attendance(user)
 game.award_points(user, 10, "Session participation")

# Check for badges
game.check_and_award_badges(user)
leaderboard = game.get_leaderboard()
```

---

## CLI Integration

Use camera features from command line:

```bash
# Integrated session
camera-master integrated --features gesture,attention,fatigue --duration 60

# Individual features
camera-master attendance --start
camera-master gesture --start
camera-master emotion --start
```

---

## Camera Configuration

### Multiple Cameras

```python
# Front camera
front_manager = CameraManager(camera_index=0)

# Back camera
back_manager = CameraManager(camera_index=1)

# External USB camera
usb_manager = CameraManager(camera_index=2)
```

### Camera Settings

```python
from camera_master.utils import VideoStreamHandler

with VideoStreamHandler(camera_index=0) as cap:
 # Set resolution
 cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
 cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
 # Set FPS
 cap.set(cv2.CAP_PROP_FPS, 30)
```

---

## Python Compatibility

### Python 3.13 (Current)
**Working Features** (No TensorFlow):
- [OK] Gesture Recognition
- [OK] Attention Tracking
- [OK] Fatigue Detection
- [OK] Spoof Detection (Blink)
- [OK] Visualization
- [OK] Reports

**Not Working** (Requires TensorFlow):
- [X] Face Recognition (Attendance)
- [X] Emotion Analysis
- [X] Age/Gender Estimation
- [X] Mask Detection
- [X] Access Control

### Python 3.11 (Recommended)
**All Features Work!** [OK]

See `PYTHON_COMPATIBILITY.md` for details.

---

## Best Practices

### 1. Resource Management

```python
# Use context managers
with VideoStreamHandler(camera_index=0) as cap:
 # Camera automatically released
 pass

# Or manually manage
manager = CameraManager(camera_index=0)
try:
 results = manager.start_integrated_session(duration=60)
finally:
 cv2.destroyAllWindows()
```

### 2. Performance Optimization

```python
# Process every Nth frame
frame_counter = 0
for frame in video:
 frame_counter += 1
 if frame_counter % 3 == 0: # Every 3rd frame
 result = manager._process_feature('gesture', gesture_instance, frame)
```

### 3. Error Handling

```python
try:
 manager.register_feature('attendance', Attendance())
except Exception as e:
 print(f"Attendance requires TensorFlow: {e}")
 # Continue with other features
```

### 4. Callbacks for Real-time Processing

```python
def on_detection(feature_name, result):
 if feature_name == 'attention' and result['is_attentive']:
 game.award_points(user, 1, "Being attentive")
 elif feature_name == 'fatigue' and result['fatigue_level'] == 'Critical':
 send_alert("Take a break!")

# Implement in your custom loop
```

---

## Use Cases

### Education
```python
# Comprehensive classroom monitoring
features = ['attendance', 'emotion', 'attention', 'gesture']
manager = setup_classroom_monitoring(features)
results = manager.start_integrated_session(duration=3600)
```

### Security
```python
# Access control with anti-spoofing
features = ['access_control', 'spoof', 'mask']
manager = setup_security_monitoring(features)
results = manager.start_integrated_session(duration=None)
```

### Healthcare
```python
# Patient monitoring
features = ['emotion', 'attention', 'fatigue']
manager = setup_patient_monitoring(features)
results = manager.start_integrated_session(duration=600)
```

### Automotive
```python
# Driver safety
features = ['attention', 'fatigue', 'emotion']
manager = setup_driver_monitoring(features)
results = manager.start_integrated_session(duration=None)
```

---

## Next Steps

1. **Try demos**: Run `python examples/demo_unified_camera.py`
2. **Read docs**: Check `README.md` for full API
3. **Customize**: Create your own feature combinations
4. **Integrate**: Add to your applications
5. **Upgrade**: Use Python 3.11 for all features

---

## Additional Resources

- **Quick Start**: `QUICKSTART.md`
- **Python Compatibility**: `PYTHON_COMPATIBILITY.md`
- **API Reference**: `README.md`
- **Examples**: `examples/` directory
- **Build Guide**: `BUILD.md`

---

**Camera Master** - All features, one camera! 
