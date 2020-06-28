#Snake Game
import turtle
import os
import math
import random 

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

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Create the player turtle
Player = turtle.Turtle()
Player.color("White")
Player.shape("triangle")
Player.penup()
Player.speed(0)
Player.setposition(0,0)
Player.setheading(90)
Player.direction = "Up"

playerspeed = 2

#Create the food turtle
Food = turtle.Turtle()
Food.color("Green")
Food.shape("circle")
Food.penup()
x = random.randint(-250, 250)
y = random.randint(-250, 250)
Food.setposition(x,y)


#Move the player up, down, left and right
def up():
	Player.direction = "Up"
	
def down():
	Player.direction = "Down"
	
def left():
	Player.direction = "Left"
	
def right():
	Player.direction = "Right"
		
def move():
	if Player.direction == "Up":
		Player.setheading(90)
		y = Player.ycor()
		y += playerspeed
		if y > 280:
			y = 280
		Player.sety(y)
	
	if Player.direction == "Down":
		Player.setheading(270)
		y = Player.ycor()
		y -= playerspeed
		if y < -280:
			y = -280
		Player.sety(y)
		
	if Player.direction == "Left":
		Player.setheading(180)
		x = Player.xcor()
		x -= playerspeed
		if x < -280:
			x = -280
		Player.setx(x)
	
	if Player.direction == "Right":
		Player.setheading(360)
		x = Player.xcor()
		x += playerspeed
		if x > 280:
			x = 280
		Player.setx(x)
	
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False
			
	
#Creat the keyboard binding
turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")


#Main game loop
while True:
	move()
	
	if isCollision(Player, Food):
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		Food.setposition(x, y)
		#Increase the snake speed
		playerspeed += 0.25
		#Increase the score
		score += 10
		scorestring = "Score: %s" %score
		score_pen.clear()
		score_pen.write(scorestring, False, align="left",font=("Arial", 14, "normal"))
	

			
			
	
		
delay = input("Press enter to finish")
