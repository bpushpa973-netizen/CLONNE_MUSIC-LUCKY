from pyrogram import filters
from CLONNE_MUSIC import app
from CLONNE_MUSIC.utils.database.clonedb import save_assistant

@app.on_message(filters.command("setstring") & filters.private)
async def set_string(client, message):

    bot = await client.get_me()
    bot_id = bot.id

    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/setstring SESSION")

    string = message.text.split(None, 1)[1]

    await save_assistant(bot_id, string)

    await message.reply_text("Assistant String Saved ✅")
