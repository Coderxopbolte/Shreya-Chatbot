# ©  - MetaVoid (Moezilla) And Alexa Team For Modification
# Give Credit ❣️Day

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from os import getenv
import re
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", None)
MONGO_URL = getenv("MONGO_URL", None)

client = Client(SESSION_NAME, API_ID, API_HASH)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in client.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    alexaai = await message.reply("👀")
    await asyncio.sleep(1)
    await alexaai.edit("**😀 𝐑𝐞𝐩𝐨 𝐢𝐬 𝐏𝐫𝐚𝐢𝐯𝐭𝐞 😀**")
    await asyncio.sleep(1)
    await alexaai.edit("**😘 𝐋𝐨𝐯𝐞 𝐲𝐨𝐮 😘**")
    await alexaai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgQAAxkBAAIBNGPBGEjm8t1RHGY0J_BheWhzKYZbAAIWEAACpvFxHvvJk-2D25XRLQQ")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/21941841a9fca15ea39e7.jpg",
        caption=f"""━━━━━━━━━━━━━━━━━━━━━━
🥀 𝐀 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐀𝐢 𝐁𝐨𝐭 𝐨𝐟 𝐒𝐚𝐧𝐠𝐫𝐚𝐦.

━━━━━━━━━━━━━━━━━━━
🥀 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝐁𝐚𝐜𝐤𝐞𝐧𝐝 𝐁𝐨𝐭 𝐟𝐨𝐫 𝐓𝐠..
┏━━━━━━━━━━━━━━━━━┓
┣➤ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ☞ [𝐒𝐚𝐧𝐠𝐫𝐚𝐦](https://t.me/The_Sangram)
┣➤ 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞 𝐨𝐧 ☞ [𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com/@Official_Sangram)
┣➤ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ☞ [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/WorldChattingFriendsWCF)
┣➤ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ☞ [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/WCFnetwork)
┣➤ 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 ☞ [𝐇𝐞𝐫𝐞](https://github.com/OpQueenbots/Shreya-Chatbot)
┣➤ 𝐎𝐰𝐧𝐞𝐫 ☞ [𝐒𝐚𝐧𝐠𝐫𝐚𝐦 𝐱𝐃](https://t.me/Sangram_XD)
┗━━━━━━━━━━━━━━━━━┛

🥀 𝐈𝐟 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐚𝐧𝐲 𝐪𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐭𝐡𝐞𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐲 [𝐎𝐰𝐧𝐞𝐫](https://t.me/The_Sangram)""",
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**𝐒𝐡𝐫𝐞𝐲𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐢𝐬 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐟𝐨𝐫 𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠**")

@client.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    alexadb = MongoClient(MONGO_URL)    
    alexa = alexadb["AlexaDb"]["Alexa"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                ""
            )
    is_alexa = alexa.find_one({"chat_id": message.chat.id})
    if not is_alexa:
        alexa.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs ᴅɪsᴀʙʟᴇᴅ ʙʏ {message.from_user.mention()} ғᴏʀ ᴜsᴇʀs ɪɴ {message.chat.title}")
    if is_alexa:
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ")
    

@client.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    alexadb = MongoClient(MONGO_URL)    
    alexa = alexadb["AlexaDb"]["Alexa"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ"
            )
    is_alexa = alexa.find_one({"chat_id": message.chat.id})
    if not is_alexa:           
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ")
    if is_alexa:
        alexa.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ᴄʜᴀᴛʙɪᴛ ɪs ᴇɴᴀʙʟᴇᴅ ʙʏ {message.from_user.mention()} ғᴏʀ ᴜsᴇʀs ɪɴ {message.chat.title}")
    

@client.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴇᴀɢᴇ:**\n/chatbot [on|off] ᴏɴʟʏ ɢʀᴏᴜᴘ")

    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       if not is_alexa:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       alexadb = MongoClient(MONGO_URL)
       alexa = alexadb["AlexaDb"]["Alexa"] 
       is_alexa = alexa.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_alexa:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def alexaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
