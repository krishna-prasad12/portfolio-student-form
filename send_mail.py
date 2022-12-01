import os
import smtplib,ssl

def mail_send(message):
    host='smtp.gmail.com'
    port=465

    username="bloodshreder1@gmail.com"
    password="xwwxetivpwxxnfsm"

    receiver="bloodshreder1@gmail.com"
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
