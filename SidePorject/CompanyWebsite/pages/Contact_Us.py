import streamlit as st
import pandas as pd
import sys
sys.path.append('/home/Portfolio_Webapp/')
from send_email import send_email

st.header("Contact Us!")
df = pd.read_csv('topics.csv')

with st.form(key='contact_form'):
    user_email = st.text_input(label="Your email address")
    
    select_box = st.selectbox(label='What topic do you want to discuss',
                              options=df.topic)
    raw_message = st.text_area(label='Your message')
    msg = f"""Subject: New message from Portfolio website\n\n
    From: {user_email}\n
    Topic: {select_box}\n
    {raw_message}"""
    submit_button = st.form_submit_button('Submit')
    
    if submit_button:
        send_email(msg)
        st.info(f"Thanks for your message! I will get back to you as soon as possible at {user_email}")
        
