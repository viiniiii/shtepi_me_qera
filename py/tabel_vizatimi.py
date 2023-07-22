import turtle
pen = turtle.Turtle()
screen = turtle.Screen()
pen.color("green")
def move_forward():
    turtle.forward(10)
def turn_left():
    turtle.left(10)
def turn_right():
    turtle.right(10)
def move_backwards():
    turtle.back(10)
def clear_screen():
    turtle.clear()
screen.listen()
screen.onkeypress(key="a",fun=turn_left)
screen.onkeypress(key="d",fun=turn_right)    
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="s",fun=move_forward)
screen.onkeypress(key="c",fun=move_forward)

screen.exitonclick()