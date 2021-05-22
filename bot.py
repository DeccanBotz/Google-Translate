import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.types import CallbackQuery
from google_trans_new import google_translator
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

Deccan = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
START_TEXT = """
Hello {}, 
I am Google Translater bot ✌

Send me a word/sentence. I will Translate it to you ✅

Click help for more details..

Made With ❤ By @Deccan_Botz 
"""
HELP_TEXT = """
Hey, 
It's not complicated 🤭

Follow these steps..

☛ Just send me a Word/Sentence/Paragraph.

☛ Select the Language and I will translate it you!

<b><u>Languages :-</u></b>

English, Tamil, Telugu, Hindi, Kannada, Malayalam, Urdu, Punjabi, Spanish, Korean, Japanese, Chinese, Greek, Italian, Vietnamese, Nepali
 
Made With ❤ By @Deccan_Botz
"""
ABOUT_TEXT = """
⭕️<b>🤖 My Name : Google Translater Bot</b>

⭕️<b>📝 Language :</b> <code>Python3</code>

⭕️<b>📚 Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a>

⭕️<b>📡 Hosted on :</b> <a href='https://heroku.com/'>Heroku</a>

⭕️<b>👥 Support Group :</b> <a href='https://t.me/Deccan_Supportz'>Deccan Support</a>

⭕️<b>📢 Updates Channel :</b> <a href='https://t.me/Deccan_Botz'>Deccan Bots</a>
"""

DONATE_TEXT = """❤ Thanks for Clicking Donate Command ❤

The bot is free to use and always will be!
But running this bot on server costs money, If you like this bot and want it to keep running, please support.

To donate you can choose any of these options and send any amount that you wish.

Made With ❤ By @Deccan_Botz
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚜ Channel ⚜', url='https://telegram.me/Deccan_Botz'),
        InlineKeyboardButton('⚜ Group ⚜', url='https://telegram.me/Deccan_Supportz'),
        InlineKeyboardButton('🗣 Feedback', url='https://telegram.me/ContactDCBot')
        ],[
        InlineKeyboardButton('⚙ Help', callback_data='help'),
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('✖ Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('🤖 About', callback_data='about'),
        InlineKeyboardButton('✖ Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('⚙ Help', callback_data='help'),
        InlineKeyboardButton('✖ Close', callback_data='close')
        ]]
    )
DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('PayPal', url='https://paypal.me/MJ8506'),
        InlineKeyboardButton('cryptocurrency', url='https://bit.ly/2RkT8SD')
        ],[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('✖ Close', callback_data='close')
        ]]
    )
@Deccan.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.translate_text()

@Deccan.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await update.reply_text(
        text=DONATE_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=DONATE_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
	
@Deccan.on_message(filters.text & filters.private )
def echo(client, message):
 
 keybord = InlineKeyboardMarkup( [
        [
            InlineKeyboardButton("English", callback_data='en'),
            InlineKeyboardButton("Tamil", callback_data='ta'),
            InlineKeyboardButton("Telugu",callback_data='te')
        ],
        [   InlineKeyboardButton("Hindi", callback_data='hi'),
        InlineKeyboardButton("Kannada", callback_data='kn'),
        InlineKeyboardButton("Malayalam",callback_data= 'ml')
        ],
        [InlineKeyboardButton("Urdu", callback_data ='ur'),
	InlineKeyboardButton("Punjabi", callback_data='pa'),
	InlineKeyboardButton("Spanish", callback_data='es')
	],
        [InlineKeyboardButton("Korean", callback_data='ko'),
         InlineKeyboardButton("Japanese", callback_data='ja'),
         InlineKeyboardButton("Chinese", callback_data='zn-cn')
        ],
        [InlineKeyboardButton("Greek", callback_data='el'),
         InlineKeyboardButton("Italian", callback_data='it'),
         InlineKeyboardButton("Nepali", callback_data='ne')
        ]
    ]
 
 )

 
 message.reply_text("Select language 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    
@Deccan.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = google_translator()
  translated_text = translator.translate(tr_text,lang_tgt=cbdata)
  await update.message.edit(translated_text)
  	

Deccan.run()
