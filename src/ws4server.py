from ws4controls import Ws4dummy

from flask import Flask

app = Flask(__name__)
ws4 = Ws4dummy()

@app.route("/")
def home():
    return """
<script>
function sendfire() {
    let request = new XMLHttpRequest();
    request.open("POST", "fire", true);
    request.send()
}
</script>

<button onclick="sendfire()">Fire</button>
"""

@app.route("/fire", methods = ["POST"])
def fire():
    ws4.fire()
    return "Fired"

app.run(host="0.0.0.0")