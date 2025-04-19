# import necessary packages
import turtle
import random

# set color mode to use (R, G, B) values
turtle.colormode(255)

# set canvas background color to "black". Instead, we can use "red" too.
turtle.bgcolor("black")


# defining the five-point star drawing function
# this function needs four arguments(=parameters)
def draw_a_star(start_angle, start_x, start_y, star_size):
    # START OF THE FUNCTION
    point = turtle.Turtle()
    point.speed(20)
    point.penup()
    
    # set starting coordinate of the star
    point.setx(start_x)
    point.sety(start_y)
    point.pendown()
    point.hideturtle()
    
    # set RGB from random values
    # RGB value consistes of 0~255 number
    # eg. Violet's R, G, B = 127, 0, 255
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # set pen color
    point.pencolor(red, green, blue)

    # first heading angle
    point.left(start_angle)
    
    # draw star with 'size' value
    point.forward(star_size)
    point.right(144)
    point.forward(star_size)
    point.right(144)
    point.forward(star_size)
    point.right(144)
    point.forward(star_size)
    point.right(144)
    point.forward(star_size)
    
    # END OF THE FUNCTION
    

for x in range(0, 79):
    # set needed values with random.
    angle = random.randint(0, 360)
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(0, 300)
    
    # calling the function
    draw_a_star(start_angle=angle, start_x=x, start_y=y, star_size=size)

