from selenium import webdriver

# setup a function for webdriver
driver = webdriver.Chrome()

# wait up to 10 secs
driver.implicitly_wait(10)

# open a link
driver.get("https://google.com")

# finding a element with a value of 'q' on the name (name = q)
search_box = driver.find_element("name", "q")

# sending a keys, value or text
search_box.send_keys("Selenium waits example")
