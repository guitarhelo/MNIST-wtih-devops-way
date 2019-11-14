# Git

One popular Version Control System

Git is the software to do the job
Github is a hosted Git server

## Installation

We are doing this on the JUMP host (windows)

Reason is we are using the VisualCode on the windows, and will write the file to the Ubuntu via a shared drive.

So we want these files on the Windows machine for reference.

**DO NOT** copy the file over to the Ubuntu machine

[ACTION]

    Open command line

    > git
    > git version

If you see something, it is working.  Else please install from

    https://git-scm.com/download/win

Note. We purposely don't install the Github version.  Just to show, it does the SAME thing.

### Step 1 - Create a local repository to pull the file to

    > mkdir funwithdevops
    > cd funwithdevops

### Step 2 - Init it

    > git init

### Step 3 - Pull it

    > git remote add origin https://github.com/LMWCoding/fun-with-devops.git
    > git pull origin master 

Now you have a copy in your company that you can work on.

--------

## Skip the rest below.  Just FYI if you want to use Git in future

    > git fetch https://github.com/LMWCoding/fun-with-devops.git master

## Creating your own project etc

Using it locally first

### Step 1 - Create a local git repository

In the directory you are storing source code (or just create a new blank directory)

    > git init

To check the status

    > git status

### Step 2 - The staging environment

Tell git what files you want to add

    > git add filename

    or to add everything

    > git add *

Commit that to the repository

    > git commit -m "type what message you have here"

### Step 3 - Optional.  You can now add branch etc

If you are at masters, and want to create a branch under masters, just do a checkout -b

    > git checkout -b new-branch-name

## Github

### Step 4 - Create GitHub Account

self explanatory
Create account
create new repository in Github

### Step 5 - Push

you would get the name in the Github UI that you created the repository

    > git remote add origin https://github.com/GithubUsername/NewRepositoryName.git

    > git push -u origin master

You would be prompt to log in

Note : Think of the 'origin' as the alias to refer to the remote repository.

### Step 6 - Subsequent Push / Branch

    > git push origin my-new-branch
