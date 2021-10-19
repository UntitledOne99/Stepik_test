from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    x_element = driver.find_element_by_css_selector('[id="input_value"]').text
    y = calc(x_element)
    box = driver.find_element_by_css_selector('[id="answer"]').send_keys(y)
    driver.execute_script("window.scrollBy(0, 200);")
    checkbox = driver.find_element_by_css_selector('[id="robotCheckbox"]').click()
    radioButton = driver.find_element_by_css_selector('[id="robotsRule"]').click()
    button = driver.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(6)
    driver.quit()