import sys
import pyautogui
import imageio
import time
import validators


def capture_and_stream(rtmp_server_url):
    try:
        # Create a writer to the RTMP server
        writer = imageio.get_writer(rtmp_server_url, fps=1)

        while True:
            # Capture the screen
            screenshot = pyautogui.screenshot()

            # Convert the screenshot to a numpy array
            img_array = imageio.core.util.Array(screenshot)

            # Add the frame to the writer
            writer.append_data(img_array)

            # Adjust the delay according to your needs
            time.sleep(1)
    except KeyboardInterrupt:
        print("Screen capture and streaming stopped.")
    finally:
        writer.close()


if __name__ == "__main__":
    stream_url = sys.argv[1]

    if not validators.url(stream_url) or len(sys.argv) < 2:
        print("Please provide a valid url")
        exit(0)
    capture_and_stream(stream_url)
