from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/messages/<int: id>')
def get_messages(id):
    received_request = request.get_json()

