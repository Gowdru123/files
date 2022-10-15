from configs import Config
from plugins.add_user_to_db import add_user_to_database
from pyrogram import (
    Client,
    enums,
    filters
)

@Client.on_message(filters.command('api') & filters.private)
async def shortener_api_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command

    if len(cmd) == 1:
        s = Config.SHORTENER_API_MESSAGE.format(base_site=Config.BASE_SITE, shortener_api=user["shortenedUrl"])
        return await m.reply(s)

    elif len(cmd) == 2:    
        api = cmd[1].strip()
        await update_user_info(user_id, {"shortenedUrl": api})
        await m.reply("Shortener API updated successfully to " + api)


        
