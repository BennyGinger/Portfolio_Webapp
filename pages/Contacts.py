import streamlit as st
from send_email import send_email
from email.mime.text import MIMEText

st.header("Contact Me")

with st.form(key='contact_form'):
    user_email = st.text_input(label="Your email address")
    raw_message = st.text_area(label='Your message')
    msg = f"""Subject: New message from Portfolio website\n\n
    From: {user_email}\n
    {raw_message}"""
    submit_button = st.form_submit_button('Submit')
    
    if submit_button:
        send_email(msg)
        st.info(f"Thanks for your message! I will get back to you as soon as possible at {user_email}")
        
