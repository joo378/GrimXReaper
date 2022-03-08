from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from config import BANNED_USERS
from strings import get_command
from XMusic import app
from XMusic.utils.database import (get_chatmode, 
                                   get_playmode,
                                   get_playtype)
from XMusic.utils.decorators import language
from XMusic.utils.inline.settings import playmode_users_markup

### Commands
PLAYMODE_COMMAND = get_command("PLAYMODE_COMMAND")


@app.on_message(
    filters.command(PLAYMODE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    if playmode == "Direct":
        Direct = True
    else:
        Direct = None
    chatmode = await get_chatmode(message.chat.id)
    if chatmode == "Group":
        Group = True
    else:
        Group = None
    playty = await get_playtype(message.chat.id)
    if playty == "Everyone":
        Playtype = None
    else:
        Playtype = True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["playmode_1"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
