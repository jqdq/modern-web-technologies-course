# To już niestety nie działa, tekstowo.pl chyba zmieniło stronę.
import requests
from bs4 import BeautifulSoup

listaglowna = []
adres = 'https://www.tekstowo.pl/piosenki_artysty,bajm'
n=0

# Pobieranie listy utworów
while True:
    n+=1

    # Pobieranie strony z listą utworów
    strona = requests.get(adres)
    # Parsowanie strony
    drzewunio=BeautifulSoup(strona.content, 'lxml')
    print("Rozpoczynam przeszukiwanie strony",n)

    # Pobieranie linków do utworów
    listazaznaczen = drzewunio.find('div', class_ = 'ranking-lista').find_all('a', class_ = 'title')
    listaglowna.extend(listazaznaczen) # Tutaj dodajemy do listy obiekty typu 'a' zawierające linki do utworów
    
    # Sprawdzanie czy jest następna strona listy utworów
    nastepna = drzewunio.find('div', class_='padding').find_all('a', title='Następna >>')
    if nastepna!=[]:
        adres = "https://www.tekstowo.pl"+nastepna[0]['href']
    else:
        break

# Mapowanie listy obiektów a na słownik {tytuł utworu:link}
listalinkow=dict()
for i in listaglowna:
    listalinkow[i.string]='https://www.tekstowo.pl'+i['href']
print("Zakończono zbieranie linków")

utwory = []
for i in listalinkow:
    # Pobieranie tekstu piosenki
    print("Pobieranie tekstu",i)
    stronka=requests.get(listalinkow[i])
    # Parsowanie strony i znalezienie fragmentu z utworem
    wybrana_tekst = BeautifulSoup(stronka.content, 'lxml').find('div', class_='song-text')
    lista = str(wybrana_tekst).splitlines()
    utwory.append({"tytul":i,"tekst":lista})
    