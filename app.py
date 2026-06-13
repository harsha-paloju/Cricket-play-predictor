from flask import Flask,request,render_template

import requests

import joblib

model=joblib.load("model.pkl")

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/result",methods=["POST","GET"])
def result():
    city=request.form["city"]
    
    api_key="6d36292dd9728055fd624957b9c46c9c"

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response=requests.get(url)

    data=response.json()

    if data.get("cod")!=200:
        return render_template("result2.html")
    else:
        condition=data["weather"][0]["main"]
        pre_condition=condition
        wind=data["wind"]["speed"]
        humidity=data["main"]["humidity"]
        temp=data["main"]["temp"]
        
        if condition=="Rain" or condition=="Drizzle" or condition=="Thunderstorm":
            condition=[0,0,1]
        elif condition=="Clear":
            condition=[0,0,0]
        elif condition=="Mist" or condition=="Fog" or condition=="Haze" or (condition == "Clouds" and data["weather"][0]["description"] != "overcast clouds"):
            condition=[1,0,0]
        else:
            condition=[0,1,0]
        
        features=[temp,humidity,wind]+condition
        
        
        prediction=model.predict([features])
        
        if prediction[0]==0:
            res="You cant play cricket today because your weather doesnt suitable for playing cricket"
        else:
            res="You can play cricket"
        
        
        
        return render_template("result.html",answer=res,city=city,temp=temp,Humidtiy=humidity,wind=wind,condition=pre_condition)
    
    


if __name__ == "__main__":
    app.run(debug=True)



