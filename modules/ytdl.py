from pytube import YouTube
from random import choice
import requests
from os import rename


def download(arg):
	try:
		link= arg.split("|")[0].strip()
		res= arg.split("|")[1].strip()
#		print(link+"\n"+res)
	except IndexError:
		return "ERROR: IndexError"
	
	proxies= list()
#	with open("proxies.txt", "r") as file:
	with open("/sdcard/python/mirrorbot/proxies.txt", "r") as file:
		lines= file.readlines()
		for line in lines:
			proxies.append(line)
	proxy= {"http": "http://"+choice(proxies)}
	vid = YouTube(link, proxies=proxy)
	
	# For Downloading Video
	if res != "audio":
		stream= vid.streams.filter(res=res).first()
		dl_vid= stream.download()
		r= requests.get(vid.thumbnail_url, stream= True)
		with open("thumb.jpg", "wb") as file:
			for chunk in r.iter_content(chunk_size=1024):
				file.write(chunk)
		return dl_vid
		
	# For Downloading audio
	dl_audio = vid.streams.get_audio_only()
	rename(dl_audio, dl_audio+".mp3")
	return dl_audio

# For testing
#download("https://youtu.be/_Lp-jRnTHKQ| audio")
