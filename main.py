import streamlit as kp
import pandas
kp.set_page_config(layout='wide')
kp.header('THE BEST COMPANY')
kp.write("""This company has been best in the industry for more than 10 years.It is currently the top logistics company in India and US
            Serving our happy customers for more than years,we think it is time for change in our approach.We are putting together the 
            best team for some new and interesting upcoming projects.Hope to get your support for our growth as you have provided over
            the years.""")
kp.subheader('Our Team')

col1,col2,col3=kp.columns(3)
df=pandas.read_csv('data.csv')
with col1:
    for index,row in df[:4].iterrows():
        kp.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        kp.write(row['role'])
        kp.image('images/'+row['image'])

with col2:
    for index,row in df[4:8].iterrows():
        kp.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        kp.write(row['role'])
        kp.image('images/'+row['image'])
with col3:
    for index,row in df[8:13].iterrows():
        kp.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        kp.write(row['role'])
        kp.image('images/'+row['image'])
