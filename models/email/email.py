#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Email Model

import smtplib
import pprint

import config
from models.database.database import MySQL_DB

pp = pprint.PrettyPrinter(indent=4)



class Email():



    def __init__(self, recipient, subject, body):

        self.user = config.user
        self.password = config.password

        self.recipient = recipient
        self.subject = subject
        self.body = body



    # taken from the internets:
    # http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-
    # as-provider-using-python
    def send(self):

        gmail_user = self.user
        gmail_pwd = self.password
        FROM = self.user
        TO = self.recipient if type(self.recipient) is list else [self.recipient]
        SUBJECT = self.subject
        TEXT = self.body

        # Prepare message
        message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (FROM, ", ".join(TO), SUBJECT, TEXT)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
        except:
            print 'failed to send mail'

        return self



    def print_dict(self):
        pp.pprint(self.__dict__)




