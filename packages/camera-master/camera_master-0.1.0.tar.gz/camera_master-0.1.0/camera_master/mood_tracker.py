"""
Mood tracking and trend analysis over time
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from collections import deque
from camera_master.utils import get_reports_dir, save_json, load_json


class MoodTracker:
    """
    Track mood trends over time using emotion history
    """
    
    def __init__(self):
        """Initialize Mood Tracker"""
        self.reports_dir = get_reports_dir()
        self.mood_history_file = self.reports_dir / "mood_history.json"
        
        self.mood_history = self._load_history()
        self.session_emotions = []
        
        # Emotion valence mapping
        self.emotion_valence = {
            'happy': 1.0,
            'surprise': 0.5,
            'neutral': 0.0,
            'sad': -0.5,
            'fear': -0.7,
            'angry': -0.8,
            'disgust': -0.6
        }
    
    def _load_history(self):
        """Load mood history from file"""
        data = load_json(self.mood_history_file)
        return data.get('history', [])
    
    def _save_history(self):
        """Save mood history to file"""
        save_json({'history': self.mood_history}, self.mood_history_file)
    
    def add_emotion(self, emotion, timestamp=None):
        """
        Add emotion to mood tracking
        
        Args:
            emotion: Emotion name
            timestamp: Timestamp (default: now)
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        valence = self.emotion_valence.get(emotion.lower(), 0.0)
        
        entry = {
            'timestamp': timestamp.isoformat() if isinstance(timestamp, datetime) else timestamp,
            'emotion': emotion,
            'valence': valence
        }
        
        self.session_emotions.append(entry)
        self.mood_history.append(entry)
    
    def get_current_mood(self, window_minutes=30):
        """
        Get current mood based on recent emotions
        
        Args:
            window_minutes: Time window in minutes
            
        Returns:
            dict: Current mood information
        """
        if not self.session_emotions:
            return {
                'mood': 'Neutral',
                'valence': 0.0,
                'dominant_emotion': 'neutral',
                'confidence': 0.0
            }
        
        # Get recent emotions
        cutoff_time = datetime.now() - timedelta(minutes=window_minutes)
        recent = [
            e for e in self.session_emotions
            if pd.to_datetime(e['timestamp']) > cutoff_time
        ]
        
        if not recent:
            return {
                'mood': 'Neutral',
                'valence': 0.0,
                'dominant_emotion': 'neutral',
                'confidence': 0.0
            }
        
        # Calculate average valence
        avg_valence = np.mean([e['valence'] for e in recent])
        
        # Get dominant emotion
        emotions = [e['emotion'] for e in recent]
        dominant = max(set(emotions), key=emotions.count)
        confidence = emotions.count(dominant) / len(emotions)
        
        # Determine mood
        if avg_valence > 0.3:
            mood = 'Positive'
        elif avg_valence < -0.3:
            mood = 'Negative'
        else:
            mood = 'Neutral'
        
        return {
            'mood': mood,
            'valence': avg_valence,
            'dominant_emotion': dominant,
            'confidence': confidence,
            'emotion_count': len(recent)
        }
    
    def get_mood_trend(self, hours=24):
        """
        Get mood trend over time
        
        Args:
            hours: Number of hours to analyze
            
        Returns:
            dict: Trend analysis
        """
        if not self.mood_history:
            return {
                'trend': 'Stable',
                'change': 0.0,
                'description': 'Insufficient data'
            }
        
        # Get data for time period
        cutoff_time = datetime.now() - timedelta(hours=hours)
        period_data = [
            e for e in self.mood_history
            if pd.to_datetime(e['timestamp']) > cutoff_time
        ]
        
        if len(period_data) < 2:
            return {
                'trend': 'Stable',
                'change': 0.0,
                'description': 'Insufficient data'
            }
        
        # Calculate trend
        df = pd.DataFrame(period_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        
        # Split into first and second half
        mid = len(df) // 2
        first_half_avg = df.iloc[:mid]['valence'].mean()
        second_half_avg = df.iloc[mid:]['valence'].mean()
        
        change = second_half_avg - first_half_avg
        
        # Determine trend
        if change > 0.2:
            trend = 'Improving'
            description = 'Mood has been getting better'
        elif change < -0.2:
            trend = 'Declining'
            description = 'Mood has been getting worse'
        else:
            trend = 'Stable'
            description = 'Mood has been relatively stable'
        
        return {
            'trend': trend,
            'change': change,
            'description': description,
            'average_valence': df['valence'].mean(),
            'period_hours': hours,
            'data_points': len(period_data)
        }
    
    def get_daily_summary(self, date=None):
        """
        Get mood summary for a specific day
        
        Args:
            date: Date to analyze (default: today)
            
        Returns:
            dict: Daily mood summary
        """
        if date is None:
            date = datetime.now().date()
        
        # Filter emotions for this day
        day_emotions = [
            e for e in self.mood_history
            if pd.to_datetime(e['timestamp']).date() == date
        ]
        
        if not day_emotions:
            return {
                'date': str(date),
                'average_mood': 'N/A',
                'dominant_emotion': 'N/A',
                'emotion_distribution': {}
            }
        
        # Calculate statistics
        avg_valence = np.mean([e['valence'] for e in day_emotions])
        emotions = [e['emotion'] for e in day_emotions]
        dominant = max(set(emotions), key=emotions.count)
        
        # Emotion distribution
        emotion_dist = {}
        for emotion in emotions:
            emotion_dist[emotion] = emotion_dist.get(emotion, 0) + 1
        
        # Determine mood
        if avg_valence > 0.3:
            mood = 'Positive'
        elif avg_valence < -0.3:
            mood = 'Negative'
        else:
            mood = 'Neutral'
        
        return {
            'date': str(date),
            'average_mood': mood,
            'average_valence': avg_valence,
            'dominant_emotion': dominant,
            'emotion_distribution': emotion_dist,
            'total_emotions': len(day_emotions)
        }
    
    def get_weekly_report(self):
        """
        Get mood report for the past week
        
        Returns:
            dict: Weekly mood report
        """
        daily_summaries = []
        
        for i in range(7):
            date = (datetime.now() - timedelta(days=i)).date()
            summary = self.get_daily_summary(date)
            daily_summaries.append(summary)
        
        # Calculate week average
        valences = [s['average_valence'] for s in daily_summaries 
                   if isinstance(s.get('average_valence'), (int, float))]
        
        week_avg = np.mean(valences) if valences else 0.0
        
        return {
            'week_average_valence': week_avg,
            'daily_summaries': daily_summaries,
            'trend': self.get_mood_trend(hours=7*24)
        }
    
    def save_session(self):
        """Save current session data"""
        self._save_history()
        print(f"Mood history saved: {len(self.session_emotions)} emotions tracked")
    
    def get_emotion_patterns(self):
        """
        Analyze emotion patterns
        
        Returns:
            dict: Pattern analysis
        """
        if not self.mood_history:
            return {}
        
        df = pd.DataFrame(self.mood_history)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Hour of day patterns
        df['hour'] = df['timestamp'].dt.hour
        hourly_mood = df.groupby('hour')['valence'].mean().to_dict()
        
        # Day of week patterns
        df['day_of_week'] = df['timestamp'].dt.day_name()
        daily_mood = df.groupby('day_of_week')['valence'].mean().to_dict()
        
        # Most common emotions by time
        morning = df[df['hour'].between(6, 12)]['emotion'].mode().tolist()
        afternoon = df[df['hour'].between(12, 18)]['emotion'].mode().tolist()
        evening = df[df['hour'].between(18, 24)]['emotion'].mode().tolist()
        
        return {
            'hourly_patterns': hourly_mood,
            'daily_patterns': daily_mood,
            'time_of_day_emotions': {
                'morning': morning[0] if morning else 'N/A',
                'afternoon': afternoon[0] if afternoon else 'N/A',
                'evening': evening[0] if evening else 'N/A'
            }
        }
    
    def clear_old_data(self, days=30):
        """
        Clear mood data older than specified days
        
        Args:
            days: Number of days to keep
        """
        cutoff_time = datetime.now() - timedelta(days=days)
        
        self.mood_history = [
            e for e in self.mood_history
            if pd.to_datetime(e['timestamp']) > cutoff_time
        ]
        
        self._save_history()
        print(f"Cleared mood data older than {days} days")
