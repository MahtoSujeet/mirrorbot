from pytube import YouTube
from random import choice


def download(arg):
	try:
		link= arg.split("|")[0].strip()
		res= arg.split("|")[1].strip()
#		print(link+"\n"+res)
	except IndexError:
		return "ERROR: IndexError"
	
	proxies= list()
	with open("proxies.txt", "r") as file:
		lines= file.readlines()
	for line in lines:
		proxies.append(line)
	proxy= {"http": "http://"+choice(proxies)}
	vid = YouTube(link, proxies=proxy)
	stream= vid.streams.filter(res=res).first()
	
	file= stream.download()
#	print(file)
	return [file, vid.thumbnail_url]

# For testing
# download("https://youtu.be/_Lp-jRnTHKQ|144")
