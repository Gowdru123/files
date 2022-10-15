from f import *
import aiohttp

start_message = """<b>
Hey There, {}
🔀 I Can Convert Link To TamizhMasters ShortLink
💬 Send Me Any Message With Links
🔗 I Will Shorten All Links In It 
🔂 Convert to <a href="https://tamizhmasters.com/member/tools/bookmarklet">TamizhMasters</a> 

©️Powered By @simplysouth_links
</b>"""
start_button = [[Button.url("Join Channel ♥️", "t.me/tamizhmastersofficial"), Button.inline("About Bot 🤖", "abt")],
                [Button.url("Connect To Shortner 🔗", "https://tamizhmasters.com/member/tools/api")]]

api_message = """
<b>Which Shortner Do u Want to Connect To:</b>
"""
api_button = [[Button.url("Shorturllink.in", "https://shorturllink.in/member/tools/bookmarklet")],
              [Button.url("Playdisk.xyz", "https://playdisk.xyz/member/tools/bookmarklet")]]


about_text = """<b>

🤖 Name :  TamizhMasters Link Convertor

🔠 Language  : Python3
📚 Library   : Telethon
👑 Owner     : @Bavabee
🧑🏻‍💻 Developer : @Yali_Kk & @HMF_Owner_1

©️Powered By @simplysouth_links</b>"""
back_button = [Button.inline("⏪ Back", "back")]

