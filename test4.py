from selenium import webdriver

# setup a function for webdriver
driver = webdriver.Chrome()

# wait up to 10 secs
driver.implicitly_wait(10)

# open a link
driver.get("https://google.com")
