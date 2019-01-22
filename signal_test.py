from flask import Flask, jsonify, g, request_finished
from flask.signals import signals_available

if not signals_available:
    raise RuntimeError('pip install blinker')

app = Flask(__name__)

def finished(sender,response, **extra):
    print('Send a response')
    print(response)


request_finished(finished)


@app.route('/api')
def microservice():
    return jsonify({'key':'value'})


if __name__ == '__main__':
    app.run(debug=True)

