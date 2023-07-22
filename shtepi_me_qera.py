from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import requests
URL2 = "https://docs.google.com/forms/d/e/1FAIpQLSfab_2YvbjGJbsi1EPqGYlxhCywwG_EpMK5GGDCZ0Gv00fiOA/viewform?usp=sf_link"
driver = webdriver.Chrome()
for i in range(1,15):
    #URL = f"https://www.gazetacelesi.al/njoftime-rezultate/prona-te-patundshme/garsoniere-1-1?cm=57;58&page={i}&action=ME%20QERA&tdv=P&dv=Tiran%C3%AB&currency=leke&address=Tregu%20elektrik&landmark=Tregu%20elektrik"
    URL = f"https://www.gazetacelesi.al/njoftime-rezultate/prona-te-patundshme/garsoniere-1-1?cm=57;58&page={i}&action=ME%20QERA&tdv=P&dv=Tiran%C3%AB"
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

    
    for a,b,c in zip(siperfaqet,cmimet,linqet):

        driver.get(URL2)
        el = driver.find_elements(By.CSS_SELECTOR,".Xb9hP input")

        el1,el2,el3 = el

        dorzo = driver.find_element(By.CSS_SELECTOR,".ThHDze .UQuaGc.Y5sE8d.VkkpIf.QvWxOd")
        el1.send_keys(a)
        el2.send_keys(b)
        el3.send_keys(c)

        dorzo.click()

driver.quit()