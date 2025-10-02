"""
Camera Master - Simple Installation Test (Python 3.13 Compatible)
Tests only the dependencies that work with Python 3.13
"""

import sys

print("=" * 60)
print("CAMERA MASTER - Simple Installation Test (Python 3.13)")
print("=" * 60)
print(f"Python Version: {sys.version}")
print("-" * 60)

# Test basic dependencies
dependencies = {
    "opencv-python (cv2)": "cv2",
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "mediapipe": "mediapipe",
    "pyttsx3": "pyttsx3",
}

working = []
failed = []

print("\nTesting Python 3.13 Compatible Dependencies:")
print("-" * 60)

for name, module in dependencies.items():
    try:
        if module == "cv2":
            import cv2
            version = cv2.__version__
        elif module == "numpy":
            import numpy as np
            version = np.__version__
        elif module == "pandas":
            import pandas as pd
            version = pd.__version__
        elif module == "matplotlib":
            import matplotlib
            version = matplotlib.__version__
        elif module == "mediapipe":
            import mediapipe as mp
            version = mp.__version__
        elif module == "pyttsx3":
            import pyttsx3
            version = "installed"
        print(f"[OK] {name}: {version}")
        working.append(name)
    except Exception as e:
        print(f"[X] {name}: {str(e)}")
        failed.append(name)

print("-" * 60)

# Test TensorFlow separately with better error handling
print("\nTesting TensorFlow (May not work on Python 3.13):")
print("-" * 60)
try:
    import tensorflow as tf
    print(f"[OK] tensorflow: {tf.__version__}")
    working.append("tensorflow")
except Exception as e:
    print(f"WARNING: tensorflow: Not compatible with Python 3.13")
    print(f" Error: {str(e)[:100]}...")
    print(f" Note: TensorFlow currently supports Python 3.8-3.11")
    failed.append("tensorflow (expected)")

try:
    from deepface import DeepFace
    print(f"[OK] deepface: installed")
    working.append("deepface")
except Exception as e:
    print(f"WARNING: deepface: Requires TensorFlow")
    failed.append("deepface (expected)")

print("-" * 60)

# Test camera_master modules that don't need TensorFlow
print("\nTesting Camera Master Modules (TensorFlow-free):")
print("-" * 60)

tensorflow_free_modules = {
    "utils": "camera_master.utils",
    "visualization": "camera_master.visualization",
    "reports": "camera_master.reports",
    "gamification": "camera_master.gamification",
    "mood_tracker": "camera_master.mood_tracker",
}

for name, module in tensorflow_free_modules.items():
    try:
        __import__(module)
        print(f"[OK] {name}: OK")
        working.append(f"camera_master.{name}")
    except ImportError as e:
        if "tensorflow" in str(e).lower() or "deepface" in str(e).lower():
            print(f"WARNING: {name}: Requires TensorFlow")
        else:
            print(f"[X] {name}: {str(e)}")
            failed.append(f"camera_master.{name}")

print("-" * 60)

# Summary
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"[OK] Working: {len(working)} components")
print(f"[X] Failed: {len([f for f in failed if 'expected' not in f])} components")
print(f"WARNING: Expected Failures (Python 3.13): {len([f for f in failed if 'expected' in f])}")

if len([f for f in failed if 'expected' not in f]) == 0:
    print("\n[OK] All Python 3.13 compatible features are working!")
    print("\n NOTE: For FULL functionality (face recognition, emotion analysis),")
    print(" please use Python 3.11 (see PYTHON_COMPATIBILITY.md)")
else:
    print("\n[X] Some components failed. Please install:")
    print(" pip install opencv-python numpy pandas matplotlib mediapipe pyttsx3")

print("\n" + "=" * 60)
print("FEATURES AVAILABLE WITH YOUR SETUP:")
print("=" * 60)
if "mediapipe" in working:
    print("[OK] Gesture Recognition (MediaPipe)")
if "opencv-python (cv2)" in working:
    print("[OK] Attention Tracking")
    print("[OK] Fatigue Detection")
    print("[OK] Spoof Detection (Blink Detection)")
    print("[OK] Mask Detection")
if "matplotlib" in working:
    print("[OK] Data Visualization")
if "pandas" in working:
    print("[OK] Report Generation")
    print("[OK] Mood Tracking")
    print("[OK] Gamification")

print("\nWARNING: FEATURES REQUIRING PYTHON 3.11:")
print("=" * 60)
print("[X] Face Recognition Attendance (requires DeepFace/TensorFlow)")
print("[X] Emotion Analysis (requires DeepFace)")
print("[X] Age/Gender Estimation (requires DeepFace)")
print("[X] Access Control (requires DeepFace)")

print("\n" + "=" * 60)
print("NEXT STEPS:")
print("=" * 60)
print("1. [OK] Your Python 3.13 setup can use gesture, attention, fatigue features")
print("2. Read PYTHON_COMPATIBILITY.md for full details")
print("3. To use ALL features, install Python 3.11 and create new venv")
print(" py -3.11 -m venv .venv311")
print(" .\\.venv311\\Scripts\\Activate.ps1")
print(" pip install -r requirements.txt")
print("=" * 60)
