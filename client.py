from configs import config

client = TelegramClient('ShortUrlLink', API_ID, API_HASH).start(
    bot_token=BOT_TOKEN)

