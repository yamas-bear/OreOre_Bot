import json
import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json','r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

data = requests.get('https://note.com/api/v2/notes')
data_number = random.randint(0,19)
data = data.json()['data']['contents'][data_number]
name = data['name']
username = data['user']['name']
urlname = data['user']['urlname']
key = data['key']

def main():
    USER_ID = info['USER_ID']
#     messages = TextSendMessage(text="おっはモーニング\nもう無理限界。\n牛丼の出汁がきいたあの香りにつられて吉野屋に来た。")
    messages = TextSendMessage(text="おっはモーニング\n今日のオススメ記事だよ。\n「{}-{}」\nhttps://note.com/{}/n/{}".format(name,username,urlname,key))
    line_bot_api.push_message(USER_ID,messages=messages)

if __name__ == "__main__":
    main()