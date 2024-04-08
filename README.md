# FACE DETECTION NOTIFICATION SYSTEM
This project is a face detection system that uses a webcam to detect faces in real time. Once a face is detected, the system captures the frame, saves it as an image, and then performs two actions:

**Displays a desktop notification** alerting that a face has been detected.
**Sends an email** with the captured image as an attachment to a predefined recipient.
The project utilizes OpenCV for face detection and the Plyer library for desktop notifications. It also makes use of the smtplib and email packages in Python to send emails.

## PREREQUISITES
Before you can run this project, you need to have Python installed on your machine. Additionally, you will need to install the following Python libraries:

OpenCV
Plyer
For sending emails: smtplib and email
You can install these dependencies using pip:
`pip install opencv-python plyer`

## SETUP AND RUNNING
To set up and run this project, follow these steps:

1. Clone this repository to your local machine.
`git clone https://github.com/yourgithubusername/face-detection-notification-system.git`

2. Navigate to the project directory.
`cd face-detection-notification-system`

3. Run the script.
`python face_detection.py`

## CONFIGURATION
To use the email notification feature, you will need to configure the sender’s email address and password.
Note: It's highly recommended to use environment variables or placeholder credentials while setting up the project.

For demonstration purposes, you can either use environment variables or edit the send_email_with_image function within the script to include your email and password (or placeholder credentials).
