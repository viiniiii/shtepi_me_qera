import pandas
import random
import smtplib
import datetime as dt

def get_person_by_birthday(month, day):
    df = pandas.read_csv('automatic_birthday_wisher\_birthdays.csv')
    matching_rows = df[(df['month'] == month) & (df['day'] == day)]
    if len(matching_rows) > 0:
        name = matching_rows.iloc[0]['name']
        email = matching_rows.iloc[0]['email']
        return name, email
    else:
        return None
date = dt.datetime.now()
dita = date.day
muaji = date.month
name,posta = get_person_by_birthday(muaji,dita)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
number = random.randint(0,2)
if number == 0:
    with open(file="automatic_birthday_wisher\letter_templates\letter_1.txt") as letter:
        letra = letter.read()
        letra = letra.replace("[NAME]",name)
elif number == 1:
    with open(file="automatic_birthday_wisher\letter_templates\letter_2.txt") as letter:
        letra = letter.read()
        letra = letra.replace("[NAME]",name)
elif number == 2:
    with open(file="automatic_birthday_wisher\letter_templates\letter_3.txt") as letter:
        letra = letter.read()
        letra = letra.replace("[NAME]",name)
email = "edvinperfundi21@gmail.com"
password = "iamvxjwtixqdwlct"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs=posta,msg=f"Subject:Happy birthday\n\n{letra}")



