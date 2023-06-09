from pyrogram import filters , __version__ as pyro
import random
import requests 
from telethon import __version__ as telever
from nandhabot import bot, arq
from PyDictionary import PyDictionary
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputTextMessageContent,
    InlineQueryResultDocument,
    InlineQueryResultArticle,
    InlineQueryResultAnimation,
    InlineQueryResultPhoto,
)

    

    


inlinecmds_text = "**Here you find moi inline functions commands!**"


inlinebuttons = [[InlineKeyboardButton(text="ᴡɪsʜ", switch_inline_query_current_chat="wish"),
                  InlineKeyboardButton(text="ᴜᴅ", switch_inline_query_current_chat="ud"),
                  InlineKeyboardButton(text="ɢɪᴛ", switch_inline_query_current_chat="git"),
                 ],[ InlineKeyboardButton(text="ᴡᴀʟʟ", switch_inline_query_current_chat="wall"),]]

@bot.on_message(filters.command("inlinecmds"))
async def inlinecmds(_, message):
            await message.reply_text(inlinecmds_text,
            reply_markup=InlineKeyboardMarkup(inlinebuttons))


@bot.on_inline_query()
async def inline_query_handler(client, query):
    string = query.query.strip().lower()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultPhoto(
                    photo_url="https://telegra.ph/file/b4769f8358a6de4794a59.jpg",
                    thumb_url="https://telegra.ph/file/b4769f8358a6de4794a59.jpg",
                    caption="Available Inline Futures!",
                    title=f"commandslist 😍😍",
                    description=f"Available commandslist for @TrunksRobot 📝 ",
                    reply_markup=InlineKeyboardMarkup(inlinebuttons))])
    
    elif string.split()[0] == "git":
        answers = []
        await client.answer_inline_query(
        query.id,
        results=answers,
        switch_pm_text="github Search | git [QUERY]",
        switch_pm_parameter="inline",
                )
        user = string.split(None, 1)[1].strip()
        res = requests.get(f'https://api.github.com/users/{user}').json()
        data = f"""Name: {res['name']}
UserName: {res['login']}
Link: [{res['login']}]({res['html_url']})
Bio: {res['bio']}
Company: {res['company']}
Blog: {res['blog']}
Location: {res['location']}
Public Repos: {res['public_repos']}
Followers: {res['followers']}
Following: {res['following']}
Acc Created: {res['created_at']}
"""
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultPhoto(
                    photo_url="http://telegra.ph/file/33868544d263e0a065b9e.jpg",
                    thumb_url="http://telegra.ph/file/33868544d263e0a065b9e.jpg",
                    caption=data,
                    title="github userinfo 😍",
                    description="github userinfo check!")])
    elif string.split()[0] == "wall":
        answers = []
        await client.answer_inline_query(
        query.id,
        results=answers,
        switch_pm_text="Wallpapers Search | wall [QUERY]",
        switch_pm_parameter="inline",
                )
        text = string.split(None, 1)[1].strip()
        x = await arq.wall(text)
        y = x.result
        image = random.choice(y).url_image
        button = [[InlineKeyboardButton("Scores Link", url=f"{image}")]]
        await client.answer_inline_query(
              query.id, 
              results=[ 
                InlineQueryResultDocument(
                document_url=image,
                thumb_url=image,
                title="Your Wall is Ready 😍",
                description="Walls from alpha coders",
                reply_markup=InlineKeyboardMarkup(button))])
            
    elif string.split()[0] == "ud":
        answers = []
        if len(string.split()) < 2:
            return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Urban Dictionary | ud [QUERY]",
                    switch_pm_parameter="inline",)
        ud_text = string.split(None, 1)[1].strip()
        results = requests.get( f'https://api.urbandictionary.com/v0/define?term={ud_text}').json() 
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultArticle(
                    input_message_content=InputTextMessageContent(
                    f"""⚠️** Warning**: Urban Dictionary does not always provide accurate descriptions\n• **Word**: {ud_text}\n• **Meaning**: {results["list"][0]["definition"]}\n• **Example**: {results["list"][0]["example"]}\n
                    """),thumb_url="https://telegra.ph/file/a463337cb8063fe15684f.jpg",
                    title=f"Urban Dictionary 📝",
                    description=f"Urban Dictionary For Ward's")])
                    
    elif string.split()[0] == "wish":
        wish_text = f"✨~~ **yoo!** ~~🤗 ✨\n~~**Your wish Possible to:  {random.choice([random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)])}%** ~~"
        api = requests.get("https://nekos.best/api/v2/happy").json()
        url = api["results"][0]['url']
        await client.answer_inline_query(
            query.id,
            results=[
                InlineQueryResultAnimation(
                animation_url=url,
                thumb_url=url,
                caption=wish_text,
                title="Your Wish 😍",
                description="Chance's of Your Wish")])
