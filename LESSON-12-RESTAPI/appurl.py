import os
from flask import Flask, request, jsonify    

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
#     return 'The double of  %i is %i' % (post_id, post_id2)

# A simple one to test GET and POST method
# @app.route('/api', methods = ['GET','POST'])
# def api():
#   if request.method == 'GET':
#       return "123"
#   elif request.method == 'POST':
#       return "456"

@app.route('/api', methods = ['GET','POST'])
def api():
  if request.method == 'GET':
    image = request.args.get('image',)
    image = int(image) * 2
    return jsonify({'prediction':image})
  elif request.method == 'POST':
#    image = request.json.get('sample_number',)
#
#    image_array = request.json.get('sample_array',)
#    image = image_array[2][3]
#
    image_obj = request.json.get('sample_obj')
    image_dic = image_obj[0]
    image = image_dic['key3']
    if request.json.get('sample_boo'):
      image = image * 2
    else:
      pass
    return jsonify({'prediction': image})

if __name__ == "__main__":
     port = int( os.getenv("PORT",4001))
     app.run(host='0.0.0.0', port=port, debug=True)