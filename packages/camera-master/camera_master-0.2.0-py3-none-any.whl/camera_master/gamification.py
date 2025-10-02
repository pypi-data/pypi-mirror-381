"""
Gamification engine for engagement tracking
"""
import json
from datetime import datetime, timedelta
import pandas as pd
from camera_master.utils import get_data_dir, save_json, load_json


class GamificationEngine:
    """
    Gamification system with badges, points, and leaderboards
    """
    
    def __init__(self):
        """Initialize Gamification Engine"""
        self.data_dir = get_data_dir()
        self.gamification_file = self.data_dir / "gamification_data.json"
        self.data = self._load_data()
        self.users = self.data.get('users', {})
        
        # Define badges
        self.badges = {
            'early_bird': {'name': 'Early Bird', 'description': 'Attend before 8 AM', 'points': 10},
            'perfect_attendance': {'name': 'Perfect Attendance', 'description': '7 consecutive days', 'points': 50},
            'emotion_master': {'name': 'Emotion Master', 'description': 'Maintain positive emotion for 1 hour', 'points': 30},
            'focus_champion': {'name': 'Focus Champion', 'description': '90% attention for 30 minutes', 'points': 40},
            'engagement_pro': {'name': 'Engagement Pro', 'description': 'Active gestures for 15 minutes', 'points': 25},
            'week_warrior': {'name': 'Week Warrior', 'description': 'Complete 5 days this week', 'points': 35},
            'mood_stabilizer': {'name': 'Mood Stabilizer', 'description': 'Maintain neutral/positive mood', 'points': 20},
            'attention_ace': {'name': 'Attention Ace', 'description': 'Zero drowsiness events in session', 'points': 30},
        }
    
    def _load_data(self):
        """Load gamification data"""
        return load_json(self.gamification_file)
    
    def _save_data(self):
        """Save gamification data"""
        data = {
            'users': self.users,
            'last_updated': datetime.now().isoformat()
        }
        save_json(data, self.gamification_file)
    
    def initialize_user(self, user_name):
        """
        Initialize user in gamification system
        
        Args:
            user_name: User name
        """
        if user_name not in self.users:
            self.users[user_name] = {
                'points': 0,
                'level': 1,
                'badges': [],
                'attendance_streak': 0,
                'total_sessions': 0,
                'last_attendance': None,
                'achievements': []
            }
            self._save_data()
    
    def add_points(self, user_name, points, reason=""):
        """
        Add points to user
        
        Args:
            user_name: User name
            points: Points to add
            reason: Reason for points
        """
        self.initialize_user(user_name)
        self.users[user_name]['points'] += points
        
        # Update level (100 points per level)
        new_level = (self.users[user_name]['points'] // 100) + 1
        if new_level > self.users[user_name]['level']:
            self.users[user_name]['level'] = new_level
            print(f"{user_name} leveled up to Level {new_level}!")
        
        # Log achievement
        self.users[user_name]['achievements'].append({
            'timestamp': datetime.now().isoformat(),
            'points': points,
            'reason': reason
        })
        self._save_data()
    
    def award_badge(self, user_name, badge_id):
        """
        Award badge to user
        
        Args:
            user_name: User name
            badge_id: Badge identifier
        """
        self.initialize_user(user_name)
        
        if badge_id not in self.badges:
            return False
        
        if badge_id in self.users[user_name]['badges']:
            return False  # Already has badge
        
        badge = self.badges[badge_id]
        self.users[user_name]['badges'].append(badge_id)
        self.add_points(user_name, badge['points'], f"Earned badge: {badge['name']}")
        print(f"{user_name} earned badge: {badge['name']}!")
        return True
    
    def record_attendance(self, user_name):
        """
        Record attendance and check for streaks
        
        Args:
            user_name: User name
        """
        self.initialize_user(user_name)
        today = datetime.now().date()
        last_attendance = self.users[user_name].get('last_attendance')
        
        # Check if already attended today
        if last_attendance and pd.to_datetime(last_attendance).date() == today:
            return
        
        # Update streak
        if last_attendance:
            last_date = pd.to_datetime(last_attendance).date()
            if (today - last_date).days == 1:
                self.users[user_name]['attendance_streak'] += 1
            else:
                self.users[user_name]['attendance_streak'] = 1
        else:
            self.users[user_name]['attendance_streak'] = 1
        
        self.users[user_name]['last_attendance'] = datetime.now().isoformat()
        self.users[user_name]['total_sessions'] += 1
        
        # Award points for attendance
        self.add_points(user_name, 5, "Daily attendance")
        
        # Check for early bird (before 8 AM)
        if datetime.now().hour < 8:
            self.award_badge(user_name, 'early_bird')
        
        # Check for perfect attendance streak
        if self.users[user_name]['attendance_streak'] >= 7:
            self.award_badge(user_name, 'perfect_attendance')
        
        self._save_data()
    
    def check_emotion_achievement(self, user_name, positive_duration_minutes):
        """
        Check emotion-based achievements
        
        Args:
            user_name: User name
            positive_duration_minutes: Duration of positive emotion
        """
        self.initialize_user(user_name)
        if positive_duration_minutes >= 60:
            self.award_badge(user_name, 'emotion_master')
            self.add_points(user_name, 20, "1 hour of positive emotion")
    
    def check_attention_achievement(self, user_name, attention_percentage, duration_minutes):
        """
        Check attention-based achievements
        
        Args:
            user_name: User name
            attention_percentage: Average attention percentage
            duration_minutes: Duration of monitoring
        """
        self.initialize_user(user_name)
        if attention_percentage >= 90 and duration_minutes >= 30:
            self.award_badge(user_name, 'focus_champion')
            self.add_points(user_name, 25, f"{attention_percentage:.1f}% attention")
    
    def check_fatigue_achievement(self, user_name, no_drowsiness=False):
        """
        Check fatigue-related achievements
        
        Args:
            user_name: User name
            no_drowsiness: True if no drowsiness detected
        """
        self.initialize_user(user_name)
        if no_drowsiness:
            self.award_badge(user_name, 'attention_ace')
            self.add_points(user_name, 15, "No drowsiness in session")
    
    def get_user_profile(self, user_name):
        """
        Get user gamification profile
        
        Args:
            user_name: User name
            
        Returns:
            dict: User profile
        """
        self.initialize_user(user_name)
        user = self.users[user_name]
        
        # Get badge details
        badges_earned = []
        for badge_id in user['badges']:
            if badge_id in self.badges:
                badges_earned.append(self.badges[badge_id])
        
        return {
            'name': user_name,
            'points': user['points'],
            'level': user['level'],
            'badges': badges_earned,
            'attendance_streak': user['attendance_streak'],
            'total_sessions': user['total_sessions'],
            'progress_to_next_level': user['points'] % 100,
            'next_level_points': 100
        }
    
    def get_leaderboard(self, limit=10):
        """
        Get top users leaderboard
        
        Args:
            limit: Number of users to return
            
        Returns:
            list: Leaderboard entries
        """
        leaderboard = []
        for user_name, user_data in self.users.items():
            leaderboard.append({
                'name': user_name,
                'points': user_data['points'],
                'level': user_data['level'],
                'badges_count': len(user_data['badges']),
                'attendance_streak': user_data['attendance_streak']
            })
        
        # Sort by points
        leaderboard.sort(key=lambda x: x['points'], reverse=True)
        return leaderboard[:limit]
    
    def get_available_badges(self):
        """
        Get all available badges
        
        Returns:
            dict: Badges information
        """
        return self.badges
    
    def generate_user_report(self, user_name):
        """
        Generate comprehensive user report
        
        Args:
            user_name: User name
            
        Returns:
            dict: User report
        """
        profile = self.get_user_profile(user_name)
        
        # Calculate statistics
        user = self.users.get(user_name, {})
        achievements = user.get('achievements', [])
        
        # Recent achievements (last 7 days)
        cutoff = datetime.now() - timedelta(days=7)
        recent = [
            a for a in achievements
            if pd.to_datetime(a['timestamp']) > cutoff
        ]
        
        return {
            'profile': profile,
            'recent_achievements': recent,
            'total_achievements': len(achievements),
            'average_points_per_session': user['points'] / max(user['total_sessions'], 1),
            'rank': self._get_user_rank(user_name)
        }
    
    def _get_user_rank(self, user_name):
        """Get user's rank on leaderboard"""
        leaderboard = self.get_leaderboard(limit=None)
        for i, entry in enumerate(leaderboard, 1):
            if entry['name'] == user_name:
                return i
        return len(leaderboard) + 1
    
    def display_user_dashboard(self, user_name):
        """
        Display user's gamification dashboard
        
        Args:
            user_name: User name
        """
        profile = self.get_user_profile(user_name)
        
        print("\n" + "="*60)
        print(f"GAMIFICATION DASHBOARD - {user_name}")
        print("="*60)
        print(f"\nLevel: {profile['level']}")
        print(f"Points: {profile['points']}")
        print(f"Progress to Level {profile['level']+1}: {profile['progress_to_next_level']}/100")
        print(f"Attendance Streak: {profile['attendance_streak']} days")
        print(f"Total Sessions: {profile['total_sessions']}")
        print(f"\nBadges ({len(profile['badges'])})")
        print("-" * 60)
        
        for badge in profile['badges']:
            print(f"  • {badge['name']}: {badge['description']} (+{badge['points']} pts)")
        
        # Show next available badges
        earned_ids = [b['name'] for b in profile['badges']]
        available = [b for b in self.badges.values() if b['name'] not in earned_ids]
        
        if available:
            print(f"\nNext Badges to Earn:")
            for badge in list(available)[:3]:
                print(f"  • {badge['name']}: {badge['description']} (+{badge['points']} pts)")
        
        print("="*60 + "\n")
