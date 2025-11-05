from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# setup the webdriver
driver = webdriver.Chrome()

# open a url link
driver.get("https://www.google.com")

# search a input text field
search_box = driver.find_element(By.NAME, "q")

# enter a text
search_box.send_keys("Selenium Python")
# submit
search_box.submit()


# alternative since it enters a text and submit at the same time
# search_box.send_keys("Ado" + Keys.RETURN)


# delay
time.sleep(15)
print("Page title after search: ", driver.title)

driver.quit()
