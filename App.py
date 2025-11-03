from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html');

@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('home.html');

@app.route('/mytask', methods=['GET','POST'])
def mytask():
    return render_template('myTask.html');

@app.route('/papercheck', methods=['GET','POST'])
def papercheck():
    return render_template('paperChecking.html');
@app.route('/checkedpaper', methods=['GET','POST'])
def checkedpaper():
    return render_template('checkedPaper.html');

@app.route('/analysis', methods=['GET','POST'])
def analysis():
    return render_template('analysis.html');

@app.route('/resources', methods=['GET','POST'])
def resources():
    return render_template('resources.html');

app.run(debug=True)

