# encoding: utf-8
from flask import Flask
from flask_restful import abort
from datetime import datetime
from pytz import utc

from models import MessageModel
import status


class MessageManager():
    last_id = 0
    def __init__(self):
        self.messages = {}


if __name__ == '__main__':
    pass
