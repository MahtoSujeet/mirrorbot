import requests


def download(arg):
	link= arg
	r= requests.get(link, stream= True)
	with open("video.mp4", "wb") as f:
		for chunk in r.iter_content(chunk_size=1024):
			f.write(chunk)
	return "video.mp4"
		
		