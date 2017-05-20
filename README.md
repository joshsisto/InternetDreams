Python 3.6 Selenium 3.4.2 https://github.com/SeleniumHQ/Selenium

Images generated can be viewed here https://deepdreamgenerator.com/gallery/user/370099
# InternetDreams
dream.py is a Python 3 script that uses the selenium package to automate the firefox web browser and submit images to the https://deepdreamgenerator.com/. The script first logs into the site and enters the username and password (you need to fill out these fields with your credentials). After the script logs in it grabs a random image and style from a local folder on the C drive. It then clicks the link on the home page 'Deep Style' https://deepdreamgenerator.com/generator-style. It then uploads a style image to be used and clicks the settings drop down menu for more options. In the additional settings the 'Preserve Image Color' is randomly selected and the image is made public. Lastly it uploads the main image to be used and submits it. The script waits 6 minutes and repeats.

deepDream.py is a Python 3 script that uses the selenium package to automate the firefox web browser and submit images to the https://deepdreamgenerator.com/. The script first logs into the site and enters the username and password (you need to fill out these fields with your credentials). After the script logs in it chooses a random image from a local folder on the C drive and clicks the 'Deep Dream' link https://deepdreamgenerator.com/generator. It then hits the settings drop down menu and chooses random settings and submits the image. After the image has uploaded it selects the 'Go Deeper' option 3 times and then repeats the process with a new random image. 

You need to download the Mozilla Gecko Driver https://github.com/mozilla/geckodriver/releases and point to the .exe in your script. In the script used the driver was located C:\dream\geckodriver.exe

Download gecko driver - https://github.com/mozilla/geckodriver/releases
Place gecko driver here C:\dream\geckodriver.exe

Dream image directory used C:\dream\dream_image
Dream style directory used C:\dream\dream_image
