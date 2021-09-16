import turtle

colors = ['red','purple', 'blue', 'green', 'yellow', 'orange']

turtle.bgcolor('black')

for x in range(360):
    turtle.pencolor(colors[x % 6])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(59)