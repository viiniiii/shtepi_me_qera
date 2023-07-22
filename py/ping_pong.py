import turtle
import time
import random
class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(0.65,6.5)
    def pozicionim(self,x,y):
        self.penup()
        self.goto(x,y)
        self.setheading(0)
    def go_up(self):
        screen.tracer(0)
        self.setheading(0)
        screen.update()
        self.forward(10)
    def go_down(self):
        screen.tracer(0)
        self.setheading(180)
        screen.update()
        self.forward(10)
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(1.5,1.5)
        self.speed(0)
    def move(self):
        self.penup()
        self.forward(10)
    def random_direction(self):
        if random.randint(0,1) == 0:
            self.setheading(random.randint(15,165))
        else:
            self.setheading(random.randint(195,345))
    def opposite_direction(self):
        if self.heading() < 180:
            self.setheading(180 - self.heading())
        else:
            self.setheading(540 - self.heading())
    def opposite_direction_2(self):
        self.setheading(360 - self.heading())
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.scoreA = 0
        self.scoreB = 0
    def increase_scoreA(self):
        self.scoreA += 1
    def increase_scoreB(self):
        self.scoreB += 1
    def print_Score(self):
        self.clear()
        self.color("Blue")
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.write(f"Player A: {self.scoreA}      Player B: {self.scoreB}",align="center",font=("Arial",24,"normal"))

turtle.mode("logo")
screen = turtle.Screen()
screen.setup(width=1000,height=700)
screen.bgcolor("black")
screen.tracer(0)
score = ScoreBoard()
paddle_1 = Paddle()
paddle_1.pozicionim(-480,0)
paddle_2 = Paddle()
paddle_2.pozicionim(480,0)
ball = Ball()
screen.update() 
screen.listen()
screen.onkeypress(key="w",fun=paddle_1.go_up)
screen.onkeypress(key="s",fun=paddle_1.go_down)
screen.onkeypress(key="Up",fun=paddle_2.go_up)
screen.onkeypress(key="Down",fun=paddle_2.go_down)
ball.random_direction()
while True:
    time.sleep(0.05)
    screen.tracer(0)
    score.print_Score()
    ball.move()
    if ball.ycor() > 345 or ball.ycor() < -345:
        ball.opposite_direction()
    if ball.distance(paddle_1) < 45 or ball.distance(paddle_2) < 45:
        ball.opposite_direction_2()
    if ball.xcor() < -505:
        ball.goto(0,0)
        ball.random_direction()
        score.increase_scoreB()
    if ball.xcor() > 505:
        ball.goto(0,0)
        ball.random_direction()
        score.increase_scoreA()
    screen.update()