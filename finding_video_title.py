from pytube import Playlist
import time
user=input("would you want total playlist time or section[yes/no]: ")
sum = 0
p = Playlist(str(input("enter the playlist link: ")))
try:
    if user=="yes":
        for video in p.videos:
            print(video.title)
            total_length = video.length
            sum = sum + total_length
    else:
        video_title = str(input("enter  the exact title of the video: "))
        count=0
        for video in p.videos:
            if video_title==video.title:
                count+=1
            if count>0:
                print(video.title)
                # video.streams.get_highest_resolution().download()
                total_length = video.length
                sum = sum + total_length

    def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)


    print("total video length of the plylist: ", convert(sum))
except:
    print("error! only enter the plylist video link or the video link from  the playlist")
time.sleep(5)