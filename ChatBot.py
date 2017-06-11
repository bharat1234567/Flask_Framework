from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "hii what are you doing"

@app.route('/wssup')
def fuck_you():
    return "wssup dude.."

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask_Framework_python3.6'

@app.route('/python/') #if i put this trailing '/', both /python and /python/ will call the same fuction hello_python
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run(debug = True)

