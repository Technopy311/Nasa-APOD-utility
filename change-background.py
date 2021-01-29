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
	

	#Here you can set the api key, you can get it at https://api.nasa.gov/?ref=public-apis#signUp

	key_from_file = open((currentDirectory + "/Assets/API-KEY.conf"), "r")
	KEY = key_from_file.readline()
	KEY = str(KEY)


	api_url = ("https://api.nasa.gov/planetary/apod?api_key=" + KEY)
	api_url = str(api_url)

	background_dir = open((currentDirectory + "/Assets/path.conf"), 'r')
	background_dir = background_dir.readline()

	error = 0	

	if api_url == "https://api.nasa.gov/planetary/apod?api_key=DEMO-KEY":
		error += 1

	if background_dir == "BACKGROUND-PATH":
		error += 2


	if error == 3:



		exit()

	elif error == 2:



		exit()

	elif error == 1:



		exit()

	elif error == 0:

		request = requests.get(api_url)
		status = request.status_code
	
	
	DATA = request.text

	# checking connection
	if status == 200:
		text = "Succesfully reached api"

	
	else:
		text = "Make shure the api key is valid \n and check if you have network connection."

		jk()
		exit()
	
	# parsing the json and 
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

	file = open( str(currentDirectory) + "log.txt", "a")
	file.write("Succesfully downloaded today's APOD image, and changed the background")
	file.close()



if __name__ == '__main__':
	loadAll()
	downloadBackground()