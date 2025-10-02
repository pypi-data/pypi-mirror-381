"""Fix indentation in example files"""
import re

def fix_indentation(file_path):
    """Fix 1-space indentation to 4-space"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        if line and line[0] == ' ' and not line.startswith('    '):
            # Count leading spaces
            spaces = len(line) - len(line.lstrip())
            # Convert 1-space to 4-space indentation
            new_spaces = spaces * 4
            fixed_line = ' ' * new_spaces + line.lstrip()
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fixed_lines))
    
    print(f'Fixed: {file_path}')

# Fix all example files
files = [
    r'd:\RNS\camera-master\examples\demo_attendance.py',
    r'd:\RNS\camera-master\examples\demo_comprehensive.py',
    r'd:\RNS\camera-master\examples\demo_gesture_interaction.py',
    r'd:\RNS\camera-master\examples\demo_unified_camera.py',
    r'd:\RNS\camera-master\camera_master\camera_manager.py',
    r'd:\RNS\camera-master\test_installation_py313.py'
]

for file in files:
    fix_indentation(file)

print('\nAll example files fixed!')
