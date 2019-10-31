# Using Web proxy in Ubuntu

## Method 1.  Using Environment variable
### Setting it
#### Method 1.1

In the command line.

    $ export http_proxy=http://user:pass@my.proxy.server:8080

    $ export https_proxy=http://user:pass@my.proxy.server:8080

    note: if special character are in the password, must replace with ascii code. Eg @ is replaced by %40 .  e.g. p@ssword -> p%40ssw0rd


Ensure it is set by 

    $ env | grep proxy

Clear it by 
    $ unset http_proxy

NOTE : If you use *sudo*, you must use *-E* option, eg 'sudo -E apt-get update' to force sudo to preserve the einvroment

#### Method 1.2 (I haven't tried)
Or set in /etc/environment

    http_proxy="http://<username>:<password>@<hostname>:<port>/"
    https_proxy="http://<username>:<password>@<hostname>:<port>/"
    ftp_proxy="http://<username>:<password>@<hostname>:<port>/"
    no_proxy="<pattern>,<pattern>,...

### Using it

#### In Ubuntu apps

The above env variable works for apt-get, pip3 (I tested)

#### In Python programs

In the python program, the parameters can be picked up by

    import urllib.request

    proxiesDict = urllib.request.getproxies()


Example of code to make restapi call using proxyDict

    r = requests.get('http://example.org', proxies=urllib.request.getproxies())


----

## Method 2 - Directly code it inside the Python program (not preferred).

Since you need to set env variables for the Linux to work anyway.  Might as well use method one.  So this method here is more FYI, to understand the structure of the proxyDict.

    Code example

        http_proxy  = "http://10.10.1.10:3128"
        https_proxy = "https://10.10.1.11:1080"
        ftp_proxy   = "ftp://10.10.1.10:3128"

        proxyDict = { 
                    "http"  : http_proxy, 
                    "https" : https_proxy, 
                    "ftp"   : ftp_proxy
                    }

    Example of code to make restapi call using proxyDict

        r = requests.get('http://example.org', proxies=proxyDict)

        