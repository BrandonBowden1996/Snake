#Snake Game
import turtle
import os

#set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Snake")

#Drawing the game border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()




delay = input("Press enter to finish")
