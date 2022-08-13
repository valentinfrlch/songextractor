import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public"

with open("credentials.txt", "r") as f:
    client_id = f.readline().strip()
    client_secret = f.readline().strip()
    playlist_id = f.readline().strip()

sp_get = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
sp_push = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri="http://127.0.0.1:9090"))

def get_track_id(query):
    """get track_id of track_name"""
    track_id = sp_get.search(q=query, type="track")
    return track_id["tracks"]["items"][0]["id"]


def add_to_playlist(track_id):
    sp_push.playlist_add_items(playlist_id, track_id)

add_to_playlist("39MtVje7wduLpwGs9QZghN")
