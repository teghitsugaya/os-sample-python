from flask import Flask, render_template, redirect, url_for, request,make_response
import socket
import os

application = Flask(__name__)

@application.route("/")
def hello():
    hostname = socket.gethostname()
    return render_template('profiles.html', hostname=hostname)

if __name__ == "__main__":
    application.run()
