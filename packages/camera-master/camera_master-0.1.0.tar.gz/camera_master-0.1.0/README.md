# 📸 Camera Master - AI-Powered Education Monitoring

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.1.0-orange.svg)

**Camera Master** is a comprehensive Python package that provides AI-powered features for education monitoring, including face recognition attendance, gesture detection, emotion analysis, attention tracking, and gamification.

## 🌟 Features

### Phase 1 - Core Features
- **👤 Face Recognition Attendance**: Automated attendance tracking using DeepFace and OpenCV
- **✋ Gesture Recognition**: Hand gesture detection (numbers 0-5) using MediaPipe
- **😊 Emotion Analysis**: Real-time emotion detection (7 emotions) using DeepFace
- **📊 Visualization**: Beautiful charts and graphs with Matplotlib

### Phase 2 - Extensions
- **😷 Mask Detection**: Face mask compliance monitoring
- **👥 Age/Gender Estimation**: Demographic analysis using DeepFace
- **👁️ Attention Tracking**: Eye aspect ratio and head pose monitoring
- **🔊 Audio Feedback**: Text-to-speech notifications (pyttsx3)
- **📄 Automated Reports**: CSV/JSON/HTML report generation

### Phase 3 - Advanced Features
- **✍️ Gesture-to-Text**: Hand sign to text conversion
- **😴 Fatigue Detection**: Drowsiness and yawning detection
- **🛡️ Spoof Detection**: Liveness check via blink detection
- **📈 Mood Tracker**: Long-term emotion trend analysis

### Phase 4 - Enterprise Ready
- **🔐 Access Control**: Face-based authentication with authorization levels
- **🎮 Gamification**: Points, badges, levels, and leaderboards
- **📱 Dashboards**: Interactive Streamlit/Gradio interfaces
- **⚠️ Anomaly Detection**: Engagement alerts and notifications

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Webcam or camera device
- Windows/Linux/macOS

### Install from source

```bash
# Clone the repository
git clone https://github.com/RNSsanjay/camera-master.git
cd camera-master

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Install from PyPI (once published)

```bash
pip install camera-master
```

## 📖 Quick Start

### 1. Attendance System

```python
from camera_master import Attendance

# Initialize
attendance = Attendance()

# Register a face
attendance.register_face("John Doe")

# Start monitoring
df = attendance.start_monitoring(camera_index=0)

# Save report
attendance.save_report()
```

### 2. Emotion Analysis

```python
from camera_master import EmotionAnalyzer

# Initialize
analyzer = EmotionAnalyzer()

# Start analysis
analyzer.start_analysis(camera_index=0)

# Get statistics
stats = analyzer.get_emotion_statistics()
print(f"Dominant emotion: {stats['dominant_emotion']}")
```

### 3. Gesture Recognition

```python
from camera_master import GestureRecognizer

# Initialize
recognizer = GestureRecognizer()

# Start recognition
recognizer.start_recognition(camera_index=0)
```

### 4. Comprehensive Monitoring

```python
from camera_master import (
    Attendance, EmotionAnalyzer, AttentionTracker,
    Visualizer, ReportGenerator
)

# Initialize all components
attendance = Attendance()
emotion = EmotionAnalyzer()
attention = AttentionTracker()
visualizer = Visualizer()
reports = ReportGenerator()

# Run monitoring session
# ... (see examples/demo_comprehensive.py)
```

## 🖥️ Command-Line Interface

Camera Master provides convenient CLI commands:

### Attendance
```bash
# Register a new face
camera-master attendance --register "John Doe"

# Start monitoring
camera-master attendance --start --camera 0
```

### Emotion Analysis
```bash
camera-master emotion --start --camera 0
```

### Gesture Recognition
```bash
camera-master gesture --start --camera 0
```

### Attention Tracking
```bash
camera-master attention --start --camera 0
```

### Mask Detection
```bash
camera-master mask --start --camera 0
```

### Fatigue Detection
```bash
camera-master fatigue --start --camera 0
```

### Spoof Detection
```bash
camera-master spoof --start --camera 0
```

### Gamification Dashboard
```bash
camera-master gamification --user "John Doe" --leaderboard
```

## 📚 Examples

Explore the `examples/` directory for complete working examples:

- `demo_attendance.py` - Basic attendance system
- `demo_emotion.py` - Emotion analysis with visualization
- `demo_comprehensive.py` - Full monitoring system with gamification

Run examples:
```bash
python examples/demo_attendance.py
python examples/demo_emotion.py
python examples/demo_comprehensive.py
```

## 🏗️ Package Structure

```
camera-master/
├── camera_master/
│   ├── __init__.py           # Package initialization
│   ├── attendance.py         # Face recognition attendance
│   ├── gesture.py            # Gesture recognition
│   ├── emotion.py            # Emotion analysis
│   ├── visualization.py      # Data visualization
│   ├── reports.py            # Report generation
│   ├── utils.py              # Utility functions
│   ├── attention.py          # Attention tracking
│   ├── mask_detection.py     # Mask detection
│   ├── age_gender.py         # Age/gender estimation
│   ├── fatigue.py            # Fatigue detection
│   ├── spoof.py              # Spoof detection
│   ├── mood_tracker.py       # Mood tracking
│   ├── access_control.py     # Access control
│   ├── gamification.py       # Gamification engine
│   └── cli.py                # Command-line interface
├── examples/
│   ├── demo_attendance.py
│   ├── demo_emotion.py
│   └── demo_comprehensive.py
├── setup.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 📊 Features Breakdown

### Attendance System
- **Face Detection**: Multiple backend support (OpenCV, SSD, MTCNN, RetinaFace)
- **Face Recognition**: Multiple models (VGG-Face, Facenet, OpenFace, ArcFace)
- **Database**: Local face database storage
- **Reports**: CSV/JSON export with timestamps

### Emotion Analysis
- **7 Emotions**: Happy, Sad, Angry, Fear, Surprise, Disgust, Neutral
- **Real-time Detection**: Frame-by-frame analysis
- **Confidence Scores**: Percentage for each emotion
- **Trend Analysis**: Mood tracking over time

### Gesture Recognition
- **Hand Detection**: MediaPipe Hands
- **Number Recognition**: 0-5 finger counting
- **Special Gestures**: OK, Thumbs up/down, Peace sign
- **Custom Training**: Train your own gestures

### Attention Tracking
- **Eye Tracking**: Eye Aspect Ratio (EAR) calculation
- **Head Pose**: Pitch, yaw, roll estimation
- **Attention Score**: Combined metric (0-1)
- **Drowsiness Alert**: Real-time warnings

### Fatigue Detection
- **Eye Closure**: Prolonged blink detection
- **Yawning**: Mouth aspect ratio analysis
- **Fatigue Levels**: Normal, Mild, Warning, Critical
- **Alerts**: Visual and audio warnings

### Gamification
- **Points System**: Earn points for engagement
- **Badges**: 8+ achievement badges
- **Levels**: Progressive leveling system
- **Leaderboards**: Compete with peers
- **Streaks**: Attendance streak tracking

## 🔧 Configuration

### Camera Settings
```python
# Use different camera
attendance = Attendance()
attendance.start_monitoring(camera_index=1)  # Use second camera
```

### Recognition Thresholds
```python
# Adjust recognition sensitivity
attendance = Attendance(
    model_name="Facenet",
    threshold=0.5,  # Lower = more strict
    detector_backend="retinaface"
)
```

### Attention Parameters
```python
# Customize attention tracking
tracker = AttentionTracker(
    ear_threshold=0.25,      # Eye closure threshold
    attention_threshold=0.5  # Minimum attention score
)
```

## 📈 Reports and Analytics

### Generate Reports
```python
from camera_master import ReportGenerator

report_gen = ReportGenerator()

# Attendance report
report_gen.generate_attendance_report(attendance_data, output_format='html')

# Emotion report
report_gen.generate_emotion_report(emotion_data, output_format='csv')

# Comprehensive report
report_gen.generate_comprehensive_report(
    attendance_data=attendance_df,
    emotion_data=emotion_df,
    attention_data=attention_df,
    output_format='html'
)
```

### Visualizations
```python
from camera_master import Visualizer

visualizer = Visualizer()

# Emotion distribution pie chart
visualizer.plot_emotion_distribution(emotion_df)

# Emotion timeline
visualizer.plot_emotion_timeline(emotion_df)

# Attention metrics
visualizer.plot_attention_metrics(attention_df)

# Complete dashboard
visualizer.create_dashboard(attendance_df, emotion_df, attention_df)
```

## 🎯 Use Cases

### Education
- **Classroom Monitoring**: Track student engagement and attention
- **Online Learning**: Monitor remote student participation
- **Attendance Management**: Automated attendance tracking
- **Behavior Analysis**: Understand student emotional patterns

### Corporate
- **Meeting Analytics**: Analyze meeting engagement
- **Training Assessment**: Monitor trainee attention
- **Security**: Face-based access control
- **HR Analytics**: Employee engagement metrics

### Healthcare
- **Patient Monitoring**: Track patient emotional state
- **Therapy Sessions**: Analyze emotional responses
- **Elderly Care**: Fatigue and attention monitoring

## 🛠️ Dependencies

- **opencv-python**: Computer vision
- **mediapipe**: Hand and face mesh detection
- **deepface**: Face recognition and analysis
- **numpy**: Numerical computing
- **pandas**: Data manipulation
- **matplotlib**: Visualization
- **pyttsx3**: Text-to-speech
- **streamlit**: Web dashboards
- **gradio**: ML interfaces
- **tensorflow**: Deep learning backend

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**RNS Sanjay**
- GitHub: [@RNSsanjay](https://github.com/RNSsanjay)

## 🙏 Acknowledgments

- DeepFace for face recognition
- MediaPipe for hand and face detection
- OpenCV for computer vision
- TensorFlow for deep learning

## 📞 Support

For support, please open an issue on GitHub or contact the maintainers.

## 🗺️ Roadmap

### Version 0.2.0
- [ ] Cloud sync (Firebase/Supabase)
- [ ] Real-time dashboards
- [ ] Mobile app integration
- [ ] Multi-camera support

### Version 0.3.0
- [ ] Advanced ML models
- [ ] Custom model training
- [ ] API endpoints
- [ ] Docker deployment

### Version 1.0.0
- [ ] Production-ready features
- [ ] Comprehensive documentation
- [ ] Performance optimization
- [ ] Enterprise features

## ⚠️ Disclaimer

This software is provided for educational and monitoring purposes. Ensure compliance with local privacy laws and regulations when using face recognition and monitoring technologies. Always obtain proper consent from individuals being monitored.

## 📊 Performance

- **Face Recognition**: ~100ms per frame (VGG-Face)
- **Emotion Detection**: ~150ms per frame
- **Gesture Recognition**: ~30ms per frame
- **Attention Tracking**: ~50ms per frame

Performance may vary based on hardware and model selection.

## 🔐 Privacy & Security

- **Local Processing**: All processing happens locally
- **No Cloud Required**: Works offline
- **Data Control**: You control all data
- **Encrypted Storage**: Option for encrypted face database

## 📱 Platform Support

- ✅ Windows 10/11
- ✅ Linux (Ubuntu 20.04+)
- ✅ macOS (10.15+)
- ⚠️ Raspberry Pi (limited performance)

---

Made with ❤️ by RNS Sanjay