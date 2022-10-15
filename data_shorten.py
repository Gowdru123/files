from pymongo import MongoClient
from configs import Config

myclient = MongoClient(DATABASE_URL)
db = myclient['mydb']
apiDB = db['api']


async def info_taker(chat):
    data = apiDB.find_one({"chat": chat})
    if data is None:
        return False, False
    print(data)
    api = data['api']
    return api


async def api_logger(chat, api):
    data = apiDB.find_one({"chat": chat})

    if data is None:
        apiDB.insert_one({"chat": chat, "api": api})
    else:
        apiDB.delete_one(data)
        apiDB.insert_one({"chat": chat, "api": api})

