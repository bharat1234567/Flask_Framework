from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)


@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/')
def index():
    return redirect(url_for('upload_file'))

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)
