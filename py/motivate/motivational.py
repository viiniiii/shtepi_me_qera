'''
import smtplib
email = "edvinperfundi21@gmail.com"
password = "iamvxjwtixqdwlct"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email,password=password)
connection.sendmail(from_addr=email,to_addrs="edvinperfumdi@gmail.com",msg="Subject:hello\n\nThis is the body uwu")
connection.close()
'''
import random
import datetime as dt
import smtplib
list = []
date = dt.datetime.now()
dita = date.weekday()
with open("motivate\quotes.txt") as data:
    list = data.read().splitlines()
if dita == 5:
    motivimi = list[random.randint(0,len(list)-1)]
    autori = motivimi[motivimi.index("-")+1:]
    mesazhi = motivimi[:motivimi.index("-")-1]
    email = "edvinperfundi21@gmail.com"
    password = "iamvxjwtixqdwlct"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,to_addrs="edvinperfundi21@gmail.com",msg=f"Subject:{autori}\n\n{mesazhi}")
