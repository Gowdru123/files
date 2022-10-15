from f import *
from plugins.url_shorten import *
from c import *
from database.url_db import *
from e import *

DB_URI = os.environ.get("DB_URI")
client = TelegramClient('ShortUrlLink', APP_ID, APP_HASH).start(
    bot_token=BOT_TOKEN)

