import asyncio 

from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
)
from pyrogram import filters

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://telegra.ph/file/d20dee1ba93fc0b0c05ac.jpg"
START_TEXT = """I'ᴍ Uʟᴛʀᴀ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Cᴏᴜʟᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ  Fᴏʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com). Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇs/Lɪɴᴋs Aɴᴅ Sᴇʟᴇᴄᴛ Mᴇᴛʜᴏᴅ Wᴀɪᴛ Fᴇᴡ Sᴇᴄᴏɴᴅs Bᴏᴛ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅ Tᴏ Oᴜʀ Sᴇʀᴠᴇʀ Aɴᴅ Gᴇɴᴀʀᴀᴛᴇ  [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) ......

Cᴜʀʀᴇɴᴛʟʏ Sᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛs :

• Lɪɴᴋs - Aʟsᴏ Sᴜᴘᴘᴏʀᴛ Bᴜʟᴋ Lɪɴᴋs 
• Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Vɪᴅᴇᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Aᴜᴅɪᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Pʜᴏᴛᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB

Mᴏʀᴇ Fᴏʀᴍᴀᴛs Cᴏᴍᴍɪɴɢ Sᴏᴏɴ ......

Pᴏᴡᴇʀᴇᴅ Bʏ : [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com)"""

@bot.on_message(filters.command("start", PREFIX))
async def help(client, message):
    await message.reply_photo(START_MEDIA, caption=START_TEXT,
                              reply_markup=InlineKeyboardMarkup(START_BUTTON))
