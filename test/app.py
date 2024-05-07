import os
from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier


pickle_in = open("maintenance.pickle", "rb")
modelm = pickle.load(pickle_in)

pickle_in = open("firemodel.pickle", "rb")
modelf = pickle.load(pickle_in)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('front.html')

@app.route('/firefront')
def front_fire():
    return render_template('fire.html')

@app.route('/maintenancefront')
def front_maintenace():
    return render_template('maintenance.html')

@app.route('/fire', methods=['POST','GET'])
def fire():
    data1 = request.form['Temperature']
    data2 = request.form['Humidity']
    data3 = request.form['TVOC']
    data4 = request.form['eCO2']
    data5 = request.form['RawH2']
    data6 = request.form['RawEthanol']
    data7 = request.form['Pressure']
    data8 = request.form['PM1']
    data9= request.form['PM2_5']
    data10= request.form['NC0_5']
    data11= request.form['NC1']
    data12= request.form['NC2_5']
    data13= request.form['CNT']
    input_list = [[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]]
    prediction = modelf.predict(input_list)
    if prediction[0] == 0:
        return render_template('fire.html', pred='NO FIRE')
    else:
        return render_template('fire.html', pred='FIRE!!')


    
@app.route('/maintenance', methods=['POST','GET'])
def predict():
    data1 = request.form['Air Temperature']
    data2 = request.form['Process Temperature']
    data3 = request.form['Rotational speed']
    data4 = request.form['Torque']
    data5 = request.form['Tool wear']
    data6 = request.form['Type']
    arr = np.array([[data1, data2, data3, data4, data5, data6]])
    prediction = modelm.predict(arr)
    if prediction[0] == 1:
        return render_template('maintenance.html', pred='failure')
    else:
        return render_template('maintenance.html', pred='no failure')

if __name__ == "__main__":
    app.run(debug=True)