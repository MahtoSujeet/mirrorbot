import youtube_dl
import time
#from bot.helper.telegram_helper.message_utils import TgBot


def progress_hook(response):
	#print(response)
	if response["status"] == "downloading":
		print(f'downloaded: {response["downloaded_bytes"]}')
	if response["status"] == "finished":
		print("download complete bitch")
ydl_opts= {
	"progress_hooks" : [progress_hook],
	"format" : "bestaudio/best",
}

link = "https://youtu.be/r6MS3xL5BVQ"
#link = "https://www.xnxx.com/video-z71wx57/18yo_step_daughter_gets_the_cum_on_her_ass"

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	info = ydl.extract_info(link, download=True)
	path = ydl.prepare_filename(info)
	print(path)


