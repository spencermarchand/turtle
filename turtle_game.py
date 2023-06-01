#Small game using turtle package, made by Spencer Marchand :) 
#import the relevant modules
import turtle
import random 
import time
screen = turtle.Screen()
screen.title("Turtle Race!")
screen.bgcolor('lightblue') #set the background color to light blue 
#this is a two player game, they both roll a dice and who ever gets to the other side first wins the
#player one
player_one = turtle.Turtle()
player_one.color('blue') #player one colour
player_one.shape('turtle') #
#player 2 
player_two = turtle.Turtle()
player_two.color('red')
player_two.shape('turtle')
#position the players
player_one.penup()
player_two.penup()
player_one.goto(-300,200)
player_two.goto(-300,-200)
#Draw a finish line and then write Finish! at the top
finsh_line = turtle.Turtle()
finsh_line.color('black')
finsh_line.penup()
finsh_line.goto(300,-250)
finsh_line.pendown()
finsh_line.left(90)
finsh_line.forward(500)
finsh_line.write("Finish!", font = 28)
finsh_line.hideturtle()
print("Test on screen")
# Create the dice value
die = [1,2,3,4,5,6]

for i in range(30):
    die_roll = random.choice(die) #Rolls dice for player 1
    player_one.forward(10*die_roll) #Moves player 1 forward
    time.sleep(0.1) #Delay
    if player_one.pos() >= (300,250): #condition for if player one crosses the finish line
        player_one.write("I win!", font = 50) #displays a winning messgage for player 1
        break
    die_roll2 = random.choice(die) #Rolls dice for player 2
    player_two.forward(10*die_roll2)  #Moves player 2 forward
    time.sleep(0.1)
    if player_two.pos() >= (300,-250): #condition for if player two crosses the finish line
        player_two.write("I win!", font = 50) #displays a winning messgage for player 2
        break


turtle.done() #keeps the window on the screen
