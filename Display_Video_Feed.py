import sys
import cv2


def display_obs_stream(stream_url):
    # Open a video capture object
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Error: Unable to open video stream.")
        return

    # Create a window to display the video stream
    cv2.namedWindow('OBS Stream', cv2.WINDOW_NORMAL)

    try:
        while True:
            # Read a frame from the video stream
            ret, frame = cap.read()

            if not ret:
                print("Error: Unable to read frame.")
                break

            # Display the frame
            cv2.imshow('OBS Stream', frame)

    except KeyboardInterrupt:
        # Release the video capture object and close the window
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    obs_stream_url = sys.argv[1]
    print(obs_stream_url)
    if len(sys.argv) > 1:
        display_obs_stream(obs_stream_url)
    else:
        print("No url for feed provided.")