from pyrogram import Client
from config import API_ID, API_HASH
from CLONNE_MUSIC.utils.database.clonedb import get_assistant

assistants = {}

async def load_assistant(user_id):

    if user_id in assistants:
        return assistants[user_id]

    string = await get_assistant(user_id)

    if not string:
        return None

    assistant = Client(
        string,
        api_id=API_ID,
        api_hash=API_HASH,
        device_model="CLONNE_MUSIC Assistant",
        system_version="v2",
        app_version="Assistant Login"
    )

    await assistant.start()
    assistants[user_id] = assistant

    return assistant
