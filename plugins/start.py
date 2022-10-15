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
async def start(client, message):
    await message.reply_photo(START_MEDIA, caption=START_TEXT,
                              reply_markup=InlineKeyboardMarkup(START_BUTTON))

START_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="ABOUT_ME"),
        ],
        [
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close"),
    ],   
]

@bot.on_callback_query(filters.regex("START_BACK"))
async def start_back(_, query: CallbackQuery):
    await query.edit_message_caption(START_TEXT,
       reply_markup=InlineKeyboardMarkup(START_BACK_BUTTON))

START_BACK_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="ABOUT_ME"),
        ],
        [
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close"),
    ],   
]

@bot.on_callback_query(filters.regex("HELP_BUT"))
async def help(_, query: CallbackQuery):
    await query.edit_message_caption(HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

HELP_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ 🔘", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="ABOUT_ME"),
        ],
        [
            InlineKeyboardButton("Bᴀᴄᴋ", callback_data="START_BACK"),
    ],   
]

@bot.on_callback_query(filters.regex("ABOUT_BUT"))
async def about(_, query: CallbackQuery):
    await query.edit_message_caption(ABOUT_TEXT,
       reply_markup=InlineKeyboardMarkup(ABOUT_BUTTON))

ABOUT_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ 🔘", callback_data="ABOUT_ME"),
        ],
        [
            InlineKeyboardButton("Bᴀᴄᴋ", callback_data="START_BACK"),
    ],   
]

        
