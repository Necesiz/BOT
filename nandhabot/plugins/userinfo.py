import os

from pyrogram import filters
from pyrogram.types import Message
from nandhabot import dev_user, bot
from nandhabot.utils.sections import section


@bot.on_message(filters.command("cinfo"))
async def cinfo(_, m):
       reply = m.reply_to_message
       if not reply:
            await m.reply_text("yoo! ultra noob reply to channel")
            return 
       if not reply.sender_chat:
            await m.reply_text("yoo! ultra noob reply to channel")
            return 
       if reply.sender_chat:
             message = await m.reply_text("information gathering!!!")
             id = reply.sender_chat.id
             type = reply.sender_chat.type
             name = reply.sender_chat.title
             username = reply.sender_chat.username
             pfp = reply.sender_chat.photo
       if not pfp:
            text = f"✪ **TYPE:** Channel\n\n"
            text += f"✪ **ID:** {id}\n\n"
            text += f"✪ **NAME:** {name}\n\n"
            text += f"✪ **USERNAME:** @{username}\n\n"
            text += f"✪ **MENTION:** [link](t.me/{username})"
            await m.reply_text(text)
            await message.delete()
            return 
       image = reply.sender_chat.photo
       if image:
            photo = await bot.download_media(image.big_file_id)
            text = f"✪ **TYPE:** Channel\n\n"
            text += f"✪ **ID:** {id}\n\n"
            text += f"✪ **NAME:** {name}\n\n"
            text += f"✪ **USERNAME:** @{username}\n\n"
            text += f"✪ **MENTION:** [link](t.me/{username})"
            await m.reply_photo(photo,caption=(text))
            await message.delete()
            
async def get_user_info(user, already=False):
    if not already:
        userss = await bot.get_chat(user)
        user = await bot.get_users(user)
    if not user.first_name:
        return ["Deleted account", None]
    user_id = user.id
    username = user.username
    first_name = user.first_name
    mention = user.mention("Link")
    dc_id = user.dc_id
    is_bot = user.is_bot
    photo_id = user.photo.big_file_id if user.photo else None
    is_dev = user_id in dev_user
    body = { 
        "✪ ID": user_id,
        "✪ DC": dc_id,
        "✪ Name": [first_name],
        "✪ Username": [("@" + username) if username else "Null"],
        "✪ Mention": [mention],
        "✪ Bot": is_bot,
        "✪ Developer": is_dev,
        "✪ Bio": userss.bio,
    }
    caption = section("User info results", body)
    return [caption, photo_id]


async def get_chat_info(chat, already=False):
    if not already:
        chat = await bot.get_chat(chat)
    chat_id = chat.id
    username = chat.username
    title = chat.title
    type_ = chat.type
    is_scam = chat.is_scam
    description = chat.description
    members = chat.members_count
    is_restricted = chat.is_restricted
    link = f"[Link](t.me/{username})" if username else "Null"
    dc_id = chat.dc_id
    photo_id = chat.photo.big_file_id if chat.photo else None
    body = {
        "✪ ID": chat_id,
        "✪ DC": dc_id,
        "✪ Type": type_,
        "✪ Name": [title],
        "✪ Username": [("@" + username) if username else "Null"],
        "✪ Mention": [link],
        "✪ Members": members,
        "✪ Scam": is_scam,
        "✪ Restricted": is_restricted,
        "✪ Description": [description],
    }
    caption = section("Chat info", body)
    return [caption, photo_id]

@bot.on_message(filters.command("info"))
async def info_func(_, message: Message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    m = await message.reply_text("Information Processing...")

    try:
        info_caption, photo_id = await get_user_info(user)
    except Exception as e:
        return await m.edit(str(e))

    if not photo_id:
        return await m.edit(info_caption, disable_web_page_preview=True)
    photo = await bot.download_media(photo_id)

    await message.reply_photo(photo, caption=info_caption, quote=False)
    await m.delete()
    os.remove(photo)

@bot.on_message(filters.command("ginfo"))
async def chat_info_func(_, message: Message):
    try:
        if len(message.command) > 2:
            return await message.reply_text(
                "**➢ Usage:**/ginfo [USERNAME|ID]"
            )

        if len(message.command) == 1:
            chat = message.chat.id
        elif len(message.command) == 2:
            chat = message.text.split(None, 1)[1]

        m = await message.reply_text("Chat info Processing...")

        info_caption, photo_id = await get_chat_info(chat)
        if not photo_id:
            return await m.edit(info_caption, disable_web_page_preview=True)

        photo = await bot.download_media(photo_id)
        await message.reply_photo(photo, caption=info_caption, quote=False)

        await m.delete()
        os.remove(photo)
    except Exception as e:
        await m.edit(e)



@bot.on_message(filters.command("id"))
async def id(_, m):
         reply = m.reply_to_message
         _reply = ""
         if not reply: 
               no_reply = f"**ʏᴏᴜʀ ᴜɪᴅ**: `{m.from_user.id}`\n\n"
               no_reply += f"**ᴍsɢ ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
               return await m.reply_text(text=(no_reply)) 
         if reply.from_user:
               _reply += f"**ʏᴏᴜʀ ᴜɪᴅ**: `{m.from_user.id}`\n\n"
               _reply += f"**ʀᴇᴘʟɪᴇᴅ ᴜɪᴅ**: `{reply.from_user.id}`\n\n"
               _reply += f"**ᴍsɢ ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
         if reply.sender_chat:
                _reply += f"\n\n**ᴄʜᴀɴɴᴇʟ  ɪᴅ**: `{reply.sender_chat.id}`\n\n"
         if reply.sticker:
                _reply += f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{reply.sticker.file_id}`"
         if reply.animation:
                _reply += f"**ᴀɴɪᴍᴀᴛɪᴏɴ ɪᴅ**: `{reply.animation.file_id}`"
         if reply.document:
                _reply += f"**ᴅᴏᴄᴜᴍᴇɴᴛ ɪᴅ**: `{reply.document.file_id}`"
         if reply.audio:
                _reply += f"**ᴀᴜᴅɪᴏ ɪᴅ**: `{reply.audio.file_id}`"
         if reply.video:
                _reply += f"**ᴠɪᴅᴇᴏ ɪᴅ**: `{reply.video.file_id}`"
         if reply.photo:
                _reply += f"**ᴘʜᴏᴛᴏ ɪᴅ**: `{reply.photo.file_id}`"
         await m.reply_text(_reply)
        
