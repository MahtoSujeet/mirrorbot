from bot.helper.telegram_helper.message_utils import TgBot
from pyrogram import Client, filters
from bot.modules.youtube_dl_downloder import Watch

mybot = Client("bot")

"""@mybot.on_message()
def echo_func(update, message):
	tgbot = TgBot("hey", update, message)
	tgbot.edit_message("new msg")"""
	
@mybot.on_message(filters.command("watch"))
def mirror_func(update, message):
	Watch(update, message)
	
mybot.run()


