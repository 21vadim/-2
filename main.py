import random
print('\nДобро пожаловать в игру "ОТГАДАЙ ЧИСЛО"!')
print('\nЗагадано натуральное число от 1 до 100.')
print('\nПопробуй его отгадать за 10 попыток!')
number=random.randint(1,100)
guess=int(input('\nВаше число:'))
tries=1
while guess !=number:
    if guess > number:
        print('Меньше...')
    elif guess < number:
        print('Больше...')
    if tries == 10:
        print('\nПОПЫТОК БОЛЬШЕ НЕТ! The end...')
        break
    guess = int(input('Следующая попытка: '))
    tries += 1
print('\nПоздравляю!!! Это число:', number)
print('\nВы затратили всего: , tries, ''попыток')
