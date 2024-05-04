from random import randint
from time import sleep
from data import *
from helpers import *

name = input('Введи свое имя: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Выбери действие:
1 - В бой!
2 - Тренировка
3 - Магазин
4 - Инвентарь
''')
    if action == '1':
        current_enemy = fight(current_enemy)
    elif action == '2':
        training_type = input('''1 - тренировать атаку
2 - тренировать оборону''')
        training(training_type)
    elif action == '3':
        shop()
    elif action == '4':
        display_inventory()