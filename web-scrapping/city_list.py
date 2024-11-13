import requests
from bs4 import BeautifulSoup

url = "https://pl.wikipedia.org/wiki/Dane_statystyczne_o_miastach_w_Polsce"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "lxml")
table_text = soup.select_one("table.wikitable").get_text()
# Note how this is equivalent to the JS querySelector method:
# document.querySelector("table.wikitable").text()

print(table_text)
