# NASA APOD Utility

## This python3 script has been made only for fun and for killing time
## and it's not official by NASA.


***


### Description

This utility script, handles the requests and automatizes some processes
using the Nasa's APOD api, whith this utility you can:

1. Download and automatically setup the APOD image as your wallpaper.
2. Single download of the low resolution version of the APOD image.
3. Single download of the  high resolution version of the APOD image
4. Donwload all information from api about the APOD image.



**APOD stands for Astro Photography Of the Day.**


### Alert:
This script, was designed overall, for **_linux enviroments_**, 
and maybe MacOs, but never tested in MacOs, it was tested and made
in Ubuntu LTS 20.4, alias focal, so it will certainly work on any debian
based distro like ubuntu-mint, or in Raspberry Pi OS.
it only uses python and no other languages.
It hasn't been tested on fedora, gentoo or arch based 
distros, so it's not known if it will work properly on 
any of these, or other.

## Installing Instructions.
First clone the repo, then in the repo folder, 
you just need to execute in the terminal

> pip3 install -r requirements.txt

Or if it doesn't works, try making:
> pip install -r requirements.txt

The last step is you to get an api key, (it's 100% free),
you can get it at: https://api.nasa.gov/?ref=public-apis#signUp

To load the api key, you must write it in Assets/API-KEY.conf file, only the key, not the url.

Then just execute the script in the terminal:

> python3 ./main.py

For setting up the proper configurations of the script,
**just run it**, and in the option selector, choose the
**option 5** (Initial Setup), then choose between **one of the 2 options** of setting up
and then just ***follow the instructions of the assistant.***
