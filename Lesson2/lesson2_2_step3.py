import os
from selenium import webdriver
import time 

curr_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(curr_dir, 'vor.txt') 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Viktor")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Chlenow")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("pilaf69@yahoo.com")
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла