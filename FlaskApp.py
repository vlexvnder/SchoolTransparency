
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key = b'_5#y2gyhsghyttryrthgfjkjutrtqtregdfgdL"F4Q8z\n\asdasdasdas]/'

@app.route('/',methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')
@app.route('/go',methods=['GET', 'POST'])
def go():
    return render_template('go.html')
@app.route('/causes',methods=['GET', 'POST'])
def causes():
    return render_template('causes.html')



