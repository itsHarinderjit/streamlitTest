import os,sys

@st.experimental_singleton
def installff():
  os.system('sbase install chromedriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/chromedriver /home/appuser/venv/bin/chromedriver')

_ = installff()

import streamlit as st
from test import download_audio

st.title('test app')
singerName = st.text_input('Enter singer name')

download_audio(singerName)

st.header(singerName)