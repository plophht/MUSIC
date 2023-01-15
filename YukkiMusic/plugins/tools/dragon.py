from YukkiMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.database import is_muted, mute_off
from YukkiMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


@app.on_message(
    command(["/id","ايدي اغاني","الايدي","id","اا"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["/id","ايدي اغاني","الايدي","id","اا"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""- ꪀᥲ️︎ꪔᥱ︎ .{message.from_user.mention}\n\n- u᥉ᥱ︎ɾ. @{message.from_user.username}\n\n- Ꭵძ . `{message.from_user.id}`\n\n- Ꭵძ 𝗀ɾ᥆uρ . `{message.chat.id}`""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "✫︎ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐄𝐌𝐎 ✫︎", url=f"https://t.me/FTTUTY"),
                ],
                [  
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["قول"])
    & filters.group
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""انت {message.from_user.mention} روح قلبي .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✫︎ sᴏᴜʀᴄᴇ sᴇᴍᴏ ✫︎", url=f"https://t.me/FTTUTY"),
                ],
            ]
        ),
    )
                    
@app.on_message(
     command(["مبرمج السورس","سمسم"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b54a79a3f470333d2e580.jpg",
        caption=f"""- مرحبا بك عزيزي المسستخدم .\n\n- للتواصل مع مطور السورس اتبع الازرا .\n\n- اليك مطور السورس : @DEV_SAMIR .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(" ✫︎ 𝚂 𝙴 𝙼 𝙾 ✫︎ ", url=f"https://t.me/DEV_SAMIR"),
                ],[
                InlineKeyboardButton(
                        " ✫︎ sᴏᴜʀᴄᴇ sᴇᴍᴏ ✫︎ ", url=f"https://t.me/FTTUTY"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["مبرمج البوت","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b54a79a3f470333d2e580.jpg",
        caption=f"""- مرحبا بك عزيزي المسستخدم .\n\n- للتواصل مع مطور السورس اتبع الازرا .\n\n- اليك مطور السورس : @DEV_SAMIR .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("✫︎ ᴅᴇᴠ sᴇᴍᴏ ✫︎", url=f"https://t.me/DEV_SAMIR"),
                ],[
                InlineKeyboardButton(
                        "✫︎ ᴅᴇᴠ sᴇᴍᴏ ✫︎", url=f"https://t.me/FTTUTY"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["صاحب السورس","صاحب العظمه","سيمو","سمير"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c96034987eb482c3d65c5.jpg",
        caption=f"""- مرحبا بك عزيزي المسستخدم .\n\n- للتواصل مع مطور السورس اتبع الازرا .\n\n- اليك ملك التلجرام 👑 : @DEV_SAMIR .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("✫︎ الـمـبـرمـجہ سـمـيـر ✫︎", url=f"https://t.me/DEV_SAMIR"),
                ],[
                InlineKeyboardButton(
                        "✫︎ sᴏᴜʀᴄᴇ sᴇᴍᴏ ✫︎", url=f"https://t.me/FTTUTY"), 
                ]
            ]
        ),
    )

@app.on_message(
     command(["المطور سمير","المبرمج سمير"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c96034987eb482c3d65c5.jpg",
        caption=f"""- مرحبا بك عزيزي المسستخدم .\n\n- للتواصل مع سمير مطور السورس اتبع الازرا .\n\n- اليك سمير مطور السورس : @DEV_SAMIR .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("✫︎ ᴅᴇᴠ sᴇᴍᴏ ✫︎", url=f"https://t.me/DEV_SAMIR"),
                ],[
                InlineKeyboardButton(
                        "✫︎ sᴜᴘᴘᴏʀᴛ sᴇᴍᴏ ✫︎", url=f"https://t.me/FTTUTY"), 
                ]
            ]
        ),
    )

@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2f29f688c12900f1d9253.jpg",
        caption=f"""[✫︎ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴏᴜʀᴄᴇ sᴇᴍᴏ ✫︎](https://t.me/FTTUTY)\n\n[✫︎ sᴇᴍᴏ ᴛʜᴇ ʙᴇsᴛ sᴏᴜʀᴄᴇ ɪɴ ᴛᴇʟᴇ ‌✫︎](https://t.me/FTTUTY)\n\n[✫︎ ғᴏʟʟᴏᴡ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ✫︎](https://t.me/FTTUTY)\n""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "✫︎ ᴅᴇᴠ sᴇᴍᴏ ✫︎ ", url=f"https://t.me/FTTUTT"),
                ],[
                    InlineKeyboardButton(
                        "✫︎ sᴏᴜʀᴄᴇ sᴇᴍᴏ ✫︎", url=f"https://t.me/FTTUTY"), 
                    InlineKeyboardButton(
                        "✫︎ sᴜᴘᴘᴏʀᴛ sᴇᴍᴏ ✫︎", url=f"https://t.me/T_S_T99"),
                ],[
                    InlineKeyboardButton(
                        "✅ ضيف البوت لمجموعتك .", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
         ),
     )
  
