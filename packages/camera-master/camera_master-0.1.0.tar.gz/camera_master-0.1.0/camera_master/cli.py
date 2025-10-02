"""
Command-line interface for camera-master
"""
import argparse
import sys
from camera_master.attendance import Attendance
from camera_master.gesture import GestureRecognizer
from camera_master.emotion import EmotionAnalyzer
from camera_master.attention import AttentionTracker
from camera_master.mask_detection import MaskDetector
from camera_master.age_gender import AgeGenderEstimator
from camera_master.fatigue import FatigueDetector
from camera_master.spoof import SpoofDetector
from camera_master.gamification import GamificationEngine


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Camera Master - AI-Powered Education Monitoring',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Attendance command
    attendance_parser = subparsers.add_parser('attendance', help='Face recognition attendance')
    attendance_parser.add_argument('--register', type=str, help='Register new person')
    attendance_parser.add_argument('--start', action='store_true', help='Start attendance monitoring')
    attendance_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    attendance_parser.add_argument('--duration', type=int, help='Monitoring duration in seconds')
    
    # Gesture command
    gesture_parser = subparsers.add_parser('gesture', help='Gesture recognition')
    gesture_parser.add_argument('--start', action='store_true', help='Start gesture recognition')
    gesture_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Emotion command
    emotion_parser = subparsers.add_parser('emotion', help='Emotion analysis')
    emotion_parser.add_argument('--start', action='store_true', help='Start emotion analysis')
    emotion_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Attention command
    attention_parser = subparsers.add_parser('attention', help='Attention tracking')
    attention_parser.add_argument('--start', action='store_true', help='Start attention tracking')
    attention_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Mask detection command
    mask_parser = subparsers.add_parser('mask', help='Mask detection')
    mask_parser.add_argument('--start', action='store_true', help='Start mask detection')
    mask_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Age/Gender command
    age_gender_parser = subparsers.add_parser('age-gender', help='Age and gender estimation')
    age_gender_parser.add_argument('--start', action='store_true', help='Start estimation')
    age_gender_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Fatigue command
    fatigue_parser = subparsers.add_parser('fatigue', help='Fatigue detection')
    fatigue_parser.add_argument('--start', action='store_true', help='Start fatigue detection')
    fatigue_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Spoof command
    spoof_parser = subparsers.add_parser('spoof', help='Spoof detection (liveness check)')
    spoof_parser.add_argument('--start', action='store_true', help='Start spoof detection')
    spoof_parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    # Gamification command
    gamification_parser = subparsers.add_parser('gamification', help='Gamification dashboard')
    gamification_parser.add_argument('--user', type=str, required=True, help='User name')
    gamification_parser.add_argument('--leaderboard', action='store_true', help='Show leaderboard')
    
    # Dashboard command
    dashboard_parser = subparsers.add_parser('dashboard', help='Launch web dashboard')
    dashboard_parser.add_argument('--port', type=int, default=8501, help='Dashboard port')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Execute commands
    if args.command == 'attendance':
        attendance_cli_handler(args)
    elif args.command == 'gesture':
        gesture_cli_handler(args)
    elif args.command == 'emotion':
        emotion_cli_handler(args)
    elif args.command == 'attention':
        attention_cli_handler(args)
    elif args.command == 'mask':
        mask_cli_handler(args)
    elif args.command == 'age-gender':
        age_gender_cli_handler(args)
    elif args.command == 'fatigue':
        fatigue_cli_handler(args)
    elif args.command == 'spoof':
        spoof_cli_handler(args)
    elif args.command == 'gamification':
        gamification_cli_handler(args)
    elif args.command == 'dashboard':
        dashboard_cli_handler(args)


def attendance_cli():
    """Attendance CLI entry point"""
    parser = argparse.ArgumentParser(description='Face recognition attendance')
    parser.add_argument('--register', type=str, help='Register new person')
    parser.add_argument('--start', action='store_true', help='Start attendance monitoring')
    parser.add_argument('--camera', type=int, default=0, help='Camera index')
    parser.add_argument('--duration', type=int, help='Monitoring duration in seconds')
    
    args = parser.parse_args()
    attendance_cli_handler(args)


def attendance_cli_handler(args):
    """Handle attendance commands"""
    attendance = Attendance()
    
    if args.register:
        print(f"Registering new person: {args.register}")
        success = attendance.register_face(args.register, camera_index=args.camera)
        if success:
            print("✓ Face registered successfully")
        else:
            print("✗ Registration failed")
    
    elif args.start:
        print("Starting attendance monitoring...")
        df = attendance.start_monitoring(camera_index=args.camera, duration=args.duration)
        
        # Save report
        report_path = attendance.save_report()
        print(f"\n📊 Attendance Report: {report_path}")
        
        # Show statistics
        stats = attendance.get_statistics()
        print(f"\n📈 Statistics:")
        print(f"  Present: {stats['total_present']}")
        print(f"  Registered: {stats['total_registered']}")
        print(f"  Rate: {stats['attendance_rate']:.1f}%")


def gesture_cli():
    """Gesture CLI entry point"""
    parser = argparse.ArgumentParser(description='Gesture recognition')
    parser.add_argument('--start', action='store_true', help='Start gesture recognition')
    parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    args = parser.parse_args()
    gesture_cli_handler(args)


def gesture_cli_handler(args):
    """Handle gesture commands"""
    recognizer = GestureRecognizer()
    
    if args.start:
        print("Starting gesture recognition...")
        recognizer.start_recognition(camera_index=args.camera)


def emotion_cli():
    """Emotion CLI entry point"""
    parser = argparse.ArgumentParser(description='Emotion analysis')
    parser.add_argument('--start', action='store_true', help='Start emotion analysis')
    parser.add_argument('--camera', type=int, default=0, help='Camera index')
    
    args = parser.parse_args()
    emotion_cli_handler(args)


def emotion_cli_handler(args):
    """Handle emotion commands"""
    analyzer = EmotionAnalyzer()
    
    if args.start:
        print("Starting emotion analysis...")
        analyzer.start_analysis(camera_index=args.camera)
        
        # Save report
        report_path = analyzer.save_report()
        if report_path:
            print(f"\n📊 Emotion Report: {report_path}")
        
        # Show statistics
        stats = analyzer.get_emotion_statistics()
        print(f"\n📈 Statistics:")
        print(f"  Total Detections: {stats['total_detections']}")
        print(f"  Dominant Emotion: {stats['dominant_emotion']}")


def attention_cli_handler(args):
    """Handle attention commands"""
    tracker = AttentionTracker()
    
    if args.start:
        print("Starting attention tracking...")
        tracker.start_tracking(camera_index=args.camera)
        
        # Show statistics
        stats = tracker.get_statistics()
        print(f"\n📈 Statistics:")
        print(f"  Average Attention: {stats['average_attention']:.2f}")
        print(f"  Attention Rate: {stats['attention_rate']:.1f}%")
        print(f"  Drowsiness Rate: {stats['drowsiness_rate']:.1f}%")


def mask_cli_handler(args):
    """Handle mask detection commands"""
    detector = MaskDetector()
    
    if args.start:
        print("Starting mask detection...")
        detector.start_detection(camera_index=args.camera)
        
        # Show statistics
        stats = detector.get_statistics()
        print(f"\n📈 Statistics:")
        print(f"  Mask Compliance: {stats['mask_compliance_rate']:.1f}%")


def age_gender_cli_handler(args):
    """Handle age/gender commands"""
    estimator = AgeGenderEstimator()
    
    if args.start:
        print("Starting age/gender estimation...")
        estimator.start_estimation(camera_index=args.camera)


def fatigue_cli_handler(args):
    """Handle fatigue detection commands"""
    detector = FatigueDetector()
    
    if args.start:
        print("Starting fatigue detection...")
        detector.start_detection(camera_index=args.camera)
        
        # Show statistics
        stats = detector.get_statistics()
        print(f"\n📈 Statistics:")
        print(f"  Drowsy Events: {stats['total_drowsy_events']}")
        print(f"  Yawns: {stats['total_yawns']}")
        print(f"  Fatigue Risk: {stats['fatigue_risk']}")


def spoof_cli_handler(args):
    """Handle spoof detection commands"""
    detector = SpoofDetector()
    
    if args.start:
        print("Starting spoof detection...")
        detector.start_detection(camera_index=args.camera, auto_liveness_check=True)


def gamification_cli_handler(args):
    """Handle gamification commands"""
    engine = GamificationEngine()
    
    if args.leaderboard:
        leaderboard = engine.get_leaderboard()
        print("\n" + "="*60)
        print("🏆 LEADERBOARD")
        print("="*60)
        for i, entry in enumerate(leaderboard, 1):
            print(f"{i}. {entry['name']}: {entry['points']} pts (Level {entry['level']}, {entry['badges_count']} badges)")
        print("="*60 + "\n")
    
    if args.user:
        engine.display_user_dashboard(args.user)


def dashboard_cli():
    """Dashboard CLI entry point"""
    parser = argparse.ArgumentParser(description='Launch web dashboard')
    parser.add_argument('--port', type=int, default=8501, help='Dashboard port')
    
    args = parser.parse_args()
    dashboard_cli_handler(args)


def dashboard_cli_handler(args):
    """Handle dashboard commands"""
    print(f"Launching dashboard on port {args.port}...")
    print("Note: Dashboard requires Streamlit. Run 'streamlit run camera_master/dashboard_app.py'")


if __name__ == '__main__':
    main()
