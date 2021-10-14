from ws4controls import Ws4dummy
from flask import Flask

app = Flask(__name__)
ws4inter = Ws4dummy()

homepage = open("index.html")

@app.route("/")
def home():
    return homepage.read()

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

@app.route("/up", methods = ["POST"])
def up():
    ws4inter.move_up()
    return "Turned up"

@app.route("/down", methods = ["POST"])
def down():
    ws4inter.move_down()
    return "Turned down"

app.run(host="0.0.0.0")