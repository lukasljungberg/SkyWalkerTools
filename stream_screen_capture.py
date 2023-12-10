import sys
import pyautogui
import imageio
import time
import subprocess


def capture_and_stream(rtmp_server_url):
    ffmpeg_process = None
    try:
        # Use subprocess to run ffmpeg command for streaming
        cmd = [
            "ffmpeg",
            "-f", "image2pipe",
            "-r", "1",  # Adjust the frame rate as needed
            "-s", "1920x1080",  # Adjust the screen resolution as needed
            "-i", "-",  # Input from pipe
            "-c:v", "libx264",
            "-b:v", "512k",  # Adjust the bitrate as needed
            "-f", "flv",
            rtmp_server_url
        ]

        ffmpeg_process = subprocess.Popen(cmd, stdin=subprocess.PIPE)

        while True:
            # Capture the screen
            screenshot = pyautogui.screenshot()

            # Convert the screenshot to bytes
            img_byte_array = screenshot.tobytes()

            # Write the bytes to the ffmpeg process stdin
            ffmpeg_process.stdin.write(img_byte_array)

            # Adjust the delay according to your needs
            time.sleep(1)

    except KeyboardInterrupt:
        print("Screen capture and streaming stopped.")
    finally:
        if ffmpeg_process:
            ffmpeg_process.stdin.close()
            ffmpeg_process.wait()

if __name__ == "__main__":
    stream_url = sys.argv[1]

    if "rtmp" not in stream_url or len(sys.argv) < 2:
        print("Please provide a valid url")
        exit(0)
    capture_and_stream(stream_url)
