import tkinter
from tkinter import font

window = tkinter.Tk()
window.minsize(width=660,height=660)

class Draw(tkinter.Label):
    def __init__(self,x,y,turn):
        super().__init__()
        if turn == 1:
            self.fg = "red"
        else: 
            self.fg = "green"
        self.x = x
        self.y = y
    
turn = 1
count = 0
winner_label = tkinter.Label()
draw_label = tkinter.Label(text="It's a draw :0")
class Table():
    def __init__(self):
        self.row1 = ["_","_","_"]
        self.row2 = ["_","_","_"]
        self.row3 = ["_","_","_"]
        self.table = [self.row1,self.row2,self.row3]
    def check_game_status(self):
        if self.table[0][0] == "x" and self.table[0][1] == "x" and self.table[0][2] == "x":

            declare_winner("x")
        elif self.table[0][0] == "o" and self.table[0][1] == "o" and self.table[0][2] == "o":
            declare_winner("o")
        elif self.table[1][0] == "x" and self.table[1][1] == "x" and self.table[1][2] == "x":
            declare_winner("x")
        elif self.table[1][0] == "o" and self.table[1][1] == "o" and self.table[1][2] == "o":
            declare_winner("o")
        elif self.table[2][0] == "x" and self.table[2][1] == "x" and self.table[2][2] == "x":
            declare_winner("x") 
        elif self.table[2][0] == "o" and self.table[2][1] == "o" and self.table[2][2] == "o":
            declare_winner("o")
        elif self.table[0][0] == "x" and self.table[1][0] == "x" and self.table[2][0] == "x":
            declare_winner("x") 
        elif self.table[0][0] == "o" and self.table[1][0] == "o" and self.table[2][0] == "o":
            declare_winner("o")
        elif self.table[0][1] == "x" and self.table[1][1] == "x" and self.table[2][1] == "x":
            declare_winner("x")
        elif self.table[0][1] == "o" and self.table[1][1] == "o" and self.table[2][2] == "o":
            declare_winner("o")
        elif self.table[0][2] == "x" and self.table[1][2] == "x" and self.table[2][2] == "x":
            declare_winner("x")
        elif self.table[0][2] == "o" and self.table[1][2] == "o" and self.table[2][2] == "o":
            declare_winner("o")
        elif self.table[0][0] == "x" and self.table[1][1] == "x" and self.table[2][2] == "x":
            declare_winner("x") 
        elif self.table[0][0] == "o" and self.table[1][1] == "o" and self.table[2][2] == "o":
            declare_winner("o")
        elif self.table[0][2] == "x" and self.table[1][1] == "x" and self.table[2][0] == "x":
            declare_winner("x")
        elif self.table[0][2] == "o" and self.table[1][1] == "o" and self.table[2][0] == "o":
            declare_winner("o")
        elif count > 8:
            declare_winner("draw")
            
table = Table()
class Square(tkinter.Button):
    def __init__(self,x,y):
        super().__init__()
        self.button = tkinter.Button(bg="lightblue",width=30,height=15,command=self.press)
        self.x = x
        self.y = y
        self.draws = [i for i in range(9)]
    def press(self):
        global turn
        global count
        if turn == 1:
            self.draws[count] = self.create()
            self.draws[count].config(text="x",bg="lightblue",fg=self.draws[count].fg, font=font.Font(size=100))
            self.draws[count].grid(row=self.x,column=self.y)
            table.table[self.x][self.y] = "x"

        else: 
            self.draws[count] = self.create()
            self.draws[count].config(text="o",bg="lightblue",fg=self.draws[count].fg, font=font.Font(size=100))
            self.draws[count].grid(row=self.x,column=self.y)
            table.table[self.x][self.y] = "o"
        count = count + 1
        turn *= -1 
        self.button.config(state= tkinter.DISABLED)
        table.check_game_status()
    def create(self):
        draw = Draw(self.x,self.y,turn)
        return draw
    
def reset_game():
    global table
    table = Table()
    global turn, count
    turn = 1
    count = 0
    for row in field:
        for col in row:
            col.button.config(state=tkinter.NORMAL)
            for i in col.draws:
                if not isinstance(i, int):
                    i.config(text="")
def declare_winner(player):
    for row in range(3):
        for col in range(3):
            button = field[row][col]
            button.config(state=tkinter.DISABLED)
    winner_label.config(text=f"Player {player} wins!")
    winner_label.grid()
    play_again_button.config(state=tkinter.NORMAL) 
    winner_window = tkinter.Toplevel(window)
    winner_window.title("Winner!")
    winner_window.geometry("600x400")
    if player == "x" or player == "o":
        winner_message = tkinter.Label(winner_window, text=f"Player {player} wins!", fg="orange", font=font.Font(size=60))
    elif player == "draw": 
        winner_message = tkinter.Label(winner_window, text="It's a draw :0",fg="orange", font=font.Font(size=60))
    winner_message.grid(pady=20)
    winner_window.after(3000, winner_window.destroy)
    reset_game()

sq00 = Square(0,0)
sq01 = Square(0,1)
sq02 = Square(0,2)
sq10 = Square(1,0)
sq11 = Square(1,1)
sq12 = Square(1,2)
sq20 = Square(2,0)
sq21 = Square(2,1)
sq22 = Square(2,2)
sq00.button.grid(row=0,column=0)
sq01.button.grid(row=0,column=1)
sq02.button.grid(row=0,column=2)
sq10.button.grid(row=1,column=0)
sq11.button.grid(row=1,column=1)
sq12.button.grid(row=1,column=2)
sq20.button.grid(row=2,column=0)
sq21.button.grid(row=2,column=1)
sq22.button.grid(row=2,column=2)

row1 = [sq00,sq01,sq02]
row2 = [sq10,sq11,sq12]
row3 = [sq20,sq21,sq22]
field = [row1,row2,row3]

play_again_button = tkinter.Button(text="Play again",font=font.Font(size=30),command=reset_game)
play_again_button.grid(row=3,columnspan=3)

window.mainloop()