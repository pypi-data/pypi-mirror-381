"""
Data visualization for attendance, emotions, and engagement metrics
"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from camera_master.utils import get_reports_dir


class Visualizer:
    """
    Create visualizations for monitoring data
    """
    
    def __init__(self):
        """Initialize Visualizer"""
        self.reports_dir = get_reports_dir()
        plt.style.use('default')
    
    def plot_attendance_over_time(self, attendance_df, save_path=None):
        """
        Plot attendance over time
        
        Args:
            attendance_df: DataFrame with attendance records
            save_path: Path to save plot
            
        Returns:
            str: Path to saved plot
        """
        if attendance_df.empty:
            print("No attendance data to visualize")
            return None
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Convert timestamp to datetime if needed
        if 'timestamp' in attendance_df.columns:
            attendance_df['timestamp'] = pd.to_datetime(attendance_df['timestamp'])
            
            # Group by date
            daily_attendance = attendance_df.groupby(
                attendance_df['timestamp'].dt.date
            ).size()
            
            ax.plot(daily_attendance.index, daily_attendance.values, 
                   marker='o', linewidth=2, markersize=8)
            ax.set_xlabel('Date', fontsize=12)
            ax.set_ylabel('Number of Attendees', fontsize=12)
            ax.set_title('Attendance Over Time', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            
            # Format x-axis
            plt.xticks(rotation=45)
            plt.tight_layout()
        
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = self.reports_dir / f"attendance_plot_{timestamp}.png"
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Attendance plot saved: {save_path}")
        return str(save_path)
    
    def plot_emotion_distribution(self, emotion_df=None, emotion_counts=None, save_path=None):
        """
        Plot emotion distribution as pie chart and bar chart
        
        Args:
            emotion_df: DataFrame with emotion records
            emotion_counts: Dictionary of emotion counts
            save_path: Path to save plot
            
        Returns:
            str: Path to saved plot
        """
        if emotion_df is not None and not emotion_df.empty:
            if 'dominant_emotion' in emotion_df.columns:
                emotion_counts = emotion_df['dominant_emotion'].value_counts().to_dict()
        
        if not emotion_counts:
            print("No emotion data to visualize")
            return None
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        emotions = list(emotion_counts.keys())
        counts = list(emotion_counts.values())
        
        # Color mapping
        colors = {
            'angry': '#FF4444',
            'disgust': '#800080',
            'fear': '#FF00FF',
            'happy': '#44FF44',
            'sad': '#4444FF',
            'surprise': '#FFFF44',
            'neutral': '#888888'
        }
        
        emotion_colors = [colors.get(e, '#CCCCCC') for e in emotions]
        
        # Pie chart
        ax1.pie(counts, labels=emotions, autopct='%1.1f%%',
               colors=emotion_colors, startangle=90)
        ax1.set_title('Emotion Distribution', fontsize=14, fontweight='bold')
        
        # Bar chart
        bars = ax2.bar(emotions, counts, color=emotion_colors)
        ax2.set_xlabel('Emotion', fontsize=12)
        ax2.set_ylabel('Count', fontsize=12)
        ax2.set_title('Emotion Frequency', fontsize=14, fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom')
        
        plt.tight_layout()
        
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = self.reports_dir / f"emotion_distribution_{timestamp}.png"
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Emotion distribution plot saved: {save_path}")
        return str(save_path)
    
    def plot_emotion_timeline(self, emotion_df, save_path=None):
        """
        Plot emotion changes over time
        
        Args:
            emotion_df: DataFrame with emotion records
            save_path: Path to save plot
            
        Returns:
            str: Path to saved plot
        """
        if emotion_df.empty or 'timestamp' not in emotion_df.columns:
            print("No emotion timeline data to visualize")
            return None
        
        fig, ax = plt.subplots(figsize=(14, 6))
        
        emotion_df['timestamp'] = pd.to_datetime(emotion_df['timestamp'])
        emotion_df = emotion_df.sort_values('timestamp')
        
        # Map emotions to numeric values
        emotion_map = {
            'happy': 3, 'surprise': 2, 'neutral': 0,
            'sad': -1, 'fear': -2, 'angry': -3, 'disgust': -3
        }
        
        emotion_df['emotion_value'] = emotion_df['dominant_emotion'].map(emotion_map)
        
        # Plot
        ax.plot(emotion_df['timestamp'], emotion_df['emotion_value'],
               marker='o', linewidth=2, markersize=6, alpha=0.7)
        
        ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Emotional Valence', fontsize=12)
        ax.set_title('Emotion Timeline', fontsize=14, fontweight='bold')
        ax.set_yticks([-3, -2, -1, 0, 1, 2, 3])
        ax.set_yticklabels(['Very Negative', 'Negative', 'Slightly Negative',
                           'Neutral', 'Slightly Positive', 'Positive', 'Very Positive'])
        ax.grid(True, alpha=0.3)
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = self.reports_dir / f"emotion_timeline_{timestamp}.png"
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Emotion timeline plot saved: {save_path}")
        return str(save_path)
    
    def plot_attention_metrics(self, attention_data, save_path=None):
        """
        Plot attention metrics over time
        
        Args:
            attention_data: DataFrame with attention metrics
            save_path: Path to save plot
            
        Returns:
            str: Path to saved plot
        """
        if attention_data.empty:
            print("No attention data to visualize")
            return None
        
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        
        if 'timestamp' in attention_data.columns:
            attention_data['timestamp'] = pd.to_datetime(attention_data['timestamp'])
        
        # Attention score over time
        if 'attention_score' in attention_data.columns:
            axes[0].plot(attention_data['timestamp'], attention_data['attention_score'],
                        color='blue', linewidth=2)
            axes[0].axhline(y=0.5, color='red', linestyle='--', label='Threshold')
            axes[0].set_ylabel('Attention Score', fontsize=12)
            axes[0].set_title('Attention Level Over Time', fontsize=14, fontweight='bold')
            axes[0].legend()
            axes[0].grid(True, alpha=0.3)
        
        # Eye aspect ratio (drowsiness indicator)
        if 'eye_aspect_ratio' in attention_data.columns:
            axes[1].plot(attention_data['timestamp'], attention_data['eye_aspect_ratio'],
                        color='green', linewidth=2)
            axes[1].axhline(y=0.2, color='red', linestyle='--', label='Drowsiness Threshold')
            axes[1].set_xlabel('Time', fontsize=12)
            axes[1].set_ylabel('Eye Aspect Ratio', fontsize=12)
            axes[1].set_title('Drowsiness Detection', fontsize=14, fontweight='bold')
            axes[1].legend()
            axes[1].grid(True, alpha=0.3)
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = self.reports_dir / f"attention_metrics_{timestamp}.png"
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Attention metrics plot saved: {save_path}")
        return str(save_path)
    
    def create_dashboard(self, attendance_df=None, emotion_df=None, 
                        attention_df=None, save_path=None):
        """
        Create comprehensive dashboard with multiple metrics
        
        Args:
            attendance_df: Attendance data
            emotion_df: Emotion data
            attention_df: Attention data
            save_path: Path to save dashboard
            
        Returns:
            str: Path to saved dashboard
        """
        fig = plt.figure(figsize=(16, 12))
        gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)
        
        # Attendance plot
        if attendance_df is not None and not attendance_df.empty:
            ax1 = fig.add_subplot(gs[0, :])
            if 'timestamp' in attendance_df.columns:
                attendance_df['timestamp'] = pd.to_datetime(attendance_df['timestamp'])
                daily = attendance_df.groupby(attendance_df['timestamp'].dt.date).size()
                ax1.bar(range(len(daily)), daily.values, color='steelblue')
                ax1.set_xticks(range(len(daily)))
                ax1.set_xticklabels([str(d) for d in daily.index], rotation=45)
                ax1.set_ylabel('Attendees')
                ax1.set_title('Daily Attendance', fontweight='bold')
                ax1.grid(True, alpha=0.3)
        
        # Emotion distribution
        if emotion_df is not None and not emotion_df.empty:
            ax2 = fig.add_subplot(gs[1, 0])
            if 'dominant_emotion' in emotion_df.columns:
                emotion_counts = emotion_df['dominant_emotion'].value_counts()
                colors_map = {
                    'angry': '#FF4444', 'disgust': '#800080', 'fear': '#FF00FF',
                    'happy': '#44FF44', 'sad': '#4444FF', 'surprise': '#FFFF44',
                    'neutral': '#888888'
                }
                colors = [colors_map.get(e, '#CCCCCC') for e in emotion_counts.index]
                ax2.pie(emotion_counts.values, labels=emotion_counts.index,
                       autopct='%1.1f%%', colors=colors, startangle=90)
                ax2.set_title('Emotion Distribution', fontweight='bold')
        
        # Emotion timeline
        if emotion_df is not None and not emotion_df.empty and 'timestamp' in emotion_df.columns:
            ax3 = fig.add_subplot(gs[1, 1])
            emotion_df['timestamp'] = pd.to_datetime(emotion_df['timestamp'])
            positive = emotion_df[emotion_df['dominant_emotion'].isin(['happy', 'surprise'])]
            negative = emotion_df[emotion_df['dominant_emotion'].isin(['sad', 'angry', 'fear'])]
            
            if not positive.empty:
                pos_hourly = positive.groupby(positive['timestamp'].dt.hour).size()
                ax3.plot(pos_hourly.index, pos_hourly.values, 
                        color='green', marker='o', label='Positive')
            if not negative.empty:
                neg_hourly = negative.groupby(negative['timestamp'].dt.hour).size()
                ax3.plot(neg_hourly.index, neg_hourly.values,
                        color='red', marker='o', label='Negative')
            
            ax3.set_xlabel('Hour of Day')
            ax3.set_ylabel('Count')
            ax3.set_title('Emotions by Hour', fontweight='bold')
            ax3.legend()
            ax3.grid(True, alpha=0.3)
        
        # Attention metrics
        if attention_df is not None and not attention_df.empty:
            ax4 = fig.add_subplot(gs[2, :])
            if 'timestamp' in attention_df.columns and 'attention_score' in attention_df.columns:
                attention_df['timestamp'] = pd.to_datetime(attention_df['timestamp'])
                ax4.plot(attention_df['timestamp'], attention_df['attention_score'],
                        color='blue', linewidth=2, label='Attention Score')
                ax4.axhline(y=0.5, color='red', linestyle='--', label='Threshold')
                ax4.set_xlabel('Time')
                ax4.set_ylabel('Attention Score')
                ax4.set_title('Attention Tracking', fontweight='bold')
                ax4.legend()
                ax4.grid(True, alpha=0.3)
                plt.xticks(rotation=45)
        
        if save_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = self.reports_dir / f"dashboard_{timestamp}.png"
        
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Dashboard saved: {save_path}")
        return str(save_path)
