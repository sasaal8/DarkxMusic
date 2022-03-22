import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/31a1aaad8469d8bdb2380.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
يتيح لك تشغيل الموسيقى والفيديو في المجموعات من خلال المكالمات الجديدة في تيلجرام 🎶!..
  💡 تعلم طريقة تشغيلي واوامر التحكم بي عن طريق الضغط علي زر  » 📚 الاوامر!  ......
┏━━━━━━━━━━━━━━━━━┓
┣★ [قـناه السـورسᐬ](https://t.me/L_S_A_V_O)
┣★ [مبـرمج السـورسᐬ](https://t.me/s_a_s_a_3li)
┣★ [جـروب الـدعمᐬ](https://t.me/D_E_V_S_A_V_O)
┣★ [الاوامـرᐬ](https://t.me/DEV_SAVO/28)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ قـم باضفتـي لـ مجمـوعتك ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "سورس", "السورس"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f3093920ea300f8851389.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "لتنـصيب بوت ع سورس سافو♥", url=f"https://t.me/s_a_s_a_3li")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["المطور","مطور", "سافو ميوزك", "مطوري", "يا سورس","سافو"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/31a1aaad8469d8bdb2380.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مبرمج السورس لو عوزت حاجه♥"", url=f"https://t.me/s_a_s_a_3li")
                ]
            ]
        ),
    )
