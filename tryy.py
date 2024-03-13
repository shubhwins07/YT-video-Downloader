from pytube import YouTube
import os

user = os.getlogin()

yt = YouTube("https://youtu.be/MatGDjb4hk8?si=d3u1OfhlzpfiQNhs")

def check_if_avail(itagg):
    
    aud = yt.streams.get_by_itag(itagg)
    return aud


diff_itags = [160,133,18,135,22,337,336,335,140,251]
results = []
            
#in the scroll widget
for itaag in diff_itags:
    print(itaag)
    lol = check_if_avail(itaag)
    if lol == None:
        results.append(False)
    else:
        results.append(True)
        
print(results)