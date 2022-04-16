

from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
from program import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      file_name = 'uploads/'+str(secure_filename(f.filename))
      f.save(file_name)
      search_number_plate(file_name)
      return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)