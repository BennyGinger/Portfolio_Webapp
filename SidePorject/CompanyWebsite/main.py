import streamlit as st
import pandas as pd
from os.path import join

st.set_page_config(layout="wide")

st.title("The Best Company")
content = """Welcome to the best company website. We are a team of highly skilled professionals 
who are passionate about using data to solve complex problems. We are always looking for new challenges 
and opportunities to learn new things. Feel free to contact us if you have any questions or if you want 
to collaborate on a project."""
st.write(content)

st.header("Our Team")
col1, col2, col3 = st.columns(3)

df = pd.read_csv('data.csv')

with col1:
    for _, row in df[0::3].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(join("images", row['image']))

with col2:
    for _, row in df[1::3].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(join("images", row['image']))

with col3:
    for _, row in df[2::3].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}".title())
        st.write(row['role'])
        st.image(join("images", row['image']))
