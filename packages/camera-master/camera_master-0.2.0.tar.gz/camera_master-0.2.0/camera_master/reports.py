"""
Automated report generation for all monitoring features
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import json
from camera_master.utils import get_reports_dir, timestamp_to_string


class ReportGenerator:
    """
    Generate comprehensive reports for education monitoring
    """
    
    def __init__(self):
        """Initialize Report Generator"""
        self.reports_dir = get_reports_dir()
    
    def generate_attendance_report(self, attendance_data, output_format='csv'):
        """
        Generate attendance report
        
        Args:
            attendance_data: DataFrame or list of attendance records
            output_format: Output format ('csv', 'json', 'html')
            
        Returns:
            str: Path to generated report
        """
        if isinstance(attendance_data, list):
            df = pd.DataFrame(attendance_data)
        else:
            df = attendance_data
        
        if df.empty:
            print("No attendance data to report")
            return None
        
        # Add analysis
        summary = {
            'total_attendees': len(df),
            'unique_attendees': df['name'].nunique() if 'name' in df.columns else 0,
            'report_date': timestamp_to_string()
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_format == 'csv':
            filepath = self.reports_dir / f"attendance_report_{timestamp}.csv"
            df.to_csv(filepath, index=False)
            
            # Save summary
            summary_path = self.reports_dir / f"attendance_summary_{timestamp}.json"
            with open(summary_path, 'w') as f:
                json.dump(summary, f, indent=4)
                
        elif output_format == 'json':
            filepath = self.reports_dir / f"attendance_report_{timestamp}.json"
            report = {
                'summary': summary,
                'records': df.to_dict('records')
            }
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=4, default=str)
                
        elif output_format == 'html':
            filepath = self.reports_dir / f"attendance_report_{timestamp}.html"
            html = self._generate_html_report(df, summary, 'Attendance Report')
            with open(filepath, 'w') as f:
                f.write(html)
        
        print(f"Attendance report generated: {filepath}")
        return str(filepath)
    
    def generate_emotion_report(self, emotion_data, output_format='csv'):
        """
        Generate emotion analysis report
        
        Args:
            emotion_data: DataFrame or list of emotion records
            output_format: Output format ('csv', 'json', 'html')
            
        Returns:
            str: Path to generated report
        """
        if isinstance(emotion_data, list):
            df = pd.DataFrame(emotion_data)
        else:
            df = emotion_data
        
        if df.empty:
            print("No emotion data to report")
            return None
        
        # Calculate statistics
        if 'dominant_emotion' in df.columns:
            emotion_counts = df['dominant_emotion'].value_counts().to_dict()
            most_common = df['dominant_emotion'].mode()[0] if len(df) > 0 else 'N/A'
        else:
            emotion_counts = {}
            most_common = 'N/A'
        
        summary = {
            'total_detections': len(df),
            'most_common_emotion': most_common,
            'emotion_distribution': emotion_counts,
            'report_date': timestamp_to_string()
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_format == 'csv':
            filepath = self.reports_dir / f"emotion_report_{timestamp}.csv"
            df.to_csv(filepath, index=False)
            
            summary_path = self.reports_dir / f"emotion_summary_{timestamp}.json"
            with open(summary_path, 'w') as f:
                json.dump(summary, f, indent=4)
                
        elif output_format == 'json':
            filepath = self.reports_dir / f"emotion_report_{timestamp}.json"
            report = {
                'summary': summary,
                'records': df.to_dict('records')
            }
            with open(filepath, 'w') as f:
                json.dump(report, f, indent=4, default=str)
                
        elif output_format == 'html':
            filepath = self.reports_dir / f"emotion_report_{timestamp}.html"
            html = self._generate_html_report(df, summary, 'Emotion Analysis Report')
            with open(filepath, 'w') as f:
                f.write(html)
        
        print(f"Emotion report generated: {filepath}")
        return str(filepath)
    
    def generate_comprehensive_report(self, attendance_data=None, emotion_data=None,
                                     attention_data=None, output_format='html'):
        """
        Generate comprehensive report combining all metrics
        
        Args:
            attendance_data: Attendance DataFrame
            emotion_data: Emotion DataFrame
            attention_data: Attention DataFrame
            output_format: Output format
            
        Returns:
            str: Path to generated report
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_data = {
            'generation_date': timestamp_to_string(),
            'attendance': {},
            'emotions': {},
            'attention': {}
        }
        
        # Process attendance data
        if attendance_data is not None and not attendance_data.empty:
            report_data['attendance'] = {
                'total_attendees': len(attendance_data),
                'unique_attendees': attendance_data['name'].nunique() if 'name' in attendance_data.columns else 0,
                'records': attendance_data.to_dict('records') if output_format == 'json' else None
            }
        
        # Process emotion data
        if emotion_data is not None and not emotion_data.empty:
            if 'dominant_emotion' in emotion_data.columns:
                emotion_counts = emotion_data['dominant_emotion'].value_counts().to_dict()
                most_common = emotion_data['dominant_emotion'].mode()[0]
            else:
                emotion_counts = {}
                most_common = 'N/A'
            
            report_data['emotions'] = {
                'total_detections': len(emotion_data),
                'most_common_emotion': most_common,
                'emotion_distribution': emotion_counts,
                'records': emotion_data.to_dict('records') if output_format == 'json' else None
            }
        
        # Process attention data
        if attention_data is not None and not attention_data.empty:
            report_data['attention'] = {
                'total_measurements': len(attention_data),
                'average_attention': attention_data['attention_score'].mean() if 'attention_score' in attention_data.columns else 0,
                'records': attention_data.to_dict('records') if output_format == 'json' else None
            }
        
        if output_format == 'json':
            filepath = self.reports_dir / f"comprehensive_report_{timestamp}.json"
            with open(filepath, 'w') as f:
                json.dump(report_data, f, indent=4, default=str)
        elif output_format == 'html':
            filepath = self.reports_dir / f"comprehensive_report_{timestamp}.html"
            html = self._generate_comprehensive_html(report_data, attendance_data,
                                                     emotion_data, attention_data)
            with open(filepath, 'w') as f:
                f.write(html)
        
        print(f"Comprehensive report generated: {filepath}")
        return str(filepath)
    
    def _generate_html_report(self, df, summary, title):
        """Generate HTML report"""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        .summary {{ background: #f0f0f0; padding: 15px; margin: 20px 0; border-radius: 5px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <div class="summary">
        <h2>Summary</h2>
"""
        
        for key, value in summary.items():
            if not isinstance(value, dict):
                html += f"        <p><strong>{key.replace('_', ' ').title()}:</strong> {value}</p>\n"
        
        html += "    </div>\n"
        html += df.to_html(index=False, classes='data-table')
        html += """
</body>
</html>
"""
        return html
    
    def _generate_comprehensive_html(self, report_data, attendance_df, emotion_df, attention_df):
        """Generate comprehensive HTML report"""
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>Comprehensive Monitoring Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }
        .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; margin-top: 30px; }
        .metric-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                      color: white; padding: 20px; margin: 10px 0; border-radius: 8px; }
        .metric-value { font-size: 2em; font-weight: bold; }
        .metric-label { font-size: 0.9em; opacity: 0.9; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #3498db; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        .emotion-badge { display: inline-block; padding: 5px 10px; margin: 2px; 
                        border-radius: 15px; font-size: 0.9em; }
        .happy { background: #2ecc71; color: white; }
        .sad { background: #3498db; color: white; }
        .angry { background: #e74c3c; color: white; }
        .neutral { background: #95a5a6; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Education Monitoring Report</h1>
        <p><strong>Generated:</strong> {}</p>
""".format(report_data['generation_date'])
        
        # Attendance section
        if report_data['attendance']:
            html += """
        <h2>Attendance Overview</h2>
        <div class="metric-card">
            <div class="metric-label">Total Attendees</div>
            <div class="metric-value">{}</div>
        </div>
""".format(report_data['attendance'].get('total_attendees', 0))
            
            if attendance_df is not None and not attendance_df.empty:
                html += "        <h3>Attendance Records</h3>\n"
                html += attendance_df.head(20).to_html(index=False)
        
        # Emotion section
        if report_data['emotions']:
            html += """
        <h2>Emotion Analysis</h2>
        <div class="metric-card">
            <div class="metric-label">Total Detections</div>
            <div class="metric-value">{}</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">Most Common Emotion</div>
            <div class="metric-value">{}</div>
        </div>
""".format(
                report_data['emotions'].get('total_detections', 0),
                report_data['emotions'].get('most_common_emotion', 'N/A')
            )
            
            # Emotion distribution
            if 'emotion_distribution' in report_data['emotions']:
                html += "        <h3>Emotion Distribution</h3><p>\n"
                for emotion, count in report_data['emotions']['emotion_distribution'].items():
                    html += f'            <span class="emotion-badge {emotion}">{emotion}: {count}</span>\n'
                html += "        </p>\n"
        
        # Attention section
        if report_data['attention']:
            html += """
        <h2>Attention Metrics</h2>
        <div class="metric-card">
            <div class="metric-label">Average Attention Score</div>
            <div class="metric-value">{:.2f}%</div>
        </div>
""".format(report_data['attention'].get('average_attention', 0) * 100)
        
        html += """
    </div>
</body>
</html>
"""
        return html
    
    def generate_daily_summary(self, date=None):
        """
        Generate daily summary from all available data
        
        Args:
            date: Date to generate summary for (default: today)
            
        Returns:
            dict: Daily summary
        """
        if date is None:
            date = datetime.now().date()
        
        # This would aggregate data from various sources
        summary = {
            'date': str(date),
            'attendance_count': 0,
            'emotion_summary': {},
            'attention_average': 0,
            'alerts': []
        }
        
        return summary
