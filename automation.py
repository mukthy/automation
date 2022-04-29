import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

time.sleep(2)

pop_button = chrome_browser.find_element(by=By.CLASS_NAME, value='at-cm-no-button')
print(pop_button.get_attribute('innerHTML'))
pop_button.click()

input_txt = chrome_browser.find_element(by=By.ID, value='user-message')
input_txt.clear()
input_txt.send_keys('Mukthy')

time.sleep(1)

show_message = chrome_browser.find_element(by=By.CLASS_NAME, value='btn-default')
show_message.click()

print_message = chrome_browser.find_element(by=By.ID, value='display')
print(print_message.get_attribute('innerHTML'))
