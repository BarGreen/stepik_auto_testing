from cgitb import text
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    x = int(x_element.text)
    y_element = browser.find_element_by_id('num2')
    y = int(y_element.text)
    
    z = x + y

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))

    button = browser.find_element_by_tag_name('button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла