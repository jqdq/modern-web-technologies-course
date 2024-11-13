from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the webdriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()

try:
    # Open DuckDuckGo
    driver.get("https://www.duckduckgo.com")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Enter the search query
    search_query = "Selenium Python"
    search_box.send_keys(search_query)

    # Submit the search query
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load
    time.sleep(2)

    # Retrieve the search results
    results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")

    # Print the titles and URLs of the search results
    for result in results:
        title = result.text
        url = result.get_attribute("href")
        print(f"Title: {title}\nURL: {url}\n")

finally:
    # Close the browser
    driver.quit()