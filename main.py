import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/BenPortrait.png", width=400)
    
with col2:
    st.title("Benoit Roux")
    content = """Hi, I'm Benoit Roux, I'm a research scientist at the University of Semmelweis.
    I'm interested in the molecular mechanisms of wound detection. I'm also a self-taught data scientist and
    software developer. I'm passionate about using data to solve complex problems. I'm currently working on
    image analysis software to automate the cells detection process and tracking over time. I'm also working
    on a high throughput screening software to identify new generation of biosensors. I'm always looking for
    new challenges and opportunities to learn new things. """
    st.info(content)

content2 = """Feel free to contact me if you have any questions or
    if you want to collaborate on a project."""
st.write(content2)

df = pd.read_csv('data.csv',sep=';')
col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

with col3:
    for idx, row in df[0::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"[Source code]({row['url']})")
        
with col4:
    for idx, row in df[1::2].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f"[Source code]({row['url']})")