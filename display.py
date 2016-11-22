#!/usr/bin/python

from SimpleCV import Image, Display
from time import sleep

myDisplay = Display()

raspberryImage = Image("lucas.jpg")
raspberryImage.save(myDisplay)

while not myDisplay.isDone():
 sleep(0.1)
