import os
import json
import uuid

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

import numpy as np                  # numeric processing package
import skimage
import skimage.io as io      # image processing

from tensorflow import keras

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = './uploads'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
  return 'go to /api for RESTAPI endpoints for Digits OCR'

@app.route('/api', methods = ['GET','POST'])
def api():
  if request.method == 'GET':
    image = request.args.get('image',)
    image = int(image) * 2
    return jsonify({'prediction':image})
  elif request.method == 'POST':
    if 'image' not in request.files:
      resp = jsonify({'message' : 'No file part in the request'})
      resp.status_code = 400
      return resp
    imagefile = request.files['image']
    if imagefile.filename == '':
      resp = jsonify({'message' : 'No file selected for uploading'})
      resp.status_code = 400
      return resp
    if imagefile and allowed_file(imagefile.filename):
      filename = secure_filename(imagefile.filename)
      # change to a UUID filename
      filename_ext = filename.rsplit('.',1)[1].lower()
      filename = str(uuid.uuid4()) + '.' + filename_ext
      imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      prediction = digitocr(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      resp = jsonify({'message' : 'File successfully uploaded' , 'prediction' : prediction , 'ver' : '1.0'})
      resp.status_code = 201
      return resp
    else:
      resp = jsonify({'message' : 'Allowed file types are png, jpg, jpeg, gif'})
      resp.status_code = 400
      return resp


def digitocr(filename):
  model = keras.models.load_model("/".join([APP_ROOT, '/my_model16.h5']))
            
  image = io.imread(filename,as_gray=True)

  # resize it
  image_small = skimage.transform.resize(image, (28,28), preserve_range=True, anti_aliasing=True, anti_aliasing_sigma=None)
  # invert the color 1 to 0, 0 to 1
  image_small1 = 1 - image_small  # when I trained the model.  It is black ink on white background.  Everywhere 0, ink is 1

  # do inference
  # need to make it a 3 dimension np.array.  that's what the model expects
  image_small2 = np.empty((1,28,28))
  image_small2[0] = image_small1

  prediction = model.predict(image_small2)
  ocr = int(np.argmax(prediction[0]))
  return (ocr)

if __name__ == "__main__":
  port = int( os.getenv("PORT",4001))
  app.run(host='0.0.0.0', port=port, debug=True)

