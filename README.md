# AI-Powered Exercise Assistant 🏋️‍♂️

This project is an **AI-based exercise correction tool** that uses **Mediapipe**, **OpenCV (cv2)**, and a **Neural Network** to help you perform exercises with proper form. By measuring angles between key body landmarks, it provides real-time feedback to ensure your movements are accurate. The frontend is powered by **Streamlit**, providing a simple and interactive interface.

---

## Features

- **Real-Time Pose Detection**: Detects body posture using Mediapipe.
- **Angle Measurement**: Calculates angles between key body joints to evaluate form.
- **Exercise Support**: Tracks the following exercises:
  - Pushups
  - Squats
  - Pullups
  - And more!
- **Live Feedback**: Alerts users when posture is incorrect.
- **Performance Metrics**: Tracks repetitions and provides a summary.
- **User-Friendly Interface**: Built with Streamlit for ease of use.

---

## Technologies Used

- **Mediapipe**: For detecting body landmarks and real-time pose estimation.
- **OpenCV (cv2)**: For video processing and visualization.
- **Neural Networks**: For classifying correct vs. incorrect movements.
- **Streamlit**: For creating an interactive web-based frontend.
- **Python**: The primary programming language for backend development.

---

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.8 or above
- pip (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   [git clone https://github.com/yourusername/exercise-assistant.git](https://github.com/harsh21052842/AI-Personal-Trainer.git)

# Navigate to the project directory:
cd exercise-assistant

# Run the application:
streamlit run app.py

# Open the app in your browser at http://localhost:8501.
