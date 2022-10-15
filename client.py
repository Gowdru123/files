from c import *
from f import *
from data_shorten import *
from shorten_link import *
from link_shorten import *

client = TelegramClient('ShortUrlLink', APP_ID, API_HASH).start(
    bot_token=BOT_TOKEN)

