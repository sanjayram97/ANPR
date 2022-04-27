from flask import Flask, render_template, url_for, request, jsonify
from werkzeug.utils import secure_filename
from program import *
from myproject import app, db
from myproject.models import NumberPlate
import sqlite3
import os
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      file_name = 'uploads/'+str(secure_filename(f.filename))
      f.save(file_name)
      print('file saved', os.path.join(basedir, 'uploads', str(secure_filename(f.filename))))
      file_name = os.path.join(basedir, 'uploads', str(secure_filename(f.filename)))
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
        return render_template('recadded.html', value='added')
    return render_template('register.html')
    


@app.route('/viewnumbersreg', methods=['POST','GET'])
def viewsal():
    if request.method == 'GET':
        strn=""
        conn = sqlite3.connect('myproject/data.sqlite')
        #cur = conn.cursor()
        #cur.execute("select * from number_plate")
        #conn.commit()
        #rows = cur.fetchall()
        conn.row_factory = sqlite3.Row  
        cur = conn.cursor()  
        cur.execute("select * from number_plate")  
        rows = cur.fetchall()  
        lst=[]
        for records in rows:
            strn="Name: "+records[1]+" -> Number: "+records[0]
            lst.append(strn)
            strn=""
        lst = '\n'.join(lst)
        print(lst)
        conn.close()
        return render_template("registered.html",rows = rows)   

        
    


#added portion
@app.route('/deleterow', methods=['POST','GET'])
def delrow():
    if request.method == 'POST':
        name = request.form.get('uname')
        number = request.form.get('no')
        print(name)
        print(number)
        conn = sqlite3.connect('myproject/data.sqlite')
        cur = conn.cursor()
        
        cur.execute("""DELETE from number_plate where reg_name = ?""", (name,))
        conn.commit()
        records = cur.fetchall()
        db.session.commit()
        conn.close()
        return render_template('recadded.html', value='deleted')
    return render_template('delete.html')
    


if __name__ == "__main__":
    app.run(debug=True)