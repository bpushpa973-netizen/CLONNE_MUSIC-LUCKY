from pyrogram import filters
from pyrogram.enums import ParseMode, ChatType
from pyrogram.errors import MessageNotModified
from pyrogram.types import (
    InputMediaVideo,
    InputMediaPhoto,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

# ⚠️ Import paths check kar lena (aapke folder structure ke hisaab se)
from CLONNE_MUSIC import app
from CLONNE_MUSIC.utils.inline.start import private_panel
from CLONNE_MUSIC.utils.decorators.language import languageCB  # ⚠️ languageCB yahan se import hona chahiye
from strings import helpers 
from config import BANNED_USERS, OWNER_ID

BOT_USERNAME = "CLONNE_MUSIC_BOT"

start_txt = """**
✪ 𝐊𝐇𝐔𝐃 𝐁𝐀𝐍𝐀 𝐁𝐇𝐎𝐒𝐃𝐈𝐊𝐄 ✪
 
**"""

@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
            [ 
            InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ʙᴧʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/The_LuckyX"),
             InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", url="https://t.me/LuckyXUpdate"),
             ],
     
             [
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/LuckyXSupport"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://files.catbox.moe/49eyev.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )

# ---------------------------------------------------
# 🚀 GIB SOURCE HANDLER (Video Switch)
# ---------------------------------------------------

@app.on_callback_query(filters.regex("gib_source") & ~BANNED_USERS)
@languageCB
async def gib_repo(client, CallbackQuery, _):
    await CallbackQuery.edit_message_media(
        media=InputMediaVideo(
            media="https://files.catbox.moe/rxiwb3.mp4",
            caption="**ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ᴍᴜsɪᴄ ʙᴏᴛ ᴡᴀᴛᴄʜɪɴɢ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄᴀʀᴇғᴜʟʟʏ.**"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="ᴏᴡɴ ᴄʀᴇᴀᴛᴇ ʙᴏᴛ", callback_data="the_lucky_help")],
                [InlineKeyboardButton(text="⌯ ʙᴀᴄᴋ ⌯", callback_data="settingsback_helper")]
            ]
        )
    )

# ---------------------------------------------------
# 🚀 HELP CALLBACK (Caption Edit)
# ---------------------------------------------------

@app.on_callback_query(filters.regex("the_lucky_help") & ~BANNED_USERS)
@languageCB
async def the_lucky_help_callback(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass

    keyboard = InlineKeyboardMarkup(
        [
            [
                # Waapis video par jaane ke liye
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ", 
                    callback_data="gib_source" 
                )
            ]
        ]
    )

    await CallbackQuery.edit_message_caption(
        caption=helpers.CLONE_HELP,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )
