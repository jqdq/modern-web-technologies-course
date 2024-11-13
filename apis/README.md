# APIs

## Useful resources

- Authentication vs. Authorization: <https://www.geeksforgeeks.org/difference-between-authentication-and-authorization/>
- Authentication explained: <https://www.postman.com/api-platform/api-authentication/>
- SOAP APIs: https://stoplight.io/api-types/soap-api

## Tasks for today

### Advices - basic API usage and testing

1. Using [Hoppscotch](https://hoppscotch.io/), retrieve an advice from the [Advice Slip API](https://api.adviceslip.com/).
2. Search for an advice using the search endpoint.

### Astronomy Picture of the Day - credentials and JavaScript

1. Use the predefined async function to retrieve the API key.
2. Use the API key to fetch the Astronomy Picture of the Day.
3. Parse the JSON response.
4. Display the APOD by modifying the DOM.

### Hotness measurement - SOAP API example

0. Install `requests` and `zeep` using: `pip install zeep requests`.
1. Try out the requests library on a GET request to the Advice Slip API.
2. Finish the `soap_raw.py` script so it sends a POST request.
3. Do the same using zeep.

### Polish Sejm Swagger - OpenAPI and client generation

Take a close look at [this](https://api.sejm.gov.pl/sejm/openapi/ui/#/) website and at [this](https://api.sejm.gov.pl/sejm/openapi/) specification. You'll encounter this format multiple times in your career. 

Load `https://api.sejm.gov.pl/sejm/openapi/` into the [Swagger online editor](https://editor.swagger.io/) and try generating a Python client for it.

### Ranking words by frequency in artist's track titles - Python and credentials

Look into the `genius.py` file for a boilerplate.
[Some info on getting the Genius API key](https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/07-Genius-API.html)

1. Retrieve the search results for an artist.
2. Extract the artist ID from the search results
3. Retrieve the artist's songs
4. Extract the song titles from the artist's songs
5. Normalize the texts by removing punctuation and converting to lowercase.
6. Count a word's frequency in the song lyrics.

### Asteroid Announcer - Apps Script, Advanced API usage and OAuth

1. Create an AppScript project on your Google Drive.
2. Get yourself an API key for the NASA API.
3. Try looking up possible destroyers of the Earth using [NeoWS](https://api.nasa.gov/index.html#NeoWS).
4. Using [CalendarApp](https://developers.google.com/apps-script/reference/calendar/calendar-app) in AppScript, and the NASA API, create "Missed opportunity to kill us all" events for some near misses.
5. Run and observe the OAuth screen
6. Add scheduling.

## Problem set

1. Choose a SOAP API on [this](https://www.postman.com/cs-demo/public-soap-apis/documentation/eebj1yq/public-soap-apis?entity=request-8854915-b0a88484-8385-4b6d-9749-f9262ec4ae93) site and write a script using it via zeep (1p). Simplest wins (there are no losers tho).
2. Using the Polish Sejm API, and the `mp_explorer_template.html` create a random MP generator. It should:
   1. Retrieve the list of polish MPs in the current term (1.5 p)
   2. Choose a random one. Display their name, date of birth and some info on them (see the template) (1 p)
   3. Display the photo (1.5 p)
