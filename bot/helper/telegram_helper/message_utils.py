from pyrogram.types import  Message

class TgBot:
	""" This class is Telegram Bot connector"""
	def __init__(self, text: str, update, message: Message):
		self.update= update
		self.message = message
		self.bot_message = update.send_message(
			chat_id = message.chat.id,
			reply_to_message_id = message.message_id,
			text= text
		)

	def edit_message(self, text: str):
		""" Edits the message """
		self.update.edit_message_text(
			chat_id = self.message.chat.id,
			message_id = self.bot_message.message_id,
			text = text
		)
		
	def send_video(self, path):
		""" Sends video """
		self.update.send_video(
			chat_id = self.message.chat.id,
			reply_to_message_id = self.message.message_id,
			video = path
		)
	