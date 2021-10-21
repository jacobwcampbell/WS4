import cv2 as opencv

def gen_frames(camera):
    """Generator function that continuously yields frames from a webcam connected to the client device"""
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = opencv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')