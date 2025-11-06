from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup a function for webdriver
driver = webdriver.Chrome()

# open a link
driver.get("https://the-internet.herokuapp.com/login")

# wait up to 10 secs until its ready
wait = WebDriverWait(driver, 10)

# Wait for username field
username_box = wait.until(
    EC.visibility_of_element_located((By.ID, "username")))
password_box = driver.find_element(By.ID, "password")

login_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button.radius")))

# Type and submit
username_box.send_keys("tomsmith")
password_box.send_keys("SuperSecretPassword!")
login_button.click()

# Wait until success message appears
wait.until(EC.text_to_be_present_in_element(
    (By.ID, "flash"), "You logged into a secure area!"))

print("Login test completed!")
driver.quit()
