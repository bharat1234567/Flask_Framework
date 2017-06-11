from flask import Flask, render_template
app = Flask(__name__)

@app.route('/results')
def results():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('results.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)

# in the html file results:
# As you are in python3 , use dict.items() instead of dict.iteritems()
#iteritems() was removed in python3, so you can't use this method anymore.
#In Built-in Changes part, it is stated that
#Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
#Instead: use dict.items(), dict.keys(), and dict.values() respectively.
