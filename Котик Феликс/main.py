token = ''
import time
import json
import random


import telebot
from telebot import types

from text import *
from items import *
from fight import *
from level import *




#функции сохранения и загрузки. пояснения не требуют
def save_(SaveID):
    b = ''
    for i in str(SaveID):
        if i == ' ':
            b += 'A'
        elif i == '[':
            b += 'B'
        elif i == ']':
            b += 'C'
        elif i == ',':
            b += 'D'
        elif i == '9':
            b += 'F'
        else:
            b += i
    return b
def load_(SaveID):
    b = ''
    for i in SaveID:
        if i == 'A':
            b += ' '
        elif i == 'B':
            b += '['
        elif i == 'F':
            b += '9'
        elif i == 'C':
            b += ']'
        elif i == 'D':
            b += ','
        else:
            b += i
    return json.loads(b)

 

#Подключение к боту

bot = telebot.TeleBot(token)

SaveID = [99999999, [0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,6,5,4,3,0,2],[0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,11,10,9,8,0,7],[0,1,0,0,0,1,1,0,10,10,40,40,10,10,20,20],[0,1,0,0,0,1,1,0,10,10,10,10,20,20,40,40], [0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]
#Код сохранения, Инвентарь Карины, способности и экипировка Карины, Инвентарь Илюши, способности и экiпировка илюши SaveID[int(4 + count/2)][0] - броня, [1] - колво использованных очков, 2 - очки обучнеия, 3 - очки способностей

#SaveID[0] и TextID - этап игры
#SaveID[1] - karina's inventory
#SaveID[2] - способности и экипировка...
#SaveID[3] - Ilysha inventory
#SaveID[4] - способности и экипировка Илюши
#SaveID[int(4 + count/2)][0] - броня, [1] - колво использованных очков, [2] - очки обучнеия, [3] - очки способностей,

'''Способности(1 раз за бой)(7-8)
SaveID[int(6 + count/2)][0] - 'Восстановление здоровья'
SaveID[int(6 + count/2)][1] - 'Восстановление маны'
SaveID[int(6 + count/2)][2] - Восстановление силы'
SaveID[int(6 + count/2)][3] - 'Восстановление ловкости'
SaveID[int(6 + count/2)][4] - 'Смертельный удар'
SaveID[int(6 + count/2)][5] - 'Магическая волна'
SaveID[int(count/2 + 6)][6] - Прорыв'
SaveID[int(count/2 + 6)][7] - Вихрь
SaveID[int(count/2 + 6)][8] - 'Высасывание энергии'
'''
'''Надето(2,4)
Голова: {items[SaveID[count][11]][0]}
Футболка: {items[SaveID[count][9]][0]}
Куртка: {items[SaveID[count][10]][0]}
Штаны: {items[SaveID[count][8]][0]}
Ботинки: {items[SaveID[count][7]][0]}
Аксессуар: {items[SaveID[count][6]][0]}
Левая рука: {items[SaveID[count][4]][0]}
Правая рука: {items[SaveID[count][5]][0]}
'''
'''Характеристики(5-6)
Уровень: {SaveID[int(4 + count/2)][1]-1}
Доступно очков обучения: {SaveID[int(4 + count/2)][2]}
Доступно очков умений: {SaveID[int(4 + count/2)][3]}
Защита: {SaveID[int(4 + count/2)][0]}
Урон левой рукой: {SaveID[int(4 + count/2)][-11]}
Урон правой рукой: {SaveID[int(4 + count/2)][-10]}
Здоровье: {SaveID[int(4 + count/2)][-2]}/{SaveID[int(4 + count/2)][-1]}
Выносливость: {SaveID[int(4 + count/2)][-4]}/{SaveID[int(4 + count/2)][-3]}
Ловкость: {SaveID[int(4 + count/2)][-6]}/{SaveID[int(4 + count/2)][-5]}
Духовные силы: {SaveID[int(4 + count/2)][-8]}/{SaveID[int(4 + count/2)][-7]}'''

'''SaveID[int(4 + count/2)][-9] - опыт'''
dung_list_ids = []
def level_dunguon_func(level_dunguon):
    global TextID, dung_list_ids, Last_TextId, SaveID
    if level_dunguon.text != 'Наружу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        out_button = types.InlineKeyboardButton('Наружу')
        go_button = types.InlineKeyboardButton('Дальше💀')
        markup.add(out_button, go_button)
        inventory_button = types.InlineKeyboardButton('Инвентарь💀')
        level_button = types.InlineKeyboardButton('Характеристики💀')
        markup.add(level_button,inventory_button)
            
        
        if level_dunguon.text == '1💀': 
            dung_list_ids = list(range(1001002, 1001022, 4))
            
        elif level_dunguon.text == '2💀💀':
            dung_list_ids = list(range(1001022, 1001046, 4))
            
        elif level_dunguon.text == '3💀💀💀':
            dung_list_ids = list(range(1001046, 10070, 4))
        bot.send_message(level_dunguon.chat.id, f'''Сложность: {level_dunguon.text}''', reply_markup=markup)
    elif level_dunguon.text == 'Наружу' :
        TextID = Last_TextId
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        photo(level_dunguon) 
        beginning_button = types.InlineKeyboardButton('Продолжить')
        markup.add(beginning_button)
        settings_button = types.InlineKeyboardButton('Меню⚙️')
        inventory_button = types.InlineKeyboardButton('Инвентарь')
        markup.add(settings_button, inventory_button)
        
        level_button = types.InlineKeyboardButton('Характеристики')
                
        rest_button = types.InlineKeyboardButton('Отдохнуть')
        markup.add(rest_button, level_button)
        dangeon_button = types.InlineKeyboardButton('ПОДЗЕМЕЛЬЕ💀')
        markup.add(dangeon_button)
        
        bot.send_message(level_dunguon.chat.id, f'''{beginning_text[str(TextID)]}''', reply_markup=markup)

        
#StartID - начальное сохранение
StartID = SaveID

#Этап текста игры
TextID = 0
'''Для подземелий'''
Last_TextId = 0

#убрать кнопку назад
no_back = [30, 29, 22, 18, 37, 40, 43, 50]
#HP and so on
#HP_Karina = 20
#MaxHP_Karina = 20
#Stamina_Karina = 10
#Max_Stamina_Karina = 10
#Agility_Karina = 40
#Max_Agility_Karina = 40
#Mana_Karina = 0
#Max_Mana_Karisha  = 0
#ExpKarina = 0

#HP_Ilusha = 40
#MaxHP_Ilusha  = 40
#Stamina_Ilusha  = 20
#Max_Stamina_Ilusha  = 20
#Agility_Ilusha = 10
#Max_Agility_Ilusha = 10
#Mana_Ilusha  = 0
#Max_Mana_Ilusha  = 0
#ExpIlusha  = 0

#Кариша или Илюша
level_last_level = 0
level_last = 0
boost = 1
name = 'Кариша'
hero = 1
count = 2
attack = 0
typeboost = ''


#отдахыл или нет
rest_count = 0
def count_hero():
    global hero, count, name
    count = hero*2
    if count == 2: name = 'Кариша'
    elif count == 4: name = 'Илюша'

# проверка на наличие предмета в инвентаре
def if_(num):
    global SaveID, count_hero
    count_hero()
    for i in reversed(range(0,12)):
        if SaveID[count-1][i] == num:
            return True
        
    return False
            


#level
def lvl(message):
    global  SaveID
    for i in range(1,12):
        if  SaveID[int(4 + count/2)][1] == i and SaveID[int(4 + count/2)][-9] >= levels[i]:
            SaveID[int(4 + count/2)][1] += 1
            bot.send_message(message.chat.id, f'Вы достигли {i}-го уровня!')
            SaveID[int(4 + count/2)][2] += 5
            SaveID[int(4 + count/2)][3] += 1
#надето: последняя вкладка - осмотреть
look_at_last = 0
use = 0
type_ = ''
def look_at_last_():
    global look_at_last, type_
    if look_at_last == 11:
        type_ = 'head'
    elif look_at_last == 10:
        type_ = 'jacket'
    elif look_at_last == 9:
        type_ = 'body'
    elif look_at_last == 8:
        type_ = 'legs'
    elif look_at_last == 7:
        type_ = 'boots'
    elif look_at_last == 6:
        type_ = 'rings'
    elif look_at_last == 5:
        type_ = 'weapon'
    elif look_at_last == 4:
        type_ = 'weapon'
#кнопки:
#starting_button - новая игра
#beginning_button - кнопка продолжить
#save_button - сохранить игру
#load_button - загрузить сохранение
#back_button - выйти из меню
#beginning_button_back - пролистнуть назад
#look_around_button - осмотреться
#settings_button -меню
#inventory - 'Продолжить'
#clothes_button - Надето:
#weapon_button - Экипировка:
#button(1-12) - слоты инвентаря
#head_button - шляпы
#body_button - куртки и футболки
#legs_button - штаны
#boots_button - ботинки
#rings_button - аксессуары

def delete_when_full(delete_item):
    count_hero()
    if delete_item.text == 'Отмена.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        clean_button = types.InlineKeyboardButton('Выбросить')
        markup.add(beginning_button, clean_button )
        
        bot.send_message(delete_item.chat.id, 'Нет места! Хотите что-то выбросить?', reply_markup=markup)
    else:

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(delete_item.chat.id, f'"{items[SaveID[count-1][int(12 - int(delete_item.text))]][0] }" - было выброшенно. ', reply_markup=markup)
        SaveID[count-1][12 - int(delete_item.text)] = 0
        take_button = types.InlineKeyboardButton('Взять')
        beginning_button = types.InlineKeyboardButton('Продолжить')
        markup.add(take_button, beginning_button)
        bot.send_message(delete_item.chat.id, f'''Вы нашли: ''{items[text_items[TextID]][0]}'' ''', reply_markup=markup)
#Функция  загрузки
def load(ID):
    global SaveID, TextID
    try:
        SaveID = load_(ID.text)
        TextID = 99999999 - SaveID[0]

        if TextID > 0:
            TextID -= 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        markup.add(beginning_button)
        bot.send_message(ID.chat.id, 'Ваше сохранение успешно загружено!', reply_markup=markup)
    except:
        if TextID != 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            beginning_button = types.InlineKeyboardButton('Продолжить')
            save_button = types.InlineKeyboardButton('Сохранить')
            load_button = types.InlineKeyboardButton('Загрузить')
            markup.add(beginning_button)
            markup.add(save_button, load_button)
            bot.send_message(ID.chat.id, 'Пауза', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            starting_button = types.InlineKeyboardButton('Новая игра')
            load_button = types.InlineKeyboardButton('Загрузить')
            markup.add(starting_button, load_button)
            bot.send_message(ID.chat.id, beginning_text[str(TextID)], reply_markup=markup)
            

#Send a Photo
def photo(message):
    try:
        bot.send_photo(message.chat.id, photo=open(f"images\love_game_photo_{TextID}.jpg", 'rb'))
    except FileNotFoundError:
        print("there' s no photo" )
def photo_id(message, photo__id):
    try:
        bot.send_photo(message.chat.id, photo=open(f"images\love_game_photo_{photo__id}.jpg", 'rb'))
    except FileNotFoundError:
        print("there' s no photo" )

#Take something
def take(ID,TextID):
    global SaveID, hero
    count_hero()
    item = text_items[TextID]
    count_ = 0
    for i in reversed(range(0,12)):
        if SaveID[count-1][i] == 0:
            SaveID[count-1][i] = item
            count_ = 1
            TextID += 1
            SaveID[0] -= 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            beginning_button = types.InlineKeyboardButton('Продолжить')
            
            markup.add(beginning_button)
            bot.send_message(ID.chat.id, f'Вы подобрали: "{items[text_items[TextID - 1]][0]}"', reply_markup=markup)
            
            break
    if count_ == 0:
        #!
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        clean_button = types.InlineKeyboardButton('Выбросить')
        markup.add(beginning_button, clean_button )
        
        bot.send_message(ID.chat.id, 'Нет места! Хотите что-то выбросить?', reply_markup=markup)

#put up fuction

def put_up_func(put_up):
    global look_at_last, SaveID
    count_hero()
    
        
    SaveID[count][look_at_last] = SaveID[count-1][12-int(put_up.text)]
    SaveID[count-1][12-int(put_up.text)] = 0

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if look_at_last == 4 or look_at_last == 5:
        some_button = types.InlineKeyboardButton('В Инвентарь')
        if count == 2:
            SaveID[5][-5 -(10 - look_at_last)] = items[SaveID[count][look_at_last]][3]
        else:
            SaveID[6][-5 -(10 - look_at_last)] = items[SaveID[count][look_at_last]][3]
    elif look_at_last == 6:
        some_button = types.InlineKeyboardButton('Вернуться')
        if items[SaveID[count][look_at_last]][5] == 'love':

            bot.send_message(put_up.chat.id, f'''Вы получаете бонус любви: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-1] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-2] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-3] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-4] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-5] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-6] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-7] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-8] += items[SaveID[count][look_at_last]][6]
                        
        elif items[SaveID[count][look_at_last]][5] == 'stamina':
            SaveID[int(4 + count/2)][-3] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-4] += items[SaveID[count][look_at_last]][6]
            bot.send_message(put_up.chat.id, f'''Вы получаете бонус выносливости: {items[SaveID[count][look_at_last]][6]}''')
                        
        elif items[SaveID[count][look_at_last]][5] == 'magic':
            bot.send_message(put_up.chat.id, f'''Вы получаете бонус магии: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-7] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-8] += items[SaveID[count][look_at_last]][6]
        elif items[SaveID[count][look_at_last]][5] == 'agility':
            bot.send_message(put_up.chat.id, f'''Вы получаете бонус ловкости: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-5] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-6] += items[SaveID[count][look_at_last]][6]
        elif items[SaveID[count][look_at_last]][5] == 'lordspower':
            bot.send_message(put_up.chat.id, f'''Вы получаете всемогущество...''')
            SaveID[int(4 + count/2)][-1] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-2] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-3] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-4] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-5] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-6] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-7] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-8] += items[SaveID[count][look_at_last]][6]
        elif items[SaveID[count][look_at_last]][5] == 'health':
            bot.send_message(put_up.chat.id, f'''Вы получаете бонус здоровья: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-1] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-2] += items[SaveID[count][look_at_last]][6]
        SaveID[int(4 + count/2)][0] += items[SaveID[count][look_at_last]][4]
    else:
        some_button = types.InlineKeyboardButton('Вернуться')
        SaveID[int(4 + count/2)] += items[SaveID[count][look_at_last]][4]
    look_at_button = types.InlineKeyboardButton('Осмотреть')
    change_button = types.InlineKeyboardButton('Сменить')
    markup.add(look_at_button, change_button)
    take_off_button = types.InlineKeyboardButton('Снять')
    markup.add(take_off_button, some_button)
    bot.send_message(put_up.chat.id, f"Надето: {items[SaveID[count][look_at_last]][0]}", reply_markup=markup)
    

#change up function
def change_up_func(change_up):
    global look_at_last
    count_hero()
    just_a_number = SaveID[count][look_at_last]
    SaveID[count][look_at_last] = SaveID[count-1][12-int(change_up.text)]
    SaveID[count-1][12-int(change_up.text)] = just_a_number

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if look_at_last == 4 or look_at_last == 5:
        some_button = types.InlineKeyboardButton('В Инвентарь')
        if count == 2:
            SaveID[5][-5 -(10 - look_at_last)] = items[SaveID[count][look_at_last]][3]
        else:
            SaveID[6][-5 -(10 - look_at_last)] = items[SaveID[count][look_at_last]][3]
    elif look_at_last == 6:
        some_button = types.InlineKeyboardButton('Вернуться')
        if items[SaveID[count][look_at_last]][5] == 'love':

            bot.send_message(change_up.chat.id, f'''Вы получаете бонус любви: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-1] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-2] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-3] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-4] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-5] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-6] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-7] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-8] += items[SaveID[count][look_at_last]][6]
            
                        
        elif items[SaveID[count][look_at_last]][5] == 'stamina':
            SaveID[int(4 + count/2)][-3] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-4] += items[SaveID[count][look_at_last]][6]
            
            bot.send_message(change_up.chat.id, f'''Вы получаете бонус выносливости: {items[SaveID[count][look_at_last]][6]}''')
                        
        elif items[SaveID[count][look_at_last]][5] == 'magic':
            bot.send_message(change_up.chat.id, f'''Вы получаете бонус магии: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-7] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-8] += items[SaveID[count][look_at_last]][6]
            
        elif items[SaveID[count][look_at_last]][5] == 'agility':
            bot.send_message(change_up.chat.id, f'''Вы получаете бонус ловкости: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-5] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-6] += items[SaveID[count][look_at_last]][6]
            
        elif items[SaveID[count][look_at_last]][5] == 'lordspower':
            bot.send_message(change_up.chat.id, f'''Вы получаете всемогущество...''')
            SaveID[int(4 + count/2)][-1] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-2] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-3] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-4] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-5] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-6] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-7] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-8] += items[SaveID[count][look_at_last]][6]
        elif items[SaveID[count][look_at_last]][5] == 'health':
            bot.send_message(change_up.chat.id, f'''Вы получаете бонус здоровья: {items[SaveID[count][look_at_last]][6]}''')
            SaveID[int(4 + count/2)][-1] += items[SaveID[count][look_at_last]][6]
            SaveID[int(4 + count/2)][-2] += items[SaveID[count][look_at_last]][6]
            
        
        if items[SaveID[count-1][12-int(change_up.text)]][5] == 'love':

            bot.send_message(change_up.chat.id, f'''Вы теряете бонус любви: {items[SaveID[count-1][12-int(change_up.text)]][6]}''')
            
            SaveID[int(4 + count/2)][-1] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-2] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-3] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-4] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-5] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-6] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-7] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-8] -= items[SaveID[count-1][12-int(change_up.text)]][6]
                        
        elif items[SaveID[count-1][12-int(change_up.text)]][5] == 'stamina':
            
            SaveID[int(4 + count/2)][-3] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-4] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            bot.send_message(change_up.chat.id, f'''Вы теряете бонус выносливости: {items[SaveID[count-1][12-int(change_up.text)]][6]}''')
                        
        elif items[SaveID[count-1][12-int(change_up.text)]][5] == 'magic':
            bot.send_message(change_up.chat.id, f'''Вы теряете бонус магии: {items[SaveID[count-1][12-int(change_up.text)]][6]}''')
            
            SaveID[int(4 + count/2)][-7] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-8] -= items[SaveID[count-1][12-int(change_up.text)]][6]
        elif items[SaveID[count-1][12-int(change_up.text)]][5] == 'agility':
            bot.send_message(change_up.chat.id, f'''Вы теряете бонус ловкости: {items[SaveID[count-1][12-int(change_up.text)]][6]}''')
            
            SaveID[int(4 + count/2)][-5] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-6] -= items[SaveID[count-1][12-int(change_up.text)]][6]
        elif items[SaveID[count-1][12-int(change_up.text)]][5] == 'lordspower':
            bot.send_message(change_up.chat.id, f'''Вы теряете всемогущество...''')
            SaveID[int(4 + count/2)][-1] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-2] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-3] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-4] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-5] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-6] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-7] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-8] -= items[SaveID[count-1][12-int(change_up.text)]][6]
        elif items[SaveID[count-1][12-int(change_up.text)]][5] == 'health':
            bot.send_message(change_up.chat.id, f'''Вы теряете бонус здоровья: {items[SaveID[count-1][12-int(change_up.text)]][6]}''')
            
            SaveID[int(4 + count/2)][-1] -= items[SaveID[count-1][12-int(change_up.text)]][6]
            SaveID[int(4 + count/2)][-2] -= items[SaveID[count-1][12-int(change_up.text)]][6]
        

        SaveID[int(4 + count/2)][0] += items[SaveID[count][look_at_last]][4]
        SaveID[int(4 + count/2)][0] -= items[SaveID[count-1][12-int(change_up.text)]][4]
        
    else:
        some_button = types.InlineKeyboardButton('Вернуться')
        SaveID[int(4 + count/2)][0] += items[SaveID[count][look_at_last]][4]
        SaveID[int(4 + count/2)][0] -= items[SaveID[count-1][12-int(change_up.text)]][4]
    look_at_button = types.InlineKeyboardButton('Осмотреть')
    change_button = types.InlineKeyboardButton('Сменить')
    markup.add(look_at_button, change_button)
    take_off_button = types.InlineKeyboardButton('Снять')
    markup.add(take_off_button, some_button)
    bot.send_message(change_up.chat.id, f'''Надето: {items[SaveID[count][look_at_last]][0]}
{items[SaveID[count-1][12-int(change_up.text)]][0]} - убрано в Инвентарь''', reply_markup=markup)
 

#способности один раз за битву
level_last_level_count0 = 0
level_last_level_count1 = 0
level_last_level_count2 = 0
level_last_level_count3 = 0
level_last_level_count4 = 0
level_last_level_count5 = 0
level_last_level_count6 = 0
level_last_level_count7 = 0
level_last_level_count8 = 0



attack = 0
enemy_hp = 0
enemy_damage = 0
def fight(ID, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    global SaveID, TextID, enemy_hp, enemy_damage , name, level_last_level_count0, level_last_level_count1, level_last_level_count2, level_last_level_count3, level_last_level_count4, level_last_level_count5, level_last_level_count6, level_last_level_count7, level_last_level_count8
    level_last_level_count0 = 0
    level_last_level_count1 = 0
    level_last_level_count2 = 0
    level_last_level_count3 = 0
    level_last_level_count4 = 0
    level_last_level_count5 = 0
    level_last_level_count6 = 0
    level_last_level_count7 = 0
    level_last_level_count8 = 0
    enemy_hp = mobsID[ID][1][0]
    enemy_damage = mobsID[ID][1][1]
    left_attack_button = types.InlineKeyboardButton('Атаковать левой рукой')
    right_attack_button = types.InlineKeyboardButton('Атаковать правой рукой')
    markup.add(left_attack_button, right_attack_button)
    if SaveID[int(6 + count/2)][0] == 1 and level_last_level_count0 == 0:
        ability_button0 = types.InlineKeyboardButton('Восстановление Здоровья')
        markup.row(ability_button0)
    if SaveID[int(6 + count/2)][1] == 1 and level_last_level_count1 == 0:
        ability_button1 = types.InlineKeyboardButton('Восстановление Маны')
        markup.row(ability_button1)
    if SaveID[int(6 + count/2)][2] == 1 and level_last_level_count2 == 0:
        ability_button2 = types.InlineKeyboardButton('Восстановление Силы')
        markup.row(ability_button2)
    if SaveID[int(6 + count/2)][3] == 1 and level_last_level_count3 == 0:
        ability_button3 = types.InlineKeyboardButton('Восстановление Ловкости')
        markup.row(ability_button3)
    if SaveID[int(6 + count/2)][4] == 1 and level_last_level_count4 == 0:
        ability_button4 = types.InlineKeyboardButton('Смертельный Удар')
        markup.row(ability_button4)
    if SaveID[int(6 + count/2)][5] == 1 and level_last_level_count5 == 0:
        ability_button5 = types.InlineKeyboardButton('Магическая Волна')
        markup.row(ability_button5)
    if SaveID[int(6 + count/2)][6] == 1 and level_last_level_count6 == 0:
        ability_button6 = types.InlineKeyboardButton('Прорыв!')
        markup.row(ability_button6)
    if SaveID[int(6 + count/2)][7] == 1 and level_last_level_count7 == 0:
        ability_button7 = types.InlineKeyboardButton('Вихрь!')
        markup.row(ability_button7)
    if SaveID[int(6 + count/2)][8] == 1 and level_last_level_count8 == 0:
        ability_button8 = types.InlineKeyboardButton('Высасывание Энергии')
        markup.row(ability_button8)
    bot.send_message(message .chat.id, f'''Ваш враг - "{mobsID[ID][0]}"
Урон: {enemy_damage} едениц. Здоровье: {enemy_hp} едениц.''', reply_markup=markup)
    
    count_hero()
#delete
def delete(delete_item):
    global look_at_last
    count_hero()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    beginning_button = types.InlineKeyboardButton('Продолжить')
    clothes_button = types.InlineKeyboardButton('Надето:')
    weapon_button = types.InlineKeyboardButton('Экипировка:')

    button1 = types.InlineKeyboardButton('1')
    button2 = types.InlineKeyboardButton('2')
    button3 = types.InlineKeyboardButton('3')
    button4 = types.InlineKeyboardButton('4')
    button5 = types.InlineKeyboardButton('5')
    button6 = types.InlineKeyboardButton('6')
    button7 = types.InlineKeyboardButton('7')
    button8 = types.InlineKeyboardButton('8')
    button9 = types.InlineKeyboardButton('9')
    button10 = types.InlineKeyboardButton('10')
    button11 = types.InlineKeyboardButton('11')
    button12 = types.InlineKeyboardButton('12')



    markup.add(clothes_button, beginning_button, weapon_button)
    markup.add(button1, button2, button3, button4, button5, button6)
    markup.add(button7, button8, button9, button10, button11, button12)
    bot.send_message(delete_item.chat.id, f'''" {items[SaveID[count-1][23 - look_at_last]][0]}"  было удалено из Инвентаря''', reply_markup=markup)
    SaveID[count-1][23 - look_at_last] = 0


#1
@bot.message_handler(commands=['start'])
def start(message):
    global TextID
    TextID = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    starting_button = types.InlineKeyboardButton('Новая игра')
    load_button = types.InlineKeyboardButton('Загрузить')
    bot.send_photo(message.chat.id, photo=open("images\love_game_photo_start.jpg", 'rb'))
    markup.add(starting_button, load_button)
    bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup)


@bot.message_handler(content_types='text')
#начальное меню
def message_reply(message):
    global TextID, StartID
    global items, Last_TextId, dung_list_ids
    global SaveID, use, level_last, no_back, level_last_level, rest_count 
    global text_items, hero, look_at_last, put_up_list, put_up_count, count_hero, enemy_hp, enemy_damage, boost, attack, typeboost, level_last_level_count0, level_last_level_count1, level_last_level_count2, level_last_level_count3, level_last_level_count4, level_last_level_count5, level_last_level_count6, level_last_level_count7, level_last_level_count8

    if message.text == "Новая игра":
        bot.send_photo(message.chat.id, photo=open("images\love_game_photo_one.jpg", 'rb'))
        TextID += 1
        SaveID[0] -= 1 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        markup.add(beginning_button)
        bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup) 

    elif message.text == "Загрузить": 
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_button = types.InlineKeyboardButton('Назад⚙️')
        markup.add(back_button)
        load_ID = bot.send_message(message.chat.id, 'Введите ваш код сохранения:', reply_markup=markup)
        bot.register_next_step_handler(load_ID, load)
        

    elif message.text == "Отмена":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        starting_button = types.InlineKeyboardButton('Новая игра')
        load_button = types.InlineKeyboardButton('Загрузить')
        markup.add(starting_button, load_button)
        bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup)

    elif message.text == "Сохранить":
        bot.send_message(message.chat.id, f'''Ваш код сохранения:''')
        time.sleep(1)
        save = save_(SaveID)
        bot.send_message(message.chat.id, f'''{save}''')

    elif message.text == "Меню⚙️":
        TextID -= 1
        SaveID[0] += 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        save_button = types.InlineKeyboardButton('Сохранить')
        load_button = types.InlineKeyboardButton('Загрузить')
        markup.add(beginning_button)
        markup.add(save_button, load_button)
        bot.send_message(message.chat.id, 'Пауза', reply_markup=markup)

#вперёд и назад
    elif message.text == "Продолжить":
        TextID += 1
        SaveID[0] -= 1
        lvl(message)
        
            
        if TextID == 11:
            for i in reversed(range(1,4)):
                time.sleep(1)
                bot.send_message(message.chat.id, f'{i}!')

            time.sleep(3)
        elif TextID == 10:
            for i in reversed(range(4,11)):
                bot.send_message(message.chat.id, f'{i}!')
                time.sleep(1)
        
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if TextID == 16:  
            photo(message)
            
            look_around_button = types.InlineKeyboardButton('Осмотреться')
            markup.add(look_around_button)
        elif TextID in [21, 44]:
            photo(message)
            

            
            
            take_button = types.InlineKeyboardButton('Взять')
            markup.add(take_button)
            
        elif TextID in mobsID.keys():
            
            
            photo_id(message, mobs_photos[TextID])
            
            fight_button = types.InlineKeyboardButton('Бой!')
            markup.add(fight_button)

        elif TextID == 30:
            photo(message)
            rest_button = types.InlineKeyboardButton('Отдохнуть')
            markup.add(rest_button)
        elif TextID == 35:
            
            if if_(1):
                hot_button = types.InlineKeyboardButton('Подогреть')
                markup.add(hot_button)
            else:
                time.sleep(0.4)
                bot.send_message(message.chat.id, beginning_text[str(TextID)])
                TextID = 1000001
                beginning_button = types.InlineKeyboardButton('Продолжить')
                markup.add(beginning_button)
                settings_button = types.InlineKeyboardButton('Меню⚙️')
                inventory_button = types.InlineKeyboardButton('Инвентарь')
                markup.add(settings_button, inventory_button)
            photo(message)    
        elif TextID == 1000002:
            time.sleep(0.4)
            bot.send_message(message.chat.id, beginning_text[str(TextID)])
            TextID = 41
            beginning_button = types.InlineKeyboardButton('Продолжить')
            markup.add(beginning_button)
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            inventory_button = types.InlineKeyboardButton('Инвентарь')
            markup.add(settings_button, inventory_button)
            photo(message)
        elif TextID == 38:
            hot_button = types.InlineKeyboardButton('Открыть упаковку')
            markup.add(hot_button)
            photo(message)
        elif TextID == 42:
            hot_button = types.InlineKeyboardButton('Ущепнуть себя')
            markup.add(hot_button)
            photo(message)
        elif TextID < 17:
            photo(message)
            beginning_button = types.InlineKeyboardButton('Продолжить')
            beginning_button_back = types.InlineKeyboardButton('Назад')
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            markup.add(beginning_button, beginning_button_back, settings_button)
        elif TextID in no_back:
            photo(message) 
            beginning_button = types.InlineKeyboardButton('Продолжить')
            markup.add(beginning_button)
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            inventory_button = types.InlineKeyboardButton('Инвентарь')
            markup.add(settings_button, inventory_button)
            if SaveID[int(4 + count/2)][1] > 1:
                level_button = types.InlineKeyboardButton('Характеристики')
                if rest_count == 0:
                    rest_button = types.InlineKeyboardButton('Отдохнуть')
                    markup.add(rest_button, level_button)
                else:
                    markup.add(level_button)
        elif TextID>1000999:
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            out_button = types.InlineKeyboardButton('Наружу')
            go_button = types.InlineKeyboardButton('Дальше💀')
            markup.add(out_button, go_button)
            inventory_button = types.InlineKeyboardButton('Инвентарь💀')
            level_button = types.InlineKeyboardButton('Характеристики💀')
            markup.add(level_button,inventory_button)
            

        else:
            photo(message)  
            beginning_button = types.InlineKeyboardButton('Продолжить')
            beginning_button_back = types.InlineKeyboardButton('Назад')
            markup.add(beginning_button, beginning_button_back)
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            inventory_button = types.InlineKeyboardButton('Инвентарь')
            markup.add(settings_button, inventory_button)     
            if SaveID[int(4 + count/2)][1] > 1:
                level_button = types.InlineKeyboardButton('Характеристики')
                if rest_count == 0:
                    rest_button = types.InlineKeyboardButton('Отдохнуть')
                    markup.add(rest_button, level_button)
                else:
                    markup.add(level_button)
                if TextID > 52 :
                    dangeon_button = types.InlineKeyboardButton('ПОДЗЕМЕЛЬЕ💀')
                    markup.add(dangeon_button)
        bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup)
        
    

    elif message.text in ['Подогреть', 'Открыть упаковку', 'Подуть', 'Ущепнуть себя']:
        TextID += 1
        SaveID[0] -= 1
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if TextID == 36:
            hot_button = types.InlineKeyboardButton('Продолжить')
            
        elif TextID == 39:
            hot_button = types.InlineKeyboardButton('Подуть')
            
        elif TextID in [40, 43]:
            hot_button = types.InlineKeyboardButton('Продолжить')
        markup.add(hot_button)
        bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup)

    elif message.text == 'Выбросить':
        item = ''
        inventory_text = f''''''
        for i in reversed(range(0,12)):
            if SaveID[1][i] == 0:
                item = 'пусто'
            else:
                item = items[SaveID[1][i]][0]
            inventory_text += f'Слот {12-i}: {item} \n'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Отмена.')
        
        
        

        button1 = types.InlineKeyboardButton('1')
        button2 = types.InlineKeyboardButton('2')
        button3 = types.InlineKeyboardButton('3')
        button4 = types.InlineKeyboardButton('4')
        button5 = types.InlineKeyboardButton('5')
        button6 = types.InlineKeyboardButton('6')
        button7 = types.InlineKeyboardButton('7')
        button8 = types.InlineKeyboardButton('8')
        button9 = types.InlineKeyboardButton('9')
        button10 = types.InlineKeyboardButton('10')
        button11 = types.InlineKeyboardButton('11')
        button12 = types.InlineKeyboardButton('12')



        markup.add(beginning_button)
        markup.add(button1, button2, button3, button4, button5, button6)
        markup.add(button7, button8, button9, button10, button11, button12)
        bot.send_message(message.chat.id, inventory_text, reply_markup=markup)
        delete_item = bot.send_message(message.chat.id, "Выберите слот. " ,reply_markup=markup)
        bot.register_next_step_handler(delete_item, delete_when_full)
    elif message.text == "Назад":
        TextID -= 1
        SaveID[0] += 1
        photo(message)

        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if TextID in [1, 28, 36, 37]:
            beginning_button = types.InlineKeyboardButton('Продолжить')
            markup.add(beginning_button)
        elif TextID in no_back or 41 > TextID > 34:
            beginning_button = types.InlineKeyboardButton('Продолжить')
            markup.add(beginning_button)
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            inventory_button = types.InlineKeyboardButton('Инвентарь')
            markup.add(settings_button, inventory_button)
            if SaveID[int(4 + count/2)][1] > 1:
                level_button = types.InlineKeyboardButton('Характеристики')
                if rest_count == 0:
                    rest_button = types.InlineKeyboardButton('Отдохнуть')
                    markup.add(rest_button, level_button)
                else:
                    markup.add(level_button)
        elif 17 > TextID:
            beginning_button = types.InlineKeyboardButton('Продолжить')
            beginning_button_back = types.InlineKeyboardButton('Назад')
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            markup.add(beginning_button, beginning_button_back, settings_button)
        else:
            photo(message)  
            beginning_button = types.InlineKeyboardButton('Продолжить')
            beginning_button_back = types.InlineKeyboardButton('Назад')
            markup.add(beginning_button, beginning_button_back)
            settings_button = types.InlineKeyboardButton('Меню⚙️')
            inventory_button = types.InlineKeyboardButton('Инвентарь')
            markup.add(settings_button, inventory_button)     
            if SaveID[int(4 + count/2)][1] > 1:
                level_button = types.InlineKeyboardButton('Характеристики')
                if rest_count == 0:
                    rest_button = types.InlineKeyboardButton('Отдохнуть')
                    markup.add(rest_button, level_button)
                else:
                    markup.add(level_button)
                if TextID > 52 :
                    dangeon_button = types.InlineKeyboardButton('ПОДЗЕМЕЛЬЕ💀')
                    markup.add(dangeon_button)
        
        bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup)
#событие
    elif message.text == "Осмотреться":
        TextID += 1
        SaveID[0] -= 1
        photo(message)

        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        take_button = types.InlineKeyboardButton('Взять')
        markup.add(take_button)
        bot.send_message(message.chat.id, beginning_text[str(TextID)], reply_markup=markup)
#to pick something up
    elif message.text == "Взять":
        take(message, TextID)
        
#inventory
    elif message.text == "Инвентарь" or message.text == 'В Инвентарь' or message.text == "Инвентарь💀":
        TextID -= 1
        SaveID[0] += 1
        item = ''
        inventory_text = f''''''
        for i in reversed(range(0,12)):
            if SaveID[1][i] == 0:
                item = 'пусто'
            else:
                item = items[SaveID[1][i]][0]
            inventory_text += f'Слот {12-i}: {item} \n'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        clothes_button = types.InlineKeyboardButton('Надето:')
        weapon_button = types.InlineKeyboardButton('Экипировка:')

        button1 = types.InlineKeyboardButton('1')
        button2 = types.InlineKeyboardButton('2')
        button3 = types.InlineKeyboardButton('3')
        button4 = types.InlineKeyboardButton('4')
        button5 = types.InlineKeyboardButton('5')
        button6 = types.InlineKeyboardButton('6')
        button7 = types.InlineKeyboardButton('7')
        button8 = types.InlineKeyboardButton('8')
        button9 = types.InlineKeyboardButton('9')
        button10 = types.InlineKeyboardButton('10')
        button11 = types.InlineKeyboardButton('11')
        button12 = types.InlineKeyboardButton('12')



        markup.add(clothes_button, beginning_button, weapon_button)
        markup.add(button1, button2, button3, button4, button5, button6)
        markup.add(button7, button8, button9, button10, button11, button12)
        bot.send_message(message.chat.id, inventory_text, reply_markup=markup)
        
        
#надето
    elif message.text == "Надето:"  or message.text == 'Вернуться':
        TextID += 1
        SaveID[0] -= 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        head_button = types.InlineKeyboardButton('Голова')
        body_button = types.InlineKeyboardButton('Тело')
        legs_button = types.InlineKeyboardButton('Штаны')
        boots_button = types.InlineKeyboardButton('Ботинки')
        rings_button = types.InlineKeyboardButton('Аксессуары')
        inventory_button = types.InlineKeyboardButton('В Инвентарь')

        count_hero()
        
        put_on_text =f'''Голова: {items[SaveID[count][11]][0]}
Футболка: {items[SaveID[count][9]][0]}
Куртка: {items[SaveID[count][10]][0]}
Штаны: {items[SaveID[count][8]][0]}
Ботинки: {items[SaveID[count][7]][0]}
Аксессуар: {items[SaveID[count][6]][0]}'''
        markup.add(head_button,inventory_button, legs_button)
        markup.add(body_button, rings_button, boots_button)
        bot.send_message(message.chat.id, put_on_text, reply_markup=markup)

    elif message.text == "Экипировка:":
        TextID += 1
        SaveID[0] -= 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        left_button = types.InlineKeyboardButton('Левая рука')
        right_button = types.InlineKeyboardButton('Правая рука')
        inventory_button = types.InlineKeyboardButton('В Инвентарь')

        count_hero()
        
        weapon_text =f'''Левая рука: {items[SaveID[count][4]][0]}
Правая рука: {items[SaveID[count][5]][0]}'''
        markup.add(left_button, right_button)
        markup.add(inventory_button)
        bot.send_message(message.chat.id, weapon_text, reply_markup=markup)

    elif message.text == "Левая рука":
        look_at_last = 4
        
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        inventory_button = types.InlineKeyboardButton('В Инвентарь')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][4] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, inventory_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, inventory_button)
        if SaveID[count][4] == 0:
            left_text = f'Ничего не надето.'
        else:
    
            left_text = f'''Надето: {items[SaveID[count][4]][0]}
{items[SaveID[count][4]][4]}. Урон: {items[SaveID[count][4]][3]} единиц.'''

        bot.send_message(message.chat.id, left_text, reply_markup=markup)
    
    elif message.text == "Правая рука":
        look_at_last = 5
        
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        inventory_button = types.InlineKeyboardButton('В Инвентарь')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][5] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, inventory_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, inventory_button)
        if SaveID[count][5] == 0:
            right_text = f'Ничего не надето.'
        else:
    
            right_text = f'''Надето: {items[SaveID[count][5]][0]}
{items[SaveID[count][5]][5]}. Урон: {items[SaveID[count][5]][3]} единиц.'''

        bot.send_message(message.chat.id, right_text, reply_markup=markup)

    elif message.text == "Аксессуары":
        look_at_last = 6
        
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][6] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, clothes_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, clothes_button)
        if SaveID[count][6] == 0:
            rings_text = f'Ничего не надето.'
        else:
    
            rings_text = f'Надето: {items[SaveID[count][6]][0]}'
        bot.send_message(message.chat.id, rings_text, reply_markup=markup)

    elif message.text == "Тело":
        count_hero()
        if SaveID[count][10] == 0:
            body_text = f'Куртка не надета.'
        else:
    
            boots_text = f'Надето: {items[SaveID[count][10]][0]}'
        bot.send_message(message.chat.id, body_text)
        if SaveID[count][9] == 0:
            short_text = f'Футболка не надета.'
        else:
    
            short_text = f'Надето: {items[SaveID[count][9]][0]}'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        jacket_button = types.InlineKeyboardButton('Куртка')
        tishort_button = types.InlineKeyboardButton('Футболка')
        markup.add(tishort_button, jacket_button)
        markup.add(clothes_button)
        bot.send_message(message.chat.id, short_text, reply_markup=markup)
    
    elif message.text == "Куртка":
        look_at_last = 10
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][10] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, clothes_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, clothes_button)
        if SaveID[count][10] == 0:
            jacket_text = f'Ничего не надето.'
        else:
    
            jacket_text = f'Надето: {items[SaveID[count][10]][0]}'
        bot.send_message(message.chat.id, jacket_text, reply_markup=markup)
    
    elif message.text == "Футболка":
        look_at_last = 9
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][9] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, clothes_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, clothes_button)
        if SaveID[count][9] == 0:
            tishort_text = f'Ничего не надето.'
        else:
    
            tishort_text = f'Надето: {items[SaveID[count][9]][0]}'
        bot.send_message(message.chat.id, tishort_text, reply_markup=markup)

    elif message.text == "Голова":
        look_at_last = 11
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][11] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, clothes_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, clothes_button)
        if SaveID[count][11] == 0:
            head_text = f'Ничего не надето.'
        else:
    
            head_text = f'Надето: {items[SaveID[count][11]][0]}'
        bot.send_message(message.chat.id, head_text, reply_markup=markup)



    elif message.text == "Штаны":
        look_at_last = 8
        
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][8] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, clothes_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, clothes_button)
        if SaveID[count][8] == 0:
            legs_text = f'Ничего не надето.'
        else:
    
            legs_text = f'Надето: {items[SaveID[count][8]][0]}'
        bot.send_message(message.chat.id, legs_text, reply_markup=markup)

    elif message.text == "Ботинки":
        look_at_last = 7
        count_hero()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        clothes_button = types.InlineKeyboardButton('Вернуться')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        change_button = types.InlineKeyboardButton('Сменить')
        if SaveID[count][7] != 0:
            markup.add(look_at_button, change_button)
            take_off_button = types.InlineKeyboardButton('Снять')
            markup.add(take_off_button, clothes_button)
        else:
            put_up_button = types.InlineKeyboardButton('Надеть')
            markup.add(put_up_button, clothes_button)
        if SaveID[count][7] == 0:
            boots_text = f'Ничего не надето.'
        else:
    
            boots_text = f'Надето: {items[SaveID[count][7]][0]}'
        bot.send_message(message.chat.id, boots_text, reply_markup=markup)
    
    elif message.text == "Осмотреть":
        
        count_hero()
        try:
            photo_id(message, photo_items[SaveID[count][look_at_last]])
        except:
            print('there is no photo in the data')
        if look_at_last > 11:
            if items[SaveID[count-1][23 - look_at_last]][2] == 'clothes':
                bot.send_message(message.chat.id, f'''{items[SaveID[count-1][23 - look_at_last]][0]}:
"{items[SaveID[count-1][23 - look_at_last]][1]}".
Защита: {items[SaveID[count-1][23 - look_at_last]][4]}''')
                if items[SaveID[count-1][23 - look_at_last]][3] == 'rings':
                    if items[SaveID[count-1][23 - look_at_last]][5] == 'love':
                        bot.send_message(message.chat.id, f'''Бонус любви: {items[SaveID[count-1][23 - look_at_last]][6]}''')
                    elif items[SaveID[count-1][23 - look_at_last]][5] == 'stamina':
                        bot.send_message(message.chat.id, f'''Бонус выносливости: {items[SaveID[count-1][23 - look_at_last]][6]}''')
                    elif items[SaveID[count-1][23 - look_at_last]][5] == 'magic':
                        bot.send_message(message.chat.id, f'''Бонус магии: {items[SaveID[count-1][23 - look_at_last]][6]}''')
                    elif items[SaveID[count-1][23 - look_at_last]][5] == 'agility':
                        bot.send_message(message.chat.id, f'''Бонус ловкости: {items[SaveID[count-1][23 - look_at_last]][6]}''')
                    elif items[SaveID[count-1][23 - look_at_last]][5] == 'lordspower':
                        bot.send_message(message.chat.id, f'''Даёт обладателю всемогущество.''')
                    elif items[SaveID[count-1][23 - look_at_last]][5] == 'health':
                        bot.send_message(message.chat.id, f'''Бонус здоровья: {items[SaveID[count-1][23 - look_at_last]][6]}''')

            else:
                bot.send_message(message.chat.id, f'''{items[SaveID[count-1][23 - look_at_last]][0]}:
"{items[SaveID[count-1][23 - look_at_last]][1]}".''')


        elif look_at_last == 6:
            if items[SaveID[count][look_at_last]][2] == 'clothes':
                bot.send_message(message.chat.id, f'''{items[SaveID[count][look_at_last]][0]}:
"{items[SaveID[count][look_at_last]][1]}".
Защита: {items[SaveID[count][look_at_last]][4]}''')
                if items[SaveID[count][look_at_last]][3] == 'rings':
                    if items[SaveID[count][look_at_last]][5] == 'love':
                        bot.send_message(message.chat.id, f'''Бонус любви: {items[SaveID[count][look_at_last]][6]}''')
                    elif items[SaveID[count][look_at_last]][5] == 'stamina':
                        bot.send_message(message.chat.id, f'''Бонус выносливости: {items[SaveID[count][look_at_last]][6]}''')
                    elif items[SaveID[count][look_at_last]][5] == 'magic':
                        bot.send_message(message.chat.id, f'''Бонус магии: {items[SaveID[count][look_at_last]][6]}''')
                    elif items[SaveID[count][look_at_last]][5] == 'agility':
                        bot.send_message(message.chat.id, f'''Бонус ловкости: {items[SaveID[count][look_at_last]][6]}''')
                    elif items[SaveID[count][look_at_last]][5] == 'lordspower':
                        bot.send_message(message.chat.id, f'''Даёт обладателю всемогущество.''')
                    elif items[SaveID[count][look_at_last]][5] == 'health':
                        bot.send_message(message.chat.id, f'''Бонус здоровья: {items[SaveID[count][look_at_last]][6]}''')
        elif 12 > look_at_last > 5:
            bot.send_message(message.chat.id, f'''{items[SaveID[count][look_at_last]][0]}:
"{items[SaveID[count][look_at_last]][1]}".
Защита: {items[SaveID[count][look_at_last]][4]}''')
        else:
            bot.send_message(message.chat.id, f'''{items[SaveID[count][look_at_last]][0]}:
"{items[SaveID[count][look_at_last]][1]}"
{items[SaveID[count][look_at_last]][4]}. Урон: {items[SaveID[count][look_at_last]][3]} единиц.''')
            
        
    elif message.text == "Снять":
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if look_at_last == 4 or look_at_last == 5:
            some_button = types.InlineKeyboardButton('В Инвентарь')
        else:
            some_button = types.InlineKeyboardButton('Вернуться ')
        put_up_button = types.InlineKeyboardButton('Надеть')
        markup.add(put_up_button, some_button)
            
        
        count_ = 0
        for i in reversed(range(0,12)):
            if SaveID[count-1][i] == 0:
                if look_at_last == 5 or look_at_last == 4:
                    if count == 2:
                        SaveID[5][-5 -(10 - look_at_last)] = 1
                    else:
                        SaveID[6][-5 -(10 - look_at_last)] = 1
                elif look_at_last == 6:
                    if items[SaveID[count][look_at_last]][5] == 'love':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус любви: {items[SaveID[count][look_at_last]][6]}''')
                        SaveID[int(4 + count/2)][-1] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-2] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-3] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-4] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-5] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-6] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-7] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-8] -= items[SaveID[count][look_at_last]][6]
                        
                    elif items[SaveID[count][look_at_last]][5] == 'stamina':
                        SaveID[int(4 + count/2)][-3] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-4] -= items[SaveID[count][look_at_last]][6]
                        bot.send_message(message.chat.id, f'''Вы теряете бонус выносливости: {items[SaveID[count][look_at_last]][6]}''')
                        
                    elif items[SaveID[count][look_at_last]][5] == 'magic':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус магии: {items[SaveID[count][look_at_last]][6]}''')
                        SaveID[int(4 + count/2)][-7] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-8] -= items[SaveID[count][look_at_last]][6]
                    elif items[SaveID[count][look_at_last]][5] == 'agility':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус ловкости: {items[SaveID[count][look_at_last]][6]}''')
                        SaveID[int(4 + count/2)][-5] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-6] -= items[SaveID[count][look_at_last]][6]
                    elif items[SaveID[count][look_at_last]][5] == 'lordspower':
                        bot.send_message(message.chat.id, f'''Вы теряете всемогущество...''')
                        SaveID[int(4 + count/2)][-1] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-2] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-3] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-4] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-5] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-6] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-7] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-8] -= items[SaveID[count][look_at_last]][6]
                    elif items[SaveID[count][look_at_last]][5] == 'health':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус здоровья: {items[SaveID[count][look_at_last]][6]}''')
                        SaveID[int(4 + count/2)][-1] -= items[SaveID[count][look_at_last]][6]
                        SaveID[int(4 + count/2)][-2] -= items[SaveID[count][look_at_last]][6]
                    SaveID[int(4 + count/2)][0] -= items[SaveID[count][look_at_last]][4]
                        
                else:
                    SaveID[int(4 + count/2)][0] -= items[SaveID[count][look_at_last]][4]

                SaveID[count-1][i] = SaveID[count][look_at_last]
                take_off_text = f'Снято: {items[SaveID[count][look_at_last]][0]}'
                bot.send_message(message.chat.id, take_off_text, reply_markup=markup)
                count_ = 1
                SaveID[count][look_at_last] = 0
                break
        if count_ == 0:
        
            bot.send_message(message.chat.id, 'Нет места!', reply_markup=markup)

    elif message.text == "Надеть":
        clothes = False
        weapon = True
        
        count_hero()
        look_at_last_()
        put_up_list = []
        if 11 >= look_at_last >= 6:
            for i in reversed(range(0,12)):
                if SaveID[count-1][i] != 0: #problema
                    if items[SaveID[count-1][i]][2] == 'clothes':
                        if items[SaveID[count-1][i]][3] == type_:
                            put_up_list.append(i)
                            clothes = True
        else:
            for i in reversed(range(0,12)):
                if SaveID[count-1][i] != 0:
                    if items[SaveID[count-1][i]][2] == 'weapon':
                        put_up_list.append(i)
                        weapon = True
        
        if len(put_up_list) != 0:
            put_up_text = 'Выберете номер слота, в котором лежит то, что вы хотели бы надеть: \n'
            if clothes == True:
                for i in range(1, len(put_up_list)+1):

                    if look_at_last == 6:
                        if items[SaveID[count-1][put_up_list[i-1]]][2] == 'clothes':
                            put_up_text += f'''Слот {12 - put_up_list[i-1]}: {items[SaveID[count-1][put_up_list[i-1]]][0]}:
"{items[SaveID[count-1][put_up_list[i-1]]][1]}" 
Защита: {items[SaveID[count-1][put_up_list[i-1]]][4]} едениц.\n '''
                            if items[SaveID[count-1][put_up_list[i-1]]][3] == 'rings':
                                if items[SaveID[count-1][put_up_list[i-1]]][5] == 'love':
                                    put_up_text += f'''Бонус любви: {items[SaveID[count-1][put_up_list[i-1]]][6]}\n\n'''
                                elif items[SaveID[count-1][put_up_list[i-1]]][5] == 'stamina':
                                    put_up_text += f'''Бонус выносливости: {items[SaveID[count-1][put_up_list[i-1]]][6]}\n\n'''
                                elif items[SaveID[count-1][put_up_list[i-1]]][5] == 'magic':
                                    put_up_text += f'''Бонус магии: {items[SaveID[count-1][put_up_list[i-1]]][6]}\n\n'''
                                elif items[SaveID[count-1][put_up_list[i-1]]][5] == 'agility':
                                    put_up_text += f'''Бонус ловкости: {items[SaveID[count-1][put_up_list[i-1]]][6]}\n\n'''
                                elif items[SaveID[count-1][put_up_list[i-1]]][5] == 'lordspower':
                                    put_up_text += f'''Даёт обладателю всемогущество.\n\n'''
                                elif items[SaveID[count-1][put_up_list[i-1]]][5] == 'health':
                                    put_up_text += f'''Бонус здоровья: {items[SaveID[count-1][put_up_list[i-1]]][6]}\n\n'''
                    else:
                        put_up_text += f'''Слот {12 - put_up_list[i-1]}: {items[SaveID[count-1][put_up_list[i-1]]][0]}:
"{items[SaveID[count-1][put_up_list[i-1]]][1]}" 
Защита: {items[SaveID[count-1][put_up_list[i-1]]][4]} едениц.\n '''
            elif weapon == True:
                for i in range(1, len(put_up_list)+1):
                    put_up_text += f'''Слот {12 - put_up_list[i-1]}: {items[SaveID[count-1][put_up_list[i-1]]][0]}:
"{items[SaveID[count-1][put_up_list[i-1]]][1]}"
 {items[SaveID[count-1][put_up_list[i-1]]][4]}. Урон: {items[SaveID[count-1][put_up_list[i-1]]][3]} единиц. \n '''
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.InlineKeyboardButton('1')
            button2 = types.InlineKeyboardButton('2')
            button3 = types.InlineKeyboardButton('3')
            button4 = types.InlineKeyboardButton('4')
            button5 = types.InlineKeyboardButton('5')
            button6 = types.InlineKeyboardButton('6')
            button7 = types.InlineKeyboardButton('7')
            button8 = types.InlineKeyboardButton('8')
            button9 = types.InlineKeyboardButton('9')
            button10 = types.InlineKeyboardButton('10')
            button11 = types.InlineKeyboardButton('11')
            button12 = types.InlineKeyboardButton('12')
            dict_ = {
                1: button1 , 2: button2, 3: button3, 4: button4, 5: button5, 6: button6, 7: button7, 8: button8, 9: button9, 10: button10, 11: button11, 12: button12
            }
            for i in range(1, len(put_up_list)+1):
                markup.row(dict_[12 - put_up_list[i -1]])


            put_up = bot.send_message(message.chat.id, f'{put_up_text}', reply_markup=markup)
            bot.register_next_step_handler(put_up, put_up_func)
        else:
            put_up_text = 'Вам нечего надеть :/'

            bot.send_message(message.chat.id, f'{put_up_text}')
    
    elif message.text == "Сменить":
        count_hero()
        look_at_last_()
        clothes = False
        weapon = True

        change_up_list = []
    
        if 11 >= look_at_last >= 6:
            for i in reversed(range(0,12)):
                if SaveID[count-1][i] != 0: #problema
                    if items[SaveID[count-1][i]][2] == 'clothes':
                        if items[SaveID[count-1][i]][3] == type_:
                            change_up_list.append(i)
                            clothes = True
        else:
            for i in reversed(range(0,12)):
                if SaveID[count-1][i] != 0:
                    if items[SaveID[count-1][i]][2] == 'weapon':
                        change_up_list.append(i)
                        weapon = True
                    
              
        if len(change_up_list) != 0:
            change_up_text = 'Выберете номер слота, в котором лежит то, что вы хотели бы надеть: \n'
            if clothes == True:
                for i in range(1, len(change_up_list)+1):

                    if look_at_last == 6:
                        if items[SaveID[count-1][change_up_list[i-1]]][2] == 'clothes':
                            change_up_text += f'''Слот {12 - change_up_list[i-1]}: {items[SaveID[count-1][change_up_list[i-1]]][0]}:
"{items[SaveID[count-1][change_up_list[i-1]]][1]}" 
Защита: {items[SaveID[count-1][change_up_list[i-1]]][4]} едениц.\n '''
                            if items[SaveID[count-1][change_up_list[i-1]]][3] == 'rings':
                                if items[SaveID[count-1][change_up_list[i-1]]][5] == 'love':
                                    change_up_text += f'''Бонус любви: {items[SaveID[count-1][change_up_list[i-1]]][6]}\n'''
                                elif items[SaveID[count-1][change_up_list[i-1]]][5] == 'stamina':
                                    change_up_text += f'''Бонус выносливости: {items[SaveID[count-1][change_up_list[i-1]]][6]}\n'''
                                elif items[SaveID[count-1][change_up_list[i-1]]][5] == 'magic':
                                    change_up_text += f'''Бонус магии: {items[SaveID[count-1][change_up_list[i-1]]][6]}\n'''
                                elif items[SaveID[count-1][change_up_list[i-1]]][5] == 'agility':
                                    change_up_text += f'''Бонус ловкости: {items[SaveID[count-1][change_up_list[i-1]]][6]}\n'''
                                elif items[SaveID[count-1][change_up_list[i-1]]][5] == 'lordspower':
                                    change_up_text += f'''Даёт обладателю всемогущество.\n'''
                                elif items[SaveID[count-1][change_up_list[i-1]]][5] == 'health':
                                    change_up_text += f'''Бонус здоровья: {items[SaveID[count-1][change_up_list[i-1]]][6]}\n'''
                    else:

                
                        change_up_text += f'''Слот {12 - change_up_list[i-1]}: {items[SaveID[count-1][change_up_list[i-1]]][0]}:
"{items[SaveID[count-1][change_up_list[i-1]]][1]}" 
Защита: {items[SaveID[count-1][change_up_list[i-1]]][4]} едениц.\n '''
            elif weapon == True:
                for i in range(1, len(change_up_list)+1):
                    change_up_text += f'''Слот {12 - change_up_list[i-1]}: {items[SaveID[count-1][change_up_list[i-1]]][0]}:
"{items[SaveID[count-1][change_up_list[i-1]]][1]}"
 {items[SaveID[count-1][change_up_list[i-1]]][4]}. Урон: {items[SaveID[count-1][change_up_list[i-1]]][3]} единиц. \n '''
                
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.InlineKeyboardButton('1')
            button2 = types.InlineKeyboardButton('2')
            button3 = types.InlineKeyboardButton('3')
            button4 = types.InlineKeyboardButton('4')
            button5 = types.InlineKeyboardButton('5')
            button6 = types.InlineKeyboardButton('6')
            button7 = types.InlineKeyboardButton('7')
            button8 = types.InlineKeyboardButton('8')
            button9 = types.InlineKeyboardButton('9')
            button10 = types.InlineKeyboardButton('10')
            button11 = types.InlineKeyboardButton('11')
            button12 = types.InlineKeyboardButton('12')
            dict_ = {
                1: button1 , 2: button2, 3: button3, 4: button4, 5: button5, 6: button6, 7: button7, 8: button8, 9: button9, 10: button10, 11: button11, 12: button12
            }
            for i in range(1, len(change_up_list)+1):
                markup.row(dict_[12 - change_up_list[i -1]])


            change_up = bot.send_message(message.chat.id, f'{change_up_text}', reply_markup=markup)
            bot.register_next_step_handler(change_up, change_up_func)
        else:
            change_up_text = 'Не на что сменить :/'

            bot.send_message(message.chat.id, f'{change_up_text}')

    elif message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"  or message.text == "5" or message.text == "6" or message.text == "7" or message.text == "8" or message.text == "9" or message.text == "10" or message.text == "11" or message.text == "12":
        count_hero()
        if SaveID[count-1][12-int(message.text)] != 0:
            
            use = int(message.text)
            look_at_last = 11 + int(message.text)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            one_text = f'''{items[SaveID[count-1][12-int(message.text)]][0]}:
"{items[SaveID[count-1][12-int(message.text)]][1]}"''' 
            delete_button = types.InlineKeyboardButton('Выкинуть')
            inventory_button = types.InlineKeyboardButton('В Инвентарь')
            look_at_button = types.InlineKeyboardButton('Осмотреть')
            change_button = types.InlineKeyboardButton('Применить')
            take_left_button = types.InlineKeyboardButton('Взять в левую руку')
            take_right_button = types.InlineKeyboardButton('Взять в правую руку')
            eat_button = types.InlineKeyboardButton('Съесть')
            if items[SaveID[count-1][12-int(message.text)]][2] == 'weapon':
                markup.add(look_at_button, inventory_button)
                markup.add(take_left_button, delete_button, take_right_button)
            elif items[SaveID[count-1][12-int(message.text)]][2] == 'clothes':
                markup.add(look_at_button, inventory_button)
                markup.add(change_button, delete_button)
            elif items[SaveID[count-1][12-int(message.text)]][2] == 'items':
                markup.add(look_at_button, inventory_button)
                markup.add(change_button, delete_button)
            elif items[SaveID[count-1][12-int(message.text)]][2] == 'food':
                if items[SaveID[count-1][12-int(message.text)]][-1] != 'food':
                    fire_button = types.InlineKeyboardButton('Поджарить')
                    markup.add(look_at_button, inventory_button)
                    markup.add(fire_button, eat_button, delete_button)
                else:
                    markup.add(look_at_button, inventory_button)
                    markup.add(eat_button, delete_button)
            elif items[SaveID[count-1][12-int(message.text)]][2] == 'goodfood':

                markup.add(look_at_button, inventory_button)
                markup.add(eat_button, delete_button)
            bot.send_message(message.chat.id, one_text, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Слот пуст.')

    elif message.text == "Выкинуть":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        yes = types.InlineKeyboardButton('Да')
        no = types.InlineKeyboardButton('Нет')
        markup.add(yes, no)
        delete_item = bot.send_message(message.chat.id, "Это действие нельзя будет отменить. Вы уверены?" ,reply_markup=markup)
        bot.register_next_step_handler(delete_item, delete)

    elif message.text == "Применить" or message.text == "Взять в левую руку" or message.text == 'Взять в правую руку':
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        if message.text == "Взять в левую руку":
            step_ = 4
            if count == 2:
                SaveID[5][-5 -(10 - step_)] = items[SaveID[count-1][12-use]][3]
            else:
                SaveID[6][-5 -(10 - step_)] = items[SaveID[count-1][12-use]][3]
            
                
        elif message.text == "Взять в правую руку":
            step_ = 5
            if count == 2:
                SaveID[5][-5 -(10 - step_)] = items[SaveID[count-1][12-use]][3]
            else:
                SaveID[6][-5 -(10 - step_)] = items[SaveID[count-1][12-use]][3]
        else:
        
            if items[SaveID[count-1][12-use]][-1] == 'fire':
                use_text = f'''Запалыхало пламя''' 
                delete_button = types.InlineKeyboardButton('Выкинуть')
                inventory_button = types.InlineKeyboardButton('В Инвентарь')
                look_at_button = types.InlineKeyboardButton('Осмотреть')
                change_button = types.InlineKeyboardButton('Применить')
                markup.add(look_at_button, inventory_button)
                markup.add(change_button, delete_button)
                bot.send_message(message.chat.id, use_text, reply_markup=markup)
            elif items[SaveID[count-1][12-use]][2] == 'items':
                use_text = f'''Сейчас вы не можите пременить: "{items[SaveID[count-1][12-use]][0]}"''' 
                delete_button = types.InlineKeyboardButton('Выкинуть')
                inventory_button = types.InlineKeyboardButton('В Инвентарь')
                look_at_button = types.InlineKeyboardButton('Осмотреть')
                change_button = types.InlineKeyboardButton('Применить')
                markup.add(look_at_button, inventory_button)
                markup.add(change_button, delete_button)
                bot.send_message(message.chat.id, use_text, reply_markup=markup)
            elif items[SaveID[count-1][12-use]][2] == 'clothes':
                step = items[SaveID[count-1][12-use]][3]
                if  step == 'head':
                    step_ = 11
                elif  step == 'jacket':
                    step_ = 10
                elif step == 'body':
                    step_ = 9
                elif  step == 'legs':
                    step_ = 8
                elif  step == 'boots':
                    step_ = 7
                elif  step == 'rings':
                    step_ = 6
            
        if items[SaveID[count-1][12-use]][2] == 'clothes' or items[SaveID[count-1][12-use]][2] == 'weapon':

            if items[SaveID[count-1][12-use]][2] == 'clothes':
                SaveID[int(4 + count/2)][0] += items[SaveID[count-1][12-use]][4]
                SaveID[int(4 + count/2)][0] -= items[SaveID[count][step_]][4]
                if step_ == 6:
                    if items[SaveID[count-1][12-use]][5] == 'love':

                        bot.send_message(message.chat.id, f'''Вы получаете бонус любви: {items[SaveID[count-1][12-use]][6]}''')
                        SaveID[int(4 + count/2)][-1] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-2] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-3] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-4] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-5] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-6] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-7] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-8] += items[SaveID[count-1][12-use]][6]
                        
                                    
                    elif items[SaveID[count-1][12-use]][5] == 'stamina':
                        SaveID[int(4 + count/2)][-3] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-4] += items[SaveID[count-1][12-use]][6]
                        
                        bot.send_message(message.chat.id, f'''Вы получаете бонус выносливости: {items[SaveID[count-1][12-use]][6]}''')
                                    
                    elif items[SaveID[count-1][12-use]][5] == 'magic':
                        bot.send_message(message.chat.id, f'''Вы получаете бонус магии: {items[SaveID[count-1][12-use]][6]}''')
                        SaveID[int(4 + count/2)][-7] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-8] += items[SaveID[count-1][12-use]][6]
                        
                    elif items[SaveID[count-1][12-use]][5] == 'agility':
                        bot.send_message(message.chat.id, f'''Вы получаете бонус ловкости: {items[SaveID[count-1][12-use]][6]}''')
                        SaveID[int(4 + count/2)][-5] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-6] += items[SaveID[count-1][12-use]][6]
                        
                    elif items[SaveID[count-1][12-use]][5] == 'lordspower':
                        bot.send_message(message.chat.id, f'''Вы получаете всемогущество...''')
                        SaveID[int(4 + count/2)][-1] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-2] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-3] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-4] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-5] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-6] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-7] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-8] += items[SaveID[count-1][12-use]][6]
                    elif items[SaveID[count-1][12-use]][5] == 'health':
                        bot.send_message(message.chat.id, f'''Вы получаете бонус здоровья: {items[SaveID[count-1][12-use]][6]}''')
                        SaveID[int(4 + count/2)][-1] += items[SaveID[count-1][12-use]][6]
                        SaveID[int(4 + count/2)][-2] += items[SaveID[count-1][12-use]][6]
                        
                    
                    if items[SaveID[count][step_]][5] == 'love':

                        bot.send_message(message.chat.id, f'''Вы теряете бонус любви: {items[SaveID[count][step_]][6]}''')
                        
                        SaveID[int(4 + count/2)][-1] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-2] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-3] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-4] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-5] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-6] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-7] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-8] -= items[SaveID[count][step_]][6]
                                    
                    elif items[SaveID[count][step_]][5] == 'stamina':
                        
                        SaveID[int(4 + count/2)][-3] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-4] -= items[SaveID[count][step_]][6]
                        bot.send_message(message.chat.id, f'''Вы теряете бонус выносливости: {items[SaveID[count][step_]][6]}''')
                                    
                    elif items[SaveID[count][step_]][5] == 'magic':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус магии: {items[SaveID[count][step_]][6]}''')
                        
                        SaveID[int(4 + count/2)][-7] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-8] -= items[SaveID[count][step_]][6]
                    elif items[SaveID[count][step_]][5] == 'agility':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус ловкости: {items[SaveID[count][step_]][6]}''')
                        
                        SaveID[int(4 + count/2)][-5] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-6] -= items[SaveID[count][step_]][6]
                    elif items[SaveID[count][step_]][5] == 'lordspower':
                        bot.send_message(message.chat.id, f'''Вы теряете всемогущество...''')
                        SaveID[int(4 + count/2)][-1] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-2] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-3] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-4] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-5] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-6] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-7] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-8] -= items[SaveID[count][step_]][6]
                    elif items[SaveID[count][step_]][5] == 'health':
                        bot.send_message(message.chat.id, f'''Вы теряете бонус здоровья: {items[SaveID[count][step_]][6]}''')
                        
                        SaveID[int(4 + count/2)][-1] -= items[SaveID[count][step_]][6]
                        SaveID[int(4 + count/2)][-2] -= items[SaveID[count][step_]][6]
        

       
                    
            just_a_number = SaveID[count][step_]
            SaveID[count][step_] = SaveID[count-1][12-use]
            SaveID[count-1][12-use] = just_a_number

            
               
    

            
            if SaveID[count-1][12-use] == 0:
                beginning_button = types.InlineKeyboardButton('Продолжить')
                clothes_button = types.InlineKeyboardButton('Надето:')
                weapon_button = types.InlineKeyboardButton('Экипировка:')

                button1 = types.InlineKeyboardButton('1')
                button2 = types.InlineKeyboardButton('2')
                button3 = types.InlineKeyboardButton('3')
                button4 = types.InlineKeyboardButton('4')
                button5 = types.InlineKeyboardButton('5')
                button6 = types.InlineKeyboardButton('6')
                button7 = types.InlineKeyboardButton('7')
                button8 = types.InlineKeyboardButton('8')
                button9 = types.InlineKeyboardButton('9')
                button10 = types.InlineKeyboardButton('10')
                button11 = types.InlineKeyboardButton('11')
                button12 = types.InlineKeyboardButton('12')



                markup.add(clothes_button, beginning_button, weapon_button)
                markup.add(button1, button2, button3, button4, button5, button6)
                markup.add(button7, button8, button9, button10, button11, button12)
                bot.send_message(message .chat.id, f'''Надето: "{items[SaveID[count][step_]][0]}"''', reply_markup=markup)
            else:
                delete_button = types.InlineKeyboardButton('Выкинуть')
                inventory_button = types.InlineKeyboardButton('В Инвентарь')
                look_at_button = types.InlineKeyboardButton('Осмотреть')
                change_button = types.InlineKeyboardButton('Применить')
                markup.add(look_at_button, inventory_button)
                if message.text == "Взять в левую руку" or message.text == 'Взять в правую руку':
                    delete_button = types.InlineKeyboardButton('Выкинуть')
                    take_left_button = types.InlineKeyboardButton('Взять в левую руку')
                    take_right_button = types.InlineKeyboardButton('Взять в правую руку')
                    markup.add(take_left_button, delete_button, take_right_button)
                else:
                    markup.add(change_button, delete_button)
                bot.send_message(message .chat.id, f'''Надето: "{items[SaveID[count][step_]][0]}"
"{items[SaveID[count-1][12-use]][0]}" - убрано в Инвентарь''', reply_markup=markup)
                

    elif message.text == "Бой!":
        count_hero()
        fight(TextID, message)
        rest_count = 0
    elif message.text in ['Восстановление Здоровья', 'Восстановление Маны', 'Восстановление Силы','Восстановление Ловкости','Смертельный Удар','Магическая Волна','Прорыв!','Вихрь!','Высасывание Энергии']:
        bbbb = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        try:
            if items[SaveID[count][attack]][5] == 'agility':
                boost = SaveID[int(4 + count/2)][-6]/10
                typeboost = 'ловкости'
            elif items[SaveID[count][attack]][5] == 'stamina':
                boost = SaveID[int(4 + count/2)][-4]/10
                typeboost = 'выносливости'
            elif items[SaveID[count][attack]][5] == 'magic':
                boost = SaveID[int(4 + count/2)][-8]/10
                typeboost = 'магии'
        except:
            boost = SaveID[int(4 + count/2)][-4]/10
            typeboost = 'выносливости'
        
        if message.text == 'Восстановление Здоровья':
            level_last_level_count0 = 1
            print(level_last_level_count0)
            ability_text = 'Вы почувствовали тепло и ваше здоровье было полностью восстановленно'
            SaveID[int(4 + count/2)][-2] = SaveID[int(4 + count/2)][-1]
            print(level_last_level_count0)

        elif message.text == 'Восстановление Маны':
            level_last_level_count1 = 1
            ability_text = 'Вы почувствовали головокружение и ваша манна была полностью восстановленна'
            SaveID[int(4 + count/2)][-8] = SaveID[int(4 + count/2)][-7]

        elif message.text == 'Восстановление Силы':
            level_last_level_count2 = 1
            ability_text = 'Вы ощутили могучую мощь и ваша выносливость была полностью восстановленна'
            SaveID[int(4 + count/2)][-4] = SaveID[int(4 + count/2)][-3]

        elif message.text == 'Восстановление Ловкости':
            level_last_level_count3 = 1
            ability_text = 'Вы ощутили небесную легкость и ваша ловкость была полностью восстановленна'
            SaveID[int(4 + count/2)][-6] = SaveID[int(4 + count/2)][-5]

        elif message.text == 'Смертельный Удар':
            level_last_level_count4 = 1
            death_damage = int((SaveID[int(4 + count/2)][1]-1)**2 * abs(-50 + SaveID[int(4 + count/2)][-11]+SaveID[int(4 + count/2)][-10]))
            ability_text = f'Вы нанесли колосальный урон в {death_damage} едениц!'
            enemy_hp -= death_damage
            
        elif message.text == 'Вихрь!':
            level_last_level_count7 = 1
            death_damage = int(8*(SaveID[int(4 + count/2)][-6]/10)*SaveID[5][-5 -(10 - attack)])
            ability_text = f'Вы совершили невероятно точный удар в {death_damage} едениц урона!'
            enemy_hp -= death_damage

        elif message.text == 'Магическая Волна':
            level_last_level_count5 = 1
            death_damage = int(8*(SaveID[int(4 + count/2)][-8]/10)*SaveID[5][-5 -(10 - attack)])
            ability_text = f'Вы прочитали заклинание  в {death_damage} едениц урона!'
            enemy_hp -= death_damage

        elif message.text == 'Прорыв!':
            level_last_level_count6 = 1
            death_damage = int(8*(SaveID[int(4 + count/2)][-4]/10)*SaveID[5][-5 -(10 - attack)])
            ability_text = f'Вы провели мощнейший удар в {death_damage} едениц урона!'
            enemy_hp -= death_damage
        elif message.text == 'Высасывание Энергии':
            level_last_level_count8 = 1
            death_damage = int(3*(SaveID[int(4 + count/2)][-4]/10)*SaveID[5][-5 -(10 - attack)])

            ability_text = f'Вы высосали {death_damage} единиц здоровья врага!'
            enemy_hp -= death_damage
            SaveID[int(4 + count/2)][-2] += death_damage
            if SaveID[int(4 + count/2)][-2] > SaveID[int(4 + count/2)][-1]: SaveID[int(4 + count/2)][-2] = SaveID[int(4 + count/2)][-1]
            SaveID[int(4 + count/2)][-4] += 15
            SaveID[int(4 + count/2)][-6] += 15
            SaveID[int(4 + count/2)][-8] += 15
            if SaveID[int(4 + count/2)][-4] > SaveID[int(4 + count/2)][-3]: SaveID[int(4 + count/2)][-4] = SaveID[int(4 + count/2)][-3]
            if SaveID[int(4 + count/2)][-6] > SaveID[int(4 + count/2)][-5]: SaveID[int(4 + count/2)][-6] = SaveID[int(4 + count/2)][-5]
            if SaveID[int(4 + count/2)][-8] > SaveID[int(4 + count/2)][-7]: SaveID[int(4 + count/2)][-8] = SaveID[int(4 + count/2)][-7]

        if message.text in ['Смертельный Удар','Магическая Волна','Прорыв!','Вихрь!','Высасывание Энергии']:
            
            if enemy_hp <= 0 :
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                beginning_button = types.InlineKeyboardButton('Продолжить')
                search_button = types.InlineKeyboardButton('Обыскать')
                markup.add(search_button, beginning_button)
                level_last_level_count0 = 0
                level_last_level_count1 = 0
                level_last_level_count2 = 0
                level_last_level_count3 = 0
                level_last_level_count4 = 0
                level_last_level_count5 = 0
                level_last_level_count6 = 0
                level_last_level_count7 = 0
                level_last_level_count8 = 0
                bot.send_message(message.chat.id, ability_text)
                bot.send_message(message.chat.id, f'''"{mobsID[TextID][0].title()}" был убит.
{name} получил(а) {mobsID[TextID][1][2]} опыта''', reply_markup=markup)
                SaveID[int(4 + count/2)][-9] += mobsID[TextID][1][2]
                lvl(message)
                SaveID[0] -= 1
                TextID += 1
                bbbb = 1
        if bbbb != 1:
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            left_attack_button = types.InlineKeyboardButton('Атаковать левой рукой')
            right_attack_button = types.InlineKeyboardButton('Атаковать правой рукой')
            markup.add(left_attack_button, right_attack_button)
            print(level_last_level_count0)
            if (SaveID[int(6 + count/2)][0] == 1) and (level_last_level_count0 == 0):
                ability_button0 = types.InlineKeyboardButton('Восстановление Здоровья')
                markup.row(ability_button0)
                
                
            if SaveID[int(6 + count/2)][1] == 1 and level_last_level_count1 == 0:
                ability_button1 = types.InlineKeyboardButton('Восстановление Маны')
                markup.row(ability_button1)
            if SaveID[int(6 + count/2)][2] == 1 and level_last_level_count2 == 0:
                ability_button2 = types.InlineKeyboardButton('Восстановление Силы')
                markup.row(ability_button2)
            if SaveID[int(6 + count/2)][3] == 1 and level_last_level_count3 == 0:
                ability_button3 = types.InlineKeyboardButton('Восстановление Ловкости')
                markup.row(ability_button3)
            if SaveID[int(6 + count/2)][4] == 1 and level_last_level_count4 == 0:
                ability_button4 = types.InlineKeyboardButton('Смертельный Удар')
                markup.row(ability_button4)
            if SaveID[int(6 + count/2)][5] == 1 and level_last_level_count5 == 0:
                ability_button5 = types.InlineKeyboardButton('Магическая Волна')
                markup.row(ability_button5)
            if SaveID[int(6 + count/2)][6] == 1 and level_last_level_count6 == 0:
                ability_button6 = types.InlineKeyboardButton('Прорыв!')
                markup.row(ability_button6)
            if SaveID[int(6 + count/2)][7] == 1 and level_last_level_count7 == 0:
                ability_button7 = types.InlineKeyboardButton('Вихрь!')
                markup.row(ability_button7)
            if SaveID[int(6 + count/2)][8] == 1 and level_last_level_count8 == 0:
                ability_button8 = types.InlineKeyboardButton('Высасывание Энергии')
                markup.row(ability_button8)
            bot.send_message(message.chat.id, ability_text, reply_markup=markup)


    elif message.text == 'Атаковать левой рукой' or message.text == 'Атаковать правой рукой':
        if message.text == 'Атаковать левой рукой':
            attack = 4
            
        else:
            attack = 5
        try:
            if items[SaveID[count][attack]][5] == 'agility':
                boost = SaveID[int(4 + count/2)][-6]/10
                typeboost = 'ловкости'
            elif items[SaveID[count][attack]][5] == 'stamina':
                boost = SaveID[int(4 + count/2)][-4]/10
                typeboost = 'выносливости'
            elif items[SaveID[count][attack]][5] == 'magic':
                boost = SaveID[int(4 + count/2)][-8]/10
                typeboost = 'магии'
        except:
            boost = SaveID[int(4 + count/2)][-4]/10
            typeboost = 'выносливости'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        strong_button = types.InlineKeyboardButton('Мощная атака')
        simple_button = types.InlineKeyboardButton('Простая атака')
        markup.add(strong_button, simple_button) 
        

        if items[SaveID[count][attack]][0] == 'Нет':
            bot.send_message(message .chat.id, f'Атака кулаком', reply_markup=markup)
        else:
            bot.send_message(message .chat.id, f'Атака предметом "{items[SaveID[count][attack]][0]}"', reply_markup=markup)
    elif message.text == 'Мощная атака' or message.text == 'Простая атака':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    
        
        random_boost = random.random() + 0.5
        random_boost_ = random.random() + 0.5
        if message.text == 'Простая атака':

            enemy_hp -= round(random_boost*boost*SaveID[5][-5 -(10 - attack)])
            bot.send_message(message.chat.id, f'Вы наносите {round(random_boost*boost*SaveID[5][-5 -(10 - attack)])} урона')
        else:
            
            if typeboost == 'магии':
                if SaveID[int(4 + count/2)][-8] > 19:
                    SaveID[int(4 + count/2)][-8] -= 10
                    lose = 10
                elif SaveID[int(4 + count/2)][-8] > 10:
                    lose = SaveID[int(4 + count/2)][-8] - 10
                else:
                    lose = 0
                    SaveID[int(4 + count/2)][-8] = 10
            elif typeboost == 'ловкости':
                if SaveID[int(4 + count/2)][-6] > 19:
                    SaveID[int(4 + count/2)][-6] -= 10
                    lose = 10
                elif SaveID[int(4 + count/2)][-6] > 10:
                    lose = SaveID[int(4 + count/2)][-6] - 10
                    SaveID[int(4 + count/2)][-6] = 10
                else:
                    lose = 0
            elif typeboost == 'выносливости':
                if SaveID[int(4 + count/2)][-4] > 19:
                    SaveID[int(4 + count/2)][-4] -= 10
                    lose = 10
                elif SaveID[int(4 + count/2)][-4] > 10:
                    lose = SaveID[int(4 + count/2)][-4] - 10
                    SaveID[int(4 + count/2)][-4] = 10
                else:
                    lose = 0
            else:
                if SaveID[int(4 + count/2)][-4] > 19:
                    SaveID[int(4 + count/2)][-4] -= 10
                    lose = 10
                elif SaveID[int(4 + count/2)][-4] > 10:
                    lose = SaveID[int(4 + count/2)][-4] - 10
                    SaveID[int(4 + count/2)][-4] = 10
                else:
                    lose = 0
            if lose != 0:
                enemy_hp -= round(random_boost*2*boost*SaveID[5][-5 -(10 - attack)])

                bot.send_message(message.chat.id, f'Вы теряете {lose} очков {typeboost} и наносите {round(random_boost*2*boost*SaveID[5][-5 -(10 - attack)])} едениц урона')
            else:
                enemy_hp -= round(random_boost*boost*SaveID[5][-5 -(10 - attack)])
                bot.send_message(message.chat.id, f'Вы наносите {round(random_boost*boost*SaveID[5][-5 -(10 - attack)])} едениц урона')
        if enemy_hp > 0:
            SaveID[int(4 + count/2)][-2] -= round(random_boost_*enemy_damage*(100 - SaveID[int(4 + count/2)][0])/100)
            if SaveID[int(4 + count/2)][-2] <= 0:
                TextID = 0
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                starting_button = types.InlineKeyboardButton('Новая игра')
                load_button = types.InlineKeyboardButton('Загрузить')
                bot.send_photo(message.chat.id, photo=open("images\death.png", 'rb'))
                markup.add(starting_button, load_button)
                bot.send_message(message.chat.id, f'''Вы умерли...''', reply_markup=markup)
                SaveID = StartID
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                left_attack_button = types.InlineKeyboardButton('Атаковать левой рукой')
                right_attack_button = types.InlineKeyboardButton('Атаковать правой рукой')
                markup.add(left_attack_button, right_attack_button)
                if (SaveID[int(6 + count/2)][0] == 1) and (level_last_level_count0 == 0):
                    ability_button0 = types.InlineKeyboardButton('Восстановление Здоровья')
                    markup.row(ability_button0)
                if SaveID[int(6 + count/2)][1] == 1 and level_last_level_count1 == 0:
                    ability_button1 = types.InlineKeyboardButton('Восстановление Маны')
                    markup.row(ability_button1)
                if SaveID[int(6 + count/2)][2] == 1 and level_last_level_count2 == 0:
                    ability_button2 = types.InlineKeyboardButton('Восстановление Силы')
                    markup.row(ability_button2)
                if SaveID[int(6 + count/2)][3] == 1 and level_last_level_count3 == 0:
                    ability_button3 = types.InlineKeyboardButton('Восстановление Ловкости')
                    markup.row(ability_button3)
                if SaveID[int(6 + count/2)][4] == 1 and level_last_level_count4 == 0:
                    ability_button4 = types.InlineKeyboardButton('Смертельный Удар')
                    markup.row(ability_button4)
                if SaveID[int(6 + count/2)][5] == 1 and level_last_level_count5 == 0:
                    ability_button5 = types.InlineKeyboardButton('Магическая Волна')
                    markup.row(ability_button5)
                if SaveID[int(6 + count/2)][6] == 1 and level_last_level_count6 == 0:
                    ability_button6 = types.InlineKeyboardButton('Прорыв!')
                    markup.row(ability_button6)
                if SaveID[int(6 + count/2)][7] == 1 and level_last_level_count7 == 0:
                    ability_button7 = types.InlineKeyboardButton('Вихрь!')
                    markup.row(ability_button7)
                if SaveID[int(6 + count/2)][8] == 1 and level_last_level_count8 == 0:
                    ability_button8 = types.InlineKeyboardButton('Высасывание Энергии')
                    markup.row(ability_button8)
                
                bot.send_message(message.chat.id, f'''"{mobsID[TextID][0]}" наносит вам {round(random_boost_*enemy_damage*(100 - SaveID[int(4 + count/2)][0])/100)} едениц урона.''', reply_markup=markup)

        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            beginning_button = types.InlineKeyboardButton('Продолжить')
            search_button = types.InlineKeyboardButton('Обыскать')
            markup.add(search_button, beginning_button)
            level_last_level_count0 = 0
            level_last_level_count1 = 0
            level_last_level_count2 = 0
            level_last_level_count3 = 0
            level_last_level_count4 = 0
            level_last_level_count5 = 0
            level_last_level_count6 = 0
            level_last_level_count7 = 0
            level_last_level_count8 = 0
            bot.send_message(message.chat.id, f'''"{mobsID[TextID][0].title()}" был убит.
{name} получил(а) {mobsID[TextID][1][2]} опыта''', reply_markup=markup)
            SaveID[int(4 + count/2)][-9] += mobsID[TextID][1][2]
            lvl(message)
            SaveID[0] -= 1
            TextID += 1
    

    



    elif message.text == 'Обыскать':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        i = random.random() * 100
        if i <= mobsID[TextID-1][1][4]:
            photo(message)

            
            
            take_button = types.InlineKeyboardButton('Взять')
            beginning_button = types.InlineKeyboardButton('Продолжить')
            markup.add(take_button, beginning_button)
            bot.send_message(message.chat.id, f'''Вы нашли: {items[mobsID[TextID-1][1][3]][0]}''', reply_markup=markup)
        else:
            
            beginning_button = types.InlineKeyboardButton('Продолжить')
            markup.add(beginning_button)
            
            bot.send_message(message.chat.id, f'''Ничего не найдено.''', reply_markup=markup)

    elif message.text == 'Отдохнуть':
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        SaveID[int(4 + count/2)][-2] += int(SaveID[int(4 + count/2)][-1]/2)
        if SaveID[int(4 + count/2)][-2] > SaveID[int(4 + count/2)][-1]: SaveID[int(4 + count/2)][-2] = SaveID[int(4 + count/2)][-1]
        SaveID[int(4 + count/2)][-4] += int(SaveID[int(4 + count/2)][-3]/2)
        SaveID[int(4 + count/2)][-6] += int(SaveID[int(4 + count/2)][-5]/2)
        SaveID[int(4 + count/2)][-8] += int(SaveID[int(4 + count/2)][-7]/2)
        if SaveID[int(4 + count/2)][-4] > SaveID[int(4 + count/2)][-3]: SaveID[int(4 + count/2)][-4] = SaveID[int(4 + count/2)][-3]
        if SaveID[int(4 + count/2)][-6] > SaveID[int(4 + count/2)][-5]: SaveID[int(4 + count/2)][-6] = SaveID[int(4 + count/2)][-5]
        if SaveID[int(4 + count/2)][-8] > SaveID[int(4 + count/2)][-7]: SaveID[int(4 + count/2)][-8] = SaveID[int(4 + count/2)][-7]
        
        rest_count = 1
        beginning_button = types.InlineKeyboardButton('Продолжить')
        beginning_button_back = types.InlineKeyboardButton('Назад')
        markup.add(beginning_button, beginning_button_back)
        settings_button = types.InlineKeyboardButton('Меню⚙️')
        inventory_button = types.InlineKeyboardButton('Инвентарь')
        markup.add(settings_button, inventory_button)
        if SaveID[int(4 + count/2)][1] > 1:
                level_button = types.InlineKeyboardButton('Характеристики')
                markup.add(level_button)
                rest_button = types.InlineKeyboardButton('Отдохнуть')
                markup.add(rest_button, level_button)
              
        bot.send_message(message.chat.id, f'{name} отдохнул(a) и восстановил(a) силы', reply_markup=markup)

    elif message.text in ["Характеристики", 'Нет',"Характеристики💀"]:
        if message.text == "Характеристики":
            TextID -= 1
            SaveID[0] += 1
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        abilities_button = types.InlineKeyboardButton('Умения')
        health_button = types.InlineKeyboardButton('Здоровье')
        stamina_button = types.InlineKeyboardButton('Выносливость')
        agility_button = types.InlineKeyboardButton('Ловкость')
        magic_button = types.InlineKeyboardButton('Духовные силы')
        markup.add(beginning_button, abilities_button)
        
        markup.add(health_button, stamina_button )
        markup.add(agility_button, magic_button)
        
        bot.send_message(message.chat.id, f'''Уровень: {SaveID[int(4 + count/2)][1]-1}
Доступно очков обучения: {SaveID[int(4 + count/2)][2]}
Доступно очков умений: {SaveID[int(4 + count/2)][3]}
Защита: {SaveID[int(4 + count/2)][0]}
Урон левой рукой: {SaveID[int(4 + count/2)][-11]}
Урон правой рукой: {SaveID[int(4 + count/2)][-10]}
Здоровье: {SaveID[int(4 + count/2)][-2]}/{SaveID[int(4 + count/2)][-1]}
Выносливость: {SaveID[int(4 + count/2)][-4]}/{SaveID[int(4 + count/2)][-3]}
Ловкость: {SaveID[int(4 + count/2)][-6]}/{SaveID[int(4 + count/2)][-5]}
Духовные силы: {SaveID[int(4 + count/2)][-8]}/{SaveID[int(4 + count/2)][-7]}''', reply_markup=markup)
        
    elif message.text in ["Здоровье", 'Выносливость', 'Ловкость','Духовные силы']:
        level_last = 0
        for i in ["Здоровье", 'Выносливость', 'Ловкость','Духовные силы']:
            level_last += 1
            if i == message.text:
                break
        count_hero()
        if SaveID[int(4 + count/2)][2] > 0:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yes_button = types.InlineKeyboardButton('Да')
            no_button = types.InlineKeyboardButton('Нет')
            markup.add(yes_button, no_button)
            bot.send_message(message.chat.id, f'Вы действительно хотите потратить одно очко обучения на {message.text}?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, f'У вас нет очков обучения. Повысьте уровень, чтобы получить больше.')

    elif message.text == 'Да':

        SaveID[int(4 + count/2)][-(level_last*2)] += 1
        SaveID[int(4 + count/2)][-(level_last*2) + 1] += 1
        SaveID[int(4 + count/2)][2] -= 1
        bot.send_message(message.chat.id, f'''{['Здоровье', 'Выносливость', 'Ловкость','Духовные силы'][level_last-1]} было повышено на 1''')
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        abilities_button = types.InlineKeyboardButton('Умения')
        health_button = types.InlineKeyboardButton('Здоровье')
        stamina_button = types.InlineKeyboardButton('Выносливость')
        agility_button = types.InlineKeyboardButton('Ловкость')
        magic_button = types.InlineKeyboardButton('Духовные силы')
        markup.add(beginning_button, abilities_button)
        
        markup.add(health_button, stamina_button )
        markup.add(agility_button, magic_button)
        
        bot.send_message(message.chat.id, f'''Уровень: {SaveID[int(4 + count/2)][1]-1}
Доступно очков обучения: {SaveID[int(4 + count/2)][2]}
Доступно очков умений: {SaveID[int(4 + count/2)][3]}
Здоровье: {SaveID[int(4 + count/2)][-2]}/{SaveID[int(4 + count/2)][-1]}
Выносливость: {SaveID[int(4 + count/2)][-4]}/{SaveID[int(4 + count/2)][-3]}
Ловкость: {SaveID[int(4 + count/2)][-6]}/{SaveID[int(4 + count/2)][-5]}
Духовные силы: {SaveID[int(4 + count/2)][-8]}/{SaveID[int(4 + count/2)][-7]}''', reply_markup=markup)

    elif message.text in ['Умения', 'Нет.']:
        if message.text in ['Умения']:
            TextID += 1
            SaveID[0] -= 1
        count_hero()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        level_button = types.InlineKeyboardButton('Характеристики')
        markup.add(level_button)
        if SaveID[int(count/2 + 6)][0] == 0:
            button_of_power0 = types.InlineKeyboardButton('Восстановление здоровья')
            markup.row(button_of_power0)
        if SaveID[int(count/2 + 6)][1] == 0:
            button_of_power1 = types.InlineKeyboardButton('Восстановление маны')
            markup.row(button_of_power1)
        if SaveID[int(count/2 + 6)][2] == 0:
            button_of_power2 = types.InlineKeyboardButton('Восстановление силы')
            markup.row(button_of_power2)
        if SaveID[int(count/2 + 6)][3] == 0:
            button_of_power3 = types.InlineKeyboardButton('Восстановление ловкости')
            markup.row(button_of_power3)
        if SaveID[int(count/2 + 6)][4] == 0:
            button_of_power4 = types.InlineKeyboardButton('Смертельный удар')
            markup.row(button_of_power4)
        if SaveID[int(count/2 + 6)][5] == 0:
            button_of_power5 = types.InlineKeyboardButton('Магическая волна')
            markup.row(button_of_power5)
        if SaveID[int(count/2 + 6)][6] == 0:
            button_of_power6 = types.InlineKeyboardButton('Прорыв')
            markup.row(button_of_power6)
        if SaveID[int(count/2 + 6)][7] == 0:
            button_of_power7 = types.InlineKeyboardButton('Вихрь')
            markup.row(button_of_power7)
        if SaveID[int(count/2 + 6)][8] == 0:
            button_of_power8 = types.InlineKeyboardButton('Высасывание энергии')
            markup.row(button_of_power8)
        bot.send_message(message.chat.id, f'''Одна способность стоит 5 очков умений
Доступно очков умений: {SaveID[int(4 + count/2)][3]}''', reply_markup=markup)
        
    elif message.text in ['Восстановление здоровья', 'Восстановление маны', 'Восстановление силы','Восстановление ловкости','Смертельный удар','Магическая волна','Прорыв','Вихрь','Высасывание энергии']:
        level_last_level = 0
        for i in ['Восстановление здоровья', 'Восстановление маны', 'Восстановление силы','Восстановление ловкости','Смертельный удар','Магическая волна','Прорыв','Вихрь','Высасывание энергии']:
            
            if i == message.text:
                break
            level_last_level += 1
        count_hero()
        if SaveID[int(4 + count/2)][3] > 4:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            yes_button = types.InlineKeyboardButton('Да!')
            no_button = types.InlineKeyboardButton('Нет.')
            markup.add(yes_button, no_button)
            bot.send_message(message.chat.id, f'''Вы действительно хотите потратить 5 очков умений на способность '{message.text}'?''', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, f'У вас не достаточно очков умений. Повысьте уровень, чтобы получить больше.') 
    elif message.text == 'Да!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        SaveID[int(6 + count/2)][level_last_level] += 1
        SaveID[int(4 + count/2)][3] -= 5 
        level_button = types.InlineKeyboardButton('Характеристики')
        markup.add(level_button)
        if SaveID[int(6 + count/2)][0] == 0:
            button_of_power0 = types.InlineKeyboardButton('Восстановление здоровья')
            markup.row(button_of_power0)
        if SaveID[int(6 + count/2)][1] == 0:
            button_of_power1 = types.InlineKeyboardButton('Восстановление маны')
            markup.row(button_of_power1)
        if SaveID[int(6 + count/2)][2] == 0:
            button_of_power2 = types.InlineKeyboardButton('Восстановление силы')
            markup.row(button_of_power2)
        if SaveID[int(6 + count/2)][3] == 0:
            button_of_power3 = types.InlineKeyboardButton('Восстановление ловкости')
            markup.row(button_of_power3)
        if SaveID[int(6 + count/2)][4] == 0:
            button_of_power4 = types.InlineKeyboardButton('Смертельный удар')
            markup.row(button_of_power4)
        if SaveID[int(6 + count/2)][5] == 0:
            button_of_power5 = types.InlineKeyboardButton('Магическая волна')
            markup.row(button_of_power5)
        if SaveID[int(count/2 + 6)][6] == 0:
            button_of_power6 = types.InlineKeyboardButton('Прорыв')
            markup.row(button_of_power6)
        if SaveID[int(count/2 + 6)][7] == 0:
            button_of_power7 = types.InlineKeyboardButton('Вихрь')
            markup.row(button_of_power7)
        if SaveID[int(count/2 + 6)][8] == 0:
            button_of_power8 = types.InlineKeyboardButton('Высасывание энергии')
            markup.row(button_of_power8)
        
        
        bot.send_message(message.chat.id, f'''Вы получили способность '{['Восстановление здоровья', 'Восстановление маны', 'Восстановление силы','Восстановление ловкости','Смертельный удар','Магическая волна','Прорыв','Вихрь','Высасывание энергии'][level_last_level]}' ''', reply_markup=markup)
        bot.send_message(message.chat.id, f'''Доступно очков умений: {SaveID[int(4 + count/2)][3]}''')
    

    
    
        

    #Подземелья dunge = "empty" - имя данжа

    elif message.text == 'ПОДЗЕМЕЛЬЕ💀':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        Last_TextId = TextID
        if TextID < 100: TextID = 1001000
        photo(message)
        out_button = types.InlineKeyboardButton('Наружу')
        go_button = types.InlineKeyboardButton('Дальше')
        markup.add(out_button, go_button)
        bot.send_message(message.chat.id, f'''{beginning_text[str(TextID)]}''', reply_markup=markup)
    elif message.text == 'Дальше':
        TextID += 1
        photo(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        out_button = types.InlineKeyboardButton('Наружу')
        button1 = types.InlineKeyboardButton('1💀')
        button2 = types.InlineKeyboardButton('2💀💀')
        button3 = types.InlineKeyboardButton('3💀💀💀')
        markup.add(button1, button2, button3)
        markup.add(out_button)
        level_dunguon = bot.send_message(message.chat.id, f'{beginning_text[str(TextID)]}', reply_markup=markup)
        bot.register_next_step_handler(level_dunguon, level_dunguon_func)
        
    elif message.text == 'Наружу':
        TextID = Last_TextId
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        photo(message) 
        beginning_button = types.InlineKeyboardButton('Продолжить')
        markup.add(beginning_button)
        settings_button = types.InlineKeyboardButton('Меню⚙️')
        inventory_button = types.InlineKeyboardButton('Инвентарь')
        markup.add(settings_button, inventory_button)
        if SaveID[int(4 + count/2)][1] > 1:
            level_button = types.InlineKeyboardButton('Характеристики')
                
            rest_button = types.InlineKeyboardButton('Отдохнуть')
            markup.add(rest_button, level_button)
            dangeon_button = types.InlineKeyboardButton('ПОДЗЕМЕЛЬЕ💀')
            markup.add(dangeon_button)
        
        bot.send_message(message.chat.id, f'''{beginning_text[str(TextID)]}''', reply_markup=markup)




    elif message.text == 'Дальше💀':
        photo(message)
        TextID = random.choice(dung_list_ids)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        out_button = types.InlineKeyboardButton('Наружу')
        go_button = types.InlineKeyboardButton('Дальше💀💀')
        markup.add(out_button, go_button)
        inventory_button = types.InlineKeyboardButton('Инвентарь💀')
        level_button = types.InlineKeyboardButton('Характеристики💀')
        markup.add(level_button,inventory_button)
        bot.send_message(message.chat.id, f'''{beginning_text[str(TextID)]}''', reply_markup=markup)
    elif message.text == 'Дальше💀💀':
        TextID += 1
        photo(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)    
        fight_button = types.InlineKeyboardButton('Бой!')
        markup.add(fight_button)
        bot.send_message(message.chat.id, f'''{beginning_text[str(TextID)]}''', reply_markup=markup)

    elif message.text == 'Поджарить':
        is_fire = False
        for i in reversed(range(0,12)):
                if SaveID[count-1][i] != 0: #problema
                    if items[SaveID[count-1][i]][-1] == 'fire':
                        is_fire = True
        if is_fire:
            
            
        
            one_text = f'''"{items[SaveID[count-1][12-int(use)]][0]}" - было поджарено.'''
            SaveID[count-1][12-int(use)] = items[SaveID[count-1][12-int(use)]][-1]
        else:
            one_text = 'Вам нечем развести огонь/'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        delete_button = types.InlineKeyboardButton('Выкинуть')
        inventory_button = types.InlineKeyboardButton('В Инвентарь')
        look_at_button = types.InlineKeyboardButton('Осмотреть')
        

        eat_button = types.InlineKeyboardButton('Съесть')
            

        markup.add(look_at_button, inventory_button)
        markup.add(eat_button, delete_button)
        bot.send_message(message.chat.id, one_text, reply_markup=markup)
        
    elif message.text == 'Съесть':
        one_text = f'''Вы съели "{items[SaveID[count-1][12-int(use)]][0]}"'''
        bot.send_message(message.chat.id, one_text)
        if items[SaveID[count-1][12-int(use)]][2] == 'goodfood':
            txt = 'Вы насытились и чувствуете себя намного лучше'
            SaveID[int(4 + count/2)][-2] += int(SaveID[int(4 + count/2)][-1]/2)
            if SaveID[int(4 + count/2)][-2] > SaveID[int(4 + count/2)][-1]: SaveID[int(4 + count/2)][-2] = SaveID[int(4 + count/2)][-1]
            SaveID[int(4 + count/2)][-4] += int(SaveID[int(4 + count/2)][-3]/2)
            SaveID[int(4 + count/2)][-6] += int(SaveID[int(4 + count/2)][-5]/2)
            SaveID[int(4 + count/2)][-8] += int(SaveID[int(4 + count/2)][-7]/2)
            if SaveID[int(4 + count/2)][-4] > SaveID[int(4 + count/2)][-3]: SaveID[int(4 + count/2)][-4] = SaveID[int(4 + count/2)][-3]
            if SaveID[int(4 + count/2)][-6] > SaveID[int(4 + count/2)][-5]: SaveID[int(4 + count/2)][-6] = SaveID[int(4 + count/2)][-5]
            if SaveID[int(4 + count/2)][-8] > SaveID[int(4 + count/2)][-7]: SaveID[int(4 + count/2)][-8] = SaveID[int(4 + count/2)][-7]
        else:
            txt = 'Вы наелись.'
            SaveID[int(4 + count/2)][-2] += int(SaveID[int(4 + count/2)][-1]/4)
            if SaveID[int(4 + count/2)][-2] > SaveID[int(4 + count/2)][-1]: SaveID[int(4 + count/2)][-2] = SaveID[int(4 + count/2)][-1]
            SaveID[int(4 + count/2)][-4] += int(SaveID[int(4 + count/2)][-3]/4)
            SaveID[int(4 + count/2)][-6] += int(SaveID[int(4 + count/2)][-5]/4)
            SaveID[int(4 + count/2)][-8] += int(SaveID[int(4 + count/2)][-7]/4)
            if SaveID[int(4 + count/2)][-4] > SaveID[int(4 + count/2)][-3]: SaveID[int(4 + count/2)][-4] = SaveID[int(4 + count/2)][-3]
            if SaveID[int(4 + count/2)][-6] > SaveID[int(4 + count/2)][-5]: SaveID[int(4 + count/2)][-6] = SaveID[int(4 + count/2)][-5]
            if SaveID[int(4 + count/2)][-8] > SaveID[int(4 + count/2)][-7]: SaveID[int(4 + count/2)][-8] = SaveID[int(4 + count/2)][-7]
        SaveID[count-1][12-int(use)] = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beginning_button = types.InlineKeyboardButton('Продолжить')
        clothes_button = types.InlineKeyboardButton('Надето:')
        weapon_button = types.InlineKeyboardButton('Экипировка:')

        button1 = types.InlineKeyboardButton('1')
        button2 = types.InlineKeyboardButton('2')
        button3 = types.InlineKeyboardButton('3')
        button4 = types.InlineKeyboardButton('4')
        button5 = types.InlineKeyboardButton('5')
        button6 = types.InlineKeyboardButton('6')
        button7 = types.InlineKeyboardButton('7')
        button8 = types.InlineKeyboardButton('8')
        button9 = types.InlineKeyboardButton('9')
        button10 = types.InlineKeyboardButton('10')
        button11 = types.InlineKeyboardButton('11')
        button12 = types.InlineKeyboardButton('12')



        markup.add(clothes_button, beginning_button, weapon_button)
        markup.add(button1, button2, button3, button4, button5, button6)
        markup.add(button7, button8, button9, button10, button11, button12)
        bot.send_message(message.chat.id, txt, reply_markup=markup)
    elif message.text == 'check':
        bot.send_message(message.chat.id, f'''Уровень: {SaveID[int(4 + count/2)][1]-1}
Доступно очков обучения: {SaveID[int(4 + count/2)][2]}
Доступно очков умений: {SaveID[int(4 + count/2)][3]}
Защита: {SaveID[int(4 + count/2)][0]}
Урон левой рукой: {SaveID[int(4 + count/2)][-11]}
Урон правой рукой: {SaveID[int(4 + count/2)][-10]}
Здоровье: {SaveID[int(4 + count/2)][-2]}/{SaveID[int(4 + count/2)][-1]}
Выносливость: {SaveID[int(4 + count/2)][-4]}/{SaveID[int(4 + count/2)][-3]}
Ловкость: {SaveID[int(4 + count/2)][-6]}/{SaveID[int(4 + count/2)][-5]}
Духовные силы: {SaveID[int(4 + count/2)][-8]}/{SaveID[int(4 + count/2)][-7]}''')

    

    


#2






























bot.polling(none_stop=True)