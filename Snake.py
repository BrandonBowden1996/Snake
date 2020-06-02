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

#Create the player turtle
Player = turtle.Turtle()
Player.color("White")
Player.shape("square")
Player.penup()
Player.speed(0)
Player.setposition(0,0)

playerspeed = 15

#Move the player up, down, left and right
def move_up():
	y = Player.ycor()
	y += playerspeed
	if y > 280:
		y = 280
	Player.sety(y)
	
def move_down():
	y = Player.ycor()
	y -= playerspeed
	if y < -280:
		y = -280
	Player.sety(y)
	
def move_left():
	x = Player.xcor()
	x -= playerspeed
	if x < -280:
		x = -280
	Player.setx(x)
	
def move_right():
	x = Player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	Player.setx(x)
	
#Creat the keyboard binding
turtle.listen()
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


delay = input("Press enter to finish")
