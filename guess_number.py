from random import randint

number_rand = randint(1, 101)
print('Угадайте число от 1 до 100')

while True:

    random_inp = int(input('Введите число '))

    if random_inp < number_rand:
        print('Ваше число меньше загаданного')
    elif random_inp > number_rand:
        print('Ваше число больше загаданного')
    elif random_inp == number_rand:
        break
print('Win')