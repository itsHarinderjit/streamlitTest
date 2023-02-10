# # import streamlit as st
# # import os, sys
# # from selenium import webdriver
# # from pytube import YouTube
# # from selenium.webdriver import FirefoxOptions

# # @st.experimental_singleton
# # def installff():
# #   os.system('sbase install geckodriver')
# #   os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

# # _ = installff()

# # def download_audio(singerName) :
# #     options = FirefoxOptions()
# #     options.add_argument("start-maximized")
# #     options.add_argument("--headless")
# #     url='https://www.youtube.com/results?search_query=' + singerName

    
# #     browser = webdriver.Firefox(options=options)

# #     browser.get(url)

# #     listings=browser.find_elements('xpath','//a[@id="thumbnail"]')
# #     links = []
# #     for l in listings:
# #         links.append(l.get_attribute("href"))
# #     st.write('Links aquired')
# #     st.write(len(links))
# #     link = links[2]

# #     yt = YouTube(link)
# #     st.write('Object created')

# #     yt.streams.get_audio_only().download()

# #     st.write('Audio downloaded')

# # st.title('test app')
# # singerName = st.text_input('Enter singer name')

# # if singerName != '' :
# #     download_audio(singerName)

# #     st.header(singerName)

# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.firefox import GeckoDriverManager
# import streamlit as st
# import os

# @st.experimental_singleton
# def installff():
#   os.system('sbase install geckodriver')
#   os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

# _ = installff()

# URL = 'http://example.com'
# TIMEOUT = 20

# st.title("Test Selenium")

# firefoxOptions = Options()
# firefoxOptions.add_argument("--headless")
# service = Service(GeckoDriverManager().install())
# # driver = webdriver.Firefox(
# #     options=firefoxOptions,
# #     service=service,
# # )
# driver = webdriver.Firefox(executable_path=r'/home/appuser/.wdm/drivers/geckodriver/linux64/0.32/geckodriver.exe',options=firefoxOptions)
# driver.get(URL)

# st.write(driver.page_source)

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