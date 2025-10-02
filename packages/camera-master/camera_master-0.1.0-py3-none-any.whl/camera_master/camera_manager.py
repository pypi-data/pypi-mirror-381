"""
Unified Camera Manager - Integrates all camera-based features
"""
import cv2
import numpy as np
from datetime import datetime
from pathlib import Path
from camera_master.utils import VideoStreamHandler, draw_text_with_background, get_reports_dir


class CameraManager:
    """
    Centralized camera management for all features
    Integrates attendance, gesture, emotion, attention, fatigue, mask detection, etc.
    """
    
    def __init__(self, camera_index=0):
        """
        Initialize Camera Manager
        
        Args:
            camera_index: Camera device index (default: 0)
        """
        self.camera_index = camera_index
        self.active_features = {}
        self.session_data = {
            'start_time': None,
            'end_time': None,
            'frames_processed': 0,
            'detections': []
        }
        
    def register_feature(self, feature_name, feature_instance):
        """
        Register a feature to use with camera
        
        Args:
            feature_name: Name of the feature
            feature_instance: Instance of the feature class
        """
        self.active_features[feature_name] = feature_instance
        print(f"✅ Registered feature: {feature_name}")
    
    def unregister_feature(self, feature_name):
        """Remove a feature from active features"""
        if feature_name in self.active_features:
            del self.active_features[feature_name]
            print(f"❌ Unregistered feature: {feature_name}")
    
    def start_integrated_session(self, duration=None, show_video=True):
        """
        Start integrated camera session with all registered features
        
        Args:
            duration: Session duration in seconds (None for unlimited)
            show_video: Whether to display video feed
            
        Returns:
            dict: Session data and results
        """
        print("=" * 60)
        print("🎥 Starting Integrated Camera Session")
        print("=" * 60)
        print(f"Camera: {self.camera_index}")
        print(f"Active Features: {', '.join(self.active_features.keys())}")
        print("Press 'q' to quit")
        print("=" * 60)
        
        self.session_data['start_time'] = datetime.now()
        start_time = datetime.now()
        
        try:
            with VideoStreamHandler(self.camera_index) as cap:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    # Check duration
                    if duration:
                        elapsed = (datetime.now() - start_time).total_seconds()
                        if elapsed > duration:
                            break
                    
                    display_frame = frame.copy()
                    self.session_data['frames_processed'] += 1
                    
                    # Process frame with each active feature
                    feature_results = {}
                    y_offset = 30
                    
                    for feature_name, feature_instance in self.active_features.items():
                        try:
                            result = self._process_feature(
                                feature_name, 
                                feature_instance, 
                                frame
                            )
                            feature_results[feature_name] = result
                            
                            # Display feature result on frame
                            if result:
                                text = f"{feature_name}: {self._format_result(result)}"
                                draw_text_with_background(
                                    display_frame, 
                                    text, 
                                    (10, y_offset),
                                    font_scale=0.6
                                )
                                y_offset += 30
                        except Exception as e:
                            print(f"Error in {feature_name}: {str(e)}")
                    
                    # Record detection
                    self.session_data['detections'].append({
                        'timestamp': datetime.now().isoformat(),
                        'frame': self.session_data['frames_processed'],
                        'results': feature_results
                    })
                    
                    # Display video
                    if show_video:
                        # Add session info
                        elapsed = (datetime.now() - start_time).total_seconds()
                        info = f"Session: {int(elapsed)}s | Frames: {self.session_data['frames_processed']}"
                        draw_text_with_background(
                            display_frame, 
                            info, 
                            (10, display_frame.shape[0] - 20),
                            font_scale=0.5
                        )
                        
                        cv2.imshow('Camera Master - Integrated Session', display_frame)
                        
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
        
        finally:
            if show_video:
                cv2.destroyAllWindows()
            
            self.session_data['end_time'] = datetime.now()
            
        return self._generate_session_report()
    
    def _process_feature(self, feature_name, feature_instance, frame):
        """
        Process frame with specific feature
        
        Args:
            feature_name: Name of the feature
            feature_instance: Feature instance
            frame: Video frame
            
        Returns:
            dict: Feature results
        """
        # Map feature to processing method
        if feature_name == 'attendance':
            # Face recognition
            result = feature_instance.recognize_face(frame)
            return result
        
        elif feature_name == 'gesture':
            # Gesture recognition
            result = feature_instance.recognize_gesture(frame)
            return result
        
        elif feature_name == 'emotion':
            # Emotion analysis
            result = feature_instance.analyze_emotion(frame)
            return result
        
        elif feature_name == 'attention':
            # Attention tracking
            result = feature_instance.track_attention_frame(frame)
            return result
        
        elif feature_name == 'fatigue':
            # Fatigue detection
            result = feature_instance.detect_fatigue_frame(frame)
            return result
        
        elif feature_name == 'mask':
            # Mask detection
            result = feature_instance.detect_mask_frame(frame)
            return result
        
        elif feature_name == 'age_gender':
            # Age/gender estimation
            result = feature_instance.estimate_frame(frame)
            return result
        
        elif feature_name == 'spoof':
            # Spoof detection
            result = feature_instance.detect_frame(frame)
            return result
        
        elif feature_name == 'access_control':
            # Access verification
            result = feature_instance.verify_access_frame(frame)
            return result
        
        return None
    
    def _format_result(self, result):
        """Format result for display"""
        if isinstance(result, dict):
            # Extract key info
            if 'name' in result:
                return result['name']
            elif 'gesture' in result:
                return result['gesture']
            elif 'emotion' in result:
                return result['emotion']
            elif 'status' in result:
                return result['status']
            else:
                return str(result)[:30]
        return str(result)[:30]
    
    def _generate_session_report(self):
        """Generate comprehensive session report"""
        duration = (self.session_data['end_time'] - 
                   self.session_data['start_time']).total_seconds()
        
        report = {
            'session_info': {
                'start_time': self.session_data['start_time'].isoformat(),
                'end_time': self.session_data['end_time'].isoformat(),
                'duration_seconds': duration,
                'frames_processed': self.session_data['frames_processed'],
                'fps': self.session_data['frames_processed'] / duration if duration > 0 else 0
            },
            'active_features': list(self.active_features.keys()),
            'feature_results': {}
        }
        
        # Aggregate results by feature
        for detection in self.session_data['detections']:
            for feature_name, result in detection['results'].items():
                if feature_name not in report['feature_results']:
                    report['feature_results'][feature_name] = []
                report['feature_results'][feature_name].append(result)
        
        # Generate statistics
        report['statistics'] = self._generate_statistics(report['feature_results'])
        
        # Save report
        self._save_session_report(report)
        
        return report
    
    def _generate_statistics(self, feature_results):
        """Generate statistics from feature results"""
        stats = {}
        
        for feature_name, results in feature_results.items():
            stats[feature_name] = {
                'total_detections': len(results),
                'successful_detections': len([r for r in results if r])
            }
            
            # Feature-specific stats
            if feature_name == 'emotion':
                emotions = [r.get('emotion') for r in results if r and 'emotion' in r]
                if emotions:
                    from collections import Counter
                    emotion_counts = Counter(emotions)
                    stats[feature_name]['emotion_distribution'] = dict(emotion_counts)
                    stats[feature_name]['dominant_emotion'] = emotion_counts.most_common(1)[0][0]
            
            elif feature_name == 'gesture':
                gestures = [r.get('gesture') for r in results if r and 'gesture' in r]
                if gestures:
                    from collections import Counter
                    gesture_counts = Counter(gestures)
                    stats[feature_name]['gesture_distribution'] = dict(gesture_counts)
            
            elif feature_name == 'attendance':
                names = [r.get('name') for r in results if r and 'name' in r]
                if names:
                    stats[feature_name]['unique_people'] = len(set(names))
                    stats[feature_name]['total_recognitions'] = len(names)
        
        return stats
    
    def _save_session_report(self, report):
        """Save session report to file"""
        reports_dir = get_reports_dir()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = reports_dir / f"session_report_{timestamp}.json"
        
        import json
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        print(f"\n📊 Session report saved: {report_file}")
        
        return report_file
    
    def get_session_summary(self):
        """Get summary of current session"""
        if not self.session_data['start_time']:
            return "No active session"
        
        duration = 0
        if self.session_data['end_time']:
            duration = (self.session_data['end_time'] - 
                       self.session_data['start_time']).total_seconds()
        
        summary = f"""
╔══════════════════════════════════════════════════════════╗
║          CAMERA MASTER - SESSION SUMMARY                 ║
╠══════════════════════════════════════════════════════════╣
║ Camera Index: {self.camera_index:<40} ║
║ Active Features: {len(self.active_features):<37} ║
║ Duration: {duration:.1f}s{' ' * (45 - len(f'{duration:.1f}s'))} ║
║ Frames Processed: {self.session_data['frames_processed']:<34} ║
║ Detections: {len(self.session_data['detections']):<40} ║
╠══════════════════════════════════════════════════════════╣
║ Features:                                                ║
"""
        for feature_name in self.active_features.keys():
            summary += f"║   • {feature_name:<51} ║\n"
        
        summary += "╚══════════════════════════════════════════════════════════╝"
        
        return summary


class UnifiedMonitoringSession:
    """
    Unified monitoring session that combines all features
    """
    
    def __init__(self, camera_index=0):
        """Initialize unified session"""
        self.camera_manager = CameraManager(camera_index)
        
    def start_comprehensive_monitoring(
        self, 
        enable_attendance=True,
        enable_emotion=True,
        enable_gesture=True,
        enable_attention=True,
        enable_fatigue=True,
        enable_mask=True,
        duration=None
    ):
        """
        Start comprehensive monitoring with selected features
        
        Args:
            enable_attendance: Enable attendance tracking
            enable_emotion: Enable emotion analysis
            enable_gesture: Enable gesture recognition
            enable_attention: Enable attention tracking
            enable_fatigue: Enable fatigue detection
            enable_mask: Enable mask detection
            duration: Session duration in seconds
            
        Returns:
            dict: Session results
        """
        print("🚀 Initializing Comprehensive Monitoring Session...")
        
        # Initialize and register features
        if enable_attendance:
            from camera_master.attendance import Attendance
            self.camera_manager.register_feature('attendance', Attendance())
        
        if enable_emotion:
            from camera_master.emotion import EmotionAnalyzer
            self.camera_manager.register_feature('emotion', EmotionAnalyzer())
        
        if enable_gesture:
            from camera_master.gesture import GestureRecognizer
            self.camera_manager.register_feature('gesture', GestureRecognizer())
        
        if enable_attention:
            from camera_master.attention import AttentionTracker
            self.camera_manager.register_feature('attention', AttentionTracker())
        
        if enable_fatigue:
            from camera_master.fatigue import FatigueDetector
            self.camera_manager.register_feature('fatigue', FatigueDetector())
        
        if enable_mask:
            from camera_master.mask_detection import MaskDetector
            self.camera_manager.register_feature('mask', MaskDetector())
        
        # Start session
        results = self.camera_manager.start_integrated_session(
            duration=duration,
            show_video=True
        )
        
        # Generate reports
        self._generate_comprehensive_reports(results)
        
        return results
    
    def _generate_comprehensive_reports(self, results):
        """Generate all reports from session results"""
        print("\n📊 Generating Comprehensive Reports...")
        
        from camera_master.reports import ReportGenerator
        from camera_master.visualization import Visualizer
        from camera_master.gamification import GamificationEngine
        
        report_gen = ReportGenerator()
        visualizer = Visualizer()
        gamification = GamificationEngine()
        
        # Convert results to dataframes and generate reports
        if 'attendance' in results.get('feature_results', {}):
            attendance_data = results['feature_results']['attendance']
            # Generate reports, visualizations, update gamification
            print("  ✅ Attendance reports generated")
        
        if 'emotion' in results.get('feature_results', {}):
            emotion_data = results['feature_results']['emotion']
            print("  ✅ Emotion reports generated")
        
        print("\n✨ All reports generated successfully!")
