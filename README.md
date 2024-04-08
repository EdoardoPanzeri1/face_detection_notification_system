# FACE DETECTION NOTIFICATION SYSTEM
This project is a face detection system that uses a webcam to detect faces in real time. Once a face is detected, the system captures the frame, saves it as an image, and then performs two actions:

Displays a desktop notification alerting that a face has been detected.
Sends an email with the captured image as an attachment to a predefined recipient.
The project utilizes OpenCV for face detection and the Plyer library for desktop notifications. It also makes use of the smtplib and email packages in Python to send emails.

PREREQUISITES
Before you can run this project, you need to have Python installed on your machine. Additionally, you will need to install the following Python libraries:

OpenCV
Plyer
For sending emails: smtplib and email
You can install these dependencies using pip:
'''sh
pip install opencv-python plyer
