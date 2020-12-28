import json
import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

data = requests.get('https://note.com/api/v2/notes')
name = data.json()['data']['contents'][0]['user']['urlname']
key = data.json()['data']['contents'][0]['key']

def main():
    USER_ID = info['USER_ID']
#     messages = TextSendMessage(text="おっはモーニング\nもう無理限界。\n牛丼の出汁がきいたあの香りにつられて吉野屋に来た。")
    messages = TextSendMessage(text="おっはモーニング\n今日のオススメ記事だよ。\nhttps://note.com/{}/n/{}".format(name,key))
    line_bot_api.push_message(USER_ID,messages=messages)

if __name__ == "__main__":
    main()