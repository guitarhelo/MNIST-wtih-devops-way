# Putting everything together

## Concept

* You have code that uploads a picture file
* You have code that does 'inference' (from the Jupyter Noteobook exercise)

Now join the code together to achieve the demo I showed

Let's try to do it yourself

## Some suggestion/reference foryou

If you want more ideas

### My step 1

Since my inference code actually works with a 28x28 matrix.  But the final software needs to load a .jpg file and decode.

So first step I did was to change the inference code to read the .jpg file, resize to 28x28 resolution, extract the 28x28 matrix.

The code is at 'app_run_on_terminal.py'

### MY Step 2

Once step 1 is done, you just have to paste this code into the right place in the 'file upload' program you did earlier

Basically, instead of just call out a 'display picture' html, the app need to run the step 1 code.

The code is at 'app.py'

# Recap

