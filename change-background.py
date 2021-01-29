import os
import requests
import json



#Downloading, Changing and setting up the new background.

def current():
	currentDirectory = os.getcwd()
	currentDirectory = str(currentDirectory)
	
	return currentDirectory



def loadAll():

	global background_dir
	currentDirectory = current()

	key_from_file = open((currentDirectory + "/Assets/API-KEY.conf"), "r" )
	KEY = key_from_file.readline()
	KEY = str(KEY)


	api_url = ("https://api.nasa.gov/planetary/apod?api_key=" + KEY)
	api_url = str(api_url)

	background_dir = open((currentDirectory + "/Assets/path.conf"), 'r')
	background_dir = background_dir.readline()

	error = 0	

	if api_url == "https://api.nasa.gov/planetary/apod?api_key=DEMO-KEY":
		error += 1

	request = requests.get(api_url )
		
	DATA = request.text

	#parsing the json and 

	global JSON_DATA 
	JSON_DATA = json.loads(DATA)


def downloadBackground():
	
	currentDirectory = current()

	background_dir = open((currentDirectory + "/Assets/path.conf"), 'r')
	background_dir = background_dir.readline()

	
	HDURL = JSON_DATA['hdurl']

	os.system('wget '+ str(HDURL) + ' -O \"APOD.jpg\" ')

	#setting the image as background
    
	os.system("mv " + (currentDirectory + "/APOD.jpg ") + background_dir)
	

	#Making log

	file = open((currentDirectory + "log.txt"), "w")
	file.write("Succesfully downloaded today's APOD image, and changed the background\n")
	file.close()



loadAll()
downloadBackground()