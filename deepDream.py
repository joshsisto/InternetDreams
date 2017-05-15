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
email_field.send_keys('joshsisto@gmail.com')   # Email account used
password_field.send_keys('forjosh1')     # Password for account
password_field.submit()

time.sleep(3)

if __name__ == '__main__':

    while True:

        ## random style and image
        dream_images = os.listdir(r'C:\dream\dream_image')
        random_image = random.choice(dream_images)
#        dream_styles = os.listdir(r'C:\dream\dream_style')
#        random_style = random.choice(dream_styles)

        # click Deep Style on the menu. https://deepdreamgenerator.com/generator-style
        linkElem = browser.find_element_by_link_text('Deep Dream').click()

        time.sleep(3)

        ### settings
        # click the settings drop down menu
        browser.find_element_by_link_text("Settings").click()

        time.sleep(3)

        ## dream type - no change for default
        # spirits
#        browser.find_element_by_xpath("(//input[@name='type'])[2]").click()
        # neuron
#        browser.find_element_by_xpath("(//input[@name='type'])[3]").click()
        # valyrian
#        browser.find_element_by_xpath("(//input[@name='type'])[4]").click()
        # use your own

        ## resolution
        # normal
#        browser.find_element_by_xpath("(//input[@name='resolution'])[2]").click()
        # medium
        browser.find_element_by_xpath("(//input[@name='resolution'])[3]").click()
        # full HD
#        browser.find_element_by_xpath("(//input[@name='resolution'])[4]").click()

        ## inception depth
        # normal (no change)
        # deep
        browser.find_element_by_xpath("(//input[@name='depth'])[2]").click()


        ## neural network layer
        browser.find_element_by_name("layer").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[2]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[3]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[4]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[5]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[6]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[7]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[8]").click()
        browser.find_element_by_xpath("(//input[@name='layer'])[9]").click()
        # browser.find_element_by_xpath("(//input[@name='layer'])[10]").click()

        time.sleep(3)

        # change from private to public
        browser.find_element_by_xpath("(//input[@name='access'])[2]").click()

        time.sleep(3)

        ## Upload dream image from file location and submit
        elem_xpath = browser.find_element_by_xpath('//input[@type=\'file\']')
        elem_xpath.send_keys('C:\\dream\\dream_image\\%s' % (random_image))
        elem_xpath.submit()

        time.sleep(180)    # wait 3 minutes

        # click 'GO DEEPER'
        browser.find_element_by_xpath("//a[3]/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(180)  # wait 3 minutes

        # click 'GO DEEPER'
        browser.find_element_by_xpath("//a[3]/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(180)  # wait 3 minutes

        # click 'GO DEEPER'
        browser.find_element_by_xpath("//a[3]/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(180)  # wait 3 minutes

        # click 'GO DEEPER'
        browser.find_element_by_xpath("//a[3]/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(180)  # wait 3 minutes

        # click 'GO DEEPER'
        browser.find_element_by_xpath("//a[3]/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(180)  # wait 3 minutes

        # click 'GO DEEPER'
        browser.find_element_by_xpath("//a[3]/span").click()
        time.sleep(5)
        browser.find_element_by_xpath("//button[@type='submit']").click()

        # wait for it to process and repeat
        time.sleep(30)
