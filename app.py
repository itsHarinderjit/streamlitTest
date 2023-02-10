import streamlit as st
# from test import download_audio

st.title('test app')
singerName = st.text_input('Enter singer name')

# download_audio(singerName)

st.header(singerName)