# 
# Telegram Script 
# 
# by @AlekseyForWork
#
# Telegram Channel - t.me/AlekseyDevelop

from pyrogram import Client

api_id =  
api_hash = "" 
session_name = 'userbot'

with Client(session_name, api_id, api_hash) as app:
    dialogs = app.get_dialogs()

    # Считаем количество чатов, групп и каналов
    chats_count = 0
    groups_count = 0
    channels_count = 0
    for dialog in dialogs:
        if str(dialog.chat.type) == 'ChatType.PRIVATE':
            chat_id = dialog.chat.id
            messages = app.get_chat_history(chat_id)

            # Получите список идентификаторов сообщений
            message_ids = [message.id for message in messages]
            app.delete_messages(chat_id, message_ids)
            print('Чат удален') # Можно убрать, принт замедляет время работы.
