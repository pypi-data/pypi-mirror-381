"""
Example: Gesture-based interaction demo
"""
from camera_master import GestureRecognizer
import pyttsx3

class GestureInteraction:
    """Interactive gesture recognition with audio feedback"""
    def __init__(self):
        self.recognizer = GestureRecognizer()
        self.tts_engine = pyttsx3.init()
        self.last_gesture = None
    
    def gesture_callback(self, gesture_data):
        """Callback for gesture events"""
        gesture = gesture_data['gesture']
        # Only speak if gesture changed
        if gesture != self.last_gesture:
            self.last_gesture = gesture
            # Provide feedback
            if 'One' in gesture or 'Two' in gesture or 'Three' in gesture or \
                    'Four' in gesture or 'Five' in gesture:
                number = gesture.split()[0]
                self.speak(f"Number {number}")
            elif gesture == "OK":
                self.speak("OK gesture detected")
            elif gesture == "Thumbs Up":
                self.speak("Thumbs up! Great job!")
            elif gesture == "Open Hand":
                self.speak("Open hand detected")
    
    def speak(self, text):
        """Speak text using TTS"""
        print(f" {text}")
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except:
            pass  # TTS might not work on all systems
    
    def run(self):
        """Run interactive gesture recognition"""
        print("Camera Master - Gesture Interaction Demo")
        print("=" * 50)
        print("\nShow gestures to the camera:")
        print(" • Numbers 1-5: Count with fingers")
        print(" • Open hand: All fingers extended")
        print(" • OK sign: Touch thumb and index finger")
        print(" • Thumbs up/down: Show approval")
        print("\nPress 'q' to quit")
        print("-" * 50)
        self.speak("Gesture recognition started")
        self.recognizer.start_recognition(
            camera_index=0,
            callback=self.gesture_callback
        )
        self.speak("Gesture recognition stopped")


def main():
    demo = GestureInteraction()
    demo.run()


if __name__ == "__main__":
    main()
