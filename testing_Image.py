# Romain

'''
1- get the browser to open map 
	1.1 online 
	or 
	1.2 from local machine Flask app
2- get a screenshot of the map
3- email this to email address
'''

# Imports
import time
import datetime
import os
import shutil
from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib

# Variables
URL = "https://dublin-town-south-pokemongo.herokuapp.com/"
email = "my.name@address.com"
password = "your_password"
d1 = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")



def open_website(url):
	# use selenium for Chrome
	browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
	# maximize browser window
	browser.maximize_window()
	browser.get(url)

	# wait for map to load
	time.sleep(10)
	
	# generate printscreen
	img = ImageGrab.grab()
	# save as: "date""format"
	name = str(d1)+".png"
	
	img.save(name)	
	
	''' Can be improved by saving directly to the folder "\\photos" '''
	for file in os.listdir("C:\\Users\\Romain\\Desktop\\PokemonGoUpdates"):
		if file.endswith(".png"):
			src = "C:\\Users\\Romain\\Desktop\\PokemonGoUpdates\\" + name
			dest = "C:\\Users\\Romain\\Desktop\\PokemonGoUpdates\\photos\\" + name
			shutil.move(src, dest)	

		
	
def download_image():
	''' function to download an image from url '''
	
def move_image_to_folder():
	''' move png file to 'photos' folder'''

def send_image_to_email():
	''' use smtplib from gmail to gmail '''  

	to = 'abc.def@gmail.com'
	gmail_user = 'abc.def@gmail.com'
	gmail_pwd = ''
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
	print (header)
	msg = header + '\n this is test msg from mkyong.com \n\n'
	smtpserver.sendmail(gmail_user, to, msg)
	print ('done!')
	smtpserver.close()

#open_website(URL)	
#download_image(URL)
send_image_to_email()