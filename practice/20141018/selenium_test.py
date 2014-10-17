from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# http://selenium-python.readthedocs.org/en/latest/getting-started.html
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
print driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()