"""
Example: Emotion analysis demo
"""
from camera_master import EmotionAnalyzer, Visualizer

def main():
    print("Camera Master - Emotion Analysis Demo")
    print("=" * 50)
    
    analyzer = EmotionAnalyzer()
    
    print("\nStarting emotion analysis...")
    print("Press 'q' to quit")
    print("-" * 50)
    
    # Start analysis
    analyzer.start_analysis(camera_index=0)
    
    # Get results
    print("\n" + "=" * 50)
    print("EMOTION ANALYSIS RESULTS")
    print("=" * 50)
    
    # Statistics
    stats = analyzer.get_emotion_statistics()
    print(f"\n📊 Total Detections: {stats['total_detections']}")
    print(f"😊 Dominant Emotion: {stats['dominant_emotion']}")
    
    print(f"\n📈 Emotion Distribution:")
    for emotion, percentage in stats['emotion_percentages'].items():
        if percentage > 0:
            print(f"  • {emotion.capitalize()}: {percentage:.1f}%")
    
    # Mood trend
    trend = analyzer.get_mood_trend()
    print(f"\n📉 Mood Trend: {trend}")
    
    # Save report
    report_path = analyzer.save_report()
    if report_path:
        print(f"\n💾 Report saved: {report_path}")
    
    # Create visualization
    visualize = input("\nCreate visualization? (y/n): ")
    if visualize.lower() == 'y':
        visualizer = Visualizer()
        
        # Get emotion data
        df = analyzer.get_emotion_report()
        
        # Create plots
        print("\nGenerating visualizations...")
        plot1 = visualizer.plot_emotion_distribution(emotion_df=df)
        plot2 = visualizer.plot_emotion_timeline(df)
        
        print(f"✓ Emotion distribution plot: {plot1}")
        print(f"✓ Emotion timeline plot: {plot2}")


if __name__ == "__main__":
    main()
