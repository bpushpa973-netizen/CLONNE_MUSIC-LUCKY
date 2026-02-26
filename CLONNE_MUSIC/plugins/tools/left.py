from CLONNE_MUSIC import app
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio

# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)

# --------------------------------------------------------------------------------- #
# PERFECT CIRCLE FIT TEMPLATE SYSTEM
# --------------------------------------------------------------------------------- #

async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path).convert("RGBA")

    # --- Template exact circle position ---
    circle_size = 420                # Real neon circle dimension
    circle_center_x = 680            # X center of circle in your template
    circle_center_y = 390            # Y center of circle in your template

    paste_x = circle_center_x - (circle_size // 2)
    paste_y = circle_center_y - (circle_size // 2)

    # --- Process & paste user's profile image ---
    if profile_path:
        img = Image.open(profile_path).convert("RGBA")
        img = img.resize((circle_size, circle_size))

        mask = Image.new("L", (circle_size, circle_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, circle_size, circle_size), fill=255)

        circular_img = Image.new("RGBA", (circle_size, circle_size), (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)

        bg.paste(circular_img, (paste_x, paste_y), circular_img)

    # Write User ID (optional)
    draw = ImageDraw.Draw(bg)
    draw.text(
        (180, 665),
        text=str(user_id).upper(),
        font=get_font(60, font_path),
        fill=(255, 0, 0),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path


# --------------------------------------------------------------------------------- #

bg_path = "CLONNE_MUSIC/assets/userinfo.png"
font_path = "CLONNE_MUSIC/assets/hiroko.ttf"

# --------------------------------------------------------------------------------- #


@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):

    # Detect if user left
    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {"banned", "left", "restricted"}
        and member.old_chat_member
    ):
        pass
    else:
        return

    user = (
        member.old_chat_member.user
        if member.old_chat_member
        else member.from_user
    )

    # Has profile pic?
    if user.photo and user.photo.big_file_id:
        try:
            photo = await app.download_media(user.photo.big_file_id)

            # Create final neon-circle image
            welcome_photo = await get_userinfo_img(
                bg_path=bg_path,
                font_path=font_path,
                user_id=user.id,
                profile_path=photo,
            )

            caption = (
                f"**#New_Member_Left**\n\n"
                f"**๏** {user.mention} **ʜᴀs ʟᴇғᴛ ᴛʜɪs ɢʀᴏᴜᴘ**\n"
                f"**๏ sᴇᴇ ʏᴏᴜ sᴏᴏɴ ᴀɢᴀɪɴ..!**"
            )

            deep_link = f"tg://openmessage?user_id={user.id}"

            message = await client.send_photo(
                chat_id=member.chat.id,
                photo=welcome_photo,
                caption=caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("๏ ᴠɪᴇᴡ ᴜsᴇʀ ๏", url=deep_link)]
                ])
            )

            # Auto delete after 30 sec
            async def delete_message():
                await asyncio.sleep(30)
                await message.delete()

            asyncio.create_task(delete_message())

        except RPCError as e:
            print(e)
            return

    else:
        print(f"User {user.id} has no profile photo.")