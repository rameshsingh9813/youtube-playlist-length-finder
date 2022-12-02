from pytube import Playlist
import time
p = Playlist(str(input("enter the playlist link: ")))
sum=0
for video in p.videos:
    print(video.title)
    total_length=video.length
    sum=sum+total_length

def convert(seconds):
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	
	return "%d:%02d:%02d" % (hour, minutes, seconds)

print("total video length of the plylist:  ",convert(sum))
time.sleep(5)