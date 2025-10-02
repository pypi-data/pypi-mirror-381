"""
Example: Basic attendance system demo
"""
from camera_master import Attendance

def main():
    # Initialize attendance system
    print("Camera Master - Attendance Demo")
    print("=" * 50)
    attendance = Attendance()
    # Register faces (optional - comment out if already registered)
    print("\n1. Register Faces")
    print("-" * 50)
    register = input("Do you want to register a new face? (y/n): ")
    if register.lower() == 'y':
        name = input("Enter person's name: ")
        print(f"\nCapturing face for {name}...")
        print("Press 's' to save the face, 'q' to skip")
        success = attendance.register_face(name)
        if success:
            print(f" {name} registered successfully!")
        else:
            print(" Registration cancelled or failed")
    # Start attendance monitoring
    print("\n2. Start Attendance Monitoring")
    print("-" * 50)
    start = input("Start attendance monitoring? (y/n): ")
    if start.lower() == 'y':
        print("\nStarting monitoring... Press 'q' to quit")
        df = attendance.start_monitoring(camera_index=0)
        # Display results
        print("\n" + "=" * 50)
        print("ATTENDANCE SUMMARY")
        print("=" * 50)
        print(df.to_string(index=False))
        # Save report
        report_path = attendance.save_report()
        print(f"\n Report saved: {report_path}")
        # Show statistics
        stats = attendance.get_statistics()
        print(f"\n Statistics:")
        print(f" • Present: {stats['total_present']}")
        print(f" • Registered: {stats['total_registered']}")
        print(f" • Attendance Rate: {stats['attendance_rate']:.1f}%")
        print(f" • Session Duration: {stats['session_duration']:.1f} minutes")


if __name__ == "__main__":
    main()
