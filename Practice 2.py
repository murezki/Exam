import random


user_input = input(
    "Привет! Введи один из вариантов на выбор: Камень, Ножницы или Бумага")
bot_input = (1, 2, 3)
dasd = random.choice(bot_input)

if bot_input == 1 & user_input == 3:
    print("Вы победили! Хотите сыграть еще?")
if bot_input == 1 & user_input == 2:
    print("Вы проиграли! Хотите сыграть еще?")
if bot_input == 3 & user_input == 1:
    print("Вы проиграли! Хотите сыграть еще?")
if bot_input == 3 & user_input == 2:
    print("Вы победили! Хотите сыграть еще?")
if bot_input == 2 & user_input == 3:
    print("Вы проиграли! Хотите сыграть еще?")
if bot_input == 2 & user_input == 1:
    print("Вы победили! Хотите сыграть еще?")

    