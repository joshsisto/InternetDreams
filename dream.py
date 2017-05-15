#! python3
import time
from selenium import webdriver
import os
import random

# open browser using gecko driver provided by Mozilla. https://github.com/mozilla/geckodriver/releases
browser = webdriver.Firefox(executable_path=r'C:\dream\geckodriver.exe')
type(browser)
browser.get('https://deepdreamgenerator.com/login')
# error check
try:
    elem = browser.find_element_by_class_name('page-login')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Error did not find element. Are you opening the correct page?')

## Login to https://deepdreamgenerator.com/login
email_field = browser.find_element_by_name('email')
password_field = browser.find_element_by_name('password')
email_field.send_keys('josh@joshsisto.com')   # Email account used
password_field.send_keys('Your Password')     # Password for account
password_field.submit()

## random style and image
dream_images = os.listdir(r'C:\dream\dream_image')
random_image = random.choice(dream_images)
dream_styles = os.listdir(r'C:\dream\dream_style')
random_style = random.choice(dream_styles)

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
browser.find_element_by_id('style-image').send_keys('C:\\dream\\dream_style\\%s' % (random_style))

time.sleep(3)

## settings
# click the settings drop down menu
browser.find_element_by_link_text("Settings").click()

time.sleep(3)

# change resolution from 'Normal' to 'Medium'
#browser.find_element_by_xpath("(//input[@name='resolution'])[2]").click()
# click 'Preserve Original Color'
#browser.find_element_by_xpath("(//input[@name='preserveOriginalColors'])[2]").click()
# change from private to public
browser.find_element_by_xpath("(//input[@name='access'])[2]").click()
# randomly click 'Preserve Original Color'
AorB = random.choice('ab')
print(AorB)
if AorB == ('a'):
    browser.find_element_by_xpath("(//input[@name='preserveOriginalColors'])[2]").click()

time.sleep(3)

## Upload dream image from file location and submit
elem_xpath = browser.find_element_by_xpath('//input[@type=\'file\']')
elem_xpath.send_keys('C:\\dream\\dream_image\\%s' % (random_image))
elem_xpath.submit()

browser.close()
