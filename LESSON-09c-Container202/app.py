from flask import Flask, request
from datetime import datetime
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello My {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>IP:</b> {hostip}<br/>" \
           "<b>DateTime:</b> {datetimenow}<br/>"

    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), hostip=request.host, datetimenow=datetime.now())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
