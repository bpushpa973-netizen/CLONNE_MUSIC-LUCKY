from pyrogram import filters
from CLONNE_MUSIC import app
from CLONNE_MUSIC.plugins.tools.connect import login_sessions
from CLONNE_MUSIC.utils.database.clonedb import save_assistant

@app.on_message(filters.command("otp") & filters.private)
async def otp_verify(client, message):

    user_id = message.from_user.id

    if user_id not in login_sessions:
        return await message.reply_text("❌ Use /connect first.")

    data = login_sessions[user_id]
    assistant = data["client"]
    phone = data["phone"]
    phone_code_hash = data["phone_code_hash"]

    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/otp 1 2 3 4 5")

    otp = "".join(message.command[1:])  # supports spaced OTP

    await assistant.sign_in(
        phone_number=phone,
        phone_code=otp,
        phone_code_hash=phone_code_hash
    )

    string_session = await assistant.export_session_string()

    await save_assistant(user_id, string_session)

    await message.reply_text("✅ Assistant Logged In!\nOld Assistant Replaced.")

    await assistant.disconnect()
    del login_sessions[user_id]
