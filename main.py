import streamlit as st

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
    new challenges and opportunities to learn new things. Feel free to contact me if you have any questions or
    if you want to collaborate on a project."""
    st.info(content)