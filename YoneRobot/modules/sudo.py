import html

from typing import List

from telegram import Update, Bot
from telegram.ext import CommandHandler, Filters
from telegram.ext.dispatcher import run_async

from YoneRobot import dispatcher, SUDO_USERS, OWNER_USERNAME, OWNER_ID
from YoneRobot.modules.helper_funcs.extraction import extract_user
from YoneRobot.modules.helper_funcs.chat_status import bot_admin


@bot_admin
@run_async
def sudopromote(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    banner = update.effective_user
    user_id = extract_user(message, args)
    
    if not user_id:
        message.reply_text("ʙʜᴀɪʏᴀ ᴛᴀɢ ᴋʀʟᴏ ᴋɪsɪ ᴋᴏ..👀")
        return ""
        
    if int(user_id) == OWNER_ID:
        message.reply_text("ᴅᴇᴠᴛᴀ ʜ ᴠᴏ ᴍᴇʀᴇ ᴏʀ ᴛᴇʀᴇ ʙᴀᴀᴘ..🤣")
        return ""
        
    if int(user_id) in SUDO_USERS:
        message.reply_text("ᴀʟʀᴇᴀᴅʏ sᴜᴅᴏ ᴜsᴇʀ ʜ ᴠᴏ ʙʜᴀɪɪ..")
        return ""
    
    with open("sudo_users.txt","a") as file:
        file.write(str(user_id) + "\n")
    
    SUDO_USERS.append(user_id)
    message.reply_text("ᴋʀᴅɪʏᴀ ᴀᴅᴅ sᴜᴅᴏ ᴍ.. ᴀʙʙ 500$ ᴅᴇ @Its_JassManak ᴋᴏ..")
        
    return ""

@bot_admin
@run_async
def sudodemote(bot: Bot, update: Update, args: List[str]):
    message = update.effective_message
    user_id = extract_user(message, args)
    
    if not user_id:
        message.reply_text("ʙʜᴀɪʏᴀ ᴛᴀɢ ᴋʀʟᴏ ᴋɪsɪ ᴋᴏ..👀")
        return ""

    if int(user_id) == OWNER_ID:
        message.reply_text("ᴅᴇᴠᴛᴀ ʜ ᴠᴏ ᴍᴇʀᴇ ᴏʀ ᴛᴇʀᴇ ʙᴀᴀᴘ..🤣")
        return ""
    
    if user_id not in SUDO_USERS:
        message.reply_text("{} ʏᴇ ʙʜᴀɪ sᴜᴅᴏ ᴜsᴇʀ ɴɪ ʜᴀɪ..".format(user_id))
        return ""

    users = [line.rstrip('\n') for line in open("sudo_users.txt")]

    with open("sudo_users.txt","w") as file:
        for user in users:
            if not int(user) == user_id:
                file.write(str(user) + "\n")

    SUDO_USERS.remove(user_id)
    message.reply_text("ʙʜᴋᴋ ʙsᴅᴋ.. ɴɪᴋᴀʟʟ ᴘʜʟɪ ғᴜʀsᴀᴛ ᴍ..")
    
    return ""


__help__ = """
*Bot owner only:*
 - /sudopromote: promotes the user to SUDO USER
 - /sudodemote: demotes the user from SUDO USER
"""

__mod_name__ = "SUDO"

SUDOPROMOTE_HANDLER = CommandHandler("sudopromote", sudopromote, pass_args=True, filters=Filters.user(OWNER_ID))
SUDODEMOTE_HANDLER = CommandHandler("sudodemote", sudodemote, pass_args=True, filters=Filters.user(OWNER_ID))

dispatcher.add_handler(SUDOPROMOTE_HANDLER)
dispatcher.add_handler(SUDODEMOTE_HANDLER)
