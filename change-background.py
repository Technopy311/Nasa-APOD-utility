import os
import pynotifier
from main import loadAll, downloadBackground, resetConf, current

currentDirectory = current()

path_file = (currentDirectory + "/Assets/path.conf")
key_file = (currentDirectory + "/Assets/API-KEY.conf")

path = "/home/technopy/.local/share/backgrounds/default.jpg"

save_path = open(path_file, 'w' )
save_path.write(path)
save_path.close()

key = "F6wkuYMeExyyZW9516419T3pGXzHcA5mkEwkNTF8"

save_key = open(key_file, 'w' )
save_key.write(key)
save_key.close()

loadAll()

downloadBackground()

resetConf()