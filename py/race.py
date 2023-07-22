import turtle
import random
screen = turtle.Screen()
screen.setup(width=700,height=400)
def end():
    return False
is_race_on = False
bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","blue","green","yellow","purple","orange"]
y_cor = [-100,-60,-20,20,60,100]
breshkat = []
for i in range(0,6):
    breshka = turtle.Turtle()
    breshka.shapesize(1.5)
    breshka.shape("turtle")
    breshka.color(colors[i])
    breshka.up()
    breshka.goto(-330,y_cor[i])
    breshkat.append(breshka)
if bet:
    is_race_on = True
while is_race_on:
    breshkat[0].forward(random.randint(0,10))
    breshkat[1].forward(random.randint(0,10))
    breshkat[2].forward(random.randint(0,10))
    breshkat[3].forward(random.randint(0,10))
    breshkat[4].forward(random.randint(0,10))
    breshkat[5].forward(random.randint(0,10))
    if breshkat[0].xcor() >= 330:
        winner = breshkat[0]
        is_race_on = end()
    elif breshkat[1].xcor() >= 330:
        winner = breshkat[1]
        is_race_on = end()
    elif breshkat[2].xcor() >= 330:
        winner = breshkat[2]
        is_race_on = end()
    elif breshkat[3].xcor() >= 330:
        winner = breshkat[3]
        is_race_on = end()
    elif breshkat[4].xcor() >= 330:
        winner = breshkat[4]
        is_race_on = end()
    elif breshkat[5].xcor() >= 330:
        winner = breshkat[5]
        is_race_on = end()
if bet == winner.color()[0]:
    print(f"You guessed it right! The {winner.color()[0]} turtle won the race.")
else:
    print(f"You guessed it wrong! The {winner.color()[0]} turtle won the race.")
screen.exitonclick()