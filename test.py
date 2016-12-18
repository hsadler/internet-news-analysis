#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Testing



from models.email.email import Email

# Email('harrysadlermusic@gmail.com', 'my subject', 'hi there').send().print_dict()



from controllers.reports.reports import Reports

Reports.send_weekly_report()
