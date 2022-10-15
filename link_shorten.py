from f import *
import re
from shorten_link import *
from configs import *
from data_shorten import *

# INITIALISATION
client.parse_mode = 'html'
commands = ["/api", ""]
welcome_re = re.compile('/start', re.IGNORECASE)


# TRIGGERS
@client.on(events.NewMessage(pattern=welcome_re))
async def welcome(e):
    chat = await e.get_chat()
    if e.raw_text.lower() == "/start":
        await client.send_message(chat, link_preview=False)
        return
    try:
        api_key = e.raw_text.split(' ')[1]

        try:
            tapi_key = api_key.split("-")[0]
            username = api_key.split("-")[1]
            api_key = tapi_key
            del tapi_key
        except IndexError:
            username = 'Unknown'
    except IndexError:
        return

    mess = await client.send_message(chat, "<B>⏳Please Wait...\nWe Are Checking Your Account</B>")
    stype, msg = await api_checker(api_key)
    print(stype)

    if stype:
        await api_logger(chat.id, api_key)
        await client.edit_message(mess,
                                  f"<b>Account Connected Sucessfully ✅</b>")
    else:
        await client.edit_message(mess, "<b>😔Invailid User Api Token!!</b>")


@client.on(events.NewMessage())
async def handler(e):
    chat = await e.get_chat()
    if re.search("/api ", e.raw_text):
        return
    s_api = await info_taker(chat.id)
    if not s_api:
        await client.send_message(chat, api_message, buttons=api_button)
        return
    caption = e.raw_text
    if caption.lower() in commands:
        return

    links = await link_extractor(caption)
    if not links:
        await client.send_message(chat, "<b>No Links Found In Message 😵</b>")
        return
    if len(links) > 50:
        await client.send_message(chat,"<b>😔 Sorry Mate U Can Only Convert 50 Links Per Post.</b>")
        return
    nlinks = await shortner(links, s_api)
    caption = await link_replacer(caption, links, nlinks)
    caption = await bolder(caption)

    mess = await client.send_message(chat, e.message)
    buttons = None
    if await username_check(caption):
        buttons = [Button.inline('Remove Usernames From Message', 'reusr')]

    await client.edit_message(mess, message=caption, buttons=buttons)


@client.on(events.NewMessage(pattern="/api"))
async def api(e):
    chat = await e.get_chat()
    try:
        api_key = e.raw_text.split(" ")[1]
    except IndexError:
        await client.send_message(chat, api_message, buttons=api_button)
        return

    mess = await client.send_message(chat, "<B>⏳Please Wait...\nWe Are Checking Your Account</B>")
    stype, msg = await api_checker(api_key)

    if stype:
        
        await api_logger(chat.id, api_key)
        await client.edit_message(mess, f"<b>Account Connected Sucessfully ✅</b>")
    else:
        await client.edit_message(mess, "<b>😔Invailid User Api Token!!</b>")


# CALLBACK-QUERY
@client.on(events.CallbackQuery(pattern="reusr"))
async def rem_user(e):
    mess = await e.get_message()
    caption = mess.raw_text
    caption = await remove_username(caption, '')
    caption = await bolder(caption)
    await client.edit_message(mess, caption)


@client.on(events.CallbackQuery(pattern="api"))
async def rem_user(e):
    mess = await e.get_message()
    await client.edit_message(mess, api_message, buttons=api_button)


@client.on(events.CallbackQuery(pattern="abt"))
async def rem_user(e):
    mess = await e.get_message()
    await client.edit_message(mess)


@client.on(events.CallbackQuery(pattern="back"))
async def rem_user(e):
    mess = await e.get_message()
    chat = await e.get_chat()
    await client.edit_message(mess, link_preview=False)


client.run_until_disconnected()

