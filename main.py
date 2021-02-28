# Youtube Video Downloader || Made By Simer00
import time
import os
import getpass
import random
import sys
from pytube import YouTube
import lolcat #Ref 12,13,14
from pyfiglet import Figlet #Ref 36,37,38

#header and footer
header = 'lolcat -a -d 3 -p 2 "./banners/header.txt"'
footer = 'lolcat -a -d 3 -p 2 "./banners/footer.txt"'
error = 'lolcat -a -d 2 -p 2 "./banners/error.txt"'
login = 'lolcat -a -d 25 -p 2 ./banners/login.txt'
geturl = 'lolcat -a -d 25 -p 2 ./banners/geturl.txt'
restart = 'python main.py'
os.system(header)

#defining colors for a user friendly environment
RED =   '\033[31;2m' # red color
BLUE =   '\033[34;2m' # blue color
GREEN =   '\033[32;1m' # green color
YELLOW =   '\033[93m' # yellow color
PINK =   '\033[95m' # ping color
PURPLE =   '\033[35m' # green color
GREY =   '\033[90;1m' # grey color
WHITE =   '\033[37;1m' # white color
END =   '\033[m' # reset to the default

# automated typing thing 
def typing(words):
  words
  for char in words:
    time.sleep(random.choice([0.04, 0.04,0.05, 0.05, 0.04, 0.038, 0.05]))
    sys.stdout.write(char)
    sys.stdout.flush()

# Banners Test (https://www.askapache.com/online-tools/figlet-ascii/)
# font = Figlet(font='smslant')
# print(font.renderText('Enter anything to make a banner to copy paste!'))

#defining login details from database and a clear command
key = os.getenv("KEY")
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

#LOGIN
if key:
  print(YELLOW)
  os.system(login) 
  inpass = getpass.getpass("")
  animation = "|/-\\"
  for i in range(25):
   time.sleep(0.1)
   sys.stdout.write(WHITE + "\rAuthenticating" + animation[i % len(animation)])
   sys.stdout.flush()
   if (inpass != key):
     i = 0
     while i < 50:
       for i in range(25):
         time.sleep(0.1)
         sys.stdout.write(WHITE + "\rAuthenticating" + animation[i % len(animation)])
         sys.stdout.flush()
         i += 1
         if i == 25:
          clear()
          os.system(error)
          print(RED)
          typing("Incorrect Password, Please Try again!\n")
          sys.exit()
   elif (inpass == key):
     continue
  clear()
  os.system(header)
  sys.stdout.write(GREEN + "\rAuthenticated!\n")

else:
  print(YELLOW)
  os.system(login) 
  print("Due to an error retrieving the password, here is an alternative password: key")
  inpass = getpass.getpass("")
  animation = "|/-\\"
  for i in range(25):
   time.sleep(0.1)
   sys.stdout.write(WHITE + "\rAuthenticating" + animation[i % len(animation)])
   sys.stdout.flush()
   if (inpass != "key"):
     i = 0
     while i < 50:
       for i in range(25):
         time.sleep(0.1)
         sys.stdout.write(WHITE + "\rAuthenticating" + animation[i % len(animation)])
         sys.stdout.flush()
         i += 1
         if i == 25:
          clear()
          os.system(error)
          print(RED)
          typing("Incorrect Password, Please Try again!\n")
          sys.exit()
   elif (inpass == "key"):
     continue
  clear()
  os.system(header)
  sys.stdout.write(GREEN + "\rAuthenticated!\n")

try: 
  #using except handing to avoid sending out complex errors
  #Ask for the link from user in the console
  print()
  os.system(geturl)
  link = input("")
  yt = YouTube(link)

  #Showing details of the requested video
  print()
  print(GREY + "Title:", END , yt.title)
  print(GREY + "Views:", END , yt.views)
  print(GREY + "Length:", END , yt.length)
  print(GREY + "Rating:", END , yt.rating)
  print()

  #Getting the highest resolution possible
  ys = yt.streams.get_highest_resolution()

  #Downloading Script
  animation = "|/-\\"
  for i in range(100):
    time.sleep(0.1)
    sys.stdout.write(WHITE + "\rDownloading" + animation[i % len(animation)])
    sys.stdout.flush()
    ys.download() # Download
  sys.stdout.write(GREEN + "\rDownloaded!\n")
  time.sleep(1.5)
  print(PURPLE)
  typing("Switch to the code section and find your video in the main directory to save it to your device!\n Note: It may take some time to load depending on video length.\n")
  os.system(footer)
  print()
except:
  i = 0
  while i < 50:
    for i in range(25):
      time.sleep(0.1)
      sys.stdout.write(WHITE + "\rDownloading" + animation[i % len(animation)])
      sys.stdout.flush()
      i += 1
      if i == 25:
        clear()
        os.system(error)
        print(RED)
        typing("404! Incorrect Url, Please Enter a valid Youtube Url!!\n")
        sys.exit()
# Youtube Video Downloader || Made By Simer00