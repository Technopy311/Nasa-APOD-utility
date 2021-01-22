# importing packages
import requests
import json
from pynotifier import Notification
from os import system



def downloadBackground():
	#Getting the info from json

	#title
	title = JSON_DATA['title']
	print("The title is: "+str(title) +"\n")
	
	#high defition photo
	url = JSON_DATA['hdurl']
	print("The url is "+ str(url) +"\n")
	
	#Photo's date
	date = JSON_DATA['date']
	print("The date is: "+ str(date) +"\n")

	description = JSON_DATA['explanation']

	#donwloading the image
	print('Downloading the image.\n')
	print("Photo Description: \n" + str(description) + " \n")
	system('wget '+ str(url) + ' --quiet  -O \"APOD.jpg\" ')
	print('Image Downloaded')

	#setting the image as background

	print("Setting as a background.")
	system("mv /home/technopy/Documentos/programming/python/nasaAPOD/APOD.jpg /home/technopy/.local/share/backgrounds/default.jpg")
	print("succesfully changed background.")
	
	#Displaying a notification	
	Notification(
		title="Image succesfully changed to today's APOD ;D",
		description="The background image has been succesfully changed to today's APOD.",
		icon_path="/home/technopy/Documentos/programming/python/nasaAPOD/python-logo.png",
		duration=2,
		urgency=Notification.URGENCY_CRITICAL
	).send()

	system("echo 'Image downloaded succesfully' >> /home/technopy/Documentos/programming/python/nasaAPOD/log.txt")


def main():
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
		exit()
	
	# parsing the json and 
	global JSON_DATA 
	JSON_DATA = json.loads(DATA)


if __name__ == '__main__':
	main()

