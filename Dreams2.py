import time
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
password_field.send_keys('')
password_field.submit()

# click Deep Style on the menu
linkElem = browser.find_element_by_link_text('Deep Style')
linkElem.click()

time.sleep(3)

# Click Upload Your Own
browser.find_element_by_xpath("//div[@id='collapse-styles']/div/div/div/div[2]/label/div/i").click()
# Click the Browse... button and then upload image
browser.find_element_by_id("style-image").click()
#elem_xpath2 = browser.find_element_by_xpath("//input[@type='file']")
#elem_xpath2.send_keys('C:\\Users\\joshs\\Pictures\\dream_style\\fractal.jpg')
#elem_xpath2.submit()



###########################
browser.find_element_by_id("style-image").clear()
browser.find_element_by_id("style-image").send_keys("C:\\Users\\joshs\\Pictures\\dream_style\\circuit.jpg")
browser.find_element_by_id("style-image").clear()
browser.find_element_by_id("style-image").send_keys("C:\\Users\\joshs\\Pictures\\dream_style\\circuit.jpg")
###########################







#linkElem3 = browser.find_element_by_id('upload-style-image')
#linkElem3.click()

#linkElem4 = browser.find_element_by_id('style-image')
#linkElem4.click()


# click UPLOAD IMAGE button
linkElem2 = browser.find_element_by_id('image-for-dream')
linkElem2.click()
# Uploads file from location and submits
elem_xpath = browser.find_element_by_xpath("//input[@type='file']")
elem_xpath.send_keys('C:\\Users\\joshs\\Pictures\\dream_image\\eye.jpg')
elem_xpath.submit()



browser.close()
