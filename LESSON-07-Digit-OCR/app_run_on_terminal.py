__author__ = 'manwei'
import os                           # default.  OS operations like files etc
import numpy as np                  # numeric processing package
import matplotlib.pyplot as plt     # graph plotting
import skimage
import skimage.io as io      # image processing
from skimage import data, data_dir       # image processing sample datas

from tensorflow import keras
# from tensorflow.keras import layers

model = keras.models.load_model('my_model16.h5')
model.summary()


# Load the image

filename = os.path.join('./test_image', 'my test picture digit7.jpg')

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


# print(image_small2[0])

print('The probability are')
print(prediction[0])
print ("OCR output is ", (np.argmax(prediction[0])))


# print(image_small1)

plt.imshow(image_small2[0], cmap=plt.cm.binary)
# plt.imshow(image_small, cmap='gray')

plt.show()
