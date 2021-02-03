from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
regressor = pickle.load(open('icu1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Li= int(request.form['Licensed Bed Day'])
        Dis=float(request.form['Discharges'])
        CD=int(request.form['Census Day'])
        IHT=int(request.form['Intra Hospital Transfer from Critical Care'])


        prediction=regressor.predict([[Li,Dis,CD,IHT]])
        output=round(prediction[0],2)
        if output==0:
            return render_template('index.html',prediction_texts="Sorry you have no Beds Available.")
        else:
            return render_template('index.html',prediction_text="You have {} Beds Available.".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)