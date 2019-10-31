import os
from flask import Flask, render_template, request, send_from_directory
import numpy as np                  # numeric processing package
import skimage
import skimage.io as io      # image processing

from tensorflow import keras

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

        model = keras.models.load_model("/".join([APP_ROOT, '/my_model16.h5']))
            
        image = io.imread(destination,as_gray=True)

        # resize it
        image_small = skimage.transform.resize(image, (28,28), preserve_range=True, anti_aliasing=True, anti_aliasing_sigma=None)
        # invert the color 1 to 0, 0 to 1
        image_small1 = 1 - image_small  # when I trained the model.  It is black ink on white background.  Everywhere 0, ink is 1

        # do inference
        # need to make it a 3 dimension np.array.  that's what the model expects
        image_small2 = np.empty((1,28,28))
        image_small2[0] = image_small1

        prediction = model.predict(image_small2)


        # print(image_small2[0])

        # print('The probability are')
        # print(prediction[0])

        #print ("OCR output is ", (np.argmax(prediction[0])))


    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete_display_image.html", image_name=filename, ocr = np.argmax(prediction[0]))

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("uploaded_images", filename)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 4555))
    app.run(host='0.0.0.0', port=port, debug=True)