from motor.motor_asyncio import AsyncIOMotorClient
from configs import Config

client = AsyncIOMotorClient(Config.DATABASE_URI)
db = client[Config.BOT_USERNAME]
col = db["users"]

async def get_user(user_id):

    user_id = int(user_id)

    user = await col.find_one({"user_id": user_id})

    if not user:
        res = {
            "user_id": user_id,
            "shortener_api": None,
        }

        await col.insert_one(res)
        user = await col.find_one({"user_id": user_id})

    return user

async def update_user_info(user_id, value:dict):
    user_id = int(user_id)
    myquery = {"user_id": user_id}
    newvalues = { "$set": value }
    await col.update_one(myquery, newvalues)

async def total_users_count():
    count = await col.count_documents({})
    return count

async def get_all_users():
    all_users = col.find({})
    return all_users

async def delete_user(user_id):
    await col.delete_one({'user_id': int(user_id)})

