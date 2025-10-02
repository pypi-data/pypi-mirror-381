# Python Compatibility Guide

## Current Issue: Python 3.13 + TensorFlow

### Problem
You're running **Python 3.13**, but TensorFlow (required by DeepFace) currently only supports **Python 3.8-3.11**.

### Error Message
```
ImportError: DLL load failed while importing _pywrap_tensorflow_internal
```

## Solutions

### Option 1: Use Python 3.11 (Recommended)

**Install Python 3.11:**
1. Download Python 3.11 from https://www.python.org/downloads/
2. Install it alongside Python 3.13
3. Create a new virtual environment:
 ```powershell
 py -3.11 -m venv venv311
 .\venv311\Scripts\Activate.ps1
 pip install -r requirements.txt
 ```

### Option 2: Use Only Non-TensorFlow Features

You can still use features that don't require TensorFlow:

**Working Features (No TensorFlow needed):**
- [OK] Gesture Recognition (MediaPipe)
- [OK] Attention Tracking (OpenCV)
- [OK] Fatigue Detection (OpenCV)
- [OK] Spoof Detection (OpenCV)
- [OK] Mask Detection (OpenCV)
- [OK] Visualization
- [OK] Reports
- [OK] Gamification
- [OK] Mood Tracking

**Features Requiring TensorFlow:**
- WARNING: Attendance (Face Recognition with DeepFace)
- WARNING: Emotion Analysis (DeepFace)
- WARNING: Age/Gender Estimation (DeepFace)
- WARNING: Access Control (DeepFace)

**Install minimal dependencies:**
```powershell
pip install opencv-python mediapipe numpy pandas matplotlib pyttsx3
```

### Option 3: Wait for TensorFlow 2.17+

TensorFlow team is working on Python 3.13 support. Check:
- https://github.com/tensorflow/tensorflow/issues
- Expected in TensorFlow 2.17 or later

### Option 4: Use Docker (Advanced)

Create a container with Python 3.11:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "examples/demo_comprehensive.py"]
```

## Quick Test Without TensorFlow

Create a test file `test_no_tensorflow.py`:

```python
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("[OK] OpenCV:", cv2.__version__)
print("[OK] MediaPipe:", mp.__version__)
print("[OK] NumPy:", np.__version__)
print("[OK] Pandas:", pd.__version__)
print("[OK] Matplotlib:", plt.matplotlib.__version__)

print("\n All non-TensorFlow dependencies working!")
```

Run:
```powershell
python test_no_tensorflow.py
```

## Verify Your Python Version

```powershell
python --version
```

Your current version: **Python 3.13**

## Recommended Action

**For full functionality**, switch to Python 3.11:

```powershell
# Check if you have Python 3.11 installed
py -3.11 --version

# If yes, create virtual environment
py -3.11 -m venv .venv311
.\.venv311\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Test
python test_installation.py
```

## Support Matrix

| Python Version | Status | TensorFlow | DeepFace | All Features |
|---------------|--------|-----------|----------|--------------|
| 3.8 | [OK] Supported | [OK] Yes | [OK] Yes | [OK] Yes |
| 3.9 | [OK] Supported | [OK] Yes | [OK] Yes | [OK] Yes |
| 3.10 | [OK] Supported | [OK] Yes | [OK] Yes | [OK] Yes |
| 3.11 | [OK] Recommended | [OK] Yes | [OK] Yes | [OK] Yes |
| 3.12 | WARNING: Limited | WARNING: Beta | WARNING: Limited | WARNING: Partial |
| 3.13 | [X] Not Yet | [X] No | [X] No | WARNING: Partial |

## Questions?

- Check TensorFlow compatibility: https://www.tensorflow.org/install
- Check DeepFace issues: https://github.com/serengil/deepface
- Camera Master docs: README.md
