from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__,template_folder='templates')

@app.route('/')
def loging():
    return render_template('login.html')



@app.route('/add')
def creating():
    return render_template('add.html')



if __name__=='__main__':
    app.run(host='0.0.0.0', port='8080',debug=True)   #https://replit.com/talk/ask/Flask-app-doesnt-load-in-the-browser-need-help/116192









