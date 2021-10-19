from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    driver.find_element_by_css_selector('[type="submit"]').click()
    driver.switch_to.alert.accept()
    x = driver.find_element_by_css_selector('[id="input_value"]').text
    y = calc(x)
    box = driver.find_element_by_css_selector('[name="text"]').send_keys(y)
    driver.find_element_by_css_selector('[class="btn btn-primary"]').click()
    alert = driver.switch_to.alert
    alert_txt = alert.text
    a = alert_txt.split(': ')[-1]
    print(a)
    alert.accept()
finally:
    time.sleep(3)
    driver.quit()