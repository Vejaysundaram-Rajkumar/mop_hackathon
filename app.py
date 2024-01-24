from flask import Flask, render_template, request
import weather
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feature1')
def feature1():
    return render_template('feature1.html')

@app.route('/feature2')
def feature2():
    return render_template('feature2.html')


@app.route('/process', methods=['POST'])
def process():
    area_region = request.form['area_region']
    weather_data=weather.get_weather_data(area_region)
    estimated_electricity=weather.print_weather_info(weather_data)
    elec=str(estimated_electricity) + " kWh"
    return render_template('feature1.html', weather_data=elec)

if __name__ == '__main__':
    app.run(debug=True)