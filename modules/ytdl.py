from pytube import YouTube

def download(arg):
	try:
		link= arg.split("|")[0].strip()
		res= arg.split("|")[1].strip()
#		print(link+"\n"+res)
	except IndexError:
		return "ERROR: IndexError"
		
	vid = YouTube(link)
	stream= vid.streams.filter(res=res).first()
	
	file= stream.download()
#	print(file)
	return [file, vid.thumbnail_url]

# For testing
# download("https://youtu.be/_Lp-jRnTHKQ|144")
