import cv2

rtsp_url = 'http://localhost:8000/video_feed'

cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('RTSP Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
