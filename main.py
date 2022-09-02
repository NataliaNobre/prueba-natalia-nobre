import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Natalia Nobre 
# CI 49746835
# 8 + 3 + 5 = 16

# Instance driver
myDriver = webdriver.Chrome("chromedriver.exe")

# First script to login into user 
myDriver.get("http://localhost:8116")
usuario = myDriver.find_element(By.ID, "user")
usuario.send_keys("root")
contrasenia = myDriver.find_element(By.NAME, "pass")
contrasenia.send_keys("password")
contrasenia.submit()

# Second script to create report
myDriver.get("http://localhost:8116")
myDriver.execute_script('document.querySelector("#CreateTicketInQueue > div.create-wide > input").click()')
text = myDriver.find_element(By.NAME, "Subject")
text.send_keys("Prueba durazno Natalia")
text.submit()
