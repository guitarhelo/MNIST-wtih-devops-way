import os
import requests
import json

from flask import Flask, render_template, request, send_from_directory
import numpy as np                  # numeric processing package
import skimage
import skimage.io as io      # image processing

from tensorflow import keras

__author__ = 'lmw'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

DIGITOCR_API = 'http://172.24.5.98:4001/api'

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'uploaded_images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))

    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):

        filename = upload.filename
        destination = "/".join([target, filename])

        upload.save(destination)

        f = open(destination, 'rb')
        myfiles = {'image': f}
        digitocr = requests.post(DIGITOCR_API, files = myfiles)
        f.close()
        digitocr_dict = digitocr.json()

        prediction = digitocr_dict['prediction']
        ver = digitocr_dict['ver']

# return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete_display_image.html", image_name=filename, ocr_output = prediction, ocr_ver = ver )


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("uploaded_images", filename)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4555))
    app.run(host='0.0.0.0', port=port, debug=True)