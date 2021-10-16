import ws4video
from ws4controls import Ws4dummy
from flask import Flask, render_template, Response

app = Flask(__name__)
ws4inter = Ws4dummy()

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    return Response(ws4video.gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/fire", methods = ["POST"])
def fire():
    ws4inter.fire()
    return "Fired"

@app.route("/left", methods = ["POST"])
def left():
    ws4inter.move_left()
    return "Turned left"

@app.route("/right", methods = ["POST"])
def right():
    ws4inter.move_right()
    return "Turned right"

app.run(host="0.0.0.0")