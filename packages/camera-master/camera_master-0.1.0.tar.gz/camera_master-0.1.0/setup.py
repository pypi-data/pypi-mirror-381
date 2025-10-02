"""
Setup configuration for camera-master package
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="camera-master",
    version="0.1.0",
    author="RNS Sanjay",
    author_email="2005sanjaynrs@gmail.com",
    description="AI-powered education monitoring system with face recognition, gesture detection, and emotion analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RNSsanjay/camera-master",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "camera-master=camera_master.cli:main",
            "camera-attendance=camera_master.cli:attendance_cli",
            "camera-gesture=camera_master.cli:gesture_cli",
            "camera-emotion=camera_master.cli:emotion_cli",
            "camera-dashboard=camera_master.cli:dashboard_cli",
        ],
    },
    include_package_data=True,
)
