class изменяемые:

# Неизменяемые списки словари и множества он либо их модифицирует либо расширяет либо добавляет новые но не берёт новую ячейку памяти соотвественно.
    # если мы захотим превратить список в словарь то нам придётся брать новую ячейку памяти

    # лист, СПИСОК
    def list_x(self, n):
        return list(range(1, n))


    # дикт, СЛОВАРЬ
    def dict_x(self):
        dict_sample = {
            "Company": "Toyota",
            "model": "Premio",
            "year": 2012
        }
        return dict_sample
    # БАЙТОВЫЙ СПИСОК
    def bait_array(self):
        pass
    
    #  МНОЖЕСТВО определяет неупорядоченную коллекцию уникальных элементов.
    def set_x(self,x):
        return set(range(1,x))
    


# Create an instance of MyClasss
my_class = изменяемые()

# Define a float value x



# ВАЖНО, когда мы меняем что то в стр флоат или инт,кортёж, мы не меняем саму строку или число мы создаём новую и новую ячейку памяти соотвественно

class неизменяемые:
    # str строка
    def str_x(self, str_x):
        return str(str_x)
    # Дробные числа флоат
    def float_x(self, float_x, n):
        return round(float_x, n)
    
    # Целые числа
    def int_x(self,x) -> int:
        import numpy 
        return numpy.sum(numpy.arange(1, x) ** 2)
        
        
    # Создаем кортеж из трех элементов
    def corteg_x(self):
        my_tuple = (1, 2, 3)

        # Печатаем кортеж
        print(my_tuple)

        # Присваиваем кортеж новой переменной
        new_tuple = my_tuple, 4

        # Печатаем новую переменную
        print(new_tuple)
        
my2_class= неизменяемые()
import timeit
# print(timeit)
x = 144_444_100
time_taken = timeit.timeit(lambda: my2_class.int_x(x), number=1)

# Выводим результат и время выполнения
print(f"Result: {my2_class.int_x(x)}")
print(f"Time taken: {time_taken}")





# Создаем обычное множество
my_set = {1, 2, 3, 4, 5}

# Создаем frozenset из обычного множества

                # делает  неизменяемые множества изменяемыми
my_frozenset = frozenset(my_set)

# Попытка изменить frozenset вызовет ошибку, так как он неизменяемый
# Например, следующая строка вызовет ошибку: "AttributeError: 'frozenset' object has no attribute 'add'"
# my_frozenset.add(6)

# Выводим множества
print("Original set:", my_set)
print("Frozen set:", my_frozenset)

# Пример использования frozenset в качестве ключа в словаре
my_dict = {my_frozenset: "This is a frozenset"}

# Выводим словарь
print("Dictionary:", my_dict)


# frozenset в Python является неизменяемой (immutable) версией множества (set). Вот несколько основных случаев использования frozenset: