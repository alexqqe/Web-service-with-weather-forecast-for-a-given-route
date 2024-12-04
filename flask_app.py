from main import main
from flask import Flask, request, render_template, jsonify, send_file


app = Flask(__name__)

received_data = {}

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/', methods=['GET', 'POST'])
def check_weather():
    if request.method == 'GET':
        return render_template('check_weather.html')
    elif request.method == 'POST':
        received_data['city1'] = request.form['City1']
        received_data['city2'] = request.form['City2']

        if main(received_data['city1']) + main(received_data['city2']) == 2:
            return render_template('good_weather.html')
        else:
            return render_template('bad_weather.html')





if __name__ == '__main__':
    app.run(debug=True)
