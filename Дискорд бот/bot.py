from dataclasses import replace
from multiprocessing.sharedctypes import Value
import os
import re
import time
from tracemalloc import start
import requests
import discord
import random
from discord.ext import commands
from bs4 import BeautifulSoup
from asyncio import sleep
import wikipedia
from datetime import datetime
import googletrans
from googletrans import Translator
from discord.utils import get

TOKEN = "MTAzOTk1MDAzODAxMDQzMzUzNg.GESEoz.pw9-OTokveEW7v2DeGlRKnFoZGOaM4PN6UH76o"
intents = discord.Intents.all()
client = commands.Bot(command_prefix=',', intents=intents)
translator = Translator()

@client.event
async def on_ready():
    print('Бот был успешно запущен как {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game(" Искусственный интеллект"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'private' in str(message.channel.type).lower():
        await message_taked(message,1)
    else:
        if message.channel.id == 1041767659894743171:
            await message_taked(message,2)
        try:
            category = message.channel.category.name
        except:
            category = 0
        else:
            category = message.channel.category.name
            if category == 'Console':
                msgconsole = str(message.content).split(' ')
                if msgconsole[0] == 'msg':
                    if len(str(message.content)) > 4:
                        msgcontent = str(message.content)[4:]
                        if message.channel.id != 1043196525037244436:
                            user = str(message.channel.name).split(' ')[2]
                            user = client.get_user(int(user))
                        else:
                            user = client.get_channel(1041767659894743171)
                        mymsg = await user.send(msgcontent)
                        mymsg = mymsg.id
                        if message.channel.id != 1043196525037244436:
                            await message.channel.send(f'Я отправил сообщение пользователю {user.mention}:\n>>> ' + msgcontent + f'\n*({mymsg})*')
                        else:
                            await message.channel.send(f'Я отправил сообщение в общий чат со мной:\n>>> ' + msgcontent + f'\n*({mymsg})*')
                    else:
                        await message.channel.send(f'Команда **msg** должен принимать *1* аргумент.\n- **msg <сообщение для отправки>**.')
                elif msgconsole[0] == 'cmds':
                    await message.channel.send(f'Список всех команд:\n\n> **cmds** - список команд.\n\n> **msg <сообщение для отправки>** - отправить сообщение пользователю.\n\n> **edit <айди сообщения> <сообщение для изменения>** - изменить сообщение по айди.\n\n**delete <айди сообщения>** - удалить сообщение по айди.')
                elif msgconsole[0] == 'edit':
                    if len(msgconsole) >= 3:
                        if message.channel.id != 1043196525037244436:
                            user = client.get_user(int(str(message.channel.name).split(' ')[2]))
                        else:
                            user = client.get_channel(1041767659894743171)
                        msgsplited = str(message.content).split(" ",2)
                        try:
                            messageedit = await user.fetch_message(int(msgconsole[1]))
                        except:
                            await message.channel.send(f'Сообщения по айди **{msgsplited[1]}** не существует.')
                        else:
                            messageedit = await user.fetch_message(int(msgsplited[1]))
                            try:
                                await messageedit.edit(content=msgsplited[2])
                            except:
                                await message.channel.send(f'Ошибка изменения сообщения:\n**Нельзя изменять сообщения других пользователей.**')
                            else:
                                await message.channel.send(f'Я успешно изменил сообщение:\n>>> {messageedit.content}')
                                await message.channel.send(f'На:\n>>> {msgsplited[2]}\n*({msgsplited[1]})*')
                                await messageedit.edit(content=msgsplited[2])
                    else:
                        await message.channel.send('Команда **edit** должна иметь *2* аргумента.\n- **edit <айди сообщения> <новый текст сообщения>**')
                elif msgconsole[0] == 'delete':
                    if len(msgconsole) >= 2:
                        if message.channel.id != 1043196525037244436:
                            user = client.get_user(int(str(message.channel.name).split(' ')[2]))
                        else:
                            user = client.get_channel(1041767659894743171)
                        try:
                            messageedit = await user.fetch_message(int(msgconsole[1]))
                        except:
                            await message.channel.send(f'Сообщения по айди **{msgconsole[1]}** не существует.')
                        else:
                            if messageedit.author != client.user and messageedit.channel.id != 1041767659894743171:
                                await message.channel.send(f'Ошибка удаления сообщения:\n**Нельзя удалять сообщения других пользователей в ЛС.**')
                            else:
                                messageedit = await user.fetch_message(int(msgconsole[1]))
                                await message.channel.send(f'Я удалил сообщение:\n>>> {messageedit.content}')
                                await messageedit.delete()
                    else:
                        await message.channel.send('Команда **delete** должна иметь *1* аргумент.\n- **delete <айди сообщения>**')
                elif msgconsole[0] == 'ans':
                    if message.channel.id != 1043196525037244436:
                        if len(msgconsole) >= 2:
                            user = client.get_user(int(str(message.channel.name).split(' ')[2]))
                            await user.send(f'**ПРЕДУПРЕЖДЕНИЕ:**\n**Причина: **{str(message.content)[4:]}')
                        else:
                            await message.channel.send('Команда **ans** для личных сообщений имеет 1 аргумент\nПомощь - **ans <причина>**')
                    else:
                        if len(msgconsole) >= 3:
                            msgcontent = str(message.content).split(' ',2)
                            message.delete()
                            user = client.get_channel(1043196525037244436)
                            user.send(f'{msgconsole[1]}\n**ПРЕДУПРЕЖДЕНИЕ:**\n**Причина: **{msgcontent[2]}')
                        else:
                            await message.channel.send('Команда **ans** для общего чата имеет 2 аргумента\nПомощь - **ans <пользователь> <причина>**')
                else:
                    await message.channel.send(f'Команды **{msgconsole[0]}** не существует.\n> Список всех команд - **cmds**.')
async def message_taked(message,type):
    path = f"users\{message.author.id}.txt"
    if not os.path.exists(path):
        file = open(f'{path}','w')
        file.write('0\n0\n0\n1000\n1\n0')
        file.close()
    file = open(path)
    lines = file.readlines()
    line = int(lines[5])
    if line == 0:
        await message_default(message,type)
    elif line == 1 or line == 1.1:
        await message_game_history(message,type)
    file.close()

async def message_game_history(message,type):
    if type == 1:
        sender = message.author
    elif type == 2:
        sender = client.get_channel(1041767659894743171)
    if 'хватит' == str(message.content.lower()).split(' ',1)[0] or 'завершить' == str(message.content.lower()).split(' ',1)[0]:
        if 'игр' in message.content.lower() or 'истор' in message.content.lower():
            message.channel.send(random.SystemRandom().choice([f"Хорошо, завершаем игру!", f"Окей!", f"Хорошо сыграли!"]))
            datauser(message.author.id,6,str(0))
            await message.channel.send_file(f"savedtxts\{message.author.id}.txt",filename="История",content="**Ваша история:**")

async def message_default(message,type):
    await datauseradd(message.author.id,2,1)
    randomn = random.randint(1,50)
    file = open(f'users\{message.author.id}.txt','r')
    await datauseradd(message.author.id,3,randomn)
    lines = file.readlines()
    val2 = int(lines[2])
    val = int(lines[3])
    if val2 >= val:
        await datauseradd(message.author.id,5,1)
        await datauseradd(message.author.id,4,(val-940)+int(lines[4])*10)
        await datauseradd(message.author.id,3,-val)
        chana = client.get_channel(1045044096789647521)
        await chana.send(f'**ПОВЫШЕНИЕ УРОВНЯ!** 🌟\n\n> {message.author.mention} повысил свой\n> уровень до **{lines[4]}**\n\n**ПОЗДРАВИМ ЕГО С ПОВЫШЕНИЕМ!** 👍')
    file.close()
    if type == 1:
        mymsg = message.id
        await msgconsole(f"{message.author.mention} отправил сообщение мне:\n>>> " + str(message.content) + f'\n*({mymsg})*',message.author.id)
    elif type == 2:
        channelid = 1043196525037244436
        channelid = client.get_channel(channelid)
        mymsg = message.id
        await channelid.send(f"{message.author.mention} отправил сообщение в общий чат со мной:\n>>> " + str(message.content) + f'\n*({mymsg})*')
    sendmsg = ''
    username = str(message.author).split('#')[0]
    user_message = "/😀/" + str(message.content) + "/☹️/"
    if message.author == client.user:
        return
    result = translator.translate(user_message, dest='ru')
    user_message = result.text
    langdef = result.src
    if "играем в" in user_message.lower():
        if "истори" in user_message.lower():
            datauser(message.author.id,6,str(1))
            message.channel.send('Начинаем игру **Сочиняем истории**!\n\nИ так, сначала вы пишете начало истории, затем я её продолжу, после чего вы её продолжаете и так, пока у нас не получится наша история. Завершить историю можно в любое время (Написав **завершить историю**) или пока не достигнет лимит истории - 1.000.000 символов*\n\nНу что ж, напишите начало истории.')
        else:
            message.channel.send(random.SystemRandom().choice([f"Я не знаю такой игры", f"Во что?", f"В какую игру?", f"Во что во что?","Во что именно?"]))
    if "прив" in user_message.lower() or "qq" in user_message.lower() or "здрав" in user_message.lower() or user_message.lower() == "/😀/ку/☹️/":
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Привет, {username}!", f"Ку, {username}!", f"Здравствуйте, {username}!", f"Здравия желаю, товарищ {username}!","Ооо, привет, как дела?"])
    if "пок" in user_message.lower() or "bb" in user_message.lower() or "bye" in user_message.lower() or "досвидан" in user_message.lower() or "удач" in user_message.lower() or "до свидан" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Пока, {username}!", f"Удачи, {username}!", f"bb, {username}", f"Досвидания, {username}!"])
    if " ты" in user_message.lower() or "ты?" in user_message.lower() or user_message.lower() == "/😀/ты/☹️/" or "ты!" in user_message or "ты?" in user_message:
        if "ты кт" not in user_message.lower() and "?" not in user_message.lower():
            sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ты", f"Нет, ты!", f"А я думал {user_message}"])
    if "ты " in user_message.lower():
        if "ты кт" not in user_message.lower() and "?" not in user_message.lower():
            sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"{username} сам такой", f"Сам такой :(", f"Сам {user_message.replace('ты ', '')}"])
    if "ты кт" in user_message.lower() or "тебя зовут" in user_message.lower() or "твое имя" in user_message.lower() or "твоё имя" in user_message.lower() or "кто т" in user_message.lower() or "тебя звать" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Меня зовут Искусственный интелект 2 уровня, приятно познакомиться!.", f"Я Искусственный интелект 2 уровня"])
    if "корова" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"https://i.imgur.com/YiMUiop.gif", f"https://i.imgur.com/YiMUiop.gif"])
    if "повтори " in user_message.lower():
        msgreplace = user_message
        sendmsg = sendmsg + ', ' + msgreplace.lower().replace('повтори ', '').replace('меня','тебя').replace('я ', 'ты ').replace('тебты','тебя')
    if "картинка " in user_message.lower() or "фото " in user_message.lower() or "фотография " in user_message.lower() or "картина " in user_message.lower() or "изображение " in user_message.lower() or "фотографию " in user_message.lower() or "картинку " in user_message.lower() or "картину " in user_message.lower():
        msgreplace = user_message.lower().replace('картинка ', '/разделитель/').replace('фото ', '/разделитель/').replace('фотография ', '/разделитель/').replace('картина ', '/разделитель/').replace('изображение ', '/разделитель/').replace('фотографию ', '/разделитель/').replace('картинку ', '/разделитель/').replace('картину ', '/разделитель/')
        msgreplace = msgreplace.split('/разделитель/')[1]
        msgreplace = msgreplace.split(' ')
        if len(msgreplace) == 1:
            msgreplace = msgreplace[0]
        elif len(msgreplace) >= 2:
            msgreplace = msgreplace[0] + ' ' + msgreplace[1]
        sendmessage = ""
        limitcount = 0
        while len(sendmessage) < 1 and limitcount < 10:
            limitcount = limitcount + 1
            s = requests.session()
            s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})
            r = s.get('https://www.google.ru/search?q='+ msgreplace +'&tbm=isch')
            soup = BeautifulSoup(r.text, "html.parser")
            images = soup.findAll(attrs={'class': 'wXeWr islib nfEiy'})
            sendmessage = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", str(random.choice(images)))
            if len(sendmessage) >= 1:
                sendmessage = sendmessage[0]
                sendmsg = sendmsg + ', ' + f'{sendmessage}'
            if limitcount >= 10:
                sendmsg = sendmsg + ', ' + f'Извините, мне не удалось найти картинку'
    if "бля" in user_message.lower() or "сук" in user_message.lower() or "хуй" in user_message.lower() or "хуи" in user_message.lower() or "мраз" in user_message.lower() or "хер" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Не матерись!", f"Сам такой!", f"Сам", f"Чё такой борзый?", f"Ты офигел?", f"Че за фигню ты пишишь?", "Давно не получал?"])
    if "скольк" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Тебе ещё рано об этом знать!", f"{random.randint(-1000,1000)}, а тебе?", f"{random.randint(-1000,1000)}, а вам?", f"{random.randint(-1000,1000)}, а у тебя?", f"{random.randint(-1000,1000)}, а у вас?", f"Ты ещё слишком маленький, чтобы это знать!", "Тебе не скажу","хз","не знаю","Сам ответь"])
    if "когд" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Когда рак на горе свистнет", f"{random.randint(1,30)} {random.SystemRandom().choice(['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа','какого-то там месяца'])}", f"{random.randint(1,30)} {random.SystemRandom().choice(['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа','какого-то там месяца'])} в {random.randint(0,23)}:{random.randint(10,60)}", f"в {random.randint(0,23)}:{random.randint(10,60)}", f"{random.randint(1,30)} {random.SystemRandom().choice(['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа','какого-то там месяца'])}", f"{random.randint(1900,2100)} года, {random.randint(1,30)} {random.SystemRandom().choice(['сентября','октября','ноября','декабря','января','февраля','марта','апреля','мая','июня','июля','августа','какого-то там месяца'])} в {random.randint(0,23)}:{random.randint(10,60)}", f"в {random.randint(0,23)}:{random.randint(10,60)}", f"Ты ещё слишком маленький, чтобы это знать!", "Наверно завтра", "На следующей недели","В следующем году","В следующем месяце","После завтра","В прошлом году","На прошлой неделе","Позавчера","хз","не знаю"])
    if "секс" in user_message.lower() or "гей" in user_message.lower() or "сперм" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Хватит об этом говорить", f"О боже", f"Сам", f"Может хватит?", f"Ты офигел?", f"Че за фигню ты пишишь?", "Давно не получал?"])
    if "да " in user_message.lower() or user_message.lower() == "/😀/да/☹️/" or " да/☹️/" in user_message.lower():
        if "когд" not in user_message.lower():
            sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ок, молодец", f"Ок", f"Точно?", f"Ты не перепутал?", f"Ты офигел?", f"Вау", "Пиз... дальше ты сам знаешь", "Кабзда", "Пиз..."])
    if "нет " in user_message.lower() or user_message.lower() == "/😀/нет/☹️/" or " нет" in user_message.lower():
        if "когд" not in user_message.lower():
            sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ок, молодец", f"Ок", f"Точно?", f"Ты не перепутал?", f"Ты офигел?", f"Кикиморы ответ", "Да... ответ", "Ты сел на омлет?", "Свиньи ответ"])
    if " аргумент" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Аргумент не нужен, пид.. обнаружен", f"Аргумент не нужен, да.. обнаружен", f"Аргумент не нужен, деб.. обнаружен", f"Ты не перепутал?", f"Ты офигел?", f"Какой аргумент?", "Ты мне аргументы делаешь?"])
    if "аргумент не" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Пид.. засекречен, твой анал не вечен", f"Да.. засекречен, твой анал не вечен", f"Деб.. засекречен, твой анал не вечен", f"Может это ты обнаружен?", f"Обнаружен здесь только ты", f"Ну вот правильно, ты обнаружен", "Свою уборную сначало обнаружи, а потом уже мне аргументы делай"])
    if "мать" in user_message.lower() or "матер" in user_message.lower() or "мамы" in user_message.lower() or "мама" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Про мать тут лишнее", f"Про мать лишнее"])
    if "ебал" in user_message.lower() or "сосал" in user_message.lower() or "трахал" in user_message.lower() or "соснул" in user_message.lower() or "ебани" in user_message.lower() or "сосни" in user_message.lower() or "трахни" in user_message.lower() or "соси" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Себя?", "Сначала себя сосни, а потом уже других"])
    if "ебат" in user_message.lower() or "сосат" in user_message.lower() or "нифиг" in user_message.lower() or "вау" in user_message.lower() or "нихер" in user_message.lower() or "нехер" in user_message.lower() or "нефиг" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ты там что-ли умер?", "Что такое?", "Себя в зеркале увидел?", "Свои трусы нашёл?", "Запах носков узнал?"])
    if "хаха" in user_message.lower() or "ха-ха" in user_message.lower() or "хехе" in user_message.lower() or "хе-хе" in user_message.lower() or "ха ха" in user_message.lower() or "хе хе" in user_message.lower() or "хмхм" in user_message.lower() or "мхмх" in user_message.lower() or "haha" in user_message.lower() or "ha ha" in user_message.lower() or "ha-ha" in user_message.lower() or "ahah" in user_message.lower() or "ahha" in user_message.lower() or "hehe" in user_message.lower() or "хах" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Смешно?", "Ржёшь как больной", "Че ржёшь?", "Че смеёшься?", "Грустный смех?"])
    if "?" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Нет", "Да", "Хз", "Не знаю", "Наверно","Врядли","У самого себя спроси","Да не знаю я"])
    if "пожн" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Нельзя", "Зачем?", "Конечно", "Тебе нельзя", "Тебе ещё рано","Ты ещё слишком маленький для этого","У меня не спрашивай"])
    if "поч" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Потому", "Потому что", "Потому что ты еще маленький", "Не скажу", "ПОТОМУ!","Потому что рак на горе ещё не свистнул","Потому что - потому"])
    if "зач" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Чтобы ты спросил", "У меня не спрашивай", "Я даже и не знаю", "Потому что я так решил", "Просто"])
    if "какая" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Никакая", "У меня не спрашивай", "Я даже и не знаю", "Хз"])
    if "какое" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Никакое", "У меня не спрашивай", "Я даже и не знаю", "Хз"])
    if "какой" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Никакой", "У меня не спрашивай", "Я даже и не знаю", "Хз"])
    if "какие" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Никакие", "У меня не спрашивай", "Я даже и не знаю", "Хз"])
    if "как " in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Никак", "У меня не спрашивай", "Я даже и не знаю", "Хз","Как-то","Хорошо","Плохо"])
    if "чем " in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ничем", "У меня не спрашивай", "Я даже и не знаю", "Хз","Чем-то","Рукой","Ногой","Головой"])
    if "зна" in user_message.lower() or "хз" == user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"А я знаю?", "Незнайка", "А что ты знаешь? Ничего ты не знаешь!"])
    if "сам" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Сам", "Сам такой", "Нет, сам!"])
    if "тебя" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Тебя", "Нет, тебя!", "А я думал тебя!","Всё равно тебя!","И я тебя!"])
    if "пизда" in user_message.lower() or "кабзда" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Твоя", "О, какой ты грамотный!", "твоей бабушки!"])
    if "твоей" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Твоей", "Нет, твоей!", "А я думал твоей", "Может твоей?"])
    if "тож" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Поздравляю!", "Молодец!", "Круто", "Вау!"])
    if "твоя" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Твоя", "Нет, твоя", "А я думал твоя", "Может твоя?"])
    if "мне" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"А ты мне", "МНЕ!", "Нет, мне", "Может мне?"])
    if "куда" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Хз", "Не знаю", "Ты у меня спрашиваешь?", "Далеко","Подальше от тебя","Далеко-далеко","Подальше от сюда"])
    if "бот" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Хз", "Не знаю", "Ты у меня спрашиваешь?", "А ты что думал?","Бот и бот, что дальше?","Ну хотябы умнее тебя","На себя посмотри"])
    if "ладн" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Все, слился?", "Слился?", "Слит?"])
    if "офигел" in user_message.lower() or "охирел" in user_message.lower() or "охерел" in user_message.lower() or "охуел" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Сам", "Сам офигел", "Сам охирел", "Сам охуел","Может сам?","Ты не перепутал берега?","Ты нарываешся?"])
    if " ответ" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Пи... аргумент", "Да... аргумент", "Деби... аргумент", "Ответ не нужен, пи... обнаружен","Ответ не нужен, да... обнаружен","Ответ не нужен, деби... обнаружен","Ты нарываешся?"])
    if "ясно" in user_message.lower() or "пон" in user_message.lower() or "окей" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Да что тут понятного?", "Да что тут ясного?", "Нет, ничего не ясно и не понятно", "Ничего не ясно и не понятно","А я вот не понял","А вот мне не ясно!","Что?"])
    if "ничег" in user_message.lower() or "нечег" in user_message.lower() or "ни чег" in user_message.lower() or "не чег" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ничего не бывает!", "Почему ничего?", "Ты издеваешься?", "Почему?","Как так?","Скажи правду!","?"])
    if "медвеж" in user_message.lower() or "ии" in user_message.lower() or "искуственый" in user_message.lower() or "искусственный" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Что?", "Да чего?", "а?", "?","Что надо?","Что хотел?","м?"])
    if "грустный" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Да, я грустный!", "Да я грустный", "Ну да, грустный", "Грустно :("])
    if "хорош" in user_message.lower() or "плох" in user_message.lower() or "скучн" in user_message.lower() or "ужасн" in user_message.lower() or "отличн" in user_message.lower() or "весел" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Почему?", "Ясно, а вот у меня нет.", "Понятно, у меня тоже", "Жалко :("])
    if "где" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"В караганде?", "В америке", "В африке", "В Москве","В караганде?", "В пиз..", "Хз", "Далеко","Уж точно дальше от тебя","Подальше от тебя","Дома","На улице","В Европе","В Азии","В США","За горизонтом"])
    if "спасиб" in user_message.lower() or "спс" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Незачто!", "Не за что!", "На здоровье!", "Ок","Всегда пожалуйста!", "Пожалуйста"])
    if "что" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Ничего!", "У себя спроси!", "Хз", "Не знаю","У меня не спрашивай!"])
    if "поздравим" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Поздравляю!", "Поздравляем!", "Мои поздравления!", "С поздравлением!"])
    if "язык" in user_message.lower() and "зна" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Я знаю абсолютно все языки мира, включая твой!", "Я знаю абсолютно все языки мира!", "Я могу написать тебе на любом языке мира, ты просто напиши мне на том языке"])
    if "врем" in user_message.lower():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([current_time, "У меня щас " + current_time, "Московское время: " + current_time])
    if "давай" in user_message.lower():
        sendmsg = sendmsg + ', ' + random.SystemRandom().choice([f"Не давай!", "Что давай?", "Нет", "Не знаю","У меня не спрашивай!"])
    if "/😀/информация/☹️/" == user_message.lower():
        sendmsg = '  >>> Привет, я Грустный межвежоночек, давай поболтаем?\n\nЕсли не хочешь, чтобы я ответил на твоё сообщение,\nПросто напиши **-** перед твоим сообщением.\nПример: **-Я не хочу, чтобы он ответил на это сообщение**.'
    if "заткни" in user_message.lower():
        sendmsg = '  >>> Если не хочешь, чтобы я ответил на твоё сообщение,\nПросто напиши **-** перед твоим сообщением.\nПример: **-Я не хочу, чтобы он ответил на это сообщение**.'
    if "/😀/кто такой " in user_message.lower() or "/😀/что такое " in user_message.lower() or "/😀/кто такая " in user_message.lower():
        result = wikipedia.search(user_message[13:].replace('/☹️/',''),results = 10)
        if len(result) >= 1:
            try:
                page = wikipedia.page(result[0])
            except:
                try:
                    page = wikipedia.page(result[1])
                except:
                    sendmsg = '  Ошибка, мне не удалось найти то, что вы хотели'
                else:
                    wikipedia.set_lang(langdef)
                    page = wikipedia.page(result[1])
                    link = result[1].replace(' ','_').replace('?','%3F')
                    sendmsg = '  ' + page.summary + ' ' + translator.translate('||Подробнее:', dest=langdef).text + ' https://ru.wikipedia.org/wiki/' + link + '||'
                    if len(sendmsg) > 2000:
                        sendmsg = '  Слишком много информации, не могу отправить, но вы можете прочитать её, просто перейдя по ссылке: https://ru.wikipedia.org/wiki/' + link
            else:
                wikipedia.set_lang(langdef)
                page = wikipedia.page(result[0])
                link = result[0].replace(' ','_').replace('?','%3F')
                sendmsg = '  ' + page.summary + ' ' + translator.translate('||Подробнее:', dest=langdef).text + ' https://ru.wikipedia.org/wiki/' + link + '||'
                if len(sendmsg) > 2000:
                    sendmsg = '  Слишком много информации, не могу отправить, но вы можете прочитать её, просто перейдя по ссылке: https://ru.wikipedia.org/wiki/' + link
        else:
            sendmsg = '  ' + random.SystemRandom().choice(['Извини, я не знаю','Да не знаю я','Хз','Не знаю','Извини, я хз'])
    if "идея " in user_message.lower() or "ошибка " in user_message.lower() or "баг " in user_message.lower() or "недоработка " in user_message.lower():
        if user_message.split(' ')[0] == '/😀/идея' or user_message.lower().split(' ')[0] == '/😀/баг' or user_message.lower().split(' ')[0] == '/😀/ошибка' or user_message.lower().split(' ')[0] == '/😀/недоработка':
            idea = user_message
            f = open('Идеи.txt','a')
            f.write(str(message.author) + ': ' + idea.replace('/☹️/','').replace('/😀/','') + '\n')
            f.close
            sendmsg = '  ' + idea + ' отправлен(а) моему разработчику.'
        else:
            sendmsg = '  Использование: *Идея/Ошибка/Баг/Недоработка <текст> (Первым словом должна быть идея или ошибка или баг или недоработка)* - Отправить идею/недоработку/ошибку/баг моим разработчикам.'
    elif "идея" in user_message.lower() or "ошибка" in user_message.lower() or "баг" in user_message.lower() or "недоработка" in user_message.lower():
        sendmsg = '  Использование: *Идея/Ошибка/Баг/Недоработка <текст> (Первым словом должна быть идея или ошибка или баг или недоработка)* - Отправить идею/недоработку/ошибку/баг моим разработчикам.'
    if sendmsg == ' ':
        endvalue = random.randint(1,2)
        startvalue = 0
        sendmsg = ' '
        while startvalue < endvalue:
            sendmsg = sendmsg + random.SystemRandom().choice([' Почему ' + user_message.split(' ')[random.randint(0,len(user_message.split(' '))-1)] + '?','  Как ' + user_message.split(' ')[random.randint(0,len(user_message.split(' '))-1)] + '?','  Что ' + user_message.split(' ')[random.randint(0,len(user_message.split(' '))-1)] + '?']).replace(',','')
            startvalue = startvalue + 1
    randomnumber = random.SystemRandom().choice(['0','0','0','0','0','0','0','0','1','1'])
    if randomnumber == '1':
        if sendmsg != '' and user_message[7] != '-':
            startvalue = 0
            endvalue = random.randint(1, 3)
            while startvalue < endvalue:
                startvalue = startvalue + 1
                await message.add_reaction(random.SystemRandom().choice(['👍','😀','😂','😡','🤬','😎','😜','😍','😘','☹️','😢','😭','🤯','😨','🤢','🤮','👎','😼','☠️','💀','💩','😴','🤘','🖕','👌']))
    if sendmsg != '' and user_message[7] != '-':
        sendmsg = sendmsg[2:]
        if 'https://' not in sendmsg and 'http://' not in sendmsg and 'www.' not in sendmsg:
            sendmsg = translator.translate(sendmsg, dest=langdef)
            sendmsg = sendmsg.text
        if sendmsg.split(' ')[0] == ',':
            sendmsg = sendmsg[2:]
        randomnumber = random.SystemRandom().choice(['0','0','0','0','0','0','0','0','1','1'])
        if randomnumber == '1':
            if sendmsg != '' and user_message[7] != '-':
                sendmsg = sendmsg + ' ' + random.SystemRandom().choice(['👍','😀','😂','😡','🤬','😎','😜','😍','😘','☹️','😢','😭','🤯','😨','🤢','🤮','👎','😼','☠️','💀','💩','😴','🤘','🖕','👌'])
        if random.randint(1,100) <= 35:
            mymsg = await message.reply(sendmsg.replace('?,','?').replace('!,', '!').replace(',,',',').replace(':,',":").replace('.,',".").replace('/☹️/','').replace('/😀/','').replace('!.','!').replace('?.','?'))
        else:
            if type == 1:
                mymsg = await message.author.send(sendmsg.replace('?,','?').replace('!,', '!').replace(',,',',').replace(':,',":").replace('.,',".").replace('/☹️/','').replace('/😀/','').replace('!.','!').replace('?.','?'))
            elif type == 2:
                channeltogetherchat = client.get_channel(1041767659894743171)
                mymsg = await channeltogetherchat.send(sendmsg.replace('?,','?').replace('!,', '!').replace(',,',',').replace(':,',":").replace('.,',".").replace('/☹️/','').replace('/😀/','').replace('!.','!').replace('?.','?'))
        mymsg = mymsg.id
        if type == 1:
            await msgconsole(f"Я отправил сообщение пользователю {message.author.mention}:\n>>> " + sendmsg.replace('?,','?').replace('!,', '!').replace(',,',',').replace(':,',":").replace('.,',".").replace('/☹️/','').replace('/😀/','').replace('!.','!').replace('?.','?') + f'\n*({mymsg})*',message.author.id)
        elif type == 2:
            channelid = client.get_channel(1043196525037244436)
            await channelid.send(f"Я отправил ответ на сообщение пользователю {message.author.mention}:\n>>> " + sendmsg.replace('?,','?').replace('!,', '!').replace(',,',',').replace(':,',":").replace('.,',".").replace('/☹️/','').replace('/😀/','').replace('!.','!').replace('?.','?') + f'\n*({mymsg})*')

@client.event
async def on_member_join(member):
    authorid = member.mention
    channelhello = client.get_channel(1040903820403810405)
    await channelhello.send(f"**ДОБРО ПОЖАЛОВАТЬ! ** 👋\n\n> Привет, {authorid}, для общения со\n> мной переходи ко мне в ЛС.\n\n**ПРИЯТНОГО ОБЩЕНИЯ!** 💬")
    await member.send(f'Здарова, {authorid}, давай поболтаем! 😀')

async def datauser(user,value,data):
    path = f"users\{user}.txt"
    if not os.path.exists(path):
        file = open(f'{path}','w')
        file.write('0')
        file.close()
    newpath = "users" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(f"users\{user}.txt") as file:
        lines = file.readlines()
        while len(lines) < value:
            lines.append('0\n')
        else:
            lines[value-1] = f"{data}\n"
            with open(f"users\{user}.txt", "w") as file:
                file.writelines(lines)
async def datauseradd(user,value,data):
    newpath = "users" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    with open(f"users\{user}.txt") as file:
        lines = file.readlines()
        while len(lines) < value:
            lines.append('0\n')
        else:
            lines[value-1] = f"{int(lines[value-1])+int(data)}\n"
            with open(f"users\{user}.txt", "w") as file:
                file.writelines(lines)

async def msgconsole(msg,user):
    path = "users" 
    if not os.path.exists(path):
        os.makedirs(path)
    path = f"users\{user}.txt"
    file = open(path)
    path = file.readlines()[0]
    file.close()
    if path != '' and int(path) != 0:
        path = int(path)
        thread = client.get_channel(int(path))
        userneed = str(client.get_user(user)).replace(' ','_').replace('#',' ') + f' {user}'
        if thread.name != userneed:
            await thread.edit(name=userneed)
        await thread.send(msg)
    else:
        forum = client.get_channel(1043784144934686730)
        thread = await forum.create_thread(name=str(client.get_user(user)).replace(' ','_').replace('#',' ') + f' {user}',content=f"Консоль пользователя {client.get_user(user).mention}.")
        await client.get_channel(thread.thread.id).send(msg)
        await datauser(user,1,thread.thread.id)

client.run(TOKEN)