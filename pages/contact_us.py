import streamlit as kp
import pandas
from send_mail import mail_send

df=pandas.read_csv('topics.csv')
kp.header('Contact Us')
with kp.form(key='email_form'):
    username1=kp.text_input('Email Address')
    option=kp.selectbox('issue you want to inquire',df["topic"])
    kp.write('Your message')
    message=kp.text_area('Text here')
    message1 =f"""
              email from :{username1}
              Topic:{option}
              {message}
              """
    button=kp.form_submit_button('Send mail')
    if button:
        mail_send(message1)
        kp.info('Mail sent')