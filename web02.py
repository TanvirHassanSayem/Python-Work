import requests

from bs4 import BeautifulSoup

url="https://www.codewithharry.com/"

r=requests.get(url)

wokring1=r.content

#web scrapping code  with harry
soup= BeautifulSoup(wokring1 , 'html.parser')

print(soup.prettify())

