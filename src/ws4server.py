import ws4video as video
import ws4controls as controls

from cv2 import VideoCapture
from threading import Thread
from flask import Flask, render_template, Response

flaskapp = Flask(__name__)
ws4inter = controls.Ws4dummy()
camera = VideoCapture(0)

@flaskapp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@flaskapp.route("/video_feed")
def video_feed():
    return Response(video.gen_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@flaskapp.route("/fire", methods = ["POST"])
def fire():
    thr = Thread(target=ws4inter.fire)
    thr.start()
    return "Fired"

@flaskapp.route("/left", methods = ["POST"])
def left():
    thr = Thread(target=ws4inter.move_left)
    thr.start()
    return "Turned left"

@flaskapp.route("/right", methods = ["POST"])
def right():
    thr = Thread(target=ws4inter.move_right)
    thr.start()
    return "Turned right"

if __name__=="__main__":
    flaskapp.run(host="0.0.0.0")