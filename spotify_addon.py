import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

scope = "playlist-modify-private"

with open("credentials.txt", "r") as f:
    client_id = f.readline().strip()
    client_secret = f.readline().strip()
    playlist_id = f.readline().strip()
    username = f.readline().strip()

sp_get = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_track_id(query):
    """get track_id of track_name"""
    track_id = sp_get.search(q=query, type="track")
    return track_id["tracks"]["items"][0]["id"]


def add_to_playlist(track_id):
    
    track_ids = [track_id]
    sp_push  = spotipy.Spotify(auth_manager=SpotifyOAuth(
            scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:9090"))
    results = sp_push.user_playlist_add_tracks(username, playlist_id, track_ids, position=None)
    return results 


add_to_playlist(get_track_id("Chaos at the spaceship"))
