import requests
import json

search_url = "https://api.genius.com/search"

def artist_songs_url(artist_id):
    return f"https://api.genius.com/artists/{artist_id}/songs"

access_token = json.load(open("api_keys.json"))["genius"]
