import aiohttp
from io import BytesIO
from CLONNE_MUSIC import app
from pyrogram import filters



async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image



@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("𝑨𝒍𝒆 𝒃𝒂𝒃𝒖 𝒂𝒂𝒑 𝒃𝒉𝒊 𝒃𝒌𝒄 𝒌𝒓𝒏𝒆 𝒍𝒂𝒈𝒆 𝒂𝒃 𝒔𝒕𝒊𝒄𝒌𝒆𝒓 𝒑𝒂𝒓 𝒕𝒂𝒈 𝒌𝒓𝒌𝒆 𝒌𝒓𝒐 𝒏 /𝒎𝒎𝒇 𝒑𝒂𝒍𝒊𝒔🥺...")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("𝑨𝒍𝒆 𝒃𝒂𝒃𝒖 𝒂𝒂𝒑 𝒃𝒉𝒊 𝒃𝒌𝒄 𝒌𝒓𝒏𝒆 𝒍𝒂𝒈𝒆 𝒂𝒃 𝒔𝒕𝒊𝒄𝒌𝒆𝒓 𝒑𝒂𝒓 𝒕𝒂𝒈 𝒌𝒓𝒌𝒆 𝒌𝒓𝒐 𝒏 /𝒎𝒎𝒇 𝒑𝒂𝒍𝒊𝒔🥺...")
    text = await message.reply("𝑨𝒍𝒆 𝒘𝒂𝒊𝒕 𝒕𝒐 𝒌𝒂𝒍𝒐 𝒏𝒂 𝒃𝒂𝒃𝒖 🤭 𝒃𝒂𝒏 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊 🫣...")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit("𝑨𝒍𝒆 𝒘𝒂𝒊𝒕 𝒕𝒐 𝒌𝒂𝒍𝒐 𝒏𝒂 𝒃𝒂𝒃𝒖 🤭 𝒃𝒂𝒏 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊 🫣...")
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()
