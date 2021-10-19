from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    box = driver.find_element_by_id("answer")
    x_element = driver.find_element_by_id('treasure')
    treasure = x_element.get_attribute('valuex')
    y = calc(treasure)
    box.send_keys(y)
    checkbox = driver.find_element_by_css_selector('[id="robotCheckbox"]')
    checkbox.click()
    radiobutton = driver.find_element_by_css_selector('[id="robotsRule"]').click()
    submittion = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(6)
    driver.quit()