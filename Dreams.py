from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

browser = webdriver.Firefox(executable_path=r'C:\GD\geckodriver.exe')
type(browser)
browser.get('https://deepdreamgenerator.com/login')

try:
    elem = browser.find_element_by_class_name('page-login')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Error did not find element.')

browser.implicitly_wait(10)
#browser.maximize_window()


email_field = browser.find_element_by_name('email')
password_field = browser.find_element_by_name('password')
email_field.send_keys('josh@joshsisto.com')
password_field.send_keys('password')
password_field.submit()

browser.close()
