from pytube import YouTube
import os

user = os.getlogin()

yt = YouTube("https://youtu.be/djV11Xbc914?si=VXOPaejbEzEWsuo6")

def check_if_avail(itagg):
    
    aud = yt.streams.get_by_itag(itagg)
    return aud


print(yt.streams.filter(res="2160p"))