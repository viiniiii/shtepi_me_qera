import turtle
import pandas
score = 0
screen = turtle.Screen()
screen.title("US states game")
image = "/Users/SIEMENS/OneDrive/Desktop/python/us-states-game-start/states.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("/Users/SIEMENS/OneDrive/Desktop/python/us-states-game-start/50_states.csv")
states = data.state.to_list()
guessed_states = []
while score < 50:
    answer_state = (screen.textinput(title=f"{score}/50 States Correct", prompt="Enter the name of the state")).title()
    if answer_state == "Exit":
        #missing_states = [for sta in states if sta not in guessed_states]
        #new_data = pandas.DataFrame(missing_states)
        #new_data.to_csv("states_to_learn")
        break
    if answer_state in states and answer_state not in guessed_states:
        score = score + 1
        guessed_states.append(answer_state)
        pen = turtle.Turtle()
        pen.up()
        pen.hideturtle()
        pen.color("blue")
        state_data = data[data.state == answer_state]
        pen.goto(float(state_data.x),float(state_data.y))
        pen.write(state_data.state.item(),align="center",font=("Arial",10,"normal"))
turtle.mainloop()