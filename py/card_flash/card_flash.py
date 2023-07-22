import tkinter
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
#----------------------------------------------------------------------------------------
try:
    data = pandas.read_csv("card_flash\data\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("card_flash\data\_french_words.csv")
finally:
    dict = data.to_dict(orient="records")
max = len(dict)
def to_frech():
    global max
    max = len(dict)
    number = random.randint(0,max-1)
    canva.delete(new_image)
    canva.create_image(400,270,image=old_image)
    global word
    canva.delete(word)
    word = canva.create_text(400,293,text=dict[number]["French"],fill=BACKGROUND_COLOR,font=("Ariel",60,"bold"))
    global language
    canva.delete(language)
    language = canva.create_text(400,133,text="French",fill=BACKGROUND_COLOR,font=("Ariel",40,"italic"))
    window.after(3000,to_english,number)
    return number
def to_french_correct():
    to_remove = to_frech()
    dict.remove(dict[to_remove])
    global max
    max = len(dict)
    new_data = pandas.DataFrame(dict)
    new_data.to_csv("card_flash\data\words_to_learn.csv",index=False)
def to_french_wrong():
    to_frech()
def to_english(number):
    canva.delete(old_image)
    canva.create_image(400,270,image=new_image)
    global word
    canva.delete(word)
    word = canva.create_text(400,293,text=dict[number]["English"],fill="white",font=("Ariel",60,"bold"))
    global language
    canva.delete(language)
    language = canva.create_text(400,133,text="English",fill="white",font=("Ariel",40,"italic"))


#----------------------------------------------UI----------------------------------------
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,width=1000,height=1000)
canva = tkinter.Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
old_image = tkinter.PhotoImage(file="card_flash\images\card_front.png")
new_image = tkinter.PhotoImage(file="card_flash\images\card_back.png")
canva.create_image(400,270,image=old_image)
language = canva.create_text(400,133,text="French",fill=BACKGROUND_COLOR,font=("Ariel",40,"italic"))
word = canva.create_text(400,293,text="word",fill=BACKGROUND_COLOR,font=("Ariel",60,"bold"))
canva.grid(row=0,column=0,columnspan=2,pady=25)

sakt = tkinter.PhotoImage(file="card_flash\images\correct.png")
correct = tkinter.Button(image = sakt, highlightthickness=0, borderwidth=0,command=to_french_correct)
correct.grid(row=1,column=0)

gabim = tkinter.PhotoImage(file="card_flash\images\wrong.png")
wrong = tkinter.Button(image=gabim, highlightthickness=0, borderwidth=0,command=to_french_wrong)
wrong.grid(row=1,column=1)
to_frech()
window.mainloop()