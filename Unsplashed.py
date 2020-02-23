#download wallpapers/images from unsplashed site


import requests
from bs4 import BeautifulSoup
from urllib import request
import random
import time
import os
from pathlib import Path

input1 = input("Enter category name: ")

#default URL from unsplashed
url = 'https://unsplash.com/s/photos/' + str(input1)

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#taking all 'img' and then bifercating class with its given name
a = soup.find_all('img', attrs = {'class' : '_2zEKz'})

images = []
for i in a:
    images.append(i['src'])

#Create a new folder with name given by userinput    
Path("E:\\picturescrapper\\" + str(input1)).mkdir(parents=True, exist_ok=True)

for i in images:
    file_name = random.randrange(1,100)
    full_file_name = str('E:\\picturescrapper\\' + str(input1)) + str('\\') + str(file_name) + '.jpg' 
    request.urlretrieve(i,full_file_name)    

time.sleep(5)
#Image folder will open after 5 seconds, meanwhile all images will be downloaded in the path given above
os.startfile('E:\\picturescrapper')



