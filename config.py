# © Telegram @HMF_Owner_1, GitHub @ThiruXD 

import os
import time 


class Config(object):
	API_ID = int(os.environ.get("API_ID", "25502576"))
	API_HASH = os.environ.get("API_HASH", "f0f35dbb5b0081cdc8d3c9d5383c4628")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6358983740:AAFEd3h7Tdn2VtJbuaYB6k8LzHOkzGQkvzM")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "Shortener_File_Store_Bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001936300025"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5123039648"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SujanC7:SujanC7@cluster0.vst9zln.mongodb.net/?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001978535504")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "")
	DOMAIN = os.environ.get("DOMAIN", "")
	ABOUT_BOT_TEXT = f"""
This is Public Files Store Bot With Shortener Support!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Shortener File Store](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

👑 **Owner:** @Sujan_Ch

🧑🏻‍💻 **Developer:** @Sujan_Ch

👥 **Support Group:** @Sujan_BotZ

📢 **Updates Channel:** @Sujan_BotZ 
"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @Sujan_Ch"""
	SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/api api`
            
Ex: `/api 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://graph.org/file/a18cf9f447a1c34e5a20a.jpg"
START_TEXT = """Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})

I'ᴍ Uʟᴛʀᴀ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Cᴏᴜʟᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ  Fᴏʀ [Vnshortener](https://vnshortener.com). Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇs/Lɪɴᴋs Aɴᴅ Sᴇʟᴇᴄᴛ Mᴇᴛʜᴏᴅ Wᴀɪᴛ Fᴇᴡ Sᴇᴄᴏɴᴅs Bᴏᴛ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅ Tᴏ Oᴜʀ Sᴇʀᴠᴇʀ Aɴᴅ Gᴇɴᴀʀᴀᴛᴇ  [Vnshortener](http://vnshortener.com) ......

Cᴜʀʀᴇɴᴛʟʏ Sᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛs :

• Lɪɴᴋs - Aʟsᴏ Sᴜᴘᴘᴏʀᴛ Bᴜʟᴋ Lɪɴᴋs 
• Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Vɪᴅᴇᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Aᴜᴅɪᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Pʜᴏᴛᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB

Mᴏʀᴇ Fᴏʀᴍᴀᴛs Cᴏᴍᴍɪɴɢ Sᴏᴏɴ ......

Pᴏᴡᴇʀᴇᴅ Bʏ : [Sujan_Ch](http://Sujan_BotZ)"""

HELP_TEXT = """Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Wᴇʙsɪᴛᴇ:

Sᴛᴇᴘ Nᴏ 1 : Jᴜsᴛ Cʟɪᴄᴋ 'Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ' Bᴜᴛᴛᴏɴ Aɴᴅ Cᴏᴘʏ Yᴏᴜʀ [Vnshortener](http://vnshortener.com) Aᴄᴄᴏᴜɴᴛ Aᴘɪ Tᴏᴋᴇɴ.

Sᴛᴇᴘ Nᴏ 2 : Tʜᴇɴ Cᴏᴍ Aɢᴀɪɴ Hᴇʀᴇ Aɴᴅ Usᴇ /api Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Yᴏᴜʀ [Vnshortener](http://Vnshortener.com) Aᴄᴄᴏᴜɴᴛ.

Exᴀᴍᴘʟᴇ : `/api s18ғsjsn737d19f08f382h19d9sd473774hd58` """

ABOUT_TEXT = """🤖 Name :  Shortener File Store Bot 

🔠 Language  : Python3
📚 Library   : Teleton And Pyrogram
👑 Owner     : @sujan_ch
🧑🏻‍💻 Developer : @sujan_ch

©️Powered By @Sujan_BotZ """



