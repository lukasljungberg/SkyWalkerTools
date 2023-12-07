import cv2

rtsp_url = 'rtsp://127.0.0.1:8554/video_feed'

cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    print(frame)

    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('RTSP Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

