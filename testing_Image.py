# Romain

'''
1- get the browser to open map 
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

		
	
        # use selenium for Chrome
        browser = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
        # maximize browser windos
        browser.maximize_window()
        browser.get(url)

        # --- Michael ---
        # Not sure if sleep needed. Eventually wait for map to load:
        #time.sleep(3)

        # generate printscreen
        img = ImageGrab.grab()

        # save as: "date""format"
        #name = str(d1)+".png"

        # --- Michael ---
        # Create "photos" directory.
        # Save file directly to this directory.
        # If the file already exists, append "(1)", "(2)", "(3)" etc... as appropriate.

        # Suffix will be appended to file. If file does not already exist, suffix is blank.
        suffix = ""

        # Create "photos" directory if it doesn't exist
        # Using os.path.join() allows us to create a directory regardless of Unix/Windows, as they use different directory separators (Unix: "/", Windows: "\")
        # os.getcwd() gives us the current working directory (i.e. where we are running our app from --> PokemonGoUpdates)
        if not os.path.isdir(os.path.join(os.getcwd(), "photos")):
                os.mkdir(os.path.join(os.getcwd(), "photos"))

        target_dir = os.path.join(os.getcwd(), "photos")

        # The file that we want to save to
        target_file = os.path.join(target_dir, str(d1)+suffix+".png")

        # Edit the "suffix" variable, and the "target_file" until the filename is unique.
        while os.path.isfile(target_file):
                suffix = str(int(suffix or "0")+1)
                target_file = os.path.join(target_dir, str(d1)+"("+suffix+").png")

        # Save directly to photos directory
        img.save(target_file)	
	

def send_image_to_email():
	''' use smtplib from gmail to gmail '''  

	to = 'abc@gmail.com'
	gmail_user = 'abc@gmail.com'
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

open_website(URL)	
download_image(URL)

send_image_to_email()

