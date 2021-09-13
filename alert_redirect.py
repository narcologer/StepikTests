from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("body > form > div > div > button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    number = browser.find_element_by_id("input_value")
    function = math.log(abs(12*math.sin(int(number.text))))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(function))
    button = browser.find_element_by_css_selector("body > form > div > div > button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
