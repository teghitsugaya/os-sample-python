from flask import Flask
import socket

application = Flask(__name__)

@application.route("/")
def hello():
    hostname = socket.gethostname()
    return render_template('profile.html', hostname=hostname)

if __name__ == "__main__":
    application.run()
