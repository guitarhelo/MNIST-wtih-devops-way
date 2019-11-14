# Some LINUX activites to get familiar with the desktop

In Windows.  Start a SSH to connect to Linux host

Once inside

    $ ls
    $ ll
    $ ls -la
    $ ls -help

    $ man ls
    
    $ mkdir mytest
    $ cd mytest
    $ pwd

Note:  Those strange commands are actually short form of many english words.  So good to know the full name to help to remember.

+ ls   - **L**i**S**t
+ cd   - **C**hang**D**irectory
+ pwd  - **P**resent **W**orking **D**irectory
+ mkdir - **M**a**k**e **Dir**ectory

Get back to home directory

    $ cd
    $ cd mytest
    $ cd .
    $ cd ..

Launch an editor and create a new file. Type something inside and save it

    $ nano myfirstfile.txt
     
    $ ls

To see what's inside

    $ cat myfirs  [after typing part of the filename, hit the TAB key. Autocompletion!]

Delete the file and directory

    $ rm myfirstfile.txt
    $ cd ..
    $ rm -r mytest

Let's know about the system
    $ ip addr show
    $ hostname

Let's try to change the name of the system, to your name, so it is easy to refer.
There is a file called *hostname* at */etc*

1. Go to the directory
2. Try to see what is in the file
3. Edit the content to your name.

Any problem?

    sudo

    $ cd /etc/hostname

    $ ls

    see the file called hostname?
    Just change the content inside the file.

    Also change /etc/hosts.  The secondline 
    
    127.0.1.1  your-new-machine-name

Up and Down arrows

    Try to press 'up' arrow on keyboard a few times

You see the previous commands?  That save lots of retyping

Try

    $ history

If you see a line, for example 12 that is the command you want to run again... you can

    $ !12

Linux is for Lazy people!

Let's reboot the system to make the new hostname seen

    $ reboot now

:)

    $ sudo reboot now

The system will take a minute or two to reboot

## Recap

How is commandline?  hard/easy?

Why commandline vs GUI?

------

## Skip remaining

Some other useful commands

    $ sudo -i

    $ export   / unset  / echo 
