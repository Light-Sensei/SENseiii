import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/5fc0fa0316da7ad8ed53a.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Konnichiwa!! [{event.sender.first_name}](tg://user?id={event.sender.id}), Yor Forger.** \n\n"
  TEXT += "♡ **I'll be giving my best for your work !!** \n\n"
  TEXT += f"♡ **Loid-San : [Light Yagami♡ (夜神月♡)](https://t.me/yagami_roito)** \n\n"
  TEXT += f"♡ **Library Version :** `{telever}` \n\n"
  TEXT += f"♡ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"♡ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ♡**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/yorXupdates"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/yorXsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
