# Ethically scraping books

## Running the project

1. Download the repository (using git or unpack the zip)
2. Open the `web-scrapping` folder in VS Code:
   1. Open the File menu
   2. Click on "Open folder..."
   3. Find the course directory (usually named `modern-web-technologies-main`)
   4. Select the `web-scrapping` folder inside it
3. Install the dependencies using `pip install requests beautifulsoup4 lxml`.
4. Ensure you have the `web-scrapping` folder opened in your terminal (the path should contain `modern-web-technologies-main/web-scrapping`).
5. Verify the installation with `python -c "import requests, bs4, lxml"` - if it prints nothing, you're good to go.

## Docs

- [Requests](https://requests.readthedocs.io/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Beautiful Soup: CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) - the exact section about `select()`/`select_one()`
- [MDN: CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors) - the full reference (classes, ids, nesting, `+`, `>`, attributes...)
- [CSS Diner](https://flukeout.github.io/) - a small game for practicing selectors, the best way to internalize the syntax
- [Selenium with Python](https://selenium-python.readthedocs.io/)
- [Playwright for Python](https://playwright.dev/python/) - the modern alternative to Selenium

## What's in this folder

Real-life examples to poke at - each one is a working (or formerly working) scraper:

- `city_list.py` - pulls text of a Wikipedia table about Polish cities.
- `crossword_clues.py` - fetches crossword clues for a given word from `krzyzowki123.pl`. Shows a slightly bigger workflow: fetch -> parse a table -> filter links by their `href` -> collect results, plus graceful handling of pages where the table doesn't exist.
- `bajmblog.py` - scrapes all Bajm lyrics from `tekstowo.pl`, following the *next page* links across many listing pages. It no longer works, but it's a good example of handling pagination in scrapers.
- `selenium-example.py` - automates a real Chrome browser (opens DuckDuckGo, searches, reads the results). Use this approach (or Playwright) when the content is rendered by JavaScript; otherwise Requests + Beautiful Soup is faster and simpler.
- `website-observer.js` - not Python at all: a Google Apps Script that periodically checks a website's content (via an MD5 digest), and emails you when it changes. It was very useful when i tried to get tickets for an event. Shows that "scraping" is the same concept regardless of the language or platform: fetch, compare, notify.
- `imgw-warnings.pdf` - a writeup of an IMGW weather-warnings project: turning Polish weather warnings published as PDFs into a JSON API (written in R). Data comes in much worse formats than HTML.

## Tasks for today

**Our goal:** write a script that starts at the main page of `books.toscrape.com` - a fake bookstore built specifically for practicing web scraping - crawls it, and then visits every book's details page to collect data (title, price, description). 

1. Fetch a page with `requests`:
   ```python
   response = requests.get(url)
   ```
   Always check `response.ok` (or `response.status_code`) before parsing.
2. Build the Soup. Hand the HTML to Beautiful Soup and pick a parser (parser is the library that will rewrite the HTML into a tree):
   ```python
   soup = bs4.BeautifulSoup(response.text, 'lxml')
   ```
3. Open the main page's HTML in devtools (F12): every book lives in its own `<article class="product_pod">`. Grab **all** of them and loop over the listing:
   ```python
   for book in soup.find_all('article', class_='product_pod'):
       ...
   ```
4. Extract the data from each listing entry. The price is a `p` with a class (`class_`, the underscore matters, `class` is a Python keyword). And note the *title*: it's truncated in the listing text (e.g. "...How to Find Love S**t Like That"), so the full one hides in the link's `title` **attribute**:
   ```python
   price = book.find('p', class_='price_color').text
   link = book.find('h3').find('a')
   print(link.get('title'))
   ```
5. The same link's `href` is our ticket to the details page. Problem: it's **relative** (`../../some-book_814/index.html`), so join it with the base URL first:
   ```python
   from urllib.parse import urljoin
   details_url = urljoin('https://books.toscrape.com/catalogue/', link.get('href'))
   ```
6. Navigate further: fetch the details page inside the loop and soup it up the same way. This listing-page -> detail-pages pattern is *the* fundamental scraping workflow - you crawl the listing, then visit every link it contains:
   ```python
   details_response = requests.get(details_url)
   details_soup = bs4.BeautifulSoup(details_response.text, 'lxml')
   ```
7. On the details page, collect the good stuff. The full title is now a plain `h1`, the price works the same as before, and the description is sneaky: its `p` has no class or id, but it sits **right after** the `div#product_description` heading:
   ```python
   title = details_soup.find('h1').text
   description = details_soup.find('div', id='product_description').find_next_sibling('p').text
   ```
8. Beautiful Soup has a `querySelectorAll` equivalent - using `select()` and `select_one()` we can find elements with CSS selectors. The syntax is the same as in devtools, and the `+` combinator can even replace `find_next_sibling`:
   ```python
   details_soup.select_one('div#product_description + p')   # querySelector
   soup.select('article.product_pod h3 a')                  # querySelectorAll
   ```
   Compare with `city_list.py`, which makes the JS equivalence explicit. If the selector syntax is new to you, check the CSS Diner game in the docs section above.
9. More tricks worth knowing once the basics click:
   - `get_text(strip=True)` - like `.text`, but collapses the whitespace mess around tags,
   - `.string` vs `.text` - `.string` only works when the tag has exactly one child,
   - `tag.attrs` - the element's attributes as a dict,
   - `find_all('a', string='Next')` - filter by text content, regexes work too,
   - `tag.parent`, `tag.children`, `find_previous_sibling()`, `find_parent()` - the rest of the navigation toolkit,
   - `tag.decompose()` - remove an element from the tree (handy for stripping out ads/scripts before parsing).

## Homework

Write a standalone script, that scrapes `books.toscrape.com`. Send it to my email.

1. Manually pick **three categories** of your choice (their pages live at `https://books.toscrape.com/catalogue/category/books/[category]/index.html`). Minimum one has to have more than one page.
2. For **every book** in each of the three categories, collect:
   - the title,
   - the price,
   - the description,
   - how many are available (stock)
3. Some categories span multiple pages - make sure you collect all the books, not just the first 20. The *next* button at the bottom of the listing is your friend.
4. The book links on a category page are relative URLs. Combine them with `https://books.toscrape.com/catalogue/` to build URLs you can fetch. ([`urllib.parse.urljoin`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin) can do the joining for you.)
5. Print everything in a readable format, or go the extra mile and save the results to a CSV/JSON file.

**Hint:** everything here is the "Tasks for today" workflow applied to a different URL - a category page is a listing just like the main page, so some tasks carry over one to one. A loop inside a loop - one over the listing pages, one over the books found on each - will get you very far (following the *next* button is exactly the fetch-a-link-from-the-listing pattern from task 6). **Politeness bonus**: put a small `time.sleep(1)` between requests so you don't hammer the poor fake bookstore.
