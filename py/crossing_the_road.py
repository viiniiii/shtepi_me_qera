import turtle
import random
import time
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
turtle.mode("logo")
turtle.colormode(255)
class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(0.9,1.8)
        self.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.setheading(270)
        self.goto(380,random.randint(-250,250))
    def move(self,number):
        if number == 1:
            self.forward(random.randint(10,12))
        elif number == 2:
            self.forward(random.randint(10,15))
        elif number == 3:
            self.forward(random.randint(10,20))
    def accident(self,Breshka):
        return self.distance(Breshka) < 15
    def restart(self):
        if self.xcor() < -400:
            self.goto(380,random.randint(-250,250))
class Level(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.value = 1
    def level_up(self):
        self.value += 1
    def level_teller(self):
        self.hideturtle()
        self.color("blue")
        self.clear()
        self.penup()
        self.goto(0,250)
        self.write(f"Level {self.value}",align="center",font=("Arial",30,"normal"))

        
class Breshka(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
    def start(self):
        self.penup()
        self.goto(0,-280)
        self.setheading(0)
    def move(self):
        self.forward(10)
screen.tracer(0)
level = Level()
level.level_teller()
cars = []
for i in range(2):
    car = Car()
    cars.append(car)
breshka = Breshka()
breshka.start()
screen.update()
screen.listen()
screen.onkeypress(fun=breshka.move,key="space")
game_on = True
koha = time.time()
need_more = True
while game_on:
    screen.update()
    time.sleep(0.1)
    koha_fund = time.time()
    if round(koha-koha_fund) % 12 == 0 and need_more == True:
        car = Car()
        cars.append(car)
        if len(cars) > 15:
            need_more == True
    for i in cars:
        i.move(level.value)
        i.restart()
        if i.accident(breshka):
            pen = turtle.Turtle() 
            pen.color("red")
            pen.hideturtle()
            pen.penup()
            pen.goto(0,0)
            pen.write("Game over",align="center",font=("Arial",40,"normal"))
            screen.update()
            time.sleep(3)
            game_on = False
    if breshka.ycor() > 250:
        level.level_up()
        breshka.start()
        level.level_teller()
    if level.value > 3:
        pen = turtle.Turtle()
        pen.color("green")
        pen.hideturtle()
        pen.penup()
        pen.goto(0,0)
        pen.write("You won!",align="center",font=("Arial",40,"normal"))
        screen.update()
        time.sleep(3)
        game_on = False


        
