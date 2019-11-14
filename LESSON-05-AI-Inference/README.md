
# Deploy the trained model

Obj - Don't retrain. Just call out saved model and deploy it.

## Step 1

Creat new Jupyter notebook

You would need all the same libraries, so let's add them first

[+ CODE]

    # APJC CSC Ignite 2019
    # Deploying the trained inference engin
    # Maint : Lee Man Wei
    # 2019 Sep 18

    # Standard Library
    import numpy as np

    # Third Part
    import tensorflow as tf
    import matplotlib.pyplot as plt 
    from tensorflow import keras 

You have to copy your saved .h5 file into where this new notebook can see
Figure out how to do it :)
We will wait

[+ CODE]

    new_model = keras.models.load_model('my_model16.h5')

    new_model.summary()

Can you see that it is the same as the one you trained before.

We will spend some time to study this, to make sure we understand the model

[+ CODE]

    #  To save / restore , view weights only
    weights = new_model.get_weights()  # Retrieves the state of the model.

    # Let's see what is stored in the model wegiths
    print ("Typ: ", type(weights))
    print ("Length: ", len(weights))

Let's print out the first item to study it

[+ CODE]

    print ("index [0] Type ", type(weights[0]))
    print ("index[0] Length: ", len(weights[0]))
    print ("")
    print ("Each [0] item type is", type(weights[0][0]))
    print ("Each [0] item len is ", len(weights[0][0]))
    print ("")
    print("Example of [0][0]")
    print(weights[0][0])

Second item

[+ CODE]

    print ("index [1] Type ", type(weights[1]))
    print ("index[1] Length: ", len(weights[1]))
    print ("")
    print ("Each [1] item is", type(weights[1][0]))
    print ("")
    print(weights[1])

Third item

[+ CODE]

    print ("index [2] Type ", type(weights[2]))
    print ("index[2] Length: ", len(weights[2]))
    print ("")
    print ("Each [2] item is", type(weights[2][0]))
    print ("")
    print(weights[2][0])

Fourth Item

[+ CODE]

    print ("index [3] Type ", type(weights[3]))
    print ("index[3] Length: ", len(weights[3]))
    print ("")
    print ("Each [3] item is", type(weights[3][0]))
    print ("")
    print(weights[3])

It makes sense?

First layer is a 28 x 28 = 784
First hidden layer is 32 nureons
Second hidden layer is 16 nureons

## Step 2

Now let's put in some data to run the prediction

[+ CODE]

    #test_data1 = np.empty((1,28,28))
    test_data1 = np.array([[
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   6,  53, 115, 179, 184, 255,254, 246, 179, 175, 106,  44,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0, 146, 254, 254, 254, 254, 254,254, 254, 218, 254, 254, 122,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0, 194, 254, 186, 204, 190, 150, 68,  59,  32, 201, 254, 227, 141,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,  72, 249, 155,   8,   0,   0,  0,  63, 213, 254, 254, 240,  80,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0, 115, 254, 154,   0,   0, 89, 246, 254, 249, 130,  21,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0, 119, 254, 131,  79,246, 252, 124,  27,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   6, 124, 250, 254,254, 102,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 121, 254,254,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 147, 254,254,  85,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  36, 239, 240,223, 251,  62,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 218, 147, 23, 207, 237,  50,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  50, 239,  11,  0,  15, 230, 204,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  39, 234,   0,  0,   0,  92, 243, 155,   2,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  36, 233,   0,  0,   0,   0, 117, 254, 101,   0,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 202,   0,  0,   0,   0,   7, 175, 245,  67,   0,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 104,  56,  0,   0,   0,   0,  14, 194, 184,   6,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  47, 170,  7,   0,   0,   0,   0,  36, 237, 107,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  95,169,   9,   0,   0,   0,   0, 131, 167,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 80, 199,  48,   0,   0,   0, 105, 194,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  48, 190, 224, 154, 141, 215, 128,   0,   0,   0,   0,   0,  0,   0],
        [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,   0]]])

    # this data is supposed to be 8.  
    y_test = [8]

    #Let's plot it
    pred = test_data1[0]
    pred = pred.reshape([28, 28]);
    plt.gray()
    plt.imshow(pred)
    plt.show()

[+ CODE]

    #scale it just like when we trained the model
    test_data2 = test_data1 / 255.0
    plt.imshow(test_data2[0], cmap=plt.cm.binary)
    plt.show()

## Step 3

Now you need to refer to your previous codes

* Get the predicitons
* Plot the predictions to see if it is correct
* This is to confirm the model is indeed deployed correctly

CHEAT.  That's the answer below if you run out of time

[+ CODE]

    # Now let's use the restored model to do the prediction

    new_prediction = new_model.predict(test_data2)

    print(new_prediction[0])
    print ()
    print(np.argmax(new_prediction[0]))

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

    def plot_value_array(i, predictions_array, true_label):
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


    i = 0
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, new_prediction, y_test, test_data2)
    plt.subplot(1,2,2)
    plot_value_array(i, new_prediction,  y_test)
    plt.show()

## Step 4

You can manually edit the input data.  To see how the interference change.  Just to be convinved the model is working correct.
(eg, change the 8 to looks more like 8, and see if the classification becomes correct)

# Recap

* How to load a model
* We studied the structure of the model, and confirmed our understanding of ANN
* We have standlone code that can OCR a handwritting represented by a 28x28 input matrix.

What would be our next step?
