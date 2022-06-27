from pyrogram import filters
from nandhabot import bot

@bot.on_message(filters.command("del"))
async def del(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await bot.get_chat_member(chat.id, user.id)
     if not user_stats.privileges:
            await m.reply_text("Your not admin")
            return 
     if not reply:
             await m.reply_text("reply to msg for deleting")
             return 
     if not user_stats.privileges.can_delete_messages:
               await m.reply_text("**your don't having the permission of**:\n`can_delete_messages`")
               return 
     if user_stats.privileges.can_delete_messages:
               await reply.delete()
               await m.reply_text("deleted!")
      
@bot.on_message(filters.command("ban"))
async def del(_, m):
     reply = m.reply_to_message
     chat = m.chat
     user = m.from_user
     user_stats = await bot.get_chat_member(chat.id, user.id)
     if not user_stats.privileges:
            await m.reply_text("Your not admin")
            return 
     if not reply:
             await m.reply_text("reply to msg for deleting")
             return 
     if not user_stats.privileges.can_restrict_members:
               await m.reply_text("**your don't having the permission of**:\n`can_restrict_members`")
               return 
     if user_stats.privileges.can_restrict_members:
             ban = reply.from_user or reply.sender_chat
             if ban:
                    await bot.ban_chat_member(chat.id, ban.id)
                     await m.reply_text("banned!")
                    
