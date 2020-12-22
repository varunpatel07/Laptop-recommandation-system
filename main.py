import numpy as np
from flask import Flask, request, render_template

import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/suggest',methods=['POST'])
def suggest():
    '''
    For rendering results on HTML GUI
    
    '''
    Laptop =  request.form["model"]
    Recommendations = util.suggest(Laptop)
    #print(Recommendations)
    return render_template('index.html' ,result=enumerate(Recommendations))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
