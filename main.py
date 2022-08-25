from ShazamAPI import Shazam
from youtubesearchpython import *
import youtube_dl
import os
import argparse
import spotify_addon


def find(query, limit=10):
    videosSearch = CustomSearch(
        query, VideoSortOrder.relevance, limit=limit)
    video_ids = []
    for video in videosSearch.result()["result"]:
        video_ids.append(video["id"])
    return video_ids


def constructURL(video_ids):
    url = "https://www.youtube.com/watch?v="
    return [url + id for id in video_ids]


def downloadMP3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            os.system("clear")
            ydl.download([url])
        except youtube_dl.utils.DownloadError:
            print("skipping...")
            return None

    """get mp3 file path in current directory"""
    mp3_file = [file for file in os.listdir() if file.endswith(".mp3")][0]
    return mp3_file


def recognize(file):
    bytemp3 = open(file, "rb").read()
    shazam = Shazam(bytemp3)
    recognize_generator = shazam.recognizeSong()
    print("running recognition...")
    """stop if not found after 1 minute"""
    for i in range(60):
        # add a progress bar
        bar = "=" * i + ">" + " " * (60 - i)
        percentage = i / 60 * 100
        os.system("clear")
        print("Running recognition...\n" + str(percentage) + "\n" + bar)
        try:
            song = next(recognize_generator)[
                1]["track"]["title"] + " " + next(recognize_generator)[1]["track"]["subtitle"]
            print(song)
            return song
            break
        except Exception as e:
            continue


def main(query, limit=10, optimizations=True):
    print("querying YouTube...")
    if optimizations:
        query = query + " -how"
    IDs = find(query, limit)
    URLs = constructURL(IDs)
    titles = []
    for url in URLs:
        """delete all file ending in .mp3 or.part"""
        for file in os.listdir():
            if file.endswith(".mp3") or file.endswith(".part"):
                os.remove(file)
        path = downloadMP3(url)
        if path is None:
            continue
        title = recognize(path)
        if title is None:
            continue
        titles.append(title)
        spotify_addon.add_to_playlist(spotify_addon.get_track_id(title))
        os.remove(path)
    return titles



# take query as command line argument
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="query YouTube, detect song(s) and add to them Spotify playlist")
    parser.add_argument(
        "-m", help="mode: *query* or path to *mp3* file", default="query")
    parser.add_argument(
        "-s", help="query to search for on youtube OR path to .mp3 file", required=True)
    parser.add_argument("-l", type=int, default=10,
                        help="number of videos to search")
    parser.add_argument("-o", type=bool, default=True, help="optimize query")
    args = parser.parse_args()
    if args.m == "query":
        main(args.s, args.l, args.o)
    else:
        spotify_addon.add_to_playlist(spotify_addon.get_track_id(recognize(args.s)))