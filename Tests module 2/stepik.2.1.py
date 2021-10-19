from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    box = driver.find_element_by_xpath('//*[@id="answer"]')
    x_element = driver.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    box.send_keys(y)
    checkbox = driver.find_element_by_css_selector('[class="form-check-label"]')
    checkbox.click()
    radiobutton =driver.find_element_by_css_selector('[for="robotsRule"]').click()
    submittion = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(60)
    driver.quit()