from flask import Flask,render_template,jsonify,request
import requests
app=Flask(__name__)

@app.route('/home')
def homepage():
    return render_template("index.html")

@app.route("/weather_app",methods=["post","get"])
def get_weather_app():
    url="https://api.openweathermap.org/data/2.5/weather"
    param={
        'q':request.form.get('city'),
        'appid':request.form.get('apiKey'),
        'units':request.form.get('units')
    }
    response=requests.get(url,params=param)
    data=response.json()
    city=data['name']
    return f"data:{data},city:{city}"
    
if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5002)