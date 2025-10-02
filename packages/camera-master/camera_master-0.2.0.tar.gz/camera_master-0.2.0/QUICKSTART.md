# Camera Master - Quick Start Guide

## Installation

1. **Install Python 3.8+**
 - Download from [python.org](https://www.python.org/downloads/)
 - Make sure to check "Add Python to PATH" during installation

2. **Install Camera Master**
 ```bash
 # Navigate to the camera-master directory
 cd camera-master
 # Install dependencies
 pip install -r requirements.txt
 # Install the package
 pip install -e .
 ```

3. **Verify Installation**
 ```bash
 python test_installation.py
 ```

## First Steps

### 1. Test Your Camera
```bash
# Quick camera test
python -c "import cv2; cap = cv2.VideoCapture(0); ret, frame = cap.read(); print('Camera OK' if ret else 'Camera Error'); cap.release()"
```

### 2. Run Your First Demo

#### Attendance System
```bash
python examples/demo_attendance.py
```

Follow the prompts to:
- Register your face
- Start attendance monitoring
- View the generated report

#### Emotion Analysis
```bash
python examples/demo_emotion.py
```

The system will:
- Detect your emotions in real-time
- Show statistics and dominant emotions
- Generate visualizations

#### Gesture Recognition
```bash
python examples/demo_gesture_interaction.py
```

Try these gestures:
- Numbers 1-5 (count with fingers)
- OK sign (thumb + index finger)
- Thumbs up
- Open hand (all fingers extended)

### 3. Use Command-Line Tools

```bash
# Attendance
camera-master attendance --register "Your Name"
camera-master attendance --start

# Emotion analysis
camera-master emotion --start

# Gesture recognition
camera-master gesture --start

# Attention tracking
camera-master attention --start

# View gamification dashboard
camera-master gamification --user "Your Name" --leaderboard
```

## Common Issues and Solutions

### Issue: "Import cv2 could not be resolved"
**Solution**: Install OpenCV
```bash
pip install opencv-python
```

### Issue: "No module named 'deepface'"
**Solution**: Install DeepFace
```bash
pip install deepface
```

### Issue: Camera not detected
**Solutions**:
1. Check if camera is connected
2. Try different camera index: `--camera 1`
3. Grant camera permissions to Python
4. Close other apps using the camera

### Issue: TensorFlow warnings
**Solution**: These are normal. The package will still work.
You can suppress them:
```python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```

### Issue: Slow performance
**Solutions**:
1. Use a more powerful model: `model_name="VGG-Face"`
2. Process fewer frames: Process every 5th or 10th frame
3. Reduce camera resolution
4. Use GPU if available (install `tensorflow-gpu`)

## Next Steps

1. **Explore More Examples**
 - Run `python examples/demo_comprehensive.py` for a complete monitoring system
 - Check out other example scripts in the `examples/` directory

2. **Customize Settings**
 - Adjust recognition thresholds
 - Configure camera settings
 - Customize emotion detection parameters

3. **Generate Reports**
 - All reports are saved in `~/.camera_master/reports/`
 - Open HTML reports in your browser
 - Analyze CSV data in Excel or Pandas

4. **Set Up Gamification**
 - Register users with `camera-master gamification --user "Name"`
 - Track progress and earn badges
 - View leaderboards

## Useful Directories

- **Face Database**: `~/.camera_master/faces_db/`
- **Reports**: `~/.camera_master/reports/`
- **Logs**: `~/.camera_master/logs/`
- **User Data**: `~/.camera_master/`

## Tips for Best Results

### Face Recognition
- [OK] Good lighting
- [OK] Face directly toward camera
- [OK] Remove glasses if possible
- [OK] Register multiple photos from different angles

### Emotion Detection
- [OK] Clear view of full face
- [OK] Neutral background
- [OK] Adequate lighting
- [OK] No obstructions

### Gesture Recognition
- [OK] Plain background
- [OK] Good lighting
- [OK] Hand fully visible
- [OK] Clear, deliberate gestures

### Attention Tracking
- [OK] Face camera directly
- [OK] Minimize head movement
- [OK] Keep eyes open naturally
- [OK] Avoid distractions in background

## Getting Help

1. **Check the README**: Comprehensive documentation in `README.md`
2. **Run Examples**: Learn from working code in `examples/`
3. **Test Installation**: Run `python test_installation.py`
4. **GitHub Issues**: Report bugs or ask questions on GitHub

## Quick Reference

### Python API
```python
# Import components
from camera_master import (
 Attendance,
 GestureRecognizer,
 EmotionAnalyzer,
 AttentionTracker,
 Visualizer,
 ReportGenerator,
 GamificationEngine
)

# Initialize
attendance = Attendance()
gesture = GestureRecognizer()
emotion = EmotionAnalyzer()
attention = AttentionTracker()

# Use
attendance.register_face("Name")
attendance.start_monitoring()
gesture.start_recognition()
emotion.start_analysis()
attention.start_tracking()
```

### CLI Commands
```bash
camera-master attendance --start
camera-master emotion --start
camera-master gesture --start
camera-master attention --start
camera-master mask --start
camera-master fatigue --start
camera-master spoof --start
camera-master gamification --user "Name"
```

## Keyboard Shortcuts

While running camera applications:
- **q**: Quit application
- **s**: Save/capture (in registration mode)
- **l**: Start liveness check (in spoof detection)
- **r**: Reset (in some applications)

## Performance Optimization

### For Faster Processing
```python
# Use lighter model
attendance = Attendance(model_name="Facenet")

# Process every Nth frame
if frame_count % 5 == 0:
 # Process this frame
 pass

# Reduce image size
frame = cv2.resize(frame, (640, 480))
```

### For Better Accuracy
```python
# Use best model
attendance = Attendance(
 model_name="ArcFace",
 detector_backend="retinaface"
)

# Lower threshold
attendance.threshold = 0.4
```

## Integration Examples

### With Flask Web App
```python
from flask import Flask, Response
from camera_master import EmotionAnalyzer

app = Flask(__name__)
analyzer = EmotionAnalyzer()

@app.route('/video_feed')
def video_feed():
 def generate():
 cap = cv2.VideoCapture(0)
 while True:
 ret, frame = cap.read()
 frame, emotions = analyzer.process_frame(frame)
 ret, jpeg = cv2.imencode('.jpg', frame)
 yield (b'--frame\r\n'
 b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
 return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
```

### With Discord Bot
```python
import discord
from camera_master import GamificationEngine

client = discord.Client()
game = GamificationEngine()

@client.event
async def on_message(message):
 if message.content.startswith('!points'):
 user = message.author.name
 profile = game.get_user_profile(user)
 await message.channel.send(f"{user}: {profile['points']} points, Level {profile['level']}")
```

## Troubleshooting Steps

1. **Check Python version**: `python --version` (should be 3.8+)
2. **Check pip**: `pip --version`
3. **Verify installation**: `pip show camera-master`
4. **Test imports**: `python test_installation.py`
5. **Check camera**: Try OpenCV camera test
6. **Update packages**: `pip install --upgrade -r requirements.txt`
7. **Check permissions**: Camera access, file permissions

## Resources

- Full Documentation: `README.md`
- Source Code: GitHub repository
- Report Issues: GitHub Issues
- Contact: See README for contact info

---

Happy monitoring! 
