from selenium import webdriver
import os
import time
link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
name1 ="Abracadabra"
name2 ="Abracadabra"
mail ="Abracadabra"
try:
    driver.get(link)
    driver.find_element_by_css_selector('[name="firstname"]').send_keys(name1)
    driver.find_element_by_css_selector('[name="lastname"]').send_keys(name2)
    driver.find_element_by_css_selector('[name="email"]').send_keys(mail)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "../template.txt"
    file_path = os.path.join(current_dir, file_name)
    driver.find_element_by_css_selector('[name="file"]').send_keys(file_path)
    driver.find_element_by_css_selector('[type="submit"]').click()
finally:
    time.sleep(6)
    driver.quit()