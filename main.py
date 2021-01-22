# importing packages

import requests
import json
from pynotifier import Notification
import os
from time import sleep


PAUSE_TIME = (2)

def loadAll():
	print("INITIALIZING")
	print("Loading the api data")
	URL = 'https://api.nasa.gov/planetary/apod?api_key=F6wkuYMeExyyZW9516419T3pGXzHcA5mkEwkNTF8'

	if URL == 'https://api.nasa.gov/planetary/apod?api_key=DEMO-KEY':
		print("Remember to put the nasa api key.")
		exit()
	else:
		print("The url is fine")

	request = requests.get(URL)
	status = request.status_code
	DATA = request.text

	# checking connection
	if status == 200:
		text = "Succesfully reached data"
		print("Status: " + str(status) +" "+ text + "\n")
	else:
		text = "Something else went wrong"
		print("Status: " + str(status) +" "+ text + "\n")
		jk()
		exit()
	
	# parsing the json and 
	global JSON_DATA 
	JSON_DATA = json.loads(DATA)



def getInfo(selection):
	
	if True:
		#title
		title = JSON_DATA['title']
		print("The title of this image is: "+str(title) +"\n")

		sleep(PAUSE_TIME)

		#Photo's date
		date = JSON_DATA['date']
		print("The date of this photo is: "+ str(date) +"\n\n")

		sleep(PAUSE_TIME)

		#high defition url photo
		global IMGURL
		IMGURL = JSON_DATA['hdurl']
		print("The high definition image's url is "+ str(IMGURL) +"\n")

		sleep(PAUSE_TIME)

		if selection == 2:
			
			media_type = JSON_DATA['media_type']
			print("The tipe of this media is: " + str(media_type) + " \n")
			sleep(PAUSE_TIME)

			service_version = JSON_DATA['service_version']
			print("The version of the service(NASA APOD API) is: " + str(service_version) + " \n")
			sleep(PAUSE_TIME)

			low_res_url = JSON_DATA['url']
			print("The low definition media url is: " + str(low_res_url) + " \n")
			sleep(PAUSE_TIME)


#TAKE SERIOSLY CARE HERE
#THIS IS THE MOST IMPORTANT DEF IN ALL APP

def jk():

	print("3")
	sleep(1)
	print("2")
	sleep(1)
	print("1")
	sleep(1)
	print("0")
	print("KABOOM")


#Of course not ;D


def downloadBackground():
	#Getting the info from json

	getInfo(1)

	#Starting the download process of the image
	print('Downloading the image. \n\n')
	sleep(PAUSE_TIME)
	
	os.system('wget '+ str(IMGURL) + ' --quiet  -O \"APOD.jpg\" ')
	print('Image Downloaded')

	#setting the image as background

	print("Setting as a background.")
	os.system("mv /home/technopy/Documentos/programming/python/nasaAPOD/APOD.jpg /home/technopy/.local/share/backgrounds/default.jpg")
	print("succesfully changed background.")
	
	currentDirectory = os.getcwd()

	#Displaying a notification	
	Notification(
		title="Image succesfully changed to today's APOD ;D",
		description="The background image has been succesfully changed to today's APOD.",
		icon_path=os.path.join(currentDirectory, "Assets/python-logo.png"),
		duration=2,
		urgency=Notification.URGENCY_NORMAL,

	).send()

	file = open( str(currentDirectory) + "log.txt", "a")
	file.write("Succesfully downloaded today's APOD image, and changed the background")
	file.close()


def main():	
	# loading all urls and api 
	
	loadAll()

	# options for the user
	
	print("What would you like to do? \n")
	print("(1) Change your current background,    (2) Get all info of today image,\n"
			"(3)Only Download low resolution image,    (4)Only Download high resolution image\n")
	

	option = input(": ")

	option = int(option)

	if option == 1:
		print("Option selected is: " +str(option) )
		downloadBackground()

	elif option == 2:
		print("Option selected is: " +str(option))
		getInfo(2)

	elif option == 3:
		print("Option selected is: " +str(option))

	elif option == 4:
		print("Option selected is: " +str(option))

	else:
		print("That option doesn't exists or something else went wrong")
		jk()
		exit()



if __name__ == '__main__':
	try:
		main()
		print("I hope c'ya soon :P")
		
	except KeyboardInterrupt:
		print("Bye ;D")
		exit()

