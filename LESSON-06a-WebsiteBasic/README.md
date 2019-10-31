# Programming a simple webpage #

## Objective

* Simple reactive webpage
* Programming Language : Python
* Framework : Flask

What is a framework?

## Let's get started

You have two choices how to finish this module

* Option 1 

    http://letmegooglethat.com/?q=python+flask+ubuntu+18.04

    Note : For simplicity, we can skip creation of python virtual environment

* Option 2

    Follow steps below


### Step 1 - Create Virtual Envronment (Python)

This installs the package use for creating virtual envrionment.  This is only done once.  No need to install in future creation of virtual envrionment

    $ sudo apt install python3-venv

Create directory 'les##'

    $ mkdir les06
    $ cd les06

Create the virtual envrionment inside that directory
    
    $ python3 -m venv venv-w

Activate it by 

    $ source venv-w/bin/activate

Create a simple python program 'app.py' code and run it.  Just a recap so you know what you are doing


    # Example of simple python code
    a = 10
    print ('I am making great progress',a)

Make sure you can run it

### Step 2 - Install Flask

Install Flask, it is a Web Framwork for Python

    $ pip3 install Flask

PIP/PIP3 is how python installs packages

Note : Once virtual envrionment is active. You can use python and pip instead of python3/pip3


### Step 3

Write the first Flask app

    import flask
    from flask import Flask, request, render_template, send_from_directory   #framwork for web

    __author__ = 'manwei'

    app = Flask(__name__)

    @app.route("/")
    def index():
        return ("hello world")

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=4001, debug=True)


Now run this code

How do you know it is work?

    Open Chrome
    Point to your ubuntu xxx.xxxx.xxx.xxx:4001  (eg 172.24.5.98:4001) 

What is the PORT 4001 thing?
Can we make it serve the standard port 80?

    Change the code to make it port 80

Any problem?  Try SUDO
Still doesn't work?  Try do this instead

    sudo ./venv-w/bin/python3 app.py

What's happening?

* Any port lower than 1024 needs root permission
* But sudo doesn't follow the path in virtual env.  Hence must specifically point to the python3 in the virtual environment

    Change it back to port 4001

Let's make a change to make the code easier to deploy
We want to try not to hard code the PORT number

Try to find out where you should change the code to following

    if __name__ == "__main__":
        port = int(os.getenv("PORT", 4001))
        app.run(host='0.0.0.0', port=port, debug=True)

    Run the code and observe which port does the app serve the page.

    Error?  Why? How to fix it?

Make sure all can reach this stage.  Should be same as before.

Now in the shell

    $ export PORT=4002
    $ echo $PORT

    $ python3 app.py

Now observe which port is the web serving the web page


Clear the envrieonmetal variable by

    $ unset PORT
    $ echo $PORT

Note :
    That's how the default value gets in
    os.getenc(variable, default)

### Step 4

Now try to add another web page.  So that when you go http://xxx.xxx.xxx.xxx/hello, it would show something else

Add the following code (guess where to add it?)

    @app.route("/hello")
    def hello():
        return ("hello who?")


How to take some inputs from the weblink?

    @app.route("/hello/<string:name>/")
    def helloName(name):
        return "Welcome " + name

Test it out

    http://xxx.xxx.xxx.xxx:4001/hello

    http://xxx.xxx.xxx.xxx:4001/hello/ManWei


## HTML, CSS etc (Make it beautiful)

### Step 5

[Action]

    copy the template & static folders (from your jump host) to the Ubuntu.  That is, for eg,
    from LESSON06/templates to les06/templates directory

[CODE - add to Library section]

    from random import randint


[CODE - add code section]


    @app.route("/quote/<string:name>/")
    def quote(name):

        quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
                "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
                "'To understand recursion you must first understand recursion..' -- Unknown",
                "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
                "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
                "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
        randomNumber = randint(0,len(quotes)-1)
        quote = quotes[randomNumber]

        return render_template(
            'test.html',**locals())


Now try it out.

Let's walk through and understand how it works
See how the variables are passed around?

### Step 6

Can we just swop out the .html / .css file and change the layout?

We would change the .css file.

Take a look what is the inside the orginal /static/style.css file

It is blank.  Actually, I dind't specify any formatting.

Let's replace it with the mystyle.css

    rm style.css
    cp mystyle.css style.css

* you can use the studio code to do the rename (instead of unix command line)

Now refresh the web browser to see the effect

**IMPORT **: Due to some browser caching the CSS file, if you edit the CSS file, need to force the brower to do a FULL RELOAD to see the effect (shift-F5 for Chrome)

You can try to edit the /static/style.css to see you can change the output


## Recap

* Built a simple web page
* html file is really specifying the information to display
* css file is the styling