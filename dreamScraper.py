#! python3
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import re

header = {'Accept-Encoding': 'identity, deflate, compress, gzip', 'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0'}
login_url = 'https://deepdreamgenerator.com/login'
gallery_url = 'https://deepdreamgenerator.com/gallery/user/370099'

session_requests = requests.session()

## payload = dictionary containing your email and password for https://deepdreamgenerator.com/login
payload = dict(email="josh@joshsisto.com", password="PASSWORD")

result = session_requests.post(login_url, data = payload, headers = dict(referer = login_url))

result2 = session_requests.get(gallery_url)

#print(result.text)
#print(result2.text)

## https://stackoverflow.com/questions/1080411/retrieve-links-from-web-page-using-python-and-beautifulsoup
http_encoding = result2.encoding if 'charset' in result2.headers.get('content-type', '').lower() else None
html_encoding = EncodingDetector.find_declared_encoding(result2.content, is_html=True)
encoding = html_encoding or http_encoding
soup = BeautifulSoup(result2.content, from_encoding=encoding)

## create empty list
link_list = []
dream_list_list = []

## Find links and append to link_list
for link in soup.find_all('a', href=True):
    link_list.append(link['href'])
    #print(link['href'])

## Save list to file
with open("dreamLinks.txt", "w") as output:
    output.write(str(link_list))

### regular expressions to be used filtering the links
## ddream/[a-z|\d]{10} - https://regex101.com/r/6dl7T5/3
## 370099\?page=[\d] - https://regex101.com/r/eHwPaC/3

#regex_dreams = re.compile(r'ddream/[a-z|\d]{10}')
#regex_pages = re.compile(r'370099\?page=[\d]')

#dream_list = filter(regex_dreams.match, link_list)

#print(dream_list)

print(link_list)
