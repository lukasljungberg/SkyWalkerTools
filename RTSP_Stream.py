import cv2
import http.server
import socketserver
import threading
import time

class VideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Change the index if you have multiple cameras
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def get_frame(self):
        ret, frame = self.cap.read()
        if ret:
            _, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

class StreamingHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/video_feed':
            content_type = 'multipart/x-mixed-replace; boundary=frame'
            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.end_headers()

            video_capture = VideoCapture()
            try:
                while True:
                    frame = video_capture.get_frame()
                    self.wfile.write(b'--frame\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
                    time.sleep(0.1)
            except BrokenPipeError:
                pass
            finally:
                video_capture.cap.release()

        else:
            self.send_response(404)
            self.end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def run_server():
    address = ('', 8000)
    httpd = ThreadedHTTPServer(address, StreamingHandler)
    print('Server started at http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
