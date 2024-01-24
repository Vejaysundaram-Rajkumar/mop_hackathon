from flask import Flask, render_template, request
import weather
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Connect with the database to get the slab rates for respective state
def connect_db():
    connection = sqlite3.connect('test.db')
    return connection



@app.template_filter('zip')
def _zip(a, b):
    return zip(a, b)

@app.route('/analytics', methods=['POST'])
def analytics():
    no_of_units =request.form['amount'] 
    no_of_units=int(no_of_units)
    sel_state = request.form['state']
    print(no_of_units)
    print(sel_state)
    con = connect_db()
    cursor = con.cursor()

    # Fetch slab data for the selected state
    cursor.execute("""
        SELECT Low, High, Rate
        FROM data
        WHERE State = ?
    """, (sel_state,))
    
    slab_data = cursor.fetchall()
    # Perform the calculation in Python
    total_cost = 0
    each_unit=[]
    each_amt=[]
    for low, high, rate in slab_data:
        if no_of_units >= low and no_of_units <= high:
            slab_units = no_of_units-low + 1
            amt=slab_units * rate
            total_cost += amt
            each_unit.append(slab_units)
            each_amt.append(amt)
        elif no_of_units >= low and no_of_units > high:
            slab_units = high-low + 1
            amt=slab_units * rate
            total_cost += amt
            each_unit.append(slab_units)
            each_amt.append(amt)


    return render_template('feature2.html',state=sel_state,no=no_of_units, cost=total_cost,each_amt=each_amt,each_unit=each_unit)

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
    elec=str(estimated_electricity[3]) + " kWh"

    return render_template('feature1.html', weather_data=elec,area=area_region,solar_energy=estimated_electricity[0],wind_energy=estimated_electricity[1],total_energy=estimated_electricity[2])

if __name__ == '__main__':
    app.run(debug=True)