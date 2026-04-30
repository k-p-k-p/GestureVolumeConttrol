# Gesture Volume Control

A Python-based application that uses Computer Vision to control your system's volume through hand gestures. By tracking the distance between your thumb and index finger, you can adjust the volume in real-time without touching your keyboard or mouse.
🚀 How It Works

The application uses your webcam to capture video frames and processes them using:

    MediaPipe: To detect hand landmarks and track the coordinates of the thumb (tip) and index finger (tip).

    OpenCV: To render the video feed and draw visual feedback (circles and lines) on the screen.

    PyCaw / Osascript: To interface with the system's audio endpoints and change the volume level based on the calculated distance.

# 🛠️ Prerequisites

Before running the project, ensure you have Python installed and the following libraries:
Bash

pip install opencv-python mediapipe numpy pycaw

Note: pycaw is typically used for Windows. For macOS, the project may utilize osascript.

# 📂 Project Structure

    VolumeGestureControl.py: The main execution script containing the hand tracking logic and volume mapping.

    HandTrackingModule.py: (If applicable) A helper module used to initialize the MediaPipe hand detection model.

🏃 Getting Started

    Clone the repository:
    Bash

    git clone https://github.com/k-p-k-p/GestureVolumeConttrol.git
    cd GestureVolumeConttrol

    Run the application:
    Bash

    python VolumeGestureControl.py

    Usage:

        Place your hand in front of the camera.

        Bring your thumb and index finger together to decrease volume.

        Move them apart to increase volume.

        A visual bar on the screen will indicate the current volume level.

# 📊 Logic Flow

    Detect Hand Landmarks: Identify the positions of Landmark 4 (Thumb Tip) and Landmark 8 (Index Tip).

    Calculate Distance: Find the Euclidean distance between these two points.

    Map Range: Convert the distance (e.g., 50–300 pixels) to the volume range (e.g., -65.25 to 0.0 dB).

    Update System: Apply the mapped value to the system audio master volume.

# 📜 License

This project is open-source and available under the MIT License.
