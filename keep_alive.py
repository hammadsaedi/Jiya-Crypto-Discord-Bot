from flask import Flask
from threading import Thread

app = Flask(__name__)

message = ""

@app.route('/', methods=['GET'])
def home():
    return """
    <h2>Crypto Discord Bot</h2>
    """

def run_flask_app():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run_flask_app)
    thread.start()