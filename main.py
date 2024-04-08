import cv2
from plyer import notification
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Build the path to the XML file
xml_file_path = os.path.join(script_dir, "haarcascade_frontalface_default.xml")

# import trained XML class
detector = cv2.CascadeClassifier(xml_file_path)

# captures frames from cam
cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)

# setting notification allert
def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Face detection!",  
        timeout=10  
    )

notification_counter = 0

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.1, 4)
        
        if len(faces) > 0:
            if notification_counter >= 100:
                show_notification("Alert!", "Someone detected")
                notification_counter = 0
            else:
                notification_counter += 1
        else:
            notification_counter = 0
        
        # draw rectangle on a face
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(img, (x,y), (x+w, y+h), (250, 0, 0), 2)
        
        cv2.imshow("Face", img)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows

    
    



