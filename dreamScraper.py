
import requests
from lxml import html
header = {'Accept-Encoding': 'identity, deflate, compress, gzip', 'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0'}
login_url = 'https://deepdreamgenerator.com/login'
gallery_url = 'https://deepdreamgenerator.com/gallery/user/370099'

session_requests = requests.session()
result = session_requests.get(login_url)
tree=html.fromstring(result.text)
auth_token = list(set(tree.xpath('//*[@name="login[_token]"]/@value')))
auth_iovat = list(set(tree.xpath('//*[@name="login[iovation]"]/@value')))
# create payload
payload = {
    "email": "josh@joshsisto.com",
    "password": "<PASSWORD>",
    "login[_token]": auth_token,
        "login[iovation]": auth_iovat,
        "login[redir]": "/gallery/user/370099"
}

#perform login
result=session_requests.post(login_url, data = payload, headers = dict(referer = login_url))

#test the result
#print(result.text)


session_requests2 = requests.session()
result2 = session_requests.get(gallery_url)
tree=html.fromstring(result2.text)

result2=session_requests.get(gallery_url)

print(result2.text)
