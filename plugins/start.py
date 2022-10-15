import asyncio 

from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
)
from pyrogram import filters

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]

@bot.on_message(filters.command("help", PREFIX))
async def help(client, message):
    await message.reply_video(HELP_MEDIA, caption=HELP_TEXT,
                              reply_markup=InlineKeyboardMarkup(HELP_BUTTON))
