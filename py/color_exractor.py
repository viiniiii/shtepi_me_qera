import turtle
import colorgram
import random
turtle.colormode(255)
colors = colorgram.extract('colors.jpeg', 15)
pen = turtle.Turtle()
pen.up()
pen.setpos(-300,-300)
pen.down()
a = 1
for j in range(12):
    for i in range(12):
        pen.dot(20,random.choice(colors).rgb)
        pen.up()
        pen.forward(50)
        pen.down()
    pen.dot(20,random.choice(colors).rgb)
    a *= -1
    pen.up()
    if a < 0:
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    else:
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.down()
