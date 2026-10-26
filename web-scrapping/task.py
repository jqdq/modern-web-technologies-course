import requests
import bs4

response = requests.get("http://books.toscrape.com/catalogue/i-had-a-nice-time-and-other-lies-how-to-find-love-sht-like-that_814/index.html")
if response.ok: 
    content = response.text
    soup = bs4.BeautifulSoup(content, 'lxml')
    title = soup.find('h1').text
    price = soup.find('p', class_='price_color').text
    description = soup.find('div', id="product_description").find_next_sibling('p').text
    print(title)
    print(price)
    print(description)
else:
    print(response.status_code)

response = requests.get("https://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html")
if response.ok: 
    content = response.text
    soup = bs4.BeautifulSoup(content, 'lxml')
    link = soup.find('a').get('href')
    print(link)
else:
    print(response.status_code)
    
# Zadanie:
# books.toscrape.com
# Skrypt zbierający z trzech kategorii:
# - Tytuł
# - Cenę
# - Opis
# Wszystkich książek