from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    number = browser.find_element_by_id("input_value")
    function = math.log(abs(12*math.sin(int(number.text))))
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
    input1.send_keys(str(function))
    checkbox = browser.find_element_by_xpath("/html/body/div/form/div[2]/label")
    checkbox.click()
    robots = browser.find_element_by_xpath("/html/body/div/form/div[4]/input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots)
    robots.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
