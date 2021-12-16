from pyrogram import client

bot = client("bot")

vid
@bot.on_message(filters.command("send"))
def send(client, message):
	bot.send_video(chat_id=message.chat.id,
			reply_to_message_id= message.message_id,
			video=vid_link)