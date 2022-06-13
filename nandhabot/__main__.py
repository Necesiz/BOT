from nandhabot import bot, arq
import logging
import random
import nandhabot.plugins
from nandhabot.config import SUPPORT_CHAT
from nandhabot.utils.dbfunctions import clean_restart_stage

# enable logging
FORMAT = "[VEGETA ROBOT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)

if __name__ == "__main__":
    bot.run()
    restart_data = await clean_restart_stage()
    x = await arq.wall("vegeta")
    y = x.result
    try:
        print("Sending online status")
        if restart_data:
            await bot.edit_message_media(
                restart_data["chat_id"],
                restart_data["message_id"],
                random.choice(y).url_image,
                caption="**Saiyan Prince Vegeta Successfully Restarted With New Powers**",
            )

        else:
            await bot.send_photo(f"@{SUPPORT_CHAT}", random.choice(y).url_image, caption="**Saiyan Prince Vegeta Was Successfully Deployed!**")
    except Exception:
        pass
 
