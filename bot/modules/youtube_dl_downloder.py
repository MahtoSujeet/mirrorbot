from pyrogram import Client
from bot.helper.telegram_helper.message_utils import TgBot
from pyrogram.types import Message
from youtube_dl import YoutubeDL

class Watch:
	def __init__(self, update, message: Message):
		bot= TgBot("Downloading......", update, message)
		args= message.text
		args = args.split(" ", maxsplit = 2)[1].split("|")
		self.link = args[0]
		try:
			self.resolution = args[1]
		except IndexError:
			bot.edit_message(text="<b>No resolution was mentioned. Downloading in maximum Quality.</b>")
			self.params = {
				'format': 'bestvideo/best',
			}
		
		self.path = self.download()
		bot.send_video(self.path)
		
				
	def download(self):
		with YoutubeDL(self.params) as ydl:
			info = ydl.extract_info(self.link, download=True)
			path = ydl.prepare_filename(info)
			return path
