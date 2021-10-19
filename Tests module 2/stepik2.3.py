from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
link = "http://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()
try:
    driver.get(link)
    select = Select(driver.find_element_by_tag_name("select"))
    num1 = driver.find_element_by_id('num1').text
    num2 = driver.find_element_by_id('num2').text
    x = int(num1)
    y = int(num2)
    result = x + y
    select.select_by_visible_text(str(result))
    button = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(6)
    driver.quit()