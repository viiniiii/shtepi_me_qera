from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
chrom_driver_path = r"C:\Users\SIEMENS\OneDrive\Desktop\New folder\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
sleep(5)
biskota = driver.find_element(By.ID,"bigCookie")
while True:
    biskota.click()
    nr_bisc = driver.find_element(By.ID,"cookies")
    produkti = driver.find_element(By.ID,"product0")
    if int((nr_bisc.text).split()[0]) > int((produkti.text).split()[1]):
        produkti.click()
    
driver.close()