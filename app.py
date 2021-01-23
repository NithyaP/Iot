# app.py
from flask import Flask,render_template
from random import randint
import datetime
app = Flask(__name__)             

@app.route("/api/sensordata/temp")
def tempdata():
    returnData ={"name" : "temp " ,"value":" ","time":" "}
    sensorData = randint(30, 40)
    time = datetime.datetime.now()
    returnData["value"] = sensorData
    returnData["time"] = time
    return   (returnData)

@app.route("/api/sensordata/hum")
def humdata():
    
    returnData ={"name" : "hum " ,"value":" ","time":" "}
    sensorData = randint(10, 20)
    time = datetime.datetime.now()
    returnData["value"] = sensorData
    returnData["time"] = time
    return   (returnData)



@app.route("/api/sensordata/prec")
def precdata():
    returnData ={"name" : "prec " ,"value":" ","time":" "}
    sensorData = randint(0, 1)
    time = datetime.datetime.now()
    returnData["value"] = sensorData
    returnData["time"] = time
    return   (returnData)



@app.route("/")                   
def Home():
    sensor = {"temp" : 90,"hum" :65,"prec" : 1}
    return render_template('index.html',sensorvalues=sensor)
    
       
if __name__ == "__main__":
    app.run(debug=True)
