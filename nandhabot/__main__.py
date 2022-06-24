from nandhabot import bot, arq, tbot,  BOT_TOKEN,WEBHOOK,LOGGER,updater,PORT
import logging 
import random
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# enable logging
FORMAT = "[VEGETA ROBOT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)


    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=BOT_TOKEN)


if __name__ == "__main__":
   tbot.start(bot_token=BOT_TOKEN)
   bot.run()
   with bot:
        bot.send_message(f"@{SUPPORT_CHAT}", "Hello there I'm Now online")
