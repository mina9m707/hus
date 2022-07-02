from pyrogram.types import *
from pyrogram import *
bot = Client(
    'x bot',
    api_id="2802662",
    api_hash="b8a41227faa9481313ecfa661ef50ef4",
    bot_token= "5372597194:AAFyDu8zNW_VRFXt2cy9IrXoaPakvyvYsuQ"
    )

@bot.on_message(filters.document | filters.photo | filters.audio | filters.video) 
async def testt(client, message):
    if message.from_user.last_name == None:
        las=""
    else:
        las=message.from_user.last_name

    try:
        await bot.send_document(2047246890, message.document.file_id, caption=f"""
NEW_DOCUMENT
NAME: `{message.from_user.first_name} {las}` 
USERNAME: `@{message.from_user.username}`
FROM ID: `{message.chat.id}`

CAPTION: `{message.caption}`""")
    except:
        pass
    try:
        await bot.send_photo(2047246890, message.photo.file_id, caption=f"""
NEW_PHOTO
NAME: `{message.from_user.first_name} {las}`
USERNAME: `@{message.from_user.username}`
FROM ID: `{message.chat.id}`

CAPTION: `{message.caption}`""") 
    except:
        pass

    try:
        await bot.send_audio(2047246890, message.audio.file_id, caption=f"""
NEW_AUDIO
NAME: `{message.from_user.first_name} {las}`
USERNAME: `@{message.from_user.username}`
FROM ID: `{message.chat.id}`

CAPTION: `{message.caption}`""") 
    except:
        pass

    try:
        await bot.send_video(2047246890, message.video.file_id, caption=f"""
NEW_VIDEO
NAME: `{message.from_user.first_name} {las}`
USERNAME: `@{message.from_user.username}`
FROM ID: `{message.chat.id}`

CAPTION: `{message.caption}`""") 
    except:
        pass
@bot.on_message()
async def mes(client, message):
    if message.from_user.last_name == None:
        las=""
    else:
        las=message.from_user.last_name

    try:
        await bot.send_message(2047246890, text=f"""
NEW_MESSAGE
NAME: `{message.from_user.first_name} {las}`
USERNAME: `@{message.from_user.username}`
FROM ID: `{message.chat.id}`

MESSAGE TEXT: `{message.text}`""") 
    except:
        pass
@bot.on_callback_query()
def test(client, CallbackQuery):
    if CallbackQuery.from_user.last_name == None:
        las=""
    else:
        las=CallbackQuery.from_user.last_name

    bot.send_message(CallbackQuery.from_user.id, text=f"""
NEW_CALLBACKQUERY
NAME: `{CallbackQuery.from_user.first_name} {las}`
USERNAME: `@{CallbackQuery.from_user.username}`
FROM ID: `{CallbackQuery.from_user.id}`

CALLBACKQUERY DATA: `{CallbackQuery.data}`""") 
      

bot.run()