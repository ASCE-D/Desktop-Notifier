from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyme(title, msg):    #Function containing notifyme code

    notification.notify(
        title=title,
        app_icon='E:\\Python projects\\images.ico',
        app_name='Source : MyAnimeList News',
        message=msg,
        timeout=10,

    )


def info(url):    #Function to get data from the url
    r = requests.get(url)      #requesting data
    return r.text       #returning it on text format


my_html_data = info("https://myanimelist.net/news")    #saving the returned text from the info funtion

soup = BeautifulSoup(my_html_data, 'html.parser')    #creating soup variable for parsing data

div = soup.findAll("div", {"class": "text"})   #using findAll funtion of soup to find all the text elements on html

content = []  #creating and empty list to append the news
for i in div:
    content.append(i.get_text()) #to remove unnecesarry tags and appending it on content list



while True:
    for a in range(len(content)):
        notifyme('Konnichiwa Otaku News ', content[a][:253] + '...')   #using slicing because notify me can support max of 256 characters
        a+=1
        time.sleep(13) #using sleep function to delay
    time.sleep(60*60*60*24)





