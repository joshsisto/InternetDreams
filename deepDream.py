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
time.sleep(3)
password_field.submit()

time.sleep(15)

if __name__ == '__main__':

    while True:

        ## random style and image
        dream_images = os.listdir(r'C:\dream\dream_image')
        random_image = random.choice(dream_images)
#        dream_styles = os.listdir(r'C:\dream\dream_style')
#        random_style = random.choice(dream_styles)

        # click Deep Style on the menu. https://deepdreamgenerator.com/generator-style
        linkElem = browser.find_element_by_link_text('Deep Dream').click()

        time.sleep(5)

        ### settings
        # click the settings drop down menu
        browser.find_element_by_link_text("Settings").click()

        time.sleep(5)

        # choose a random dream type
        random_type = random.choice(range(4))
        if random_type == int(0):
            browser.find_element_by_xpath("(//input[@name='type'])[2]").click()
        elif random_type == int(1):
            browser.find_element_by_xpath("(//input[@name='type'])[2]").click()
        elif random_type == int(2):
            browser.find_element_by_xpath("(//input[@name='type'])[2]").click()
        else:
            print('not using any dream type')

        ## resolution
        # normal
#        browser.find_element_by_xpath("(//input[@name='resolution'])[2]").click()
        # medium
        browser.find_element_by_xpath("(//input[@name='resolution'])[3]").click()
        # full HD
#        browser.find_element_by_xpath("(//input[@name='resolution'])[4]").click()

        ## inception depth
        # normal - comment out (#deep) for normal
        # deep
        browser.find_element_by_xpath("(//input[@name='depth'])[2]").click()

        ## click the layer area and choose a random layer
        browser.find_element_by_name("layer").click()
        random_layer = random.choice(range(9))
        if random_layer == int(0):
            browser.find_element_by_xpath("(//input[@name='layer'])[2]").click()
        elif random_layer == int(1):
            browser.find_element_by_xpath("(//input[@name='layer'])[3]").click()
        elif random_layer == int(2):
            browser.find_element_by_xpath("(//input[@name='layer'])[4]").click()
        elif random_layer == int(3):
            browser.find_element_by_xpath("(//input[@name='layer'])[5]").click()
        elif random_layer == int(4):
            browser.find_element_by_xpath("(//input[@name='layer'])[6]").click()
        elif random_layer == int(5):
            browser.find_element_by_xpath("(//input[@name='layer'])[7]").click()
        elif random_layer == int(6):
            browser.find_element_by_xpath("(//input[@name='layer'])[8]").click()
        elif random_layer == int(7):
            browser.find_element_by_xpath("(//input[@name='layer'])[9]").click()
        elif random_layer == int(8):
            browser.find_element_by_xpath("(//input[@name='layer'])[10]").click()

        time.sleep(5)

        # change from private to public
        browser.find_element_by_xpath("(//input[@name='access'])[2]").click()

        time.sleep(5)

        ## upload dream image from file location and submit
        elem_xpath = browser.find_element_by_xpath('//input[@type=\'file\']')
        elem_xpath.send_keys('C:\\dream\\dream_image\\%s' % (random_image))
        elem_xpath.submit()

        time.sleep(120)    # wait 2 minutes

        ## click go deeper and submit 3 times
        for x in range(0, 3):
            browser.find_element_by_xpath("//a[3]/span").click()
            time.sleep(5)
            browser.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(90)

        time.sleep(30)   # wait for it to process and repeat
