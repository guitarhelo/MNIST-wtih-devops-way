
# AI - with Tensorflow

# Jupyter Notebook

Basic Jupyter Notebook Practice.  

    please log in https://colab.research.google.com/

    Create new notebook

When you see this [+ CODE] here, it means you click the top left icon which says +CODE  to create a new code segment in Jupyter notebook

*NOTE :  WAIT for instructor.  Instrucutor would lead you through.*

[+ CODE]

    # APJC CSC Ignite 2019
    # First Jupyter Notebook Exercise

    a = 10
    b = 20
    c = a + b
    c

Run It

[+ CODE]

    print ('Wow    {} + {} = {}'.format(a,b,c))

Run it, step by step

Save it

# Digit OCR

*NOTE : Complete step 1 by yourself.*

## Step 1

Remove all the earlier codes. Start fresh.

Let's use the Tensorflow package

[+ CODE]

    import tensorflow as tf

    tf.__version__

Get the dataset for our exercise

[+ CODE]

    # Loading the dataset for the Digits OCR
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    print("Training data")
    print(len(X_train))
    print(X_train.shape)

    print(len(y_train))
    print(y_train.shape)

    print("Testing Data")
    print(len(X_test))
    print(X_test.shape)

    print(len(y_test))
    print(y_test.shape)

Let's explor the data to understand it more.

[+ CODE]

    X_train[3]

So what's the digit it represents?
Is it tagged correctly?

[+ CODE]

    y_train[3]

Let's plot it out

[+ CODE]

    # Let's visualise how the train data looks like
    index = 3
    
    pred = X_train[index]
    pred = pred.reshape([28, 28]);
    plt.gray()
    plt.imshow(pred)
    plt.show()

    print("Tagged digit: ", y_train[index])

Opps..... error.
Let's understand libaries/packages
Add this on top, same place as the 'import tensorflow'

    import matplotlib.pyplot as plt 

## Step 2

Now... let's switch gear for a moment.

Q: Are the codes Python codes?

Q: Would it work on the Linux machine we were using earlier?

A: Let's export the code and put it there to try!

* Export the .py code
* Copy into the Ubuntu
* Try to run it
* What's the outcome?

    Pause here to wait for instructor.  Make sue everyone at the same page before we proceed

* Why no error in colab?

    $ pip3 tensorflow
    $ sudo apt install python3-pip

* This is a good point to have a break when the system installs

Now.  All able to run the code?

Note : Because we only SHELL into the Ubuntu.  There is no UI.  So you wouldn't see the graphics.  if you see the response "Tagged digit: 1", you are successful

Q: Notice how easy to install the required packages etc

Q: Why did we have problem deploying the code onto the ubuntu?

Q:  So if developer developed in Colab, or other platform, then deploy onto the Ubuntu, are there potential problems?  How to reduce such problems?

## Step 3

Back to Jupyter Notebook

Let's build the NN and do some training

We will study the dataset more to ensure we understand what is happening

[+ CODE]

    #Scale the values by 255, so it is between 0 to 1
    X_train_scale = X_train / 255.0
    X_test_scale = X_test / 255.0

    #Show the first 25 data in the training set
    plt.figure(figsize=(10,10))
    for i in range(25):
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(X_train_scale[i], cmap=plt.cm.binary)
        plt.xlabel(y_train[i])
    plt.show()

## Step 4

So the training data is all good
Let's go into building the NN, and training it

[+ CODE]

    #The NN layer setting
    #n_input = 784  # input layer (28x28 pixels)
    #n_hidden1 = 512  # 1st hidden layer
    #n_hidden2 = 256  # 2nd hidden layer
    #n_hidden3 = 128  # 3rd hidden layer
    #n_output = 10  # output layer (0-9 digits)
    #learning_rate = 1e-4
    #n_iterations = 1000
    #batch_size = 128
    #dropout = 0.5

    #setup the model for training
    model = keras.Sequential([
        # transforms the format of the images from a 2d-array (of 28 by 28 pixels), to a 1d-array of 28 * 28 = 784 pixels.  No parameters to train
        keras.layers.Flatten(input_shape=(28, 28)),
        # 1st hidden layer
        keras.layers.Dense(32, activation=tf.nn.relu),
        # 2nd hidden layer
       keras.layers.Dense(16, activation=tf.nn.relu),
        # this returns an array of 10 probability scores that sum to 1. Each node contains a score that indicates the probability that the current image belongs to one of the 10 classes.
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy']  )

    model.summary()

Error?  That's becuase a library is missing.  We uses *Keras*, which is a already inside the tensorflow.  So technically, we can refer to it by tf.keras.  But it is easier to refer to as keras.  So add the codes in the import section (right on top with import tensorflow)

    from tensorflow import keras 

That's all is needed to create the model.
Now, let's train it

[+ CODE]

    # Let's run the training
    history = model.fit(X_train_scale, y_train, epochs=20)

Let's see how accurate is the model

[+ CODE]

    # This eval the model against the test dataset
    test_loss, test_acc = model.evaluate(X_test_scale, y_test)
    print('Test accuracy:', test_acc)

[+ CODE]

    ##  Run through the test dataset.  The prediction is output to the variable 'predictions'
    predictions = model.predict(X_test_scale)

## Step 5

Let's study the classifications. We will try to plot it out.  Again, will use a library, so add this to the improts

    import numpy as np

Now, add the following codes

[+ CODE]

    # Routines to help to plot the data
    def plot_image(i, predictions_array, true_label, img):
        predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])

        plt.imshow(img, cmap=plt.cm.binary)

        predicted_label = np.argmax(predictions_array)
        if predicted_label == true_label:
            color = 'blue'
        else:
            color = 'red'

        plt.xlabel("I:{} " "{} {:2.0f}% ({})".format(i, predicted_label,
                                    100*np.max(predictions_array),
                                    true_label),
                                    color=color)

    def plot_value_array(i,  predictions_array, true_label):
        predictions_array, true_label = predictions_array[i], true_label[i]
        plt.grid(False)
        plt.xticks([0,1,2,3,4,5,6,7,8,9])
        plt.yticks([0,0.5,1])
        thisplot = plt.bar(range(10), predictions_array, color="#777777")
        plt.ylim([0, 1])
        predicted_label = np.argmax(predictions_array)

        thisplot[predicted_label].set_color('red')
        thisplot[true_label].set_color('blue')

    ##########################################

    #Show25 data in the test set
    offset = 2000

    plt.figure(figsize=(10,10))
    # for i in range(25):
    for i in range(36):
        plt.subplot(6,6,i+1)
        plot_image(i+offset, predictions, y_test, X_test_scale)

    plt.show()

Spend some time to understand the above model.  And the plots.

* First Box.
  * From picture, what is the digit?
  * What the NN classified it as?
  * What is the Tagged data?
  * Did the NN classify it correctly?

* Look at box index 2004 (top row, 5th from left)
  * From picture, what is the digit?
  * What the NN classified it as?
  * What is the Tagged data?
  * Did the NN classify it correctly?

Let's get into the details of couple of the classification.  Put these codes

[+ CODE]

    ## some interesting dataset to see 2004, 2024,   2043,   
    i = 2004
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions, y_test, X_test_scale)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions,  y_test)
    plt.show()

    i = 2018
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions, y_test, X_test_scale)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions,  y_test)
    plt.show()

    i = 2043
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions, y_test, X_test_scale)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions,  y_test)
    plt.show()

Q: What does the NN actually look for?
Q : Why is the 8 classified wrongly?

Action : Go and play around with the model.

    * Try to make it more accurate
    * How does the training accuracy changes, vs the actual test accuracy?

## Step 6

Now that we have trained it.
We need to deploy it.

Let's save the model, so we don't need to re-train it again.

[+ CODE]

    ## To export the trained model

    # Save entire model to a HDF5 file
    model.save('my_model16.h5')

ACTION : Since it is on the cloud.  Find a way to save the file to your windows jump host.  We need this .h5 file later

# Recap

* How's Jupyter Notebook?
* AI with Tensorflow. Easy? Hard?
