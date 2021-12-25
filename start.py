from pyrogram import Client, filters
from modules import ytdl, mirror, xnxx
from bot.helper import send_message, edit_message
import os

bot = Client("bot")


@bot.on_message(filters.command("mirror"))
def mirror_func(client, message):
	try:
		arg= message.text.split("mirror")[1].strip()
		msg= arg
	except IndexError:
		msg= "<strong>ERROR: Incorrect Format!</strong><br>Add a link after /mirror to mirror it!"
		
		
	send_message("Got mirror Request", bot=bot, message=message)
	
	msg= mirror.mirror(arg)
	
	if "ERROR" in msg:
		edit_message(msg, bot, message)
	else:
		bot.send_document(
			chat_id=message.chat.id,
			reply_to_message_id= message.message_id,
			document=msg
		)



@bot.on_message(filters.command("ytdl"))
def ytdl_func(client, message):
	try:
		arg= message.text.split("ytdl")[1].strip()
		if len(arg)==0:
			msg= "No Arguments passed!"
		else:
			bot.send_message(chat_id=message.chat.id,
			reply_to_message_id=message.message_id,
			text= "Got YouTube Download Request!")
			vid_link = ytdl.download(arg)

			if "ERROR" in vid_link:
				bot.send_message(chat_id=message.chat.id, reply_to_message_id= message.message_id, text= vid_link, parse_mode="html")
				return
			
			# Sending file to telegram
			if "audio" or "Audio" in arg:
				bot.send_audio(chat_id=message.chat.id,
				 reply_to_message_id= message.message_id,
				  audio= vid_link)
				  
			else:
				bot.send_video(chat_id=message.chat.id,
				reply_to_message_id= message.message_id,
				video=vid_link, thumb="thumb.jpg")
			if os.path.exists(vid_link):
				os.remove(vid_link)
			
 
	except Exception as e:
		msg= f"<strong>Unknown Error: </strong><br> {e}"
	print(msg)
	bot.send_message(chat_id=message.chat.id,
	reply_to_message_id= message.message_id,
	text= msg, parse_mode="html")
	


@bot.on_message(filters.command("xnxx"))
def xnxx_func(client, message):
	file= xnxx.download("https://www.xvideos.com/embedframe/58723571")
	bot.send_video(
		chat_id=message.chat.id,
		reply_to_message_id= message.message_id,
		video=file
	)
	if os.path.exists(file):
		os.remove(file)
		
				
@bot.on_message(filters.command("test"))
def alive(client, message):
	bot.send_message(chat_id=message.chat.id,
	reply_to_message_id= message.message_id,
	text= "Yes, I'm Alive. ")
	
bot.run()
