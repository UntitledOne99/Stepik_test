from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    driver.find_element_by_css_selector('[type="submit"]').click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x = driver.find_element_by_css_selector('[id="input_value"]').text
    y = calc(x)
    box = driver.find_element_by_css_selector('[id="answer"]').send_keys(y)
    driver.find_element_by_css_selector('[type="submit"]').click()
    alert = driver.switch_to.alert
    alert_txt = alert.text
    a = alert_txt.split(': ')[-1]
    print(a)
    alert.accept()

finally:
    time.sleep(2)
    driver.quit()