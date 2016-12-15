#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Email Model

import time
import pprint

import config
from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)



class Email():



    def __init__(self, recipient, subject, body):

        self.user = config.user
        self.pwd = config.password

        self.recipient = recipient
        self.subject = subject
        self.body = body



    def print_dict(self):
        pp.pprint(self.__dict__)




