from pyrogram import Client, enums

import Reze.strings as strings
from Reze import custom_filter
from Reze.helper.chat_status import isUserCan
from Reze.mongo.rules_mongo import set_rule_button
from Reze.pyro.connection.connection import connection
from Reze.utils.decorators import *


@Client.on_message(custom_filter.command(commands="resetrulesbutton"))
@anonadmin_checker
async def reset_rules(client, message):
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if (
        not str(chat_id).startswith("-100")
        and message.chat.type == enums.ChatType.PRIVATE
    ):
        return await message.reply(strings.is_pvt)

    if not await isUserCan(message, privileges="can_change_info"):
        return

    await set_rule_button(chat_id, "Rules")
    await message.reply("Reset the rules button name to default", quote=True)
