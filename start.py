from pyrogram import Client, filters
from modules import ytdl, mirror
import os

bot = Client("bot")


@bot.on_message(filters.command("mirror"))
def mirror_func(client, message):
	try:
		arg= message.text.split("mirror")[1].strip()
		msg= arg
	except IndexError:
		msg= "<strong>ERROR: Incorrect Format!</strong><br>Add a link after /mirror to mirror it!"
	
	msg= mirror.mirror(arg)
	if "ERROR" in msg:
		bot.send_message(chat_id=message.chat.id,
	reply_to_message_id= message.message_id,
	text=msg, parse_mode="html")
	else:
		bot.send_document(chat_id=message.chat.id,
	reply_to_message_id= message.message_id,
	document=msg, parse_mode="html")



@bot.on_message(filters.command("ytdl"))
def ytdl_func(client, message):
	try:
		arg= message.text.split("ytdl")[1].strip()
		if len(arg)==0:
			msg= "No Arguments passed!"
		else:
			vid_link= ytdl.download(arg)
			if "ERROR" in vid_link:
				bot.send_message(chat_id=message.chat.id, reply_to_message_id= message.message_id, text= vid_link, parse_mode="html")
				return
			
			bot.send_video(chat_id=message.chat.id,
			reply_to_message_id= message.message_id,
			video=vid_link)
			if os.path.exists(vid_link):
				os.remove(vid_link)
			
 
	except Exception as e:
		msg= f"<strong>Unknown Error: </strong><br> {e}"
	print(msg)
	bot.send_message(chat_id=message.chat.id,
	reply_to_message_id= message.message_id,
	text= msg, parse_mode="html")
	
	
@bot.on_message(filters.command("test"))
def test(client, message):
	print("sending file")
	bot.send_document(chat_id=message.chat.id,
	document="downloads/Shot on iPhone Meme 10.3gpp")
	
print("Bot started!")
bot.run()
