class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Используем итератор
my_iterator = MyIterator(1, 5)
for num in my_iterator:
    print(num)

'''Итераторы предоставляют удобный способ обхода последовательностей в Python.'''
'''Инициализация: 
    Вы создаете объект my_iterator, передавая начальное и конечное значения (1 и 5) в конструктор класса MyIterator.

Итераторы в Python:
 Ваш класс MyIterator реализует методы __iter__() и __next__(). Это делает его итератором. 
    Метод __iter__() возвращает сам объект, и метод __next__() 
    возвращает следующее значение в последовательности при каждом вызове и поднимает исключение StopIteration,
        когда последовательность завершается.

Использование в цикле for: 
Вы используете объект my_iterator в цикле for.
 Когда цикл начинается, вызывается метод __iter__(),
   который возвращает сам объект итератора. 
    Затем цикл вызывает __next__() для получения следующего значения до тех пор,
         пока не возникнет исключение StopIteration.

Вывод: 
В результате на экран выводятся числа от 1 до 5, 
так как ваш итератор генерирует значения в этом диапазоне.

Итераторы полезны,
 когда у вас есть последовательность данных, 
 которую вы хотите обойти поочередно, 
 не загружая все значения в память сразу.
   Это помогает экономить ресурсы и поддерживает ленивое вычисление.
     Ваш пример итератора является простым и понятным,
       но в более сложных сценариях итераторы предоставляют эффективный и удобный способ обработки данных.'''

