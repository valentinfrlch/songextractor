from ShazamAPI import Shazam
from youtubesearchpython import *
import youtube_dl
import os


def find(query, limit=10):
    videosSearch = CustomSearch(
        query, VideoSortOrder.viewCount, limit=limit)
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
        ydl.download([url])
    """get mp3 file path in current directory"""
    mp3_file = [file for file in os.listdir() if file.endswith(".mp3")][0]
    return mp3_file


def recognize(file):
    bytemp3 = open(file, "rb").read()
    shazam = Shazam(bytemp3)
    recognize_generator = shazam.recognizeSong()
    print("recognizing...")
    """stop if not found after 1 minute"""
    for i in range(60):
        try:
            print(next(recognize_generator)[1]["track"]["title"])
            return (next(recognize_generator)[1]["track"]["title"])
            break
        except Exception as e:
            continue


def main(query, limit=10):
    print("querying YouTube...")
    IDs = find(query, limit)
    URLs = constructURL(IDs)
    titles = []
    for url in URLs:
        path = downloadMP3(url)
        title = recognize(path)
        titles.append(title)
        os.remove(path)
    return titles

print(main("cinematic drone videos"))