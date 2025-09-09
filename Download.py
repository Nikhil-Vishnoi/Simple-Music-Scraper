# Download youtube files into mp4s 
import pytubefix as pytube
from pytubefix.cli import on_progress

# Curl from the internet and get html code 
import requests

# Parse html code for specific lines 
from bs4 import BeautifulSoup

import os
import numpy as np 
# If web searchiung throws a error try changing the "httpx to be less than version 24 
# py -m pip install "httpx<0.24" 
from youtubesearchpython import VideosSearch

# Use youtube-search-python to find the most relevant youtube link 
def getSong(query):
    print(query)
    videosSearch = VideosSearch(query, limit=1)

    results = videosSearch.result()
    first_video = results['result'][0]

    title = first_video['title']
    link = first_video['link']

    print("Title:", title)
    print("URL:", link)
    return link 
# Uses Pytube to download the song as a mp4 file 
def DownloadVideo(url,loc,prt =0):
    # os.chdir(r""+loc)
    song = pytube.YouTube(url, on_progress_callback = on_progress) 
    video = song.streams.filter(only_audio = True).first().download()
    if prt == 1:
        print('Downloading '+song.title+'...')
        print("Complete")
    os.rename(video,video.replace(" ",""))
    return video.replace(" ","")

workfolder = os.listdir("ToDownload")
for file in workfolder: 
    queue = np.loadtxt(("ToDownload/"+file),dtype =str,delimiter=' ')
    try:
        os.mkdir(("Downloaded/"+file.replace(".txt","")))
    except FileExistsError:
        i = 1 + 1
    path = "Downloaded/"+file.replace(".txt","")+"/"
    os.chdir(r""+path)
    for spotify_song in queue: 
        # Each spotify song is a link to a spotify page for the song
        # use this to find the optimal google search to use to find the 
        # youtube video most likely to correlate to the song we want \
        page = requests.get(spotify_song)
        # print(page.content)
        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            s = soup.title.string.replace('<title>','').replace('</title>','').replace('| Spotify','')+" full song"
        except AttributeError:
            print("Could not download ",spotify_song,"\n") 
            continue 
        try: 
            url = getSong(s)
        except IndexError: 
            print("Could not download ",spotify_song,"\n") 
            continue 
        try: 
            DownloadVideo(url,path,prt=1)
        except FileExistsError: 
            print("Already downloaded ",spotify_song) 
    os.chdir("../../")
    os.rename(("ToDownload/"+file),(("Downloaded/"+file)))
