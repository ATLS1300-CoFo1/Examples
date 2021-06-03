#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use
import random
colormode(255)

#Create a panel to draw on. 
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#======= DEFINE VARIABLES BELOW ======

# 1. draw a filled blue circle at a specific location
up() # pick up pen
goto(500,100)  #go to upper right corner

color("blue") # or color((0,0,255))

down() # set down pen
begin_fill()
circle(25) # open circle, radius = 25
end_fill()

# 2. draw empty red circle with a thick line
up()
forward(100) # move over

color((255,0,0)) #use RGB values to change color to red
pensize(5) #set pen width to 5 pixels wide

down()

#draw square
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)

up() #pick up pen



#======= PERFORM TASKS BELOW ======




#======= DO NOT ADD CODE BELOW THIS LINE ======

#done() # UNCOMMENT LINE BELOW BEFORE SUBMITTING 