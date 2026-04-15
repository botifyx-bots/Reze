from pyrogram import Client, enums

import Reze.strings as strings
from Reze import custom_filter
from Reze.helper.chat_status import isUserCan
from Reze.mongo.blocklists_mongo import setblocklistreason_db
from Reze.pyro.connection.connection import connection
from Reze.utils.decorators import *


@Client.on_message(custom_filter.command(commands="resetblocklistreason"))
@anonadmin_checker
async def resetblocklistreason(client, message):
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, chat_id=chat_id, privileges="can_change_info"):
        return

    await setblocklistreason_db(chat_id, None)
    await message.reply("The default blocklist reason has been reset.")
