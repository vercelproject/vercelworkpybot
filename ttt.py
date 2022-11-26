from telethon import TelegramClient
from telethon import TelegramClient, events
from datetime import datetime
from datetime import timedelta
import time

token='5429424084:AAFtRnWXgwYCQoEbZYW5sp50arZUStFYzPI'
api_id = 16364839
api_hash = '437dccac05784e2236b0e541a54cd5be'
chat_id = '1741415210'
chat = 'Data'

YurikJr = 0
Tanya = 0
Vitalii = 0
Maksym = 0
Galya = 0
Yurii = 0
prevNum = 0

bot=TelegramClient('bot', api_id, api_hash).start(bot_token=token)
client = TelegramClient('seion_name', api_id, api_hash)
client.start()

client.connect()

print('0')

async def startCount():
    global YurikJr, Tanya, Vitalii, Maksym, Galya, Yurii, prevNum
    YurikJr = 0
    Tanya = 0
    Vitalii = 0
    Maksym = 0
    Galya = 0
    Yurii = 0
    prevNum = 0
    async def my_function(text):
        global YurikJr, Tanya, Vitalii, Maksym, Galya, Yurii, prevNum

        text.upper()
        num = int(text.split(" ")[0])
        id = text.split(" ")[1]
        if id == 'Ю':
            YurikJr += num - int( prevNum)
            prevNum = int(num)
        elif id == 'Т':
            Tanya += num - int(prevNum)
            prevNum = int(num)
        elif id == 'В':
            Vitalii += num - int(prevNum)
            prevNum = int(num)
        elif id == 'М':
            Maksym += num - int(prevNum)
            prevNum = int(num)
        elif id == 'Г':
            Galya += num - int(prevNum)
            prevNum = int(num)
        elif id == 'С':
            Yurii += num - int(prevNum)
            prevNum = int(num)




    chats = client.get_dialogs
    messages = await client.get_messages('Data', limit=200, reverse = False)
    print("mes")
    messages.reverse()
    for message in messages:
        date = message.date + timedelta(hours=2)
        text = message.text.replace("*", "")

        if date.day == datetime.now().day:    
            await my_function(text)
        else:
            prevNum = text.split(" ")[0]
    print(prevNum)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await startCount()
    await event.respond(str(Maksym) + ' М')
    await event.respond(str(Tanya) + ' Т')
    await event.respond(str(Yurii) + ' С')
    await event.respond(str(YurikJr) + ' Ю')
    await event.respond(str(Galya) + ' Г')
    await event.respond(str(Vitalii) + ' В')


    
def main():
    bot.run_until_disconnected()    
if __name__ == '__main__':
    main()



print(str(YurikJr) + ' Ю    ',str(Tanya) +' Т    ', str(Vitalii) + ' В    ', str(Maksym) + ' М    ', str(Galya) + ' Г    ', str(Yurii) + ' С    ')
messages = ["Hello i am working"]
print(messages)
client.run_until_disconnected()