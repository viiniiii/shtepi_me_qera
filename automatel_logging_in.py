from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from time import sleep
chrom_driver_path = r"C:\Users\SIEMENS\OneDrive\Desktop\New folder\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
emri = driver.find_element(By.NAME,"fName")
emri.send_keys("Edvin")
mbiemri = driver.find_element(By.NAME,"lName")
mbiemri.send_keys("Perfundi")
email = driver.find_element(By.NAME,"email")
email.send_keys("edvinperfundi21@gmail.com")
button = driver.find_element(By.CSS_SELECTOR,"form button")
sleep(1)
button.click()
sleep(5)
driver.close()