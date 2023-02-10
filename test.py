from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pytube import YouTube

def download_audio(singerName) :
    options=Options()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
#path to chrome driver
    driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
    url='https://www.youtube.com/results?search_query=' + singerName
    driver.get(url)
    listings=driver.find_elements('xpath','//a[@id="thumbnail"]')
    links = []
    for l in listings:
    #  print(l.get_attribute("href"))
        links.append(l.get_attribute("href"))
# print(links)
    print('Links aquired')
    print(len(links))
    link = links[2]

# try:
    yt = YouTube(link)
    print('Object created')
# except :
#     print('connection error')

# myfile = yt.filter('mp4')

# yt.streams.get_lowest_resolution().download()

    yt.streams.get_audio_only().download()

    print('Audio downloaded')

# d_video = yt.get(myfile[-1].extension,myfile[-1].resolution) 
# try: 
#         # downloading the video 
#     d_video.download('D:\\college\\"Data Science"\\PAS\\Assignment2\\')
# except: 
#     print("Some Error!")



# print(listings.text)

# file = open('file.txt','w')

# file.write(listings.text)
