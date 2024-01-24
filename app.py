from flask import Flask, render_template, request
import weather
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('feature2.html')



if __name__ == '__main__':
    app.run(debug=True)