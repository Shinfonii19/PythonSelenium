from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# open Chrome
driver = webdriver.Chrome()

# open a website (you can use your local project here)
driver.get("http://localhost/parkingsystem/login.php")

# wait 3 seconds
time.sleep(5)

# print title
print("Page title is:", driver.title)

# close browser
driver.quit()
