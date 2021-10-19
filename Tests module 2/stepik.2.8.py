from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    driver.get(link)
    button = WebDriverWait(driver,15).until(EC.text_to_be_present_in_element((By.ID,"price"),'100'))
    driver.find_element_by_css_selector('[id="book"]').click()
    driver.execute_script("window.scrollBy(0, 300);")
    x = driver.find_element_by_id("input_value").text
    y = calc(x)
    box = driver.find_element_by_id('answer').send_keys(y)
    driver.find_element_by_id('solve').click()
    alert = driver.switch_to.alert
    alert_txt = alert.text
    a = alert_txt.split(': ')[-1]
    print(a)
    alert.accept()
finally:
    driver.quit()
