# © MrkillerDeveloper 
# © https://t.me/Hpbot_update
# © https://t.me/HP_Bot_discuss_group



from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from edit_me import Config

cbot = Client(
    "Maintenance-Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)



BOT_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="Channel", url=f"{Config.CHANNEL_LINK}"),
            InlineKeyboardButton(text="Developer", url=f"https://t.me/{Config.DEV_ID}"),
        ]
    ]
)


@cbot.on_message(filters.private)
async def start(bot, update):
    text = Config.BOT_TEXT.format(update.from_user.mention)
    reply_markup = BOT_BUTTONS
    await update.reply_text(
        text=text, disable_web_page_preview=True, reply_markup=reply_markup, quote=True
    )

cbot.run()
