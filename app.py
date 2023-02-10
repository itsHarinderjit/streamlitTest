# import streamlit as st
# import os, sys
# from selenium import webdriver
# from pytube import YouTube
# from selenium.webdriver import FirefoxOptions

# @st.experimental_singleton
# def installff():
#   os.system('sbase install geckodriver')
#   os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

# _ = installff()

# def download_audio(singerName) :
#     options = FirefoxOptions()
#     options.add_argument("start-maximized")
#     options.add_argument("--headless")
#     url='https://www.youtube.com/results?search_query=' + singerName

    
#     browser = webdriver.Firefox(options=options)

#     browser.get(url)

#     listings=browser.find_elements('xpath','//a[@id="thumbnail"]')
#     links = []
#     for l in listings:
#         links.append(l.get_attribute("href"))
#     st.write('Links aquired')
#     st.write(len(links))
#     link = links[2]

#     yt = YouTube(link)
#     st.write('Object created')

#     yt.streams.get_audio_only().download()

#     st.write('Audio downloaded')

# st.title('test app')
# singerName = st.text_input('Enter singer name')

# if singerName != '' :
#     download_audio(singerName)

#     st.header(singerName)

import streamlit as st
import os, sys

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

_ = installff()
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)

browser.get('http://example.com')
st.write(browser.page_source)