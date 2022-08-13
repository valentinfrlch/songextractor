import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

with open("credentials.txt", "r") as f:
    client_id = f.readline().strip()
    client_secret = f.readline().strip()
    playlist_id = f.readline().strip()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_track_id(query):
    """get track_id of track_name"""
    track_id = sp.search(q=query, type="track")
    return track_id["tracks"]["items"][0]["id"]


def add_to_playlist(track_id):
    sp.playlist_add_items(playlist_id, track_id)