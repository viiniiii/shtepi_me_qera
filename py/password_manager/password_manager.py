import tkinter
from tkinter import messagebox 
import random
import json
# ---------------------------- SEARCH DATA ------------------------------- #
def search_webiste():
    try:
        with open("password_manager\passwords_Data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"OPSS",message="Data file does not exist.")
    else:
        web = web_input.get()
        if web in data:
            dict = data[web]
            email = dict["email"]
            password = dict["password"]
            messagebox.showinfo(title=f"{web}",message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title=f"OPSS",message=f"No details for {web} exist.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 3)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_input.delete(0,tkinter.END)
    password_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def enter_data():
    if len(web_input.get()) == 0 or len(web_input.get()) == 0 or len(web_input.get()) == 0:
        messagebox.showinfo(title="Empty fields",message="You left some empty fields! \nPlease enter the required information.")
    else: 
        is_okay = messagebox.askokcancel(title=web_input.get(),message=f"These are the details entered: \nEmail: {username_input.get()} \nPassword: {password_input.get()} \nIs it okay to save? ")
        if is_okay:
            new_data = {
                web_input.get(): {
                    "email": username_input.get(),
                    "password": password_input.get()
                }
            }
            try:
                with open("password_manager\passwords_Data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password_manager\passwords_Data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("password_manager\passwords_Data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                web_input.delete(0,tkinter.END)
                password_input.delete(0,tkinter.END)
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.minsize(width=500,height=500)
window.title("Password manager")
window.config(padx=50,pady=50)

canva = tkinter.Canvas(width=200,height=200,highlightthickness=0)
image = tkinter.PhotoImage(file="password_manager\password_manager.png")
canva.create_image(100,100,image=image)
canva.grid(row=0,column=1)

web = tkinter.Label(text="Website:",pady=10)
web.grid(row=1,column=0)

web_input = tkinter.Entry(width=17)
web_input.grid(row=1,column=1,padx=10)
web_input.focus()

search = tkinter.Button(text="Search",command=search_webiste,width=14)
search.grid(row=1,column=2,sticky="EW")

username = tkinter.Label(text="Email/Username:",pady=10)
username.grid(row=2,column=0)

username_input = tkinter.Entry(width=35)
username_input.insert(0,"edvinperfundi21@gmail.com")
username_input.grid(row=2,column=1,columnspan=2,padx=10)

password = tkinter.Label(text="Password:",pady=10)
password.grid(row=3,column=0)

password_input = tkinter.Entry(width=17)
password_input.grid(row=3,column=1)

password_generate = tkinter.Button(text="Generate Password",command=generate_password)
password_generate.grid(row=3,column=2,sticky="EW")

add = tkinter.Button(text="Add",width=30,command=enter_data)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()