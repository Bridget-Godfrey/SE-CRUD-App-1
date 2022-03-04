#req:
#python 3
#flask
#pip freeze for venv
#render_template

from flask import Flask, request, render_template
import sqlite3
from sqlite3 import Error
import sys

def create_connection(p):
    conn = None
    try:
        conn = sqlite3.connect(p)
        print("Connection successful")
    except Error as e:
        print(f"ERROR: '{e}'")

    return conn



testDB = create_connection("students.db")
try:
  testDB.execute("CREATE TABLE IF NOT EXISTS `students` ( `Name` TEXT, `Id` INTEGER, `Points` INTEGER, `studentKey` INTEGER PRIMARY KEY AUTOINCREMENT )")
  testDB.commit()
  testDB.close()
except:
  pass

app = Flask(__name__)





@app.route("/ping")
def ping():
    return "pong"


@app.route("/addEntry", methods=['GET', 'POST'])
def addEntry():
    if request.method == 'POST':
        name = request.form.get('name')
        if (name == None):
            name = "NO NAME"
        
        studentID = request.form.get('sid')
        if (studentID == None):
            studentID = "0000"
        
        grade = request.form.get('grade')
        if (grade == None):
            grade = "0"
        
        
        try:
          testDB = create_connection("students.db")  
          testDB.execute("INSERT INTO `students` (`Name`, `Id`, `Points`) VALUES ('" +  str(name) + "', "+  str(studentID)+ ", " + str(grade) + ")")
          testDB.commit()
          testDB.close()
          return render_template('update_good.html')
        except Error as e:
          return render_template('update_bad.html', debug_stuff = "Database INSERT operation failed")
    else:
        css_list = []
        pg_title = "New Student"
        js_list = []
        content_div_class = "newForm"
        return render_template('new_form.html', page_title = pg_title, css_sources = css_list, js_sources = js_list, content_name = content_div_class)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    #UPDATES STUDENTS
    if request.method == 'POST':
        testDB = None
        name = None
        studentID = None
        grade = None
        studentKey = None
        try:
            testDB = create_connection("students.db") 
            name = request.form['name']
            studentID = request.form['sid']
            grade = request.form['grade']
            studentKey = request.form['studentKey']
        except Error as e:
            return render_template('update_bad.html', debug_stuff = "INVALID PARAMETER")
        
        sqlCmd = "UPDATE `students` SET `Name` = '" + str(name) + "',  `Id` = " + str(studentID) + ",  `Points` = " + str(grade) + " WHERE `studentKey` =" + str(studentKey)
        try:
            testDB = create_connection("students.db") 
            name = request.form['name']
            studentID = request.form['sid']
            grade = request.form['grade']
            studentKey = request.form['studentKey']
            testDB.execute(sqlCmd)
            testDB.commit()
            testDB.close()
            return render_template('update_good.html')
        except Error as e:
            return render_template('update_bad.html', debug_stuff = "" + str(e))
    else: #SHOW STUDENT EDIT FORM 
        studentKey = request.args.get('studentKey')
        testDB = create_connection("students.db")
        csr = testDB.cursor()
        csr.execute("SELECT * FROM `students` WHERE `studentKey` =" + str(studentKey))
        currRow = csr.fetchall()
        name = ""
        studentID = ""
        grade = ""
        for row in currRow:
             name = row[0]
             studentID = row[1]
             grade = row[2]
        

    css_list = []
    pg_title = "Edit Student"
    js_list = []
    content_div_class = "editForm"
    return render_template('edit_form.html', page_title = pg_title, css_sources = css_list, js_sources = js_list, content_name = content_div_class, student_name = name , student_id = studentID , student_grade = grade , student_key = studentKey )

@app.route("/remove", methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        try:
            testDB = create_connection("students.db") 
            studentKey = request.form['studentKey']
            sqlCmd = "DELETE FROM `students` WHERE `studentKey` =" + str(studentKey)
            testDB.execute(sqlCmd)
            testDB.commit()
            testDB.close()
            return render_template("update_good.html")
        except Error as e:
            return render_template('update_bad.html', debug_stuff = "" + str(e))
    else:
        return render_template("update_bad.html", debug_stuff = "Unable to perform this action from a GET request!!")



@app.route("/getTable")
def displayDBTable():
    testDB = create_connection("students.db")
    csr = testDB.cursor()
    csr.execute("SELECT * FROM `students`")
    currRow = csr.fetchall()
    tableData = []
    rowID = 1
    for row in currRow:
      tableData.append([str(row[0]),str(row[1]), str(row[2]), str(row[3]), str(rowID)])
      rowID += 1

    
    testDB.close()
    return render_template("tableTemplate.html", table_rows = tableData)





@app.route("/")
@app.route("/displayDB")
def displayDB():
    output =  "<head><link rel='stylesheet' href='/static/viewPage.css'><script src='https://code.jquery.com/jquery-3.6.0.min.js' integrity='sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=' crossorigin='anonymous'></script></head><body><div style = 'background-color:black'>"

    
    output += "</div><br><div id = 'tableHere'></div><br><br><br><br><br><a href='/addEntry' class='newStudent'>New Student</a>"
    
    



    output += "<script src = '/static/viewPage.js'></script>"

    output += "</body>"
    return output


