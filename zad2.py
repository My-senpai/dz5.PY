'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
'''

import random


def candyNumber(name):
    candy = int(input('введите количество конфет 1- 28 '))
    while 1>candy>29:
        print('нельзя взять столько конфет')
    return candy

def botmode(value):
    count = random.randint(1, 29)
    while value - count > 28 and value > 29:
        count = random.randint(1, 29)
    return count

def printResult(count, value, name, counter):
    print(name, 'взял', count, 'теперь у него', counter, 'конфет ')

mode = input('Укажи сложность игры \n1 - человек с человеком \n2, 3 - против бота \n')

player_1 = input('Введите имя игрока 1 ')
if mode == 1:
    player_2 = input('Введите имя игрока 2 ')
else:
    player_2 = 'bot'

value = int(input('Введите количество конфет на столе '))

o4eredb = random.randint(0, 2)
if o4eredb:
    print('первый ходит ', player_1)
else:
    print('первый ходит ', player_2)

counter1 = 0
counter2 = 0
while value > 28:
    if o4eredb:
        count = candyNumber(player_1)
        counter1+=count
        value -= count
        o4eredb = False
        printResult(player_1, count, counter1, value)
    else:
        if mode == 2:
            count = random.randint(1, 29)
        elif mode == 3:
            count = botmode(value)
        counter2 += count
        value -= count
        o4eredb = True
printResult(player_2, count, counter2, value)

if o4eredb:
    print('победил игрок ', player_1)
else:
    print('победил игрок ', player_2)


