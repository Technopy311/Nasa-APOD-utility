# importing packages

import requests
import json
from pynotifier import Notification
import os
from time import sleep


PAUSE_TIME = (2)

def loadAll():
	global background_dir 
	global currentDirectory 

	currentDirectory = os.getcwd()

	conf = open((currentDirectory + "/Assets/path.conf"), 'w')
	conf.write(" ")
	conf.close()
	
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
	
	background_dir = open((currentDirectory + "/Assets/path.conf"), 'r')
	background_dir = background_dir.readline()


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



def DownloadLowRes():
	#This function only downloads the low resolution image

	#Get the url from the json
	low_res_url = JSON_DATA['url']

	#Download the image and save it
	os.system("wget " + str(low_res_url) + " -O Low-Resolution-Img.jpg") 
	
	sleep(PAUSE_TIME)

	print("\n")
	print("Low resolution image download succesfully")
	print("\n\n")



def DownloadHD():
	#This function only downloads the high resolution image

	#Get the url from the json
	high_res_url = JSON_DATA['hdurl']

	#Download the image and save it
	os.system("wget " + str(high_res_url) + " -O High-Resolution-Img.jpg") 
	
	sleep(PAUSE_TIME)

	print("\n")
	print("Highresolution image download succesfully")
	print("\n\n")



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
	global currentDirectory

	background_dir = open((currentDirectory + "/Assets/path.conf"), 'r')
	background_dir = background_dir.readline()


	#Getting the info from json

	getInfo(1)

	#Starting the download process of the image
	print('Downloading the image. \n\n')
	sleep(PAUSE_TIME)
	
	os.system('wget '+ str(IMGURL) + ' --quiet  -O \"APOD.jpg\" ')
	print('Image Downloaded')

	#setting the image as background

	print("Setting as a background.")
	
	os.system("mv " + (currentDirectory + "/APOD.jpg ") + background_dir)
	print("succesfully changed background.")

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


def setup1():
	
	currentDirectory = os.getcwd()
	currentDirectory = str(currentDirectory)
	save_file = (currentDirectory + "/Assets/path.conf")

	print("Be conscient that your current wallpaper will be replaced, ")
	print("So make a copy of it, if you wana save it.")
	print("let's continue: \n")
	
	print("Input here, the ABSOLUTE PATH of your actual desktop wallpaper \n"
	"you must include the name of the file, "
	"Example: /home/USERNAME/Desktop/wallpaper.jpg \n")

	path = input("Enter the path: ")
	print("make shure its the right path, else,\n just run or re run the option 1.")

	save = open(save_file, 'w' )
	save.write(path)
	save.close()
	
	print("the configuration is done, would you like now to change your background? (1)Y / (2)N")
	SecondOption = input(": ")
	SecondOption = int(SecondOption)

	if SecondOption == 1:
		downloadBackground()
	else:
		jk()
		exit()



def setup2():

	print("This option consists in download the image,\n"
	" and manually set it as background.")

	print("The helper has pre-programmed pauses, of maximum 30secs,"
	"so don't think that the script has been freezed or stoped.")

	print("Follow the steps, ill show you here")
	sleep(10)
	print("Ill download the image for you, wait a little and dont do nothing. \n")
	sleep(3)
	DownloadHD()
	print("\n Ok, the image has been downloaded and saved")
	print("In your current directory as High-Resolution-Img.jpg")
	sleep(4)
	print("you can move the file wherever you want, but copy the path to it")
	print("Example: /home/USERNAME/Desktop/anyname.jpg")
	sleep(PAUSE_TIME)
	print("yes, it must include the name of the file.")
	sleep(10)
	print("Once you made all that, just make it as your background wallpaper, \n"
	"in fact, is not neccesary to inmediatly make it as your wallpaper, "
	"and you can make it before the script ends, but you must do it \n"
	"Else, when you run the automatized script, it wont work 100%. \n\n")
	print("Here come the pause of 30 secs \n")
	sleep(30)
	print("If you did it, now the only missing thing to do, is to ")
	print("enter the path where the file is, that way")
	sleep(PAUSE_TIME)
	print("The next time you execute the script, you only have to choose the ")
	print("Option 1 \n")
	sleep(PAUSE_TIME)

	setup1()

def InitialSetup():
	

	print("Initializing... \n")
	

	print("here are two options of setup")
	print("(1) Replace your actual wallpaper file.\n"
		"(2) Download the image, and set it as wallapaper.")

	print("Disclaimer, This are only short descriptions, "
	"if you wish to stop the script, just type CTRL + C. \n")
	
	print("What do you choose?")

	option = input(": ")
	option = int(option)
	
	if option == 1:
		setup1()
	
	elif option == 2:
		setup2()

	else:
		print("That option doesn't exists or something else went wrong")



def main():	
	# loading all urls and api 
	
	loadAll()

	# options for the user
	
	print("What would you like to do? \n")
	print("(1) Change your current background.      (2) Get all info of today image. \n"
		"(3) Only Download low resolution image.  (4) Only Download high resolution image.\n"
		"(5) Initial Setup. ")
	
	option = input(": ")

	option = int(option)

	if option == 1:
		print("The option selected is: " +str(option) )
		downloadBackground()

	elif option == 2:
		print("The option selected is: " +str(option))
		getInfo(2)

	elif option == 3:
		print("The option selected is: " +str(option))
		DownloadLowRes()

	elif option == 4:
		print("The option selected is: " +str(option))
		DownloadHD()

	elif option == 5:
		print("The option selected is: " +str(option))
		InitialSetup()

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

