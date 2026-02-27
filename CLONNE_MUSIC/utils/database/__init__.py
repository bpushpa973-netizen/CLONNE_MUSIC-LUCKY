from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

mongo = AsyncIOMotorClient(MONGO_DB_URI)
db = mongo.CLONNE_MUSIC

clonebotdb = db.clonebots
cmode = db.cmode
async def get_cmode(chat_id):
    data = cmode.find_one({"chat_id": chat_id})
    return data.get("mode") if data else None


async def set_cmode(chat_id, mode):
    cmode.update_one(
        {"chat_id": chat_id},
        {"$set": {"mode": mode}},
        upsert=True
    )
