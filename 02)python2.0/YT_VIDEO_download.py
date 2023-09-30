#  youtube video downloading



import pytube

link = input ("enter youtube video link:")
Yt=pytube.youtube(link)
Yt.streams.first().download()
print("download",link)