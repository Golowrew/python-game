from random import randint
from time import sleep
from data import *

def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            crit = randint(1, 100)
            if crit < player['luck']:
                enemy_hp -= player['attack'] * 3
            else:
                enemy_hp -= player['attack']
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack'] * player['armor']
            sleep(1)
        print(f'''{player['name']}: {player['hp']}
{enemy['name']}: {enemy_hp}''')
        print()
        sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
        current_enemy += 1
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    player['hp'] = 100
    print()
    return current_enemy

def training(training_type):
    for i in range(0, 101, 20):
        print(f'Тренировка завершена на {i}%')
        sleep(1.5)
    if training_type == '1':
        player['attack'] += 2
        print(f'Треннировка окончена, сила атаки {player["attack"]}')
    elif training_type == '2':
        player['armor'] -= 0.09
        print(f'Тренировка окончена, ваша защита {player["armor"]}')

def display_inventory():
    print('У вас есть: ')

    for value in player['inventory']:
        print(value)

        print(f'{player["money"]} монет')
        print()
    if 'Зелье удачи' in player['inventory']:
        options = input('''
Желаешь ли ты удачи, воин?
1 - да
2 - нет''')
        if options == '1':
            player['luck'] += 7
            print(f'Готово! Ты воин, получил удачу')
            player['inventory'].remove('Зелье удачи')

def shop():
    print('Приветствую тебя, воин, чего изволите купить на свои копейки?')
    print(f'И это все ваши гроши: {player["money"]}')
    for key, value in items.items():
        print(f'{key} - {value["name"]}: {value["price"]}')

    item = input()
    if item in player['inventory']:
        print(f'Воин, ты ошибся, у тебя уже есть {items[item]["name"]}')
    elif player['money'] >= items[item]['price']:
        print(f'Воин,ты потратил денег на это барахло {items[item]["name"]}')
        player['inventory'].append(items[item]["name"])
        player['money'] -= items[item]['price']
