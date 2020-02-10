import requests
from bs4 import BeautifulSoup as BS

with open("1.wav", 'rb') as file:
    url = "http://127.0.0.1:8000/api/audio/"
    r = requests.post(url, files={"1.wav":file})
    html = BS(r.content, 'html.parser')
    print(r.content)
