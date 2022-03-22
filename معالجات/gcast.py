# Copyright (C) 2021 By Sumityadav

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from modules.callsmusic.callsmusic import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["اذاعه"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`بدء الاذاعه♥ ...`")
        if not message.reply_to_message:
            await wtf.edit("**__من فضـلك قـم بالرد علي رسـاله لاذعـاتها...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`احصائيات` \n\n**تم الارسـال الي:** `{sent}` مجموعه \n**فشل الارسال في:** {failed} مجموعه")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`احصائيات \n\n**تـم الارسال الي:** `{sent} مجموعه \n**فشل الارسال في:** {failed} مجموعه")
