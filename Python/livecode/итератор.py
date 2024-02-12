my_list = [1, 2, 3, 4, 5]

# Получаем итератор из списка
my_iterator = iter(my_list)

# Выводим элементы итератора
print(next(my_iterator))   # выведет 1
print(next(my_iterator))   # выведет 2
print(next(my_iterator))   # выведет 3


def my_generator():
    yield 1
    yield 2
    yield 3
    yield '123'
    yield 5

# Получаем итератор из генератора
my_iterator = my_generator()

# Выводим элементы итератора
print(next(my_iterator))   # выведет 1
print(next(my_iterator))   # выведет 2
print(next(my_iterator))   # выведет 3
print(next(my_iterator))   # выведет 4
print(next(my_iterator))   # выведет 5