import os
import requests

token = os.getenv('TELE_TOKEN')
method = 'getUpdates'

#c9에서 telegram 안됨
url = "https://api.hphk.io/telegram/bot{}/{}".format(token,method)

res = requests.get(url).json()

res = requests.get(url).json()

user_id = res["result"][0]["message"]['from']['id']
msg = "서희수 ㅄ"
method = 'sendMessage'

msg_url = "https://api.hphk.io/telegram/bot{}/{}?chat_id={}&text={}".format(token,method,user_id,msg)
print(msg_url)
requests.get(msg_url)