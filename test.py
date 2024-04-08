import cv2

cap = cv2.VideoCapture(0)  # Start with the most default setup

if not cap.isOpened():
    print("Error: Could not open video capture")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Couldn't read frame")
            break
        cv2.imshow("Test Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()