from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# This is driver browser (like a function)
driver = webdriver.Chrome()

# It will open based on the url that you enter
driver.get("http://localhost/parkingsystem/login.php")

# delay with 5 secs
time.sleep(5)

# get the title and stores it into the variable
title = driver.title

print("Page title is: ", driver.title)
# if the title is equal to Login that you get, it will output Correct title
if title == "Login":
    print("Correct title")
else:
    print("Wrong Title")

driver.quit()
