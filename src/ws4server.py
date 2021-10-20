import ws4video as video
import ws4controls as controls

from flask import Flask, render_template, Response

flaskapp = Flask(__name__)
ws4inter = controls.Ws4dummy()

@flaskapp.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@flaskapp.route("/video_feed")
def video_feed():
    return Response(video.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@flaskapp.route("/fire", methods = ["POST"])
def fire():
    ws4inter.fire()
    return "Fired"

@flaskapp.route("/left", methods = ["POST"])
def left():
    ws4inter.move_left()
    return "Turned left"

@flaskapp.route("/right", methods = ["POST"])
def right():
    ws4inter.move_right()
    return "Turned right"

if __name__=="__main__":
    flaskapp.run(host="0.0.0.0")