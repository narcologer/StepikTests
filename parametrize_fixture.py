import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_answer_should_be_correct(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    time.sleep(5)
    input1 = browser.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[4]/button")
    button.click()
    time.sleep(3)
    congrats = browser.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div[1]/div[2]/div/pre")
    assert congrats.text=="Correct!", congrats.text
