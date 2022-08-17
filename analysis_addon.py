from matplotlib.pyplot import get
import spotify_addon as spotify

def get_analysis(track_id):
    """get analysis of track_id"""
    analysis = spotify.sp_get.audio_analysis(track_id)
    return analysis

print(get_analysis(spotify.get_track_id("Chaos at the spaceship")))