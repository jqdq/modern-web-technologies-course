import requests, bs4
from pprint import pprint

books = []  # lista dictów z tytułem, ceną i opisem

main_page_request = requests.get("https://books.toscrape.com/")
if not main_page_request.ok:
    print("Nie udało się pobrać strony")
else:
    main_page_text = main_page_request.text
    main_page_soup = bs4.BeautifulSoup(main_page_text)
    articles = main_page_soup.find_all("li", class_="col-xs-6")
    for i in articles:
        # wchodzimy na strony ze szczegółami
        href = next(i.find("h3").children).get("href")
        full_path = "https://books.toscrape.com/" + href
        details_request = requests.get(full_path)
        if not details_request.ok:
            print("Nie udało się zebrać:", href)
            continue

        # Parsujemy stronę
        details_page = bs4.BeautifulSoup(details_request.text)
        title = details_page.select_one("h1").text
        description = details_page.select_one("article > p").text

        # Wydobywamy co chcemy
        books.append(
            {
                "href": href,
                "title": title,
                "description": description,
                "price": float(
                    i.find("p", class_="price_color").text.replace("Â£", "")
                ),
            }
        )

pprint(books)
