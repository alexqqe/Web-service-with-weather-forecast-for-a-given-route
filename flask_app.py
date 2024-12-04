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
        # записываем полученные данные в словарь
        received_data['city1'] = request.form['City1']
        received_data['city2'] = request.form['City2']

        # получаем значения из основной функции:
        c1 = main(received_data['city1'])
        c2 = main(received_data['city2'])
        if c1 not in [0, 1]:
            return render_template('error.html', error1=c1)
        elif c2 not in [0, 1]:
            return render_template('error.html', error1=c2)
        elif c1 + c2 == 2:
            return render_template('good_weather.html')
        else:
            return render_template('bad_weather.html')





if __name__ == '__main__':
    app.run(debug=True)
