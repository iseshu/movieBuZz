import requests
import json
import os
bot_token = os.environ.get('BOT_TOKEN') 
channel_id = os.environ.get('CHANNEL_ID')
bot_username = os.environ.get('BOT_USERNAME')
website_url = os.environ.get('WEBSITE_URL')
url = "https://api.telegram.org/bot{}/{}"
start_inline = {
    'inline_keyboard': [
        [{'text': 'MovieBuZz Website', 'url': website_url}],
        [
            {'text': 'Join Channel', 'url': 'https://t.me/yssprojects'},
            {'text': 'Share', 'url': f'tg://msg_url?url=https://t.me/{bot_username}'}
        ]
    ]
}

def telegram(data):
    chat_id = data['message']['from']['id']
    name = data['message']['from']['first_name']
    text = data['message']['text']
    if '/start id' in text:
        id = text.replace('/start id','')
        file_inline = {'inline_keyboard': [
        [{'text': 'Share', 'url': f'tg://msg_url?url=https://t.me/{bot_username}?start=id{id}'}],
        [
            {'text': 'MovieBuZz Website', 'url': website_url},
            {'text': 'Join Channel', 'url': 'https://t.me/yssprojects'}            
        ]
        ]
        }
        parms = {
            'chat_id':chat_id,
            'from_chat_id':channel_id,
            'message_id':id,
            'reply_markup':json.dumps(file_inline)
        }
        requests.post(url.format(bot_token,'copyMessage'),params=parms)
    else:
        message = f"Hello **{name}**,\nWelcome to MovieBuZz Bot\nI'm just file sender bot for the MovieBuZz Website\nFor more movies visit MovieBuZz Website"
        parms = {'chat_id':chat_id,
                 'text':message,
                 'parse_mode':'markdown',
                 "reply_markup":json.dumps(start_inline)
                }
        requests.post(url.format(bot_token,'sendMessage'),params=parms)
    