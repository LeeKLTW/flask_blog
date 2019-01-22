from flask import Flask, jsonify, request, g
from datetime import datetime


app = Flask(__name__)


@app.before_request
def authenticate():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'


@app.route('/api',methods=['GET'])
def microservice():
    print(request)
    print(request.environ)
    now = datetime.now()
    now = now.strftime(('%Y-%m-%d-%H-%m'))
    response = jsonify({'user':g.user,'Time now':now})
    print(response)
    print(response.data)
    return response


#string, int,
@app.route('/api/person/<string:person_name>')
def say_hello(person_name):
    response = jsonify({'hello':person_name})
    return response


if __name__ == '__main__':
    app.run(debug=True)
