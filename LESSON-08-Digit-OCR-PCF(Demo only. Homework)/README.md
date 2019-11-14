
# Deploy using PCF  (PAS)

## Installing the CF Commandline

Instructions at
     <https://docs.cloudfoundry.org/cf-cli/install-go-cli.html#pkg-linux>

Or just execute the following

     $ wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | sudo apt-key add -

     $ echo "deb https://packages.cloudfoundry.org/debian stable main" | sudo tee /etc/apt/sources.list.d/cloudfoundry-cli.list

     $ sudo apt-get update

     $ sudo apt-get install cf-cli

## Let's deploy it

## Step 1

     PCF api server at   https://login.system.csc-dell.com/login

     username : user2
     password : ****************


          cf api --skip-ssl-validation api.system.csc-dell.com
          cf login -u user2

## Step 2

Guess what it takes to push the app there?

Make sure you are in the directory with all the sourcecode.

     cf push testing

Error?  Here are some configuration files needed (some minor change)

<https://gist.github.com/ihuston/e87c1d4719f7e72e9760>

* Change the Flask to use the port provided by PCF

    if __name__ == "__main__":
        port = int(os.getenv("PORT", 4555))
        app.run(host='0.0.0.0', port=port)

* Since the code uses os library, add *import os* in code

* create file 'runtime.txt' with following content. To tell PCF which version of Python to use

    python-3.6.7

* create file 'Procfile', with following content, to tell PCF what command to run

    web: python app.py

* 'requirements.txt' file for all the libraries

# Recap

Easy / Hard?

Just run it
