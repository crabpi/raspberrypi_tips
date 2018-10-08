#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#     I2C OLED Slideshow
#
# This script creates a slideshow of images
# on an I2C OLED Display using the Adafruit
# python library.
#
# It shows images found in the same directory
# as this script.
#
# Please see https://www.raspberrypi-spy.co.uk/
# for more information.
#
# Author : Matt Hawkins
# Date   : 12/03/2018
#
#--------------------------------------
import os
import sys
import time
import Adafruit_SSD1306
from PIL import Image

# Default delay of 1 second unless provided
# via command line parameter
delay=1
if len(sys.argv)==2:
  if sys.argv[1].isdigit():
    delay=int(sys.argv[1])

print("Using "+str(delay)+" second delay")

# List of image file extensions to look for
imageExtensions=[".jpg",".pgm",".ppm",".pbm",".bmp",".png"]

# 128x32 display with hardware I2C:
#disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

while True:

  # Find all files in current directory
  for root, dirs, files in os.walk("."):
    for filename in files:
      # Split filename to find file extension
      head, ext=os.path.splitext(filename)

      # Check if file has suitable image extension
      if ext in imageExtensions:

        print(filename)

        # Open image file
        image = Image.open(filename)

        # Check if image size matches display size
        if image.size==(disp.width, disp.height):
          # Convert image to 1-bit colour
          image=image.convert('1')
        else:
          # Resize to match display and convert to 1-bit colour
          image=image.resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

        # Display image.
        disp.image(image)
        disp.display()

        # Wait before showing next image
        time.sleep(delay)

