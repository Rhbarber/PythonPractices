import requests

URL = "http://checkip.dyndns.org"
request = requests.get(URL)
result = request.text.split(': ', 1)[1]
IP = result.split('</body></html>', 1)[0]

print(IP)
