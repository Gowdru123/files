# © Telegram @HMF_Owner_1, GitHub @ThiruXD 

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BASE_SITE = os.environ.get("BASE_SITE", "tamizhmasters.com")
	DOMAIN = os.environ.get("DOMAIN", "urlsopen.com")
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

👑 **Owner:** @Bavabee

🧑🏻‍💻 **Developer:** @HMF_Owner_1

👥 **Support Group:** @HangOverXD

📢 **Updates Channel:** @simplysouth_links 
"""
	ABOUT_DEV_TEXT = f"""
**🌐 This Bot Was Devloped By** : @HMF_Owner_1"""
	SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, `/apikey api`
            
Ex: `/apikey 6LZq851sXofffPHugiKQq`

Current Website: {base_site}

Current Shortener API: `{shortener_api}`"""

PREFIX = ["/", ".", "?", "#", "@", "₹", "+", ":", "!", "^", "|"]
START_MEDIA = "https://telegra.ph/file/d20dee1ba93fc0b0c05ac.jpg"
START_TEXT = f"""Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})

I'ᴍ Uʟᴛʀᴀ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Cᴏᴜʟᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ  Fᴏʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com). Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇs/Lɪɴᴋs Aɴᴅ Sᴇʟᴇᴄᴛ Mᴇᴛʜᴏᴅ Wᴀɪᴛ Fᴇᴡ Sᴇᴄᴏɴᴅs Bᴏᴛ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅ Tᴏ Oᴜʀ Sᴇʀᴠᴇʀ Aɴᴅ Gᴇɴᴀʀᴀᴛᴇ  [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) ......

Cᴜʀʀᴇɴᴛʟʏ Sᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛs :

• Lɪɴᴋs - Aʟsᴏ Sᴜᴘᴘᴏʀᴛ Bᴜʟᴋ Lɪɴᴋs 
• Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Vɪᴅᴇᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Aᴜᴅɪᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Pʜᴏᴛᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB

Mᴏʀᴇ Fᴏʀᴍᴀᴛs Cᴏᴍᴍɪɴɢ Sᴏᴏɴ ......

Pᴏᴡᴇʀᴇᴅ Bʏ : [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com)"""

HELP_TEXT = """Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Wᴇʙsɪᴛᴇ:

Sᴛᴇᴘ Nᴏ 1 : Jᴜsᴛ Cʟɪᴄᴋ 'Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ' Bᴜᴛᴛᴏɴ Aɴᴅ Cᴏᴘʏ Yᴏᴜʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) Aᴄᴄᴏᴜɴᴛ Aᴘɪ Tᴏᴋᴇɴ.

Sᴛᴇᴘ Nᴏ 2 : Tʜᴇɴ Cᴏᴍ Aɢᴀɪɴ Hᴇʀᴇ Aɴᴅ Usᴇ /api Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Yᴏᴜʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) Aᴄᴄᴏᴜɴᴛ.

Exᴀᴍᴘʟᴇ : `/api s18ғsjsn737d19f08f382h19d9sd473774hd58` """

ABOUT_TEXT = """🤖 Name :  Tamizh Masters Link Convertor

🔠 Language  : Python3
📚 Library   : Teleton And Pyrogram
👑 Owner     : @Bavabee
🧑🏻‍💻 Developer : @HMF_Owner_1

©️Powered By @simplysouth_links """


