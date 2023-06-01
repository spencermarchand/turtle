#a math game where your turtle starts on one side of the screen and then you have to answer questions to move it across the screen
# You get 3 lives if you mess up then you lose a life
# Written by Spencer Marchand Feb 22, 2022. 
import turtle
import random
import time
screen = turtle.Screen() #creates a screen
screen.bgcolor('#00BFFF') # Changes background color
player = turtle.Turtle() #creates the player
player.color('black') #Changes player color
player.shape('turtle') #Changes player shape
player.penup()#Lifts the pen so player doesnt draw
player.goto(-300,250) #Moves player to start position
finish_line = turtle.Turtle() #creates the finish line
life_counter = turtle.Turtle() #Creates the turtle that is going to update the lives
life_counter.hideturtle()
lives = 3 #number of lives
finish_line.penup() #Lifts the pen
finish_line.goto(200,200) #
finish_line.pendown() #puts pen down
finish_line.left(90) #spins 90 degrees left
finish_line.goto(200,300)
finish_line.write('Cross here to win the game') 
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(-300,100)
finish_line.write('You have 3 lives. Answer the qestions to move the turtle across the screen and cross the line to win',font = 29)
life_counter.penup()

#Start of the game loop
while lives > 0:
    if lives >1:
     life_counter.clear()
     life_counter.goto(-150, 200)
     life_counter.write(f'You currently have {lives} lifes left', font = 29)
    if lives ==1:
     life_counter.clear()
     life_counter.goto(-150, 200)
     life_counter.write(f'You currently have {lives} life left', font = 29) 
    if player.pos() >= (200,0): #if player crosses this line they win 
        player.write('I won!', font = 29) #writes out a winning note
        break
    num1 = random.randint(1,5) #Random number between 0 and 15 for num 1 
    num2 = random.randint(1,5) # Random nubmer between 0 and 15 for num 2   
    question = turtle.numinput(f"What is {num1} x {num2}?", 'enter the number') #input box to ask player question 
    if question == num1*num2: #If player gets the math question right they move forward 50 pixels
        player.forward(50) #moves player forward
        player.write('you got it right. Keep moving on.') 
        time.sleep(0.5) #pauses for half a second
        player.clear()  # Clears the writing 
    else: 
        player.write('you got the question wrong', font = 29, align = 'left') #writes out message for wrong guess
        player.color('red') # Changes the turtle color to red idicating wrong anwer
        player.left(360)  #Spins the turtle as a sign of frustration
        player.color('black') #returns the turtle color to black
        time.sleep(0.5) #Pauses for half a second 
        player.clear() #Clears the writing on the screen
        lives = lives -1; 
        
turtle.done()