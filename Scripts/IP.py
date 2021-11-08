import requests

URL = "https://checkip.amazonaws.com/"
IP = requests.get(URL).text

print(IP.replace('\n',''))
