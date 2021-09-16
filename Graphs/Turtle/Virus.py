import turtle
from turtle import *

speed(50)
color('yellow')
bgcolor('black')
i = 200

while i > 0:
    left(i)
    forward(i * 3)
    i = i - 1

turtle.exitonclick()
