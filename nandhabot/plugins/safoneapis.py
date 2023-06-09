from pyrogram import filters
from nandhabot import bot
from SafoneAPI import SafoneAPI
api = SafoneAPI()

@bot.on_message(filters.command("anews"))
async def animenews(_, message):
       api = f"https://api.safone.tech/anime/news"
       anews = requests.get(api).json() 
       caption = anews["results"][0]['description']
       img = anews["results"][0]["imageUrl"]
       link = anews["results"][0]["link"]
       title = anews["results"][0]["title"] 
       caption = f"""**Title**: `{title}`\n\n**News**: `{caption}`"""
       await message.reply_photo(img,caption=caption,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Source Link", url=link)]]))


@bot.on_message(filters.command("carbon"))
async def carbon(_, message):
        if not message.reply_to_message:
             return await message.reply("**Reply To Message.**") 
        elif message.reply_to_message:
             msg = await message.reply("**Process Your Request.**")
             carbon = await api.carbon(message.reply_to_message.text)
             await msg.edit("**Complete Process.**")
             await message.reply_photo(carbon,caption=f"**Request by {message.from_user.mention}**")


@bot.on_message(filters.command("webshot"))
async def webshot(_, m):
         if len(m.command) <2:
                return await m.reply("**Give A URL to Shot **\n**- /webshot github.com**")
         text = m.text.split(None, 1)[1]
         msg = await m.reply("**Your Request is Processing**")
         make_shot = await api.webshot(text)
         await msg.edit("**Complete Process.**")
         await m.reply_document(make_shot,caption=f"**Request by {m.from_user.mention}**")

@bot.on_message(filters.command("app"))
async def apps(_, message):
           if len(message.command) <2:
                return await message.reply("**Give A App Name**\n**- /app telegram**")
           text = message.text.split(None, 1)[1]
           apps = await api.apps(text)
           app_text = f"Results of {text}:\n\n"
           for app in apps.results:
                   app_text += f"~ [{app.title}]({app.link})\n"
           await message.reply_text(app_text)
