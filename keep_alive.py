from flask import Flask
from threading import Thread

app = Flask('hodl bot')

@app.route('/', methods=['GET'])
def home():
  res = "<h1>Crypto Bot</h1>"
  return res

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()