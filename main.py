#importing packages
from colorama import Fore, Style
import requests
import json
import os
from time import sleep
import ctypes


'''
Copyright, this project is owned by @Technopy311, it can 
be modified, but always giving credit to it's owner (me)
and citing the github profile.
[GitHub Profile: (https://github.com/Technopy311)]
'''


PAUSE_TIME = (2)


def download_image(url, write_path):
	print("Downloading")
	
	response = requests.get(url) 

	if response.status_code == 200:
		print('Image Downloaded')
	else:
		print("Something else happened")
		print("HTTP error: " + response.status_code)
		exit()

	#setting the image as background

	print("Saving Image")
	
	#opening the file, writing and closing image
	wallpaper = open(write_path, 'wb')
	wallpaper.write(response.content)
	wallpaper.close()


def current():
	currentDirectory = os.getcwd()
	currentDirectory = str(currentDirectory)
	
	return currentDirectory


def resetConf():

	print("Making reset to all config files")
	currentDirectory = current()
	key_conf = open((currentDirectory + "/Assets/API-KEY.conf"), 'w')
	key_conf.write("DEMO-KEY")
	key_conf.close

	path_conf = open((currentDirectory + "/Assets/path.conf"), 'w')
	path_conf.write("BACKGROUND PATH")
	path_conf.close

	print("Config files succesfully reseted.")


def loadAll():

	global background_dir
	currentDirectory = current()
	

	print("INITIALIZING... ")
	print("Loading the api data.")
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
		print("Code error: " + str(error) )
		print("you must make a right configuration of wallpaper and your background path")
		print("You can make the complete initial setup with the assistant, (option 5 in the main menu selector).")
		exit()

	elif error == 2:
		print("Code error: " + str(error) )
		print("Remember to setup your wallpaper path configuration in Assets/path.conf")
		print("You can make the complete initial setup with the assistant, (option 5 in the main menu selector).")
		exit()

	elif error == 1:
		print("Code error: " + str(error) )
		print("Remember to put the key in the Assets/API-KEY.conf")
		print("You can make the complete initial setup with the assistant, (option 5 in the main menu selector).")
		exit()

	elif error == 0:
		print("Api key loaded succesfully.")	
		print("And background conf loaded succesfully.")

	request = requests.get(api_url)
	status = request.status_code
	
	
	DATA = request.text

	# checking connection
	if status == 200:
		text = "Succesfully reached api"
		print("Status: " + str(status) +", "+ text + "\n")
	
	else:
		text = "Make shure the api key is valid \n and check if you have network connection."
		print("Request to the API status: " + str(status) +" "+ text + "\n")
		jk()
		exit()
	
	# parsing the json and 
	global JSON_DATA 
	JSON_DATA = json.loads(DATA)


def change_wallpaper(path):
	#ctypes.windll.user32.SystemParametersInfo(a,b,c,d)
	# a = 20.  b = 0. c = complete image path. d = 0
	path = str(path)
	formated_path = path.replace("\\", "/")
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)



def DownloadLowRes():
	#check if the media type is an image
	media_type = JSON_DATA['media_type']

	if media_type.lower() != "image":
		print("This media type cannot be set as wallpaper, because it is")
		print("Media type: " + media_type)
		exit()

	#This function only downloads the low resolution image

	#Get the url from the json
	low_res_url = JSON_DATA['url']

	currentdirectory = current()
	download_image(low_res_url, (currentdirectory + Low-Resolution-Img.jpg))

	sleep(PAUSE_TIME)

	print("\n")
	print("Low resolution image download succesfully")
	print("\n\n")



def DownloadHD():
	#check if the media type is an image
	
	media_type = JSON_DATA['media_type']

	if media_type.lower() != "image":
		print("This media type cannot be set as wallpaper, because it is")
		print("Media type: " + media_type)
		exit()

	current_directory = current()

	#This function only downloads the high resolution image

	#Get the url from the json
	high_res_url = JSON_DATA['hdurl']

	#Download the image and save it
	download_image(high_res_rl, (current_directory + "./APOD.jpg"))

	sleep(PAUSE_TIME)

	print("\n")
	print("High resolution image download succesfully")
	print("\n\n")



def getInfo():
	
	# number 1 is the same asTrue

	#Get the image's title
	title = JSON_DATA['title']
	print("The title of this image is: " + str(title) + "\n")

	sleep(PAUSE_TIME)


	#Image's date
	date = JSON_DATA['date']
	print("The date of this photo is: " + str(date) + "\n")

	sleep(PAUSE_TIME)

	#Get the media type
	media_type = JSON_DATA['media_type']
	print("The tipe of this media is: " + str(media_type) + " \n")


	try:
		#high defition url of the image	
		IMGURL = JSON_DATA['hdurl']
		print("The high definition image's url is " + str(IMGURL) + "\n")
		
	except:
		print("No information for parameter hdurl")
		pass

	sleep(PAUSE_TIME)


	try:
		#Retrieves the low definition url of the image
		low_res_url = JSON_DATA['url']
		print("The low definition media url is: " + str(low_res_url) + " \n")
	
	except:
		print("No information for parameter url")
		pass
		
	sleep(PAUSE_TIME)


	#Retrieves the nasa api version
	service_version = JSON_DATA['service_version']
	print("The version of the service(NASA APOD API) is: " + str(service_version) + " \n")
	
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
	
	#Check if the file is an image
	media_type = JSON_DATA['media_type']

	if media_type.lower() != "image":
		print("This media type cannot be set as wallpaper, because it is")
		print("Media type: " + media_type)
		exit()



	currentDirectory = current()

	#read the wallpaper route from the path.conf file
	background_dir = open((currentDirectory + "/Assets/path.conf"), 'r')
	background_dir = background_dir.readline()


	#Getting the info of the image from the json
	getInfo()

	#Starting the download process of the image
	print('Downloading the image. \n\n')
	sleep(PAUSE_TIME)
	
	HDURL = JSON_DATA['hdurl']
	
	#calling the download image function
	download_image(HDURL, background_dir)


	#setting the image as background
	change_wallpaper(background_dir)

	print("Setting as a background.")
	
	#opening the file, writing and closing image
	wallpaper = open(background_dir, 'wb')
	wallpaper.write(response.content)
	wallpaper.close()

	#Calling the function 
	#for refreshing the wallpaper

	


	print("succesfully changed background.")

	#writing to the logs

	file = open( str(currentDirectory) + "log.txt", "a")
	file.write("Succesfully downloaded today's APOD image, and changed the background")
	file.close()


#this next function retrieves an APOD image from an specified date, 
# using the user's input

def specific():
	currentDirectory = current()
	path_file = (currentDirectory + "/Assets/path.conf")
	key_file = (currentDirectory + "/Assets/API-KEY.conf")

	
	print("this function retrieves an APOD image from an specified date.")
	
	year = input("Enter the year of the image to retrive, format = YYYY, eg: 2011 \n Year: ")
	month = input("Enter the month of the year, of image to retrieve, format = MM, eg: 7 \n Month: ")
	day = input("Enter the day of the month, of image to retrieve, format = DD, eg: 21 \n Day: ")

	#data conversion and verify process
	
	#conversion to int, to verify if each value, is valid
	year = int(year)
	month = int(month)
	day = int(day)

	#verification of the values


	#re conversion to str, to make the request

	year = str(year)
	month = str(month)
	day = str(day)

	
	#reading the api key, from the file
	
	file = open(key_file, 'r')
	key = file.readline()
	file.close()

	key = str(key)

	#format the url of the api, and the date argument

	api_url = ("https://api.nasa.gov/planetary/apod?api_key=" + key) 
	date = ("&date=" + year + "-" + month + "-" + day)

	final_url = (api_url + date)
	print(final_url)

	#making the request of the json data
	#the final request format is this one: 
	# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY?date=YYYY-MM-DD

	request = requests.get(final_url) 
	status = request.status_code
	
	downloaded_data = request.text

	# checking connection
	if status == 200:
		text = "Succesfully reached api"
		print("Status: " + str(status) +", "+ text + "\n")
	
	else:
		text = "Make shure the api key is valid \n and check if you have network connection."
		print("Request to the API status: " + str(status) +" "+ text + "\n")
		jk()
		exit()
	
	# parsing the json and 
	json_data = json.loads(downloaded_data)

	hdurl = json_data['hdurl']
	
	#use requests for download the image
	response = requests.get(hdurl)
	
	if response.status_code == 200:
		print('Image reached')
	else:
		print("Something else happened")
		print("HTTP error: " + response.status_code)
		exit()

	#setting the image as background

	print("Setting as a background.")
	
	file = open(path_file, 'r')
	background_dir = file.read()
	file.close()

	#opening the file, writing and closing image
	wallpaper = open(background_dir, 'wb')
	wallpaper.write(response.content)
	wallpaper.close()

	print("succesfully changed background.")

	#writing to the logs

	file = open( str(currentDirectory) + "log.txt", "a")
	file.write("Succesfully downloaded today's APOD image, and changed the background")
	file.close()




def setup1():
	currentDirectory = current()
	path_file = (currentDirectory + "/Assets/path.conf")
	key_file = (currentDirectory + "/Assets/API-KEY.conf")

	print("Be conscient that your current wallpaper will be replaced, ")
	print("So make a copy of it, if you wana save it.")
	print("let's continue: \n")
	
	print("Input here, the ABSOLUTE PATH of your actual desktop wallpaper \n"
	"you must include the name of the file, "
	"Example: /home/USERNAME/Desktop/wallpaper.jpg \n")

	path = input("Enter the path: ")
	print("make shure its the right path, else,\n just re run the option 1. \n")

	save_path = open(path_file, 'w' )
	save_path.write(path)
	save_path.close()

	print("Now input here the key of your api, it will be saved at /Assets/API-KEY.conf file, \n "
	"If you modify it, make shure it doesn't have white lines \n")

	key = input("Enter the key: ")
	print("make shure its the right key, else,\n just re run the option 1.\n\n")

	save_key = open(key_file, 'w' )
	save_key.write(key)
	save_key.close()

	print("the configuration is done, would you like now to change your background? (1)Y / (2)N")
	SecondOption = input(": ")
	SecondOption = int(SecondOption)

	if SecondOption == 1:
		loadAll()
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
	
	resetConf()

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

	# options for the user
	
	print("What would you like to do? \n")
	print("(1) Change your current background.      (2) Get all info of today image. \n"
		"(3) Only Download low resolution image.  (4) Only Download high resolution image.\n"
		"(5) Initial Setup. (6) Reset all config files (wallpaper path & api-key)\n"
		"(7) Download an image from an specified date")
	
	option = input(": ")

	try:
		option = int(option)
	except ValueError:
		print("The value entered isn't valid")


	if option == 1:
		print("The option selected is: " +str(option) + "\n")
		loadAll()
		downloadBackground()

	elif option == 2:
		print("The option selected is: " +str(option) + "\n")
		loadAll()
		getInfo()

	elif option == 3:
		print("The option selected is: " +str(option) + "\n")
		loadAll()
		DownloadLowRes()

	elif option == 4:
		print("The option selected is: " +str(option) + "\n")
		loadAll()
		DownloadHD()

	elif option == 5:
		print("The option selected is: " +str(option) + "\n")
		InitialSetup()

	elif option == 6:
		print("The option selected is: " +str(option) + "\n")
		resetConf()

	elif option == 7:
		specific()
	
	else:
		print("That option doesn't exists or something else went wrong \n")
		jk()
		exit()



if __name__ == '__main__':
	try:
		#Configuring colorama
		print(Fore.CYAN)
		print(Style.BRIGHT)	
		main()
		
		print("If you are on windows, and the wallpaper doesn't change, do right click on the desktop,\n "
		"and click refresh. If all its fine, should change, else wait a little more, writing big images is a little slow some times, \n"
		"else verify the path of the download destination and re configure,\n "
		"using the assistant" )

		print("\n Would you like to make another thing?")
		print("(1)Yes (2)No")

		option = input(": ")
		option = int(option)

		if option == 1:
			try:
				main()
			
			except KeyboardInterrupt:
				print("\n Bye ;D")
				exit()

		elif option == 2:
			print("\n I hope c'ya soon, bye :P")
		else:
			print("\n Something else went wrong.")


	except KeyboardInterrupt:
		print("\n Bye ;D")
		exit()

