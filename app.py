from flask import Flask, render_template, url_for, request, jsonify
from werkzeug.utils import secure_filename
from program import *
from myproject import app, db
from myproject.models import NumberPlate
import sqlite3


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      file_name = 'uploads/'+str(secure_filename(f.filename))
      f.save(file_name)
      x = search_number_plate(file_name)
      print('file uploaded successfully')
      return render_template('button1.html', x = x)




@app.route('/register', methods=['GET', 'POST'])
def register_files():
    if request.method == 'POST':
        name = request.form.get('uname')
        number = request.form.get('no')
        print(name)
        print(number)
        record = NumberPlate(number, name)
        db.session.add(record)
        db.session.commit()
        return 'record added'
    return render_template('register.html')
    


@app.route('/viewnumbersreg', methods=['POST','GET'])
def viewsal():
    conn = sqlite3.connect('myproject/data.sqlite')
    cur = conn.cursor()
    cur.execute("select * from number_plate")
    rows = cur.fetchall()
    print(rows)
    conn.close()
    return str(rows)

if __name__ == "__main__":
    app.run(debug=True)