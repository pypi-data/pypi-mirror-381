"""
Simple test script to verify installation
"""
import sys

def test_imports():
    """Test if all modules can be imported"""
    print("Testing camera-master package imports...")
    print("-" * 50)
    
    modules = [
        "camera_master",
        "camera_master.attendance",
        "camera_master.gesture",
        "camera_master.emotion",
        "camera_master.visualization",
        "camera_master.reports",
        "camera_master.utils",
        "camera_master.attention",
        "camera_master.mask_detection",
        "camera_master.age_gender",
        "camera_master.fatigue",
        "camera_master.spoof",
        "camera_master.mood_tracker",
        "camera_master.access_control",
        "camera_master.gamification",
    ]
    
    failed = []
    for module in modules:
        try:
            __import__(module)
            print(f"  {module}")
        except Exception as e:
            print(f"  {module}: {str(e)}")
            failed.append((module, str(e)))
    
    print("-" * 50)
    
    if failed:
        print(f"\n[X] {len(failed)} modules failed to import:")
        for module, error in failed:
            print(f"  • {module}: {error}")
        return False
    else:
        print(f"\n[OK] All {len(modules)} modules imported successfully!")
        return True


def test_dependencies():
    """Test if required dependencies are available"""
    print("\nTesting dependencies...")
    print("-" * 50)
    
    dependencies = [
        "cv2",
        "mediapipe",
        "deepface",
        "numpy",
        "pandas",
        "matplotlib",
    ]
    
    failed = []
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"  {dep}")
        except Exception as e:
            print(f"  {dep}: {str(e)}")
            failed.append((dep, str(e)))
    
    print("-" * 50)
    
    if failed:
        print(f"\n[X] {len(failed)} dependencies missing:")
        for dep, error in failed:
            print(f"  • {dep}: {error}")
        print("\nInstall missing dependencies:")
        print("  pip install -r requirements.txt")
        return False
    else:
        print(f"\n[OK] All {len(dependencies)} dependencies available!")
        return True


def test_classes():
    """Test if main classes can be instantiated"""
    print("\nTesting class instantiation...")
    print("-" * 50)
    
    tests = []
    
    try:
        from camera_master import Attendance
        att = Attendance()
        print("  Attendance")
        tests.append(True)
    except Exception as e:
        print(f"  Attendance: {e}")
        tests.append(False)
    
    try:
        from camera_master import GestureRecognizer
        gest = GestureRecognizer()
        print("  GestureRecognizer")
        tests.append(True)
    except Exception as e:
        print(f"  GestureRecognizer: {e}")
        tests.append(False)
    
    try:
        from camera_master import EmotionAnalyzer
        emo = EmotionAnalyzer()
        print("  EmotionAnalyzer")
        tests.append(True)
    except Exception as e:
        print(f"  EmotionAnalyzer: {e}")
        tests.append(False)
    
    try:
        from camera_master import Visualizer
        viz = Visualizer()
        print("  Visualizer")
        tests.append(True)
    except Exception as e:
        print(f"  Visualizer: {e}")
        tests.append(False)
    
    try:
        from camera_master import ReportGenerator
        rep = ReportGenerator()
        print("  ReportGenerator")
        tests.append(True)
    except Exception as e:
        print(f"  ReportGenerator: {e}")
        tests.append(False)
    
    try:
        from camera_master import GamificationEngine
        game = GamificationEngine()
        print("  GamificationEngine")
        tests.append(True)
    except Exception as e:
        print(f"  GamificationEngine: {e}")
        tests.append(False)
    
    print("-" * 50)
    
    if all(tests):
        print(f"\n[OK] All {len(tests)} classes instantiated successfully!")
        return True
    else:
        print(f"\n[X] {tests.count(False)} classes failed to instantiate")
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 50)
    print("CAMERA MASTER - Installation Test")
    print("=" * 50)
    
    results = []
    
    # Test imports
    results.append(test_imports())
    
    # Test dependencies
    results.append(test_dependencies())
    
    # Test class instantiation
    results.append(test_classes())
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    if all(results):
        print("[OK] All tests passed!")
        print("\nCamera Master is ready to use!")
        print("\nTry running:")
        print("  python examples/demo_attendance.py")
        print("  camera-master --help")
        return 0
    else:
        print("[X] Some tests failed")
        print("\nPlease fix the issues above before using the package.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
