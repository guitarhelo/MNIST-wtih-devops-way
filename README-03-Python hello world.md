#  Python Programming

## Install Python

Where shall you type the commands?  Ubuntu (using the PuTTY)

Let's see what's in the system

    $ python -V

See the version.  it is old

    $ python3 -V

It is 3.6.8, not latest, but much newer.

We will use *Python3*.  Still lots of Python 2.7 out there, but 2.7 support is going to stop.

It is already preinstalled!  So you don't even need to do anything and can start using Python on typical Unix installation

Installing it is also easy, but we wouldn't do it now.  We would learn to install something else later.

## Interactive Mode

Python is an interpreter lanuage.  So we get into the interpreter first

    $ python3

Let's do some exercise with Python

    >>> print ("Hello World")

    >>> print ('Hello World Again')
    
    >>> a = 10
    >>> a
    >>> print(a)
    >>> b = 20
    >>> print (a + b)

    >>> print ("wow... this is easy", c)

notice error msg

    >>> c = a + b

(try up arrow twice)

    >>> print ("wow... this is easy", c)

A little more formats 

    >>> print ('I think %n + %n is  %n' % (a, b, a+b))

How to exit python?

    >>> quit()

## A Python "Program"

Create a directory, call it 'les03', short for lesson 3.  A note, in following lessons, will refer to create directory 'les##', replace ## with the lesson number.

    $ mkdir les03
    $ cd les03

Create a file and edit a file called 'myfirst.py'

    $ nano myfirst.py

Put in a simple program like what you did above, eg

    a = 10
    b = 20
    print ('I think %n + %n is  %n' % (a, b, a+b))

Save and exit (ctrl-X)

Now run it by

    $  python3 myfirst.py

You are now a Python Programmer :)

## Using a code editor to make our lifes easier

In this setup, we run the *Visual Studio Code* on the Windows Jump Host

The Ubuntu is already configured with a SAMBA share.
On Jump host.  Map a network drive to the Ubuntu

Then you can see the files from Jump Host

    Launch the Visual Studio Code

    open your file 'myfirst.py'

    make a change.

    Run the program again on Ubuntu

See the beautiful highlighting?

Note: If the highlighting doesn't work, VS Code would prompt you to install some components.  You may need to install python3 on the windows for some more features of the VS Code to work.

# Recap

You can create a Python program
You can run it
