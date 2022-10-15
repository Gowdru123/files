
# © Telegram @HMF_Owner_1, GitHub @ThiruXD 

import os
import asyncio
import traceback
from binascii import (
    Error
)
from pyrogram import (
    Client,
    enums,
    filters
)
from pyrogram.errors import (
    UserNotParticipant,
    FloodWait,
    QueryIdInvalid
)
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
from configs import Config
from database.database import db
from plugins.add_user_to_db import add_user_to_database
from plugins.send_file import send_media_and_reply
from plugins.helpers import b64_to_str, str_to_b64
from plugins.check_user_status import handle_user_status
from plugins.force_sub_handler import (
    handle_force_sub,
    get_invite_link
)
from plugins.broadcast_handlers import main_broadcast_handler
from plugins.save_media import (
    save_media_in_channel,
    save_batch_media_in_channel
)
from plugins.users_api import get_user, update_user_info

MediaList = {}

START_MEDIA = "https://telegra.ph/file/d20dee1ba93fc0b0c05ac.jpg"

START_TEXT = """**Hɪ/Hᴇʟʟᴏ [{}](tg://user?id={})**

I'ᴍ Uʟᴛʀᴀ Fᴀsᴛ Tᴇʟᴇɢʀᴀᴍ Cᴏᴜʟᴅ Sᴛᴏʀᴀɢᴇ Bᴏᴛ  Fᴏʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com). Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇs/Lɪɴᴋs Aɴᴅ Sᴇʟᴇᴄᴛ Mᴇᴛʜᴏᴅ Wᴀɪᴛ Fᴇᴡ Sᴇᴄᴏɴᴅs Bᴏᴛ Wɪʟʟ Bᴇ Uᴘʟᴏᴀᴅ Tᴏ Oᴜʀ Sᴇʀᴠᴇʀ Aɴᴅ Gᴇɴᴀʀᴀᴛᴇ  [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) ......

**Cᴜʀʀᴇɴᴛʟʏ Sᴜᴘᴘᴏʀᴛᴇᴅ Fᴏʀᴍᴀᴛs** :

• Lɪɴᴋs - Aʟsᴏ Sᴜᴘᴘᴏʀᴛ Bᴜʟᴋ Lɪɴᴋs 
• Fɪʟᴇs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Vɪᴅᴇᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Aᴜᴅɪᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB
• Pʜᴏᴛᴏs - Sᴜᴘᴘᴏʀᴛᴇᴅ Uᴘ Tᴏ 4GB

Mᴏʀᴇ Fᴏʀᴍᴀᴛs Cᴏᴍᴍɪɴɢ Sᴏᴏɴ ......

Pᴏᴡᴇʀᴇᴅ Bʏ - [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](https://tamizhmasters.com)"""

ABOUT_BOT_TEXT = f"""
This is Permanent File/Links Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](https://t.me/tmfile_short_bot)

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

👑 **Owner:** @Bavabee

🧑🏻‍💻 **Developer:** @HMF_Owner_1

👥 **Support Group:** @HangOverXD

📢 **Updates Channel:** @simplysouth_links 
"""

HELP_TEXT = """**Hᴏᴡ Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Wᴇʙsɪᴛᴇ:**

Sᴛᴇᴘ Nᴏ 1 : Jᴜsᴛ Cʟɪᴄᴋ 'Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ' Bᴜᴛᴛᴏɴ Aɴᴅ Cᴏᴘʏ Yᴏᴜʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) Aᴄᴄᴏᴜɴᴛ Aᴘɪ Tᴏᴋᴇɴ.

Sᴛᴇᴘ Nᴏ 2 : Tʜᴇɴ Cᴏᴍ Aɢᴀɪɴ Hᴇʀᴇ Aɴᴅ Usᴇ /api Tᴏ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Yᴏᴜʀ [Tᴀᴍɪᴢʜᴀ Mᴀsᴛᴇʀ](http://tamizhmasters.com) Aᴄᴄᴏᴜɴᴛ.

Exᴀᴍᴘʟᴇ : `/api s18ғsjsn737d19f08f382h19d9sd473774hd58` """


Bot = Client(
    name=Config.BOT_USERNAME,
    in_memory=True,
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)


@Bot.on_message(filters.private)
async def _(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)


@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):


    if cmd.from_user.id in Config.BANNED_USERS:
        await cmd.reply_text("Sorry, You are banned.")
        return
    if Config.UPDATES_CHANNEL is not None:
        back = await handle_force_sub(bot, cmd)
        if back == 400:
            return

    user_id = cmd.from_user.id
    user = await get_user(user_id)
    
    try:
        if len(cmd.command) == 2:
            if "api" in cmd.command[1].strip():
                user_api = cmd.command[1].strip().replace("api_", "")
                await update_user_info(user_id, {"shortener_api": user_api})

            return await cmd.reply_text(f"You have successfully connected your API\n\nYour Api: {user_api}\n\nStart sending me Files" )
    except Exception as e:
        print(e)
        
    usr_cmd = cmd.text.split("_", 1)[-1]
    if usr_cmd == "/start":
        await add_user_to_database(bot, cmd)
        await cmd.reply_photo(START_MEDIA,
            caption=START_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
                ],
                [
                    InlineKeyboardButton("Hᴇʟᴘ", callback_data="HELP_BUT"),
                    InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="ABOUT_BUT"),
                ],
                [
                    InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close"),
                    ]
                ]
            )
        )

    else:
        try:
            try:
                file_id = int(b64_to_str(usr_cmd).split("_")[-1])
            except (Error, UnicodeDecodeError):
                file_id = int(usr_cmd.split("_")[-1])
            GetMessage = await bot.get_messages(chat_id=Config.DB_CHANNEL, message_ids=file_id)
            message_ids = []
            if GetMessage.text:
                message_ids = GetMessage.text.split(" ")
                _response_msg = await cmd.reply_text(
                    text=f"**Total Files:** `{len(message_ids)}`",
                    quote=True,
                    disable_web_page_preview=True
                )
            else:
                message_ids.append(int(GetMessage.id))
            for i in range(len(message_ids)):
                await send_media_and_reply(bot, user_id=cmd.from_user.id, file_id=int(message_ids[i]))
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")


@Bot.on_message((filters.document | filters.video | filters.audio | filters.photo) & ~filters.chat(Config.DB_CHANNEL))
async def main(bot: Client, message: Message):

    if message.chat.type == enums.ChatType.PRIVATE:

        user = await get_user(message.from_user.id)

        if not user["shortener_api"]:
            return await message.reply_text(f"Fɪʀsᴛ Cᴏɴɴᴇᴄᴛ Wɪᴛʜ Yᴏᴜʀ Wᴇʙsɪᴛᴇ Aᴘɪ\n\n[Cʟɪᴄᴋ Tᴏ Cᴏɴɴᴇᴄᴛ](https://tamizhmasters.com/member/tools/api)")

        await add_user_to_database(bot, message)

        if Config.UPDATES_CHANNEL is not None:
            back = await handle_force_sub(bot, message)
            if back == 400:
                return

        if message.from_user.id in Config.BANNED_USERS:
            await message.reply_text("Sorry, You are banned!\n\nContact [Support Group](https://t.me/HangOverXD)",
                                     disable_web_page_preview=True)
            return

        if Config.OTHER_USERS_CAN_SAVE_FILE is False:
            return

        await message.reply_text(
            text="**Choose an option To Upload Your Files**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Upload To Batch", callback_data="addToBatchTrue")],
                [InlineKeyboardButton("Upload To Single File", callback_data="addToBatchFalse")]
            ]),
            quote=True,
            disable_web_page_preview=True
        )
    elif message.chat.type == enums.ChatType.CHANNEL:
        if (message.chat.id == int(Config.LOG_CHANNEL)) or (message.chat.id == int(Config.UPDATES_CHANNEL)) or message.forward_from_chat or message.forward_from:
            return
        elif int(message.chat.id) in Config.BANNED_CHAT_IDS:
            await bot.leave_chat(message.chat.id)
            return
        else:
            pass

        try:
            forwarded_msg = await message.forward(Config.DB_CHANNEL)
            file_er_id = str(forwarded_msg.id)
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=AbirHasan2005_{str_to_b64(file_er_id)}"
            CH_edit = await bot.edit_message_reply_markup(message.chat.id, message.id,
                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                                                              "Get Sharable Link", url=share_link)]]))
            if message.chat.username:
                await forwarded_msg.reply_text(
                    f"#CHANNEL_BUTTON:\n\n[{message.chat.title}](https://t.me/{message.chat.username}/{CH_edit.id}) Channel's Broadcasted File's Button Added!")
            else:
                private_ch = str(message.chat.id)[4:]
                await forwarded_msg.reply_text(
                    f"#CHANNEL_BUTTON:\n\n[{message.chat.title}](https://t.me/c/{private_ch}/{CH_edit.id}) Channel's Broadcasted File's Button Added!")
        except FloodWait as sl:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(message.chat.id)}` !!",
                disable_web_page_preview=True
            )
        except Exception as err:
            await bot.leave_chat(message.chat.id)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#ERROR_TRACEBACK:\nGot Error from `{str(message.chat.id)}` !!\n\n**Traceback:** `{err}`",
                disable_web_page_preview=True
            )

@Bot.on_message(filters.command('api') & filters.private)
async def shortener_api_handler(bot, m: Message):
    user_id = m.from_user.id
    user = await get_user(user_id)
    cmd = m.command

    if len(cmd) == 1:
        s = Config.SHORTENER_API_MESSAGE.format(base_site=Config.BASE_SITE, shortener_api=user["shortener_api"])
        return await m.reply(s)

    elif len(cmd) == 2:    
        api = cmd[1].strip()
        await update_user_info(user_id, {"shortener_api": api})
        await m.reply("Shortener API updated successfully to " + api)
        
@Bot.on_message(filters.private & filters.command("broadcast") & filters.user(Config.BOT_OWNER) & filters.reply)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)


@Bot.on_message(filters.private & filters.command("status") & filters.user(Config.BOT_OWNER))
async def sts(_, m: Message):
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Total Users in DB:** `{total_users}`",
        quote=True
    )


@Bot.on_message(filters.private & filters.command("ban_user") & filters.user(Config.BOT_OWNER))
async def ban(c: Client, m: Message):
    
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban any user from the bot.\n\n"
            f"Usage:\n\n"
            f"`/ban_user user_id ban_duration ban_reason`\n\n"
            f"Eg: `/ban_user 1234567 28 You misused me.`\n"
            f"This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = ' '.join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."
        try:
            await c.send_message(
                user_id,
                f"You are banned to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n"
                f"**Message from the admin**"
            )
            ban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            ban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"

        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(
            ban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Bot.on_message(filters.private & filters.command("unban_user") & filters.user(Config.BOT_OWNER))
async def unban(c: Client, m: Message):

    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban any user.\n\n"
            f"Usage:\n\n`/unban_user user_id`\n\n"
            f"Eg: `/unban_user 1234567`\n"
            f"This will unban user with id `1234567`.",
            quote=True
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user {user_id}"
        try:
            await c.send_message(
                user_id,
                f"Your ban was lifted!"
            )
            unban_log_text += '\n\nUser notified successfully!'
        except:
            traceback.print_exc()
            unban_log_text += f"\n\nUser notification failed! \n\n`{traceback.format_exc()}`"
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(
            unban_log_text,
            quote=True
        )
    except:
        traceback.print_exc()
        await m.reply_text(
            f"Error occurred! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )


@Bot.on_message(filters.private & filters.command("banned_users") & filters.user(Config.BOT_OWNER))
async def _banned_users(_, m: Message):
    
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ''

    async for banned_user in all_banned_users:
        user_id = banned_user['id']
        ban_duration = banned_user['ban_status']['ban_duration']
        banned_on = banned_user['ban_status']['banned_on']
        ban_reason = banned_user['ban_status']['ban_reason']
        banned_usr_count += 1
        text += f"> **user_id**: `{user_id}`, **Ban Duration**: `{ban_duration}`, " \
                f"**Banned on**: `{banned_on}`, **Reason**: `{ban_reason}`\n\n"
    reply_text = f"Total banned user(s): `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open('banned-users.txt', 'w') as f:
            f.write(reply_text)
        await m.reply_document('banned-users.txt', True)
        os.remove('banned-users.txt')
        return
    await m.reply_text(reply_text, True)


@Bot.on_message(filters.private & filters.command("clear_batch"))
async def clear_user_batch(bot: Client, m: Message):
    MediaList[f"{str(m.from_user.id)}"] = []
    await m.reply_text("Cleared your batch files successfully!")

@Bot.on_callback_query(filters.regex("START_BACK"))
async def start_back(_, query: CallbackQuery):
    await query.edit_message_caption(START_TEXT,
       reply_markup=InlineKeyboardMarkup(START_BACK_BUTTON))

START_BACK_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="ABOUT_BUT"),
        ],
        [
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close"),
    ],   
]

@Bot.on_callback_query(filters.regex("close"))
async def delete(_, query):
    await query.message.delete()

@Bot.on_callback_query(filters.regex("HELP_BUT"))
async def help(_, query: CallbackQuery):
    await query.edit_message_caption(HELP_TEXT,
       reply_markup=InlineKeyboardMarkup(HELP_BUTTON))

HELP_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ 🔘", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="ABOUT_BUT"),
        ],
        [
            InlineKeyboardButton("Bᴀᴄᴋ", callback_data="START_BACK"),
    ],   
]

@Bot.on_callback_query(filters.regex("ABOUT_BUT"))
async def about(_, query: CallbackQuery):
    await query.edit_message_caption(ABOUT_BOT_TEXT,
       reply_markup=InlineKeyboardMarkup(ABOUT_BUTTON))

ABOUT_BUTTON = [
        [
            InlineKeyboardButton("Cʟɪᴄᴋ Tᴏ Gᴇᴛ Aᴘɪ", url="https://tamizhmasters.com/member/tools/api"),
        ],
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="HELP_BUT"),
            InlineKeyboardButton("Aʙᴏᴜᴛ 🔘", callback_data="ABOUT_BUT"),
        ],
        [
            InlineKeyboardButton("Bᴀᴄᴋ", callback_data="START_BACK"),
    ],   
]

        

@Bot.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):

    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_BOT_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Go Home", callback_data="gotohome")
                    ]
                ]
            )
        )

    elif "aboutdevs" in cb_data:
        await cmd.message.edit(
            Config.ABOUT_DEV_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("GO TO HOME", callback_data="gotohome")
                    ]
                ]
            )
        )

    elif "gotohome" in cb_data:
        await cmd.message.edit(
            Config.HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ 𝖢𝖫𝖨𝖢𝖪 𝖳𝖮 𝖢𝖮𝖭𝖭𝖤𝖢𝖳 ⚡", url="https://tamizhmasters.com/member/tools/api")
                    ],
                    [
                        InlineKeyboardButton("❓ 𝖧𝖮𝖶 𝖳𝖮 𝖢𝖮𝖭𝖭𝖤𝖢𝖳 ❓", url="https://tamizhmasters.com")
                    ],
                    [
                        InlineKeyboardButton("⚙️ ʜᴏᴡ ᴛᴏ ᴜsᴇ ⚙️", url="https://tamizhmasters.com")
                    ],
                    [
                        InlineKeyboardButton("✅ 𝖠𝖡𝖮𝖴𝖳 𝖡𝖮𝖳 ✅", callback_data="aboutdevs")
                    ]
                ]
            )
        )

    elif "refreshForceSub" in cb_data:
        if Config.UPDATES_CHANNEL:
            if Config.UPDATES_CHANNEL.startswith("-100"):
                channel_chat_id = int(Config.UPDATES_CHANNEL)
            else:
                channel_chat_id = Config.UPDATES_CHANNEL
            try:
                user = await bot.get_chat_member(channel_chat_id, cmd.message.chat.id)
                if user.status == "kicked":
                    await cmd.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/HangOverXD).",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                invite_link = await get_invite_link(channel_chat_id)
                await cmd.message.edit(
                    text="**You Still Didn't Join ☹️, Please Join My Updates Channel to use this Bot!**\n\n"
                         "Due to Overload, Only Channel Subscribers can use the Bot!",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                            ]
                        ]
                    )
                )
                return
            except Exception:
                await cmd.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/HangOverXD).",
                    disable_web_page_preview=True
                )
                return
        await cmd.message.edit(
            text=Config.HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Support Group", url="https://t.me/HangOverXD"),
                        InlineKeyboardButton("Bots Channel", url="https://t.me/Discovery_Updates")
                    ],
                    [
                        InlineKeyboardButton("About Bot", callback_data="aboutbot"),
                        InlineKeyboardButton("About Dev", callback_data="aboutdevs")
                    ]
                ]
            )
        )

    elif cb_data.startswith("ban_user_"):
        user_id = cb_data.split("_", 2)[-1]
        if Config.UPDATES_CHANNEL is None:
            await cmd.answer("Sorry Sir, You didn't Set any Updates Channel!", show_alert=True)
            return
        if not int(cmd.from_user.id) == Config.BOT_OWNER:
            await cmd.answer("You are not allowed to do that!", show_alert=True)
            return
        try:
            await bot.kick_chat_member(chat_id=int(Config.UPDATES_CHANNEL), user_id=int(user_id))
            await cmd.answer("User Banned from Updates Channel!", show_alert=True)
        except Exception as e:
            await cmd.answer(f"Can't Ban Him!\n\nError: {e}", show_alert=True)

    elif "addToBatchTrue" in cb_data:
        if MediaList.get(f"{str(cmd.from_user.id)}", None) is None:
            MediaList[f"{str(cmd.from_user.id)}"] = []
        file_id = cmd.message.reply_to_message.id
        MediaList[f"{str(cmd.from_user.id)}"].append(file_id)
        await cmd.message.edit("Files Saved Successfully ✅\n\n"
                               "Press below button to get batch link.",
                               reply_markup=InlineKeyboardMarkup([
                                   [InlineKeyboardButton("Get Link", callback_data="getBatchLink")],
                                   [InlineKeyboardButton("Close", callback_data="closeMessage")]
                               ]))

    elif "addToBatchFalse" in cb_data:
        await save_media_in_channel(bot, editable=cmd.message, message=cmd.message.reply_to_message)

    elif "getBatchLink" in cb_data:
        message_ids = MediaList.get(f"{str(cmd.from_user.id)}", None)
        if message_ids is None:
            await cmd.answer("Batch List Empty!", show_alert=True)
            return
        await cmd.message.edit("Please wait....\n\n Your Files Downloding 📥")
        await save_batch_media_in_channel(bot=bot, editable=cmd.message, message_ids=message_ids, cmd=cmd)
        MediaList[f"{str(cmd.from_user.id)}"] = []

    elif "closeMessage" in cb_data:
        await cmd.message.delete(True)

    try:
        await cmd.answer()
    except QueryIdInvalid: pass


Bot.run()
