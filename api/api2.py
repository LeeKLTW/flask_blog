from flask import Flask, request, jsonify
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from datetime import datetime
from ..module import debug
debug = debug

# from models import MessageModel
# print(MessageModel)
# app = Flask(__name__)
#
#
# @app.route('/api/messages/<int: id>')
# def get_messages(id):
#     received_request = request.get_json()

