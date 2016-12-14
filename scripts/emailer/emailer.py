
# taken from the internets:
# http://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-
# as-provider-using-python

import smtplib

def send_email(user, pwd, recipient, subject, body):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"



user = ''
pwd = ''
recipient = ''
subject = 'email TEST SUBJECT'
body = 'email TEST BODY'

send_email(user, pwd, recipient, subject, body)
