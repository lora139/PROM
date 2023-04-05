import turtle
from turtle import Turtle, Screen

pen = turtle.Turtle()
screen = Screen()
turtle = Turtle()
  

# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    pen.color('red')
  
    # Start filling the color
    pen.begin_fill()
    pen.pensize(3)
    # Draw the left line
    pen.left(50)
    pen.forward(133)
    pen.circle(50,200)
    pen.right(140)
    pen.circle(50,200)
    pen.forward(112)
    pen.end_fill()
  
# Defining method to write text
def txt():
  
    # Move turtle to air
    pen.up()
  
    # Move turtle to a given position
    pen.setpos(-68, 95)
  
    # Move the turtle to the ground
    pen.down()
  
    # Set the text color to lightgreen
    pen.color('white')
  
    # Write the specified text in 
    # specified font style and size
    pen.write("I LOVE YOU", font=(
      "Verdana",12, "bold"))
    
    
def click_handler(x, y):
    screen.onclick(None)  # disable handler while in handler

    try:
        next(heart)
        
    except StopIteration:
        return  

heart()
txt()
screen.onclick(click_handler)

screen.mainloop()
# To hide turtle
pen.ht()