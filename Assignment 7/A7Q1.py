from flask import Flask
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.txt"

@app.route('/')
def home():
    return "<h1>Flask Server is Running ✅</h1>"

@app.route('/data/<int:id>/<float:temp>/<float:humidity>', methods=['GET', 'POST'])
def receive_data(id, temp, humidity):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a") as f:
        f.write(f"{time} - ID: {id}, Temperature: {temp} °C, Humidity: {humidity}%\n")
    return f"Data received for ID: {id}"

@app.route('/get_data')
def get_data():
    try:
        with open(DATA_FILE, "r") as f:
            return f"<pre>{f.read()}</pre>"
    except:
        return "No data available"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)