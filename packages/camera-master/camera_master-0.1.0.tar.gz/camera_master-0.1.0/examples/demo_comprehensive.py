"""
Example: Complete monitoring system
"""
from camera_master import (
    Attendance, EmotionAnalyzer, AttentionTracker,
    GestureRecognizer, Visualizer, ReportGenerator,
    GamificationEngine
)
import threading
import time
from datetime import datetime

class ComprehensiveMonitor:
    """Complete monitoring system integrating all features"""
    
    def __init__(self, user_name="Student"):
        self.user_name = user_name
        
        # Initialize components
        self.attendance = Attendance()
        self.emotion_analyzer = EmotionAnalyzer()
        self.attention_tracker = AttentionTracker()
        self.visualizer = Visualizer()
        self.report_gen = ReportGenerator()
        self.gamification = GamificationEngine()
        
        # Initialize user
        self.gamification.initialize_user(user_name)
        
        self.running = False
        
    def emotion_callback(self, emotion_data):
        """Callback for emotion events"""
        if emotion_data['dominant_emotion'] in ['happy', 'surprise']:
            # Award points for positive emotion
            if hasattr(self, 'last_positive_point') and \
               (datetime.now() - self.last_positive_point).seconds < 60:
                return
            
            self.gamification.add_points(self.user_name, 2, "Positive emotion")
            self.last_positive_point = datetime.now()
    
    def attention_callback(self, attention_data):
        """Callback for attention events"""
        if attention_data['is_attentive']:
            if hasattr(self, 'last_attention_point') and \
               (datetime.now() - self.last_attention_point).seconds < 60:
                return
            
            self.gamification.add_points(self.user_name, 1, "High attention")
            self.last_attention_point = datetime.now()
    
    def run_monitoring(self, duration_minutes=5):
        """Run comprehensive monitoring"""
        print("\n" + "=" * 60)
        print(f"🎯 COMPREHENSIVE MONITORING - {self.user_name}")
        print("=" * 60)
        print(f"Duration: {duration_minutes} minutes")
        print("Press 'q' in any window to stop")
        print("-" * 60)
        
        # Record attendance
        self.gamification.record_attendance(self.user_name)
        print(f"✓ Attendance recorded for {self.user_name}")
        
        # Start monitoring (simplified - in production, run in parallel)
        print("\n📹 Starting video analysis...")
        print("Window will open - showing emotion and attention metrics")
        
        import cv2
        from camera_master.utils import VideoStreamHandler
        
        start_time = datetime.now()
        frame_count = 0
        
        self.last_positive_point = datetime.now()
        self.last_attention_point = datetime.now()
        
        with VideoStreamHandler(0) as cap:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                
                # Process every 5th frame for performance
                if frame_count % 5 == 0:
                    # Emotion analysis
                    emotion_frame, emotions = self.emotion_analyzer.process_frame(frame.copy())
                    if emotions:
                        self.emotion_callback(emotions[0])
                    
                    # Attention tracking
                    attention_frame, attention = self.attention_tracker.process_frame(frame.copy())
                    if attention:
                        self.attention_callback(attention)
                    
                    # Use attention frame (has more info)
                    display_frame = attention_frame if attention else emotion_frame
                else:
                    display_frame = frame
                
                # Display time remaining
                elapsed = (datetime.now() - start_time).seconds
                remaining = max(0, duration_minutes * 60 - elapsed)
                
                time_text = f"Time: {remaining//60}:{remaining%60:02d}"
                cv2.putText(display_frame, time_text, (10, display_frame.shape[0] - 50),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                
                cv2.imshow('Comprehensive Monitoring', display_frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q') or elapsed >= duration_minutes * 60:
                    break
        
        cv2.destroyAllWindows()
        
        # Generate report
        print("\n" + "=" * 60)
        print("📊 GENERATING REPORTS")
        print("=" * 60)
        
        # Get data
        emotion_df = self.emotion_analyzer.get_emotion_report()
        attention_df = self.attention_tracker.get_attention_report()
        
        # Generate comprehensive report
        report_path = self.report_gen.generate_comprehensive_report(
            emotion_data=emotion_df,
            attention_data=attention_df,
            output_format='html'
        )
        print(f"✓ Comprehensive report: {report_path}")
        
        # Create dashboard visualization
        dashboard_path = self.visualizer.create_dashboard(
            emotion_df=emotion_df,
            attention_df=attention_df
        )
        print(f"✓ Dashboard visualization: {dashboard_path}")
        
        # Check achievements
        print("\n" + "=" * 60)
        print("🏆 CHECKING ACHIEVEMENTS")
        print("=" * 60)
        
        # Emotion achievements
        emotion_stats = self.emotion_analyzer.get_emotion_statistics()
        positive_percentage = emotion_stats['emotion_percentages'].get('happy', 0) + \
                            emotion_stats['emotion_percentages'].get('surprise', 0)
        
        if positive_percentage > 60:
            self.gamification.check_emotion_achievement(self.user_name, duration_minutes)
        
        # Attention achievements
        attention_stats = self.attention_tracker.get_statistics()
        self.gamification.check_attention_achievement(
            self.user_name,
            attention_stats['attention_rate'],
            duration_minutes
        )
        
        # Show gamification dashboard
        print("\n" + "=" * 60)
        self.gamification.display_user_dashboard(self.user_name)
        
        print("\n✅ Monitoring session complete!")


def main():
    print("Camera Master - Comprehensive Monitoring Demo")
    print("=" * 60)
    
    # Get user name
    user_name = input("Enter your name: ").strip()
    if not user_name:
        user_name = "Student"
    
    # Get duration
    try:
        duration = int(input("Enter monitoring duration in minutes (default 5): ") or "5")
    except:
        duration = 5
    
    # Create monitor
    monitor = ComprehensiveMonitor(user_name=user_name)
    
    # Run monitoring
    monitor.run_monitoring(duration_minutes=duration)


if __name__ == "__main__":
    main()
