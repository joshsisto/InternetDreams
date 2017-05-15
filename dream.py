#! python3
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Open browser using gecko driver provided by Mozilla. https://github.com/mozilla/geckodriver/releases
browser = webdriver.Firefox(executable_path=r'C:\dream\geckodriver.exe')
type(browser)
browser.get('https://deepdreamgenerator.com/login')

try:
    elem = browser.find_element_by_class_name('page-login')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Error did not find element. Are you opening the correct page?')

## Login to https://deepdreamgenerator.com/login
email_field = browser.find_element_by_name('email')
password_field = browser.find_element_by_name('password')
email_field.send_keys('joshsisto@gmail.com')   # Email account used
password_field.send_keys('forjosh1')          # Password for account
password_field.submit()

time.sleep(3)

# click Deep Style on the menu. https://deepdreamgenerator.com/generator-style
linkElem = browser.find_element_by_link_text('Deep Style')
linkElem.click()

time.sleep(3)

## add style image
# click 'Upload Your Own'
browser.find_element_by_xpath("//div[@id='collapse-styles']/div/div/div/div[2]/label/div/i").click()
# Add style image
browser.find_element_by_id('style-image').clear()
browser.find_element_by_id('style-image').send_keys(r'C:\dream\dream_style\circuit2.jpg')

time.sleep(3)

## Upload dream image from file location and submit
elem_xpath = browser.find_element_by_xpath('//input[@type=\'file\']')
elem_xpath.send_keys(r'C:\dream\dream_image\trump1.jpg')
elem_xpath.submit()

browser.close()
