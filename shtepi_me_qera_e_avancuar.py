from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup
import requests
import smtplib

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

URL = f"https://www.gazetacelesi.al/njoftime-rezultate/prona-te-patundshme/garsoniere-1-1?page=1&cm=57;58&tdv=P&dv=Tiran%C3%AB&action=ME%20QERA&pricef=[0%20TO%2027000]&currency=leke"
response = requests.get(URL)
sleep(0.1)
web_html = response.text
sleep(0.1)
soup = BeautifulSoup(web_html,"html.parser")
sleep(0.1)
linqet = soup.select(selector=".testo-annuncio a")
sleep(0.1)
linqet = [i.get("href") for i in linqet]
cmimet = soup.select(selector=".testo-annuncio b")
sleep(0.1)
cmimet = [j.getText() for j in cmimet]
vlera = [k.split()[len(k.split())-2] for k in cmimet]
njesia = [k.split()[len(k.split())-1] for k in cmimet]
sip = [k.split()[len(k.split())-5] for k in cmimet]
madhesia = [k.split()[len(k.split())-4] for k in cmimet]
cmimet = [x + " " + y for x, y in zip(vlera, njesia)]
siperfaqet = [x + " " + y for x, y in zip(sip, madhesia)]

i = 1
list = []
for a,b,c in zip(siperfaqet,cmimet,linqet):
    list.append(f"{i}.  {a} --- {b}  {c}")
    i += 1 
driver.quit()
list_str = "\n".join(list)
email = "edvinperfundi21@gmail.com"
password = "iamvxjwtixqdwlct"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs="edvinperfundi21@gmail.com",msg=f"Shtepi me qera\n\n{list_str}")
