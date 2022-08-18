# Songextractor
## Looking for music ideas on a topic?
This little program searches YouTube for provided search term and extracts songs from found videos.

Credit goes to ShazamAPI, youtube_search_python and youtube_dl


## Get started
Install the required modules:
```
pip install -r requirements.txt
```

Make sure that you have ffmpeg installed:
```
apt install ffmpeg
```

1. Go to https://developer.spotify.com/dashboard/ and create an application
2. Note your client_id and your client_secret
3. Set the redirect url to "http://localhost:9090"
4. Create a playlist in your spotify library and note it's ID (the string right behind the "/"
5. Note your username

6. Create a credentials.txt file in the songextractor folder
7. Fill the information from above in the following order and each information on a new line:
```
client_id
client_secret
playlist_id
username
```
