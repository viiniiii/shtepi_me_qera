import tkinter 
window = tkinter.Tk()
window.title("Miles to kilometers converter")
window.minsize(width=500,height=400)
window.config(bg="lightgreen")

kilometers_value = tkinter.Label(text="0")
kilometers_value.config(padx=10,pady=10,fg="blue",bg="lightgreen",font=("Arial",22,"normal"))
kilometers_value.grid(row=0,column=1)

kilometers_text = tkinter.Label(text="kilometers")
kilometers_text.config(padx=10,pady=10,fg="blue",bg="lightgreen",font=("Arial",22,"normal"))
kilometers_text.grid(row=0,column=2)

is_equal_text = tkinter.Label(text="is equal to: ")
is_equal_text.config(padx=10,pady=10,fg="blue",bg="lightgreen",font=("Arial",22,"normal"))
is_equal_text.grid(row=1,column=0)

miles_value = tkinter.Entry(width=30)
miles_value.focus()
miles_value.grid(row=1,column=1)

miles_text = tkinter.Label(text="miles")
miles_text.config(padx=10,pady=10,fg="blue",bg="lightgreen",font=("Arial",22,"normal"))
miles_text.grid(row=1,column=2)

def printo():
    if type(int(miles_value.get())) == int:
        vlera = float(miles_value.get())
        kilometers_value.config(text=vlera/5*8)

convert = tkinter.Button(text="Convert",command=printo)
convert.config(padx=10,pady=10,fg="blue",bg="green",font=("Arial",22,"normal"))
convert.grid(row=2,column=1)


window.mainloop()