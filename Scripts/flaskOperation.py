
import sqlite3
from flask import *
app = Flask(__name__,template_folder='templates')

@app.route('/', methods=["POST", "GET"])
def loging():
    if request.method == "POST":
        #Connect to db
        con = sqlite3.connect("unit3.db")
        cur = con.cursor()
        #HTML Form
        email = request.form['email']
        password = request.form['password']
        #Querry
        cur.execute("SELECT * FROM nurses WHERE  email='"+email+"' AND password= '"+password+"'")
        info = cur.fetchall()
        if len(info) == 0:
            print("Incorrect credentials entered.Please try again")

        else:
            return redirect(url_for('saveDetails'))
    return render_template('login.html')





@app.route('/duties')
def kazi():
    return render_template('duties.html')

@app.route('/add')
def creating():
    return render_template('add.html')

@app.route('/save')
def saveDetails():
    return render_template("success.html")








if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080',debug=True)   #https://replit.com/talk/ask/Flask-app-doesnt-load-in-the-browser-need-help/116192









