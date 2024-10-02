# Импорт функции получения случайных чисел
# из модуля random.
from random import randint

# Получаем случайное число в диапазоне от 1 до 100.
number = randint(1, 100)
print('Угадайте число от 1 до 100')
def main():
    while True:
        nado = int(input('Введите число: '))
        
        # Если число меньше загаданного...
        if nado < number:
            # ...выводим сообщение.
            print('Ваше число меньше того, что загадано.')
        
        
        # Если число больше загаданного...
        elif nado > number:
            # ...выводим сообщение.
            print('Ваше число больше того, что загадано.')
        
        # Если число угадано...
        elif nado == number:
            # ...прерываем выполнение программы и...
            break



main()

# ...выводим сообщение.
print('Отличная интуиция! Вы угадали число :)')
