#! python3
import requests

header = {'Accept-Encoding': 'identity, deflate, compress, gzip', 'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0'}
login_url = 'https://deepdreamgenerator.com/login'
gallery_url = 'https://deepdreamgenerator.com/gallery/user/370099'

session_requests = requests.session()

## payload = dictionary containing your email and password for https://deepdreamgenerator.com/login
payload = dict(email="joshsisto@gmail.com", password="forjosh1")

result = session_requests.post(login_url, data = payload, headers = dict(referer = login_url))

result2 = session_requests.get(gallery_url)

print(result.text)
print(result2.text)
