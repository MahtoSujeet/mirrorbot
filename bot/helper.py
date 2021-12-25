

def send_message(text, bot, message):
	"""Send reply to command message"""
	bot.send_message(
		chat_id=message.chat.id,
		reply_to_message_id=message.message_id,
		text= {text},
		parse_mode= "html"
	)
	
def edit_message(text, bot, message):
	"""Edits the cmd message"""
	bot.edit_message_text(
		chat_id= message.chat.id,
		message_id= message.id,
		text= {text},
		parse_mode= "html"
	)

