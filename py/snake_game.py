import turtle
import random
import time
starting_positions = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segmentet = []
        self.create_snake()
        
    def create_snake(self):
        for i in range(3):
            new_segment = turtle.Turtle("square")
            new_segment.color("white")
            new_segment.up()
            new_segment.goto(starting_positions[i])
            self.segmentet.append(new_segment)
    def move(self):
        for i in range(len(self.segmentet)-1,0,-1):
            x = self.segmentet[i-1].xcor()
            y = self.segmentet[i-1].ycor()
            self.segmentet[i].goto(x,y)
        self.segmentet[0].forward(20)
    def turn_left(self):
        if self.segmentet[0].heading() != 0:
            self.segmentet[0].setheading(180)
    def turn_right(self):
        if self.segmentet[0].heading() != 180:
            self.segmentet[0].setheading(0)
    def turn_up(self):
        if self.segmentet[0].heading() != 270:
            self.segmentet[0].setheading(90)
    def turn_down(self):
        if self.segmentet[0].heading() != 90:
            self.segmentet[0].setheading(270)
    def add_segment(self,position):
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segmentet.append(new_segment)
    def extend(self):
        self.add_segment(self.segmentet[-1].position())
    def collision(self):
        for i in self.segmentet[1:]:
            if self.segmentet[0].distance(i) < 15:
                return True 
    def reset(self):
        for i in self.segmentet:
            i.goto(1000,1000)
        self.segmentet.clear()
        self.create_snake()
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.new_location()
    def new_location(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))
class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        file = open("data.txt",mode="r")
        self.score = 0
        self.high_score = int(file.read())
        file.close()
    def increase_score(self):
        self.score += 1
    def print_Score(self):
        self.clear()
        self.color("Blue")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.write(f"Score: {self.score}   High score: {self.high_score}",align="center",font=("Arial",24,"normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.print_Score()

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(key="Up",fun=snake.turn_up)
screen.onkey(key="Down",fun=snake.turn_down)
screen.onkey(key="Left",fun=snake.turn_left)
screen.onkey(key="Right",fun=snake.turn_right)
game_is_on = True
while game_is_on:
    score.print_Score()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segmentet[0].distance(food) < 15:
        food.new_location()
        score.increase_score()
        snake.extend()
    if snake.segmentet[0].xcor() > 280 or snake.segmentet[0].xcor() < -280 or snake.segmentet[0].ycor() > 280 or snake.segmentet[0].ycor() < -280:
        score.reset()
        snake.reset()
    if snake.collision():
       score.reset()
       snake.reset()

screen.exitonclick()
