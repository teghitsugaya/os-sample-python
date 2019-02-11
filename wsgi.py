from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    hostname = socket.gethostname()
    return "Hello World! {{ hostname }}"

if __name__ == "__main__":
    application.run()
