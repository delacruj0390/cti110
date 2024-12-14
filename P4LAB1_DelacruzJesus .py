# Delacruz, Jesus M
# 2980390
# November 1, 2024
# P4LAB1


import turtle
t = turtle.Turtle() # Create a turtle

# Draw a square using a while loop
side_length = 150  # Length of each side 
sides_drawn = 0
while sides_drawn < 4:
    t.forward(side_length)
    t.left(90)
    sides_drawn += 1

# Draw a triangle using a while loop
t.penup()
t.goto(0, 80)  
t.pendown()
t.setheading(0)  

sides_drawn = 0
while sides_drawn < 3:
    t.forward(side_length)
    t.right(120)  
    sides_drawn += 1

# End Commands 
t.hideturtle()
turtle.done()
