"""
Demo: Unified Camera Integration
Shows all camera-based features working together using CameraManager
"""

from camera_master import CameraManager, UnifiedMonitoringSession


def demo_camera_manager():
    """
    Demonstrate CameraManager integrating multiple features
    """
    print("=" * 70)
    print("CAMERA MASTER - Unified Camera Integration Demo")
    print("=" * 70)
    print("\nThis demo shows all camera features working together!\n")
    # Create camera manager
    manager = CameraManager(camera_index=0)
    # Register features (only non-TensorFlow features for Python 3.13 compatibility)
    try:
        from camera_master import GestureRecognizer
        manager.register_feature('gesture', GestureRecognizer())
    except Exception as e:
        print(f"WARNING: Gesture: {e}")
    try:
        from camera_master import AttentionTracker
        manager.register_feature('attention', AttentionTracker())
    except Exception as e:
        print(f"WARNING: Attention: {e}")
    try:
        from camera_master import FatigueDetector
        manager.register_feature('fatigue', FatigueDetector())
    except Exception as e:
        print(f"WARNING: Fatigue: {e}")
    try:
        from camera_master import MaskDetector
        manager.register_feature('mask', MaskDetector())
    except Exception as e:
        print(f"WARNING: Mask: {e}")
    try:
        from camera_master import SpoofDetector
        spoof = SpoofDetector()
        spoof.start_liveness_check()  # Start automatic liveness checking
        manager.register_feature('spoof', spoof)
    except Exception as e:
        print(f"WARNING: Spoof: {e}")
    # Features that require TensorFlow (will fail on Python 3.13)
    print("\nWARNING: The following features require Python 3.11 and TensorFlow:")
    print(" - Attendance (Face Recognition)")
    print(" - Emotion Analysis")
    print(" - Age/Gender Estimation")
    print(" - Access Control")
    # Start integrated session (30 seconds)
    print("\n Starting 30-second integrated camera session...")
    print("Press 'q' to quit early\n")
    results = manager.start_integrated_session(duration=30, show_video=True)
    # Display summary
    print("\n" + manager.get_session_summary())
    # Show statistics
    if 'statistics' in results:
        print("\n FEATURE STATISTICS:")
        print("=" * 70)
        for feature_name, stats in results['statistics'].items():
            print(f"\n{feature_name.upper()}:")
            for key, value in stats.items():
                print(f"  {key}: {value}")
    return results


def demo_unified_monitoring():
    """
    Demonstrate UnifiedMonitoringSession (all features in one)
    """
    print("\n" + "=" * 70)
    print("CAMERA MASTER - Unified Monitoring Session Demo")
    print("=" * 70)
    print("\nComprehensive monitoring with all features!\n")
    # Create unified session
    session = UnifiedMonitoringSession(camera_index=0)
    # Start comprehensive monitoring
    # Note: TensorFlow features will be disabled on Python 3.13
    results = session.start_comprehensive_monitoring(
    enable_attendance=False, # Requires TensorFlow
    enable_emotion=False, # Requires TensorFlow
    enable_gesture=True,
    enable_attention=True,
    enable_fatigue=True,
    enable_mask=False, # Requires TensorFlow
    duration=30
    )
    print("\n[OK] Monitoring session complete!")
    print(f" Reports saved to: {results['session_info']}")
    return results


def demo_custom_feature_combination():
    """
    Demonstrate custom feature combinations
    """
    print("\n" + "=" * 70)
    print("CAMERA MASTER - Custom Feature Combination Demo")
    print("=" * 70)
    print("\nExample: Attention + Fatigue monitoring for drivers\n")
    manager = CameraManager(camera_index=0)
    # Register only attention and fatigue for driver monitoring
    try:
        from camera_master import AttentionTracker, FatigueDetector
        manager.register_feature('attention', AttentionTracker())
        manager.register_feature('fatigue', FatigueDetector())
        print(" Driver Monitoring System Active")
        print("Monitoring: Attention + Fatigue")
        print("Duration: 20 seconds")
        print("Press 'q' to quit\n")
        results = manager.start_integrated_session(duration=20, show_video=True)
        # Analyze results
        stats = results.get('statistics', {})
        if 'fatigue' in stats:
            fatigue_stats = stats['fatigue']
            print(f"\nWARNING: Fatigue Events: {fatigue_stats.get('successful_detections', 0)}")
        if 'attention' in stats:
            attention_stats = stats['attention']
            print(f" Attention Checks: {attention_stats.get('total_detections', 0)}")
        print("\n[OK] Driver monitoring complete!")
        return results
    except Exception as e:
        print(f"[X] Error: {e}")
        return None


def demo_gesture_only():
    """
    Demonstrate gesture recognition only (works on Python 3.13)
    """
    print("\n" + "=" * 70)
    print("CAMERA MASTER - Gesture Recognition Demo")
    print("=" * 70)
    print("\nGesture-based interaction (Python 3.13 compatible)\n")
    manager = CameraManager(camera_index=0)
    try:
        from camera_master import GestureRecognizer
        manager.register_feature('gesture', GestureRecognizer())
        print(" Gesture Recognition Active")
        print("Show hand gestures:")
        print(" • Numbers: 0-5 fingers")
        print(" • Thumbs up/down")
        print(" • OK sign")
        print(" • Peace sign")
        print("\nDuration: 20 seconds")
        print("Press 'q' to quit\n")
        results = manager.start_integrated_session(duration=20, show_video=True)
        # Analyze gestures
        if 'gesture' in results.get('feature_results', {}):
            gestures = results['feature_results']['gesture']
            gesture_names = [g.get('gesture') for g in gestures if g and 'gesture' in g]
            if gesture_names:
                from collections import Counter
                gesture_counts = Counter(gesture_names)
                print("\n GESTURE STATISTICS:")
                print("=" * 50)
                for gesture, count in gesture_counts.most_common():
                    print(f"  {gesture}: {count} times")
        return results
    except Exception as e:
        print(f"[X] Error: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    import sys
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║ CAMERA MASTER INTEGRATION DEMOS ║
╠═══════════════════════════════════════════════════════════════════╣
║ Choose a demo: ║
║ ║
║ 1. Camera Manager (Multi-feature integration) ║
║ 2. Unified Monitoring (Comprehensive session) ║
║ 3. Custom Combination (Attention + Fatigue) ║
║ 4. Gesture Only (Python 3.13 compatible) ║
║ 5. Run All Demos ║
║ ║
║ Note: Some features require Python 3.11 and TensorFlow ║
╚═══════════════════════════════════════════════════════════════════╝
""")
    choice = input("Enter your choice (1-5): ").strip()
    if choice == '1':
        demo_camera_manager()
    elif choice == '2':
        demo_unified_monitoring()
    elif choice == '3':
        demo_custom_feature_combination()
    elif choice == '4':
        demo_gesture_only()
    elif choice == '5':
        print("\n Running all demos...\n")
        demo_gesture_only()
        input("\nPress Enter to continue to next demo...")
        demo_custom_feature_combination()
        input("\nPress Enter to continue to next demo...")
        demo_camera_manager()
    else:
        print("Invalid choice. Running gesture demo (most compatible)...")
        demo_gesture_only()
    print("\n" + "=" * 70)
    print("[OK] Demo Complete!")
    print("=" * 70)
    print("\nNext steps:")
    print(" • Check generated reports in data/reports/")
    print(" • Try other examples: examples/demo_*.py")
    print(" • Read documentation: README.md")
    print(" • For full features, use Python 3.11 (see PYTHON_COMPATIBILITY.md)")
    print("=" * 70)
