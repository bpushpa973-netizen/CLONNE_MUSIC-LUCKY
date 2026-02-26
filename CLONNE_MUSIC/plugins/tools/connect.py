from pyrogram import Client, filters
from CLONNE_MUSIC import app
from config import API_ID, API_HASH

login_sessions = {}

@app.on_message(filters.command("connect") & filters.private)
async def connect_assistant(client, message):

    bot = await client.get_me()
    bot_id = bot.id

    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/connect +91XXXXXXXXXX")

    phone = message.command[1]

    msg = await message.reply_text("📲 Sending OTP...")

    assistant = Client(
        name=f"assistant_login_{bot_id}",
        api_id=API_ID,
        api_hash=API_HASH,
        device_model="CLONNE_MUSIC Assistant",
        system_version="v2",
        app_version="Assistant Login"
    )

    await assistant.connect()

    sent_code = await assistant.send_code(phone)

    login_sessions[bot_id] = {
        "client": assistant,
        "phone": phone,
        "phone_code_hash": sent_code.phone_code_hash
    }

    await msg.edit("OTP sent ✅\nSend:\n/otp 1 2 3 4 5")
