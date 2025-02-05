import os
import time
import telebot
import cv2
import pyautogui
import keyboard
import datetime
import pytesseract
from selenium import webdriver
from auth_data import token
from telebot import types

# Раздел определения размера экрана #

# xy = str(pyautogui.size())
# i = 0
# global x, y, vol_shape
# for el in xy.split(', '):
#     i += 1
#     if i == 1:
#         x = int(el.replace('Size(width=', ''))
#     if i == 2:
#         y = el.replace('height=', '')
#         y = int(y.replace(')', ''))

# Раздел определения времени #

now = datetime.datetime.now()
date_today = str(now.strftime("%d-%m-%Y"))
i = 0
global number_today, month_today, year_today
for el in date_today.split('-'):
    if i == 0:
        if int(el) < 10:
            el = el.replace('0', '')
        number_today = int(el)
    if i == 1:
        if int(el) < 10:
            el = el.replace('0', '')
        month_today = int(el)
    if i == 2:
        year_today = int(el)
        break
    i += 1

# Основное тело кода #

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    now = datetime.datetime.now()
    time_now = str(now.strftime("%H:%M"))
    if time_now == time_now:
        @bot.message_handler(['start'])
        def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Задать объёмы")
            btn2 = types.KeyboardButton("Стандартный запуск бота")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, text="Выберите конфигурацию запуска бота", reply_markup=markup)
        @bot.message_handler(content_types=['text'])
        def func(message):
            vol_shape = -1
            if (message.text == "Стандартный запуск бота"):
                vol_shape = 2
                bot.send_message(message.chat.id, "Начинаю работу")
            elif (message.text == "Задать объёмы"):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                btn1 = types.KeyboardButton("15 минут")
                btn2 = types.KeyboardButton("1 час")
                btn3 = types.KeyboardButton("1 день")
                btn4 = types.KeyboardButton("Без объёмов")
                back = types.KeyboardButton("Назад")
                markup.add(btn1, btn2, btn3, btn4, back)
                bot.send_message(message.chat.id, text="Выберите период", reply_markup=markup)
            elif (message.text == "15 минут"):
                vol_shape = 0
                bot.send_message(message.chat.id, "Начинаю работу")
            elif (message.text == "1 час"):
                vol_shape = 1
                bot.send_message(message.chat.id, "Начинаю работу")
            elif (message.text == "1 день"):
                vol_shape = 2
                bot.send_message(message.chat.id, "Начинаю работу")
            elif(message.text == "Без объёмов"):
                vol_shape = 3
                bot.send_message(message.chat.id, "Начинаю работу")
            elif (message.text == "Назад"):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                btn1 = types.KeyboardButton("Задать объёмы")
                btn2 = types.KeyboardButton("Стандартный запуск бота")
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, "Выберите конфигурацию запуска бота", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "У меня нет такой комманды")
            if vol_shape != -1:
                global driver, element
                options = webdriver.FirefoxOptions()
                options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
                options.set_preference("general.useragent.override",
                                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
                options.set_preference("dom.webdriver.enabled", False)
                try:
                    driver = webdriver.Firefox(
                            executable_path="C:\py.projects\parser\geckodriver.exe",
                            options=options
                            )
                    with open('urls.py', 'r') as file:
                        cl = 0
                        for element in file:
                            urlend = element
                            url = 'https://ru.tradingview.com/chart/?symbol=' + urlend
                            driver.set_page_load_timeout(10)
                            try:
                                driver.get(url=url)
                            except:
                                time.sleep(1)
                            time.sleep(7)
                            try:
                                if cl == 0:
                                    pyautogui.moveTo(1920 / 2, 1080 / 2)
                                    pyautogui.leftClick(1920 / 2, 1080 / 2)
                                    time.sleep(1)
                                    pyautogui.leftClick(1920 / 2, 1080 / 2)

                                    keyboard.send("f11")
                                    time.sleep(2)

                                    pyautogui.moveTo(1920 / 32 + 25, 1080 / 21.6 + 35)
                                    pyautogui.rightClick(1920 / 32 + 25, 1080 / 21.6 + 35)
                                    pyautogui.moveTo(1920 / 32 + 20 + 25, 1080 / 21.6 + 10 + 40)
                                    pyautogui.leftClick(1920 / 32 + 20 + 25, 1080 / 21.6 + 10 + 40)

                                    # Когда рынок закрыт +80, когда открыт +40 #

                                    # pyautogui.moveTo(1920 / 32 + 25, 1080 / 21.6 + 35)
                                    # pyautogui.rightClick(1920 / 32 + 25, 1080 / 21.6 + 35)
                                    # pyautogui.moveTo(1920 / 32 + 20 + 25, 1080 / 21.6 + 80 + 35)
                                    # pyautogui.leftClick(1920 / 32 + 20 + 25, 1080 / 21.6 + 80 + 35)

                                    # Используется только тогда, когда рынок открыт #

                                    pyautogui.moveTo(1920 / 32 + 25, 1080 / 21.6 + 35)
                                    pyautogui.rightClick(1920 / 32 + 25, 1080 / 21.6 + 35)
                                    pyautogui.moveTo(1920 / 32 + 20 + 25, 1080 / 21.6 + 140 + 35)
                                    pyautogui.leftClick(1920 / 32 + 20 + 25, 1080 / 21.6 + 140 + 35)

                                    pyautogui.moveTo(1920 / 1.33 - 124, 1080 / 4.68)
                                    pyautogui.leftClick(1920 / 1.33 - 124, 1080 / 4.68)

                                    time.sleep(3)
                                    cl += 1
                                else:
                                    pyautogui.moveTo(1920 / 1.33 - 124, 1080 / 4.68)
                                    pyautogui.leftClick(1920 / 1.33 - 124, 1080 / 4.68)

                                global nsovpmaks, nsovpmun, nsovpzakp, exdatesmaks, exdatesmun, exdateszakp, srvol
                                exdatesmaks = '';   exdatesmun = ''
                                exdateszakp = '';   nsovpmaks = 0
                                nsovpmun = 0;       nsovpzakp = 0

                                pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-ORC\tesseract.exe'

                                if vol_shape != 2:
                                    srvol = 0
                                    if vol_shape == 0:
                                        keyboard.send('1')
                                        time.sleep(0.2)
                                        keyboard.send('5')
                                        time.sleep(0.2)
                                        keyboard.send('Enter')
                                        time.sleep(0.2)
                                        pyautogui.moveTo(1920 / 1.33 - 124, 1080 / 4.68)
                                        pyautogui.leftClick(1920 / 1.33 - 124, 1080 / 4.68)
                                        keyboard.send('right')
                                        time.sleep(0.2)
                                    elif vol_shape == 1:
                                        keyboard.send('6')
                                        time.sleep(0.2)
                                        keyboard.send('0')
                                        time.sleep(0.2)
                                        keyboard.send('Enter')
                                        time.sleep(0.2)
                                        pyautogui.moveTo(1920 / 1.33 - 124, 1080 / 4.68)
                                        pyautogui.leftClick(1920 / 1.33 - 124, 1080 / 4.68)
                                        keyboard.send('right')
                                        time.sleep(0.2)
                                    # j = 1
                                    # while j < 11:
                                    #     custom_config = r'--oem 3 --psm 6'
                                    #     driver.save_screenshot("prices_15_1d.png")
                                    #     img_date_shaped = cv2.imread(r'C:\py.projects\parser\prices_15_1d.png')
                                    #     img_vol_shaped = img_date_shaped
                                    #     img_date_shaped = cv2.resize(img_date_shaped, None, fx=2, fy=2)
                                    #     img_date_shaped = cv2.cvtColor(img_date_shaped, cv2.COLOR_BGR2GRAY)
                                    #     img_date_shaped = img_date_shaped[975 * 2:995 * 2, 1460 * 2:1500 * 2]
                                    #     extime = pytesseract.image_to_string(img_date_shaped, lang='rus', config=custom_config)
                                    #     extime = extime.replace('[', '');   extime = extime.replace(']', '')
                                    #     extime = extime.replace('"', '');   extime = extime.replace("'", "")
                                    #     extime = extime.replace('|', '');   extime = extime.replace(' ', '')
                                    #     extime = extime.replace('_', '');   extime = extime.replace('-', '')
                                    #     extime = extime.upper();            i = 0
                                    #     print(extime)
                                    #     for el in extime.split(':'):
                                    #         el = el.replace('О', '0');  el = el.replace('Д', '2')
                                    #         el = el.replace('З', '3');  el = el.replace('А', '4')
                                    #         el = el.replace('Ч', '4');  el = el.replace('Б', '6')
                                    #         el = el.replace('У', '7');  el = el.replace('Т', '7')
                                    #         el = el.replace('В', '8');  el = el.rstrip('\n')
                                    #         if i == 0:
                                    #             exhour = str(el)
                                    #         if i == 1:
                                    #             exmin = str(el)
                                    #         i += 1
                                    #     extime = str(exhour) + str(exmin)
                                    #     print(extime)
                                    #     if extime == '1000' or extime == '1015' or extime == '1830' or extime == '1845' or extime == '1900':
                                    #         keyboard.send('left')
                                    #         continue
                                    #     custom_config = r'--oem 3 --psm 13'
                                    #     img_vol_shaped = cv2.cvtColor(img_vol_shaped, cv2.COLOR_BGR2GRAY)
                                    #     img_vol_shaped = cv2.resize(img_vol_shaped, None, fx=2, fy=2)
                                    #     img_vol_shaped = img_vol_shaped[105 * 2:120 * 2, 110 * 2:175 * 2]
                                    #     vol = pytesseract.image_to_string(img_vol_shaped, lang='eng', config=custom_config)
                                    #     vol = vol.replace('A', '4');    vol = vol.replace('|', '')
                                    #     vol = vol.replace(' ', '');     vol = vol.replace('_', '')
                                    #     vol = vol.replace('—', '');     vol = vol.replace('-', '')
                                    #     vol = vol.rstrip('\n');         vol = vol.upper()
                                    #     if vol[-1] == 'K':
                                    #         vol = vol.replace('K', '')
                                    #         vol = float(vol) * 1000
                                    #     elif vol[-1] == 'M':
                                    #         vol = vol.replace('M', '')
                                    #         vol = float(vol) * 1000000
                                    #     elif vol[-1] == 'B':
                                    #         vol = vol.replace('B', '')
                                    #         vol = float(vol) * 100000000015
                                    #     print(vol)
                                    #     if j == 1:
                                    #         vol_today = vol
                                    #     if j > 1:
                                    #         if j < 11:
                                    #             srvol += vol
                                    #         elif (j == 10) and (float(vol_today) >= (float(srvol) / 9 * 1.2)):
                                    #             print('ПОВЫШЕННЫЙ ОБЪЁМ!!!')
                                    #             print(vol_today)
                                    #             print(srvol)
                                    #             if vol_shape == 0:
                                    #                 add = '15m'
                                    #             if vol_shape == 1:
                                    #                 add = '1h'
                                    #             bot.send_message(message.chat.id, f'#{urlend}\nПовышенный объём - {add}')
                                    #     j += 1
                                    #     keyboard.send('left')
                                    #     time.sleep(0.5)
                                    # keyboard.send('1')
                                    # time.sleep(0.2)
                                    # keyboard.send('d')
                                    # time.sleep(0.2)
                                    # keyboard.send('Enter')
                                    # time.sleep(1)
                                    # pyautogui.moveTo(1920 / 1.33 - 124, 1080 / 4.68)
                                    # pyautogui.leftClick(1920 / 1.33 - 124, 1080 / 4.68)
                                    # for l in range(1, 10):
                                    #     keyboard.send('right')
                                    # time.sleep(1)
                                n = 0
                                srvol = 0
                                while n < 1000:
                                    n += 1
                                    driver.save_screenshot("prices.png")
                                    img_vol = cv2.imread(r'C:\py.projects\parser\prices.png')
                                    img_date = img_vol
                                    img_prc = img_date

                                    # Блок обработки изображения с датой #

                                    custom_config = r'--oem 3 --psm 6'
                                    img_date = cv2.resize(img_date, None, fx=2, fy=2)
                                    img_date = cv2.cvtColor(img_date, cv2.COLOR_BGR2GRAY)
                                    img_date = img_date[950 * 2:970 * 2, 1294 * 2:1375 * 2]
                                    exdate = pytesseract.image_to_string(img_date, lang='rus', config=custom_config)
                                    exdate = exdate.replace('[', '');   exdate = exdate.replace(']', '')
                                    exdate = exdate.replace('"', '');   exdate = exdate.replace("'", "")
                                    exdate = exdate.replace('.', '');   exdate = exdate.replace("‚", "")
                                    exdate = exdate.upper();            i = 0
                                    global exnumber, exmonth, exyear

                                    for el in exdate.split(' '):
                                        if i == 0:
                                            el = el.replace('|', '1')
                                            el = el.replace('О', '0');  el = el.replace('Д', '2')
                                            el = el.replace('З', '3');  el = el.replace('А', '4')
                                            el = el.replace('Ч', '4');  el = el.replace('Б', '6')
                                            el = el.replace('У', '7');  el = el.replace('Т', '7')
                                            el = el.replace('В', '8');  exnumber = el.rstrip('\n')
                                        elif i == 1:
                                            el = el.replace('ЯНВ', '01');   el = el.replace('ФЕВ', '02')
                                            el = el.replace('МАР', '03');   el = el.replace('АПР', '04')
                                            el = el.replace('АЛР', '04');   el = el.replace('МАЙ', '05')
                                            el = el.replace('КАЙ', '05');   el = el.replace('ИЮН', '06')
                                            el = el.replace('ИЮЛ', '07');   el = el.replace('АВГ', '08')
                                            el = el.replace('СЕН', '09');   el = el.replace('ОКТ', '10')
                                            el = el.replace('0КТ', '10');   el = el.replace('НОЯ', '11')
                                            el = el.replace('Н0Я', '11');   el = el.replace('ДЕК', '12')
                                            exmonth = el.rstrip('\n')
                                        elif i == 2:
                                            el = el.replace('О', '0');  el = el.replace('Д', '2')
                                            el = el.replace('З', '3');  el = el.replace('А', '4')
                                            el = el.replace('Ч', '4');  el = el.replace('Б', '6')
                                            el = el.replace('У', '7');  el = el.replace('Т', '7')
                                            el = el.replace('В', '8');  exyear = '20' + el.rstrip('\n')
                                            break
                                        i += 1

                                    exdate = str(exnumber) + '-' + str(exmonth) + '-' + str(exyear)
                                    print(exdate)

                                    # cv2.imshow('test-date', img_date)
                                    # cv2.waitKey()
                                    # time.sleep(1000)

                                    # Блок проверки даты "left-right" #

                                    if int(exnumber) < 10:
                                        exnumber = exnumber.replace('0', '')
                                    if int(exmonth) < 10:
                                        exmonth = exmonth.replace('0', '')
                                    if n == 1 and int(exmonth) == int(month_today) and int(exnumber) == int(number_today):
                                        print('Мы на месте')
                                        n += 1
                                    if n == 1 and int(exmonth) > int(month_today):
                                        print('Сработало влево')
                                        keyboard.send('left')
                                        time.sleep(0.5)
                                        n -= 1
                                        continue
                                    if n == 1 and int(exmonth) <= int(month_today):
                                        if int(exmonth) == int(month_today):
                                            if int(exnumber) > int(number_today):
                                                print('Сработало влево')
                                                keyboard.send('left')
                                                time.sleep(0.5)
                                                n -= 1
                                                continue
                                            else:
                                                print('Сработало вправо')
                                                keyboard.send('right')
                                                time.sleep(0.5)
                                                n -= 1
                                                continue
                                        elif int(exmonth) < int(month_today):
                                            print('Сработало вправо')
                                            keyboard.send('right')
                                            time.sleep(0.5)
                                            n -= 1
                                            continue
                                    if ((int(month_today) - int(exmonth) > 3) or (12 - int(exmonth) - int(month_today)) == 1):
                                        # print(12 - int(exmonth) - int(month_today))
                                        print('Прошло три месяца')
                                        break

                                    # Блок обработки изображения с объёмами #

                                    custom_config = r'--oem 3 --psm 13'
                                    if vol_shape == 2:
                                        if n < 12:
                                            img_vol = cv2.cvtColor(img_vol, cv2.COLOR_BGR2GRAY)
                                            img_vol = cv2.resize(img_vol, None, fx=2, fy=2)
                                            img_vol = img_vol[135*2:150*2, 145*2:220*2]

                                            # cv2.imshow('test', img_vol)
                                            # cv2.waitKey()
                                            # time.sleep(1000)

                                            vol = pytesseract.image_to_string(img_vol, lang='eng', config=custom_config)
                                            vol = vol.replace('A', '4');    vol = vol.replace('|', '')
                                            vol = vol.replace(' ', '');     vol = vol.replace('_', '')
                                            vol = vol.replace('—', '');     vol = vol.replace('-', '')
                                            vol = vol.rstrip('\n');         vol = vol.upper()
                                            vol = vol.replace('©', '');     vol = vol.replace('K.', 'K')
                                            vol = vol.replace('M.', 'M');   vol = vol.replace('B.', 'B')

                                            if vol[-1] == 'K':
                                                vol = vol.replace('K', '')
                                                vol = float(vol) * 1000
                                            elif vol[-1] == 'M':
                                                vol = vol.replace('M', '')
                                                vol = float(vol) * 1000000
                                            elif vol[-1] == 'B':
                                                vol = vol.replace('B', '')
                                                vol = float(vol) * 1000000000
                                            print(vol)
                                            if n == 2:
                                                vol_today = vol
                                            if n > 2:
                                                if n < 12:
                                                    srvol += vol
                                                elif (n == 12) and (float(vol_today) >= (float(srvol) / 9 * 1.2)):
                                                    print('ПОВЫШЕННЫЙ ОБЪЁМ!!!')
                                                    print(vol_today)
                                                    print(srvol)
                                                    bot.send_message(message.chat.id, f'#{urlend}\nПовышенный объём')

                                    # Блок обработки изображения с ценами #

                                    custom_config = r'--oem 3 --psm 13'
                                    img_prc = cv2.cvtColor(img_prc, cv2.COLOR_BGR2GRAY)
                                    img_prc = cv2.resize(img_prc, None, fx=1.5, fy=1.5)
                                    img_prc = img_prc[93:134, 235:1200]

                                    # cv2.imshow('ex', img_prc)
                                    # cv2.waitKey()
                                    # time.sleep(1000)

                                    exprices = pytesseract.image_to_string(img_prc, lang='eng', config=custom_config)
                                    exprices = exprices.replace('[', '');       exprices = exprices.replace(']', '')
                                    exprices = exprices.replace('"', '');       exprices = exprices.replace("'", "")
                                    exprices = exprices.replace(',', '.');      exprices = exprices.replace(' ', '.')
                                    exprices = exprices.replace('..', '.');     exprices = exprices.replace('_', '')
                                    exprices = exprices.replace('—', '');       exprices = exprices.replace('-', '')
                                    exprices = exprices.replace('..', '.');     exprices = exprices.upper()
                                    # print(exprices)
                                    i = 0
                                    global OTKP, MAKC, MUN, ZAKP, exMAKC, exMUN, exZARP
                                    for el in exprices.split('.'):
                                        el = el.replace('O', '0');  el = el.replace('I', '1')
                                        el = el.replace('S', '5');  el = el.replace('E', '')
                                        m = 0
                                        for letter in exprices:
                                            if letter == ".":
                                                m += 1
                                        if el[0] == '0' and len(el) > 1 and i == 0: el = el[1:]
                                        if el[0] == '3' and (len(el) > 1 and (el[1] == 'A' or el[1] == 'B')): el = el[1:]
                                        digits = "0123456789"
                                        found = [el.index(dig) for dig in digits if dig in el]
                                        firstdig = min(found) if found else None
                                        if m >= 7:
                                            if i == 0:
                                                if firstdig != None:
                                                    OTKP = el[firstdig:]
                                                    b = len(OTKP)
                                                else:
                                                    i -= 1
                                            if i == 1:
                                                a = len(el)
                                                OTKP += '.' + el
                                            if i == 2:
                                                if firstdig != None:
                                                    MAKC = el[firstdig:]
                                                    if len(MAKC) > b:
                                                        MAKC = MAKC[:b]
                                                else:
                                                    i -= 1
                                            elif i == 3:
                                                if len(el) > a:
                                                    el = el[:a]
                                                MAKC += '.' + el
                                            elif i == 4:
                                                if firstdig != None:
                                                    MUN = el[firstdig:]
                                                    if len(MUN) > b:
                                                        MUN = MUN[:b]
                                                else:
                                                    i -= 1
                                            elif i == 5:
                                                if len(el) > a:
                                                    el = el[:a]
                                                MUN += '.' + el
                                            elif i == 6:
                                                if firstdig != None:
                                                    ZAKP = el[firstdig:]
                                                    if len(ZAKP) > b:
                                                        ZAKP = ZAKP[:b]
                                                else:
                                                    i -= 1
                                            elif i == 7:
                                                if len(el) > a:
                                                    el = el[:a]
                                                ZAKP += '.' + el
                                                break
                                            i += 1
                                        else:
                                            if i == 0:
                                                if firstdig != None:
                                                    OTKP = el[firstdig:]
                                                    b = len(OTKP)
                                                else:
                                                    i -= 1
                                            elif i == 1:
                                                if firstdig != None:
                                                    MAKC = el[firstdig:]
                                                    if len(MAKC) > b:
                                                        MAKC = MAKC[:b]
                                                else:
                                                    i -= 1
                                            elif i == 2:
                                                if firstdig != None:
                                                    MUN = el[firstdig:]
                                                    if len(MUN) > b:
                                                        MUN = MUN[:b]
                                                else:
                                                    i -= 1
                                            elif i == 3:
                                                if firstdig != None:
                                                    ZAKP = el[firstdig:]
                                                    if len(ZAKP) > b:
                                                        ZAKP = ZAKP[:b]
                                                else:
                                                    i -= 1
                                            i += 1
                                    OTKP = OTKP.replace('Z', '2')
                                    exMAKC = MAKC.replace('Z', '2')
                                    exMUN = MUN.replace('Z', '7')
                                    exZARP = ZAKP.replace('Z', '7')
                                    if exMAKC < OTKP:
                                        MAKC = MAKC.replace('Z', '7')
                                    else:
                                        MAKC = MAKC.replace('Z', '2')
                                    if exMUN > MAKC:
                                        MUN = MUN.replace('Z', '2')
                                    else:
                                        MUN = MUN.replace('Z', '7')
                                    if exZARP > MAKC:
                                        ZAKP = ZAKP.replace('Z', '2')
                                    else:
                                        ZAKP = ZAKP.replace('Z', '7')
                                    exprices = OTKP + ' ' + MAKC + ' ' + MUN + ' ' + ZAKP
                                    print(exprices)

                                    # Блок определения уровня #

                                    global prices_today

                                    if n == 2:
                                        prices_today = OTKP + ' ' + MAKC + ' ' + MUN + ' ' + ZAKP
                                    if n > 2:
                                        i = 0
                                        j = 0
                                        for el1 in prices_today.split(' '):
                                            for el2 in exprices.split(' '):
                                                if (i > 0) and (j > 0) and (j % 4 != 0):
                                                    el2 = el2.rstrip('\n')
                                                    el1 = el1.rstrip('\n')
                                                    if ((float(el2) * 0.9995) <= float(el1) <= (float(el2) * 1.0005)): # 0.9993 и 1.0007 #
                                                        m = j
                                                        if (m == 1) or (m == 5) or (m == 9) or (m == 13):
                                                            m = 'МАКС'
                                                        elif (m == 2) or (m == 6) or (m == 10) or (m == 14):
                                                            m = 'МИН'
                                                        elif (m == 3) or (m == 7) or (m == 11) or (m == 15):
                                                            m = 'ЗАКР'
                                                        urlend = urlend.strip('\n')
                                                        if i == 1:
                                                            nsovpmaks += 1
                                                            exdatesmaks += str(exdate.rstrip('\n')) + ' ' + str(el2) + ' ' + str(m) + '\n'
                                                            if nsovpmaks >= 4:
                                                                f1 = open('outputmax.py', 'w')
                                                                f1.write('#' + urlend + ' — ' + el1 + '\n\n' + exdatesmaks)
                                                                f1.close()
                                                        if i == 2:
                                                            nsovpmun += 1
                                                            exdatesmun += str(exdate.rstrip('\n')) + ' ' + str(el2) + ' ' + str(m) + '\n'
                                                            if nsovpmun >= 4:
                                                                f2 = open('outputmin.py', 'w')
                                                                f2.write('#' + urlend + ' — ' + el1 + '\n\n' + exdatesmun)
                                                                f2.close()
                                                        if i == 3:
                                                            nsovpzakp += 1
                                                            exdateszakp += str(exdate.rstrip('\n')) + ' ' + str(el2) + ' ' + str(m) + '\n'
                                                            if nsovpzakp >= 4:
                                                                f3 = open('outputclose.py', 'w')
                                                                f3.write('#' + urlend + ' — ' + el1 + '\n\n' + exdateszakp)
                                                                f3.close()
                                                j += 1
                                            i += 1
                                    keyboard.send("left")
                                    time.sleep(1)
                                f1 = open('outputmax.py', 'r');     f_1 = f1.read()
                                if os.stat('outputmax.py').st_size != 0:
                                    bot.send_message(message.chat.id, f'{f_1}');    f1.close()
                                f2 = open('outputmin.py', 'r');     f_2 = f2.read()
                                if os.stat('outputmin.py').st_size != 0:
                                    bot.send_message(message.chat.id, f'{f_2}');    f2.close()
                                f3 = open('outputclose.py', 'r');   f_3 = f3.read()
                                if os.stat('outputclose.py').st_size != 0:
                                    bot.send_message(message.chat.id, f'{f_3}');    f3.close()
                            except Exception as ex:
                            #     keyboard.send('1')
                            #     time.sleep(0.5)
                            #     keyboard.send('d')
                            #     time.sleep(0.5)
                            #     keyboard.send('Enter')
                            #     time.sleep(0.5)
                                print(ex)
                                pass
                except Exception as ex:
                    print(ex)
                finally:
                    driver.close();                     driver.quit()
                    f1 = open('outputmax.py', 'w');     f1.close()
                    f2 = open('outputmin.py', 'w');     f2.close()
                    f3 = open('outputclose.py', 'w');   f3.close()
                    file.close()
                    bot.send_message(message.chat.id, "На сегодня всё!")
        bot.polling()
    else:
        print('Подождите')
        print(time_now)
        time.sleep(60)
        telegram_bot(token)
if __name__ == '__main__':
    telegram_bot(token)