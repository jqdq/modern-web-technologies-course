from bs4 import BeautifulSoup as Soup
import lxml
from itertools import groupby
from requests import get as send_get
from pprint import pprint

def retrieve_clues(word):
    found = []
    if " " in word or "-" in word:
        return []
    res = send_get(f"https://krzyzowki123.pl/haslo/{word}")
    assert res.ok
    soup = Soup(res.text, "lxml")
    try:
        tags = soup.find("table", class_="search-results").find_all("a")
    except AttributeError:
        return []
    for i in tags:
        if not i["href"].endswith("/krzyzowka"):
            continue
        found.append(i.text)
    return found

pprint(retrieve_clues("kot"))