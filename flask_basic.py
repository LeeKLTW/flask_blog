from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/n_echo/<int:n>')
def n_echo(n):
    li = ['hello']
    response = jsonify({'echo': li * n})
    return response


if __name__ == '__main__':
    app.run(debug=True)
