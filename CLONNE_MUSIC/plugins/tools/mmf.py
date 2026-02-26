
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from CLONNE_MUSIC import app

@app.on_message(filters.command("mmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        await message.reply_text("𝑨𝒍𝒆 𝒃𝒂𝒃𝒖 𝒂𝒂𝒑 𝒃𝒉𝒊 𝒃𝒌𝒄 𝒌𝒓𝒏𝒆 𝒍𝒂𝒈𝒆 𝒂𝒃 𝒔𝒕𝒊𝒄𝒌𝒆𝒓 𝒑𝒂𝒓 𝒕𝒂𝒈 𝒌𝒓𝒌𝒆 𝒌𝒓𝒐 𝒏 /𝒎𝒎𝒇 𝒑𝒂𝒍𝒊𝒔🥺...")
        return

    msg = await message.reply_text("𝑨𝒍𝒆 𝒘𝒂𝒊𝒕 𝒕𝒐 𝒌𝒂𝒍𝒐 𝒏𝒂 𝒃𝒂𝒃𝒖 🤭 𝒃𝒂𝒏 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊 🫣...")
    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    meme = await drawText(file, text)
    await app.send_document(chat_id, document=meme)

    await msg.delete()

    os.remove(meme)


async def drawText(image_path, text):
    img = Image.open(image_path)

    os.remove(image_path)

    i_width, i_height = img.size

    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "./CLONNE_MUSIC/assets/font.ttf"

    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))

    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""

    draw = ImageDraw.Draw(img)

    current_h, pad = 10, 5

    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            uwl, uht, uwr, uhb = m_font.getbbox(u_text)
            u_width, u_height = uwr - uwl, uhb - uht

            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )

            current_h += u_height + pad

    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            uwl, uht, uwr, uhb = m_font.getbbox(l_text)
            u_width, u_height = uwr - uwl, uhb - uht

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )

            current_h += u_height + pad

    image_name = "memify.webp"

    webp_file = os.path.join(image_name)

    img.save(webp_file, "webp")

    return webp_file


__mod_name__ = "mmf"
