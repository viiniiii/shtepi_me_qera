import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = tkinter.Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.window.minsize(width=300,height=600)
        self.text = tkinter.Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("Arial",20,"bold"))
        self.text.grid(row=0,column=1,pady=20)
        self.canva = tkinter.Canvas(width=300,height=250,bg="white",borderwidth=0,highlightthickness=0)
        self.question_text = self.canva.create_text(150,125,text="Score: 0",fill=THEME_COLOR,width=280,font=("Arial",20,"italic"))
        self.canva.grid(row=1,column=0,columnspan=2,pady=20)

        sakt = tkinter.PhotoImage(file="py\_trivia\images\_true.png")
        self.correct = tkinter.Button(image=sakt,highlightthickness=0,borderwidth=0,command=self.true_pressed)
        self.correct.grid(row=2,column=0)
    
        gabim = tkinter.PhotoImage(file="py\_trivia\images\_false.png")
        self.wrong = tkinter.Button(image=gabim,highlightthickness=0,borderwidth=0,command=self.false_pressed)
        self.wrong.grid(row=2,column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.text.config(text=f"Score: {self.quiz.score}")
            self.canva.config(bg="white")
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.question_text,text=q_text)
        else:
            self.canva.config(bg="white")
            self.canva.itemconfig(self.question_text,text=f"You have completed the quiz. Your final score is: {self.quiz.score}")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self,is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000,self.get_next_question)