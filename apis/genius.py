import requests
import json

search_url = "https://api.genius.com/search"

def artist_songs_url(artist_id):
    return f"https://api.genius.com/artists/{artist_id}/songs"

access_token = json.load(open("apis/api_keys.json"))["genius"]

def search_genius(query):
    response = requests.get(
        search_url,
        params={
            "q": query
        },
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    response.raise_for_status()
    return response.json()["response"]["hits"]

def get_artist_id(query):
    response = search_genius(query)
    return response[0]["result"]["primary_artist"]["id"]

def get_artist_songs(query):
    artist_id = get_artist_id(query)
    response = requests.get(
        artist_songs_url(artist_id),
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    response.raise_for_status()
    if response.ok:
        return response.json()["response"]["songs"]

def get_artist_song_titles(query):
    result = get_artist_songs(query)
    return [
        song["title"]
        for song in result
    ]

from pprint import pprint
pprint(get_artist_song_titles("Rychu Peja"))