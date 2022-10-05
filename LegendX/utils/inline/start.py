from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from LegendX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀🎼ADD ME TO YOUƦ GƦOUᴩ🎼🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ʜᴇʟᴘ🎼🥀",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🥀🎼ꜱᴇᴛᴛɪɴɢꜱ🎼🥀", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ᴏᴡɴᴇʀ🎼🥀", user_id=OWNER),
            InlineKeyboardButton(
                text="🥀🎼ꜱᴜᴘᴘᴏʀᴛ🎼🥀", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥀🎼ADD ME TO YOUƦ GƦOUᴩ🎼🥀",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥀🎼ʜᴇʟᴘ🎼🥀", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🥀🎼ᴍᴀɪɴᴛᴀɪɴᴇʀ🎼🥀", user_id=OWNER),
            InlineKeyboardButton(
                text="🥀🎼ꜱᴜᴘᴘᴏʀᴛ🎼🥀", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥀🎼𓊈𒆜🆂ᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜʏ🎼🥀𒆜𓊉", url=f"https://t.me/ll_OFFICIAL_LEGENDBOY_ll"
                )
        ],
     ]
    return buttons
