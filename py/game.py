import turtle as t
import os
lojtari_a_piket = 0
lojtari_b_piket = 0

win = t.Screen()    
win.title("Ping Pong") 
win.bgcolor('blue')    
win.setup(width=900,height=700) 
win.tracer(0)   



pllaka_majte = t.Turtle()
pllaka_majte.speed(0)
pllaka_majte.shape('square')
pllaka_majte.color('yellow')
pllaka_majte.shapesize(stretch_wid=5,stretch_len=1)
pllaka_majte.penup()
pllaka_majte.goto(-350,0)


pllaka_djathte = t.Turtle()
pllaka_djathte.speed(0)
pllaka_djathte.shape('square')
pllaka_djathte.shapesize(stretch_wid=5,stretch_len=1)
pllaka_djathte.color('green')
pllaka_djathte.penup()
pllaka_djathte.goto(350,0)


topi = t.Turtle()
topi.speed(0)
topi.shape('circle')
topi.color('red')
topi.penup()
topi.goto(0,0)
topi_dx = 0.3   
topi_dy = 0.3


pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Lojtari A: 0   Lojtari B: 0 ",align="center",font=('Monaco',24,"normal"))



def pllaka_majte_up():
    y = pllaka_majte.ycor()
    y = y + 15
    pllaka_majte.sety(y)


def pllaka_majte_down():
    y = pllaka_majte.ycor()
    y = y - 15
    pllaka_majte.sety(y)

#levizja e pllakes se djathte    - Redor Laci

def pllaka_djathte_up():
    y = pllaka_djathte.ycor()
    y = y + 15
    pllaka_djathte.sety(y)


def pllaka_djathte_down():
    y = pllaka_djathte.ycor()
    y = y - 15
    pllaka_djathte.sety(y)

# Kontrollet - Kesiana Myftari

win.listen()
win.onkeypress(pllaka_majte_up,"w")
win.onkeypress(pllaka_majte_down,"s")
win.onkeypress(pllaka_djathte_up,"Up")
win.onkeypress(pllaka_djathte_down,"Down")




# Zhvillimi i lojes    - Edvin Perfundi

while True:
    win.update() 

    topi.setx(topi.xcor() + topi_dx)
    topi.sety(topi.ycor() + topi_dy)


    if topi.ycor() > 290: 
        topi.sety(290)
        topi_dy = topi_dy * -1


    if topi.ycor() < -290: 
        topi.sety(-290)
        topi_dy = topi_dy * -1


    if topi.xcor() > 390:   
        topi.goto(0,0)
        topi_dx = topi_dx * -1
        lojtari_a_piket = lojtari_a_piket + 1
        pen.clear()
        pen.write("Lojtari A: {}                    Lojtari B: {} ".format(lojtari_a_piket,lojtari_b_piket),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(topi.xcor()) < -390:
        topi.goto(0,0)
        topi_dx = topi_dx * -1
        lojtari_b_piket = lojtari_b_piket + 1
        pen.clear()
        pen.write("Lojtari A: {}                    Lojtari B: {} ".format(lojtari_a_piket,lojtari_b_piket),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")


    if(topi.xcor() > 340) and (topi.xcor() < 350) and (topi.ycor() < pllaka_djathte.ycor() + 40 and topi.ycor() > pllaka_djathte.ycor() - 40):
        topi.setx(340)
        topi_dx = topi_dx * -1
        os.system("afplay paddle.wav&")

    if(topi.xcor() < -340) and (topi.xcor() > -350) and (topi.ycor() < pllaka_majte.ycor() + 40 and topi.ycor() > pllaka_majte.ycor() - 40):
        topi.setx(-340)
        topi_dx = topi_dx * -1
        os.system("afplay paddle.wav&")