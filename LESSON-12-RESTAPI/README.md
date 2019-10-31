# Passing Data to and From a Web service

Target is to seperate the code to 2 
* A frontend for the UI
* A 'microservice' to do the interference

Steps
* Will explore different methods to pass data to web service
     * Method 1: Using URL endpoints
          * Develop web service to response

     * Method 2: Using RESTAPI GET querries
          * Read from a website (public weather data)
          * Develop web service to response
               * GET Querries
               * POST JSON

## Method 1 - Using URL to pass in the data

Creat a new directory, and new app.py. Put in following code and try out.


     import os
     from flask import Flask    

     app = Flask(__name__)

     @app.route('/')
     def index():
          return 'Index Page'    

     #adding variables
     @app.route('/querry/<username>')
     def show_user(username):
          #returns the username
          return 'Username: %s' % username

     @app.route('/querry/<int:post_id>')
     def show_post(post_id):
          #returns the post, the post_id should be an int
          post_id2 = post_id * 2
          return 'The double of {} is {}'.format(post_id, post_id2)

     if __name__ == "__main__":
          port = int( os.getenv("PORT",4001))
          app.run(host='0.0.0.0', port=port, debug=True)

Exercise

     * use Chrome to access different URL, and see how the app get the parameters, and response
     * try same with Insomnia GET method

This is one method of doing.

Let's try to use RESTFUL methods  (RESTAPI)

## Method 2 - RESTAPI 

### Intro Exercise

Explore a web site

     https://data.gov.sg/dataset/realtime-weather-readings

Use Insomia on your desktop to generate the querry.  Find out the temperature in Singapore on 2019-09-26  (26th Sep 2019)

Can you understand the response?

     HINT : Must enter request with a date querry

### Use Python to send the querry
  


    Try to write a simple restapi-get.py that reads the data. And just dump it out.  Note, it uses *requests* library.

Hint: Just google for "python restapi example"

Note : For those sites which uses proxy to access the web, google for examples that uses proxy.  If you have problem, read the <code>README-proxies.md</code> file here for help.

## Let's write a 'service', an app that responses to RESTAPI GET/PUT
   

     https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

Add new endpoints to your app.py
Remove other endpoints and use this enpoint

      @app.route('/api', methods = ['GET','POST'])
      def api():
        if request.method == 'GET':
            return "123"
        elif request.method == 'POST':
            return "456"

Use Insomnia to GET and POST.  See the response

### GET method - passing Query

Now, let's pass some paramters (query)

    Let's try to pass query  'image'

    @app.route('/api', methods = ['GET','POST'])
     def api():
     if request.method == 'GET':
          image = request.args.get('image',)
          image = int(image) * 2
          return jsonify({'prediction':image}) 
     else
          pass

### POST method - passing JSON data

Challenge

     Use Isomnia to do a POST with the following sample JSON

     Write a RESTAPI web service to return with the data you want

     eg, want a response of 123.  Which is the data of "sample_number"

     Hint.  Use following command

     image_obj = request.json.get('sample_number')

Sample JSON

     {
          "sample_text": "hello",
          "sample_number": 123,
          "sample_boo": false,
          "sample_array": [ 
                                   [ 10, 11, 12, 13, 14, 15],
                                   [ 20, 21, 22, 23, 24, 25],
                                   [ 30, 31, 32, 33, 34, 35] ],
          "sample_obj": 
               [{
                    "key1": "hello1",
                    "key2": "5678",
                    "key3": 6789
               },
               {
                    "key1": "world",
                    "key2": "peace",
                    "key3": 12345
               }]
          ,
          "sample_data": null
     }



-----

# Just some Info

thislist = ["apple", "banana", "cherry"]

have a string that format like json
json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

json.loads        string ->  dict

json.dumps     json -> string  (to list out the json)