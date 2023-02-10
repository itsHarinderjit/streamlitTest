import os,sys
import streamlit as st

@st.experimental_singleton
def installff():
  os.system('sbase install chromedriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/chromedriver /home/appuser/venv/bin/chromedriver')

_ = installff()

from test import download_audio

st.title('test app')
singerName = st.text_input('Enter singer name')

download_audio(singerName)

st.header(singerName)