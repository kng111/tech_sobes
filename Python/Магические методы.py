





'''от несколько часто используемых магических методов:

__init__(self, ...): Инициализация объекта. Вызывается при создании нового экземпляра класса.

__str__(self): Возвращает строковое представление объекта. Вызывается функцией str().

__repr__(self): Возвращает представление объекта, которое может быть использовано для его воссоздания. Вызывается функцией repr().

__len__(self): Возвращает длину объекта. Вызывается функцией len().

__getitem__(self, key): Возвращает элемент по указанному ключу. Вызывается при использовании оператора [].

__setitem__(self, key, value): Устанавливает значение элемента по указанному ключу. Вызывается при использовании оператора [] для присваивания.

__delitem__(self, key): Удаляет элемент по указанному ключу. Вызывается при использовании оператора del.

__call__(self, ...): Позволяет объектам класса вызываться как функции.

__eq__(self, other): Определяет поведение оператора равенства (==).

__lt__(self, other): Определяет поведение оператора меньше (<).

__gt__(self, other): Определяет поведение оператора больше (>).

Это лишь небольшой перечень магических методов, их существует много больше. Использование этих методов позволяет определить поведение объектов в различных контекстах и интегрировать их с определенными языковыми конструкциями.
'''

'''
Называются так потому что начинаются с двух подчёркиваний и заканчиваются ими
'''

'''

Этот термин скорее означает,
 что эти методы обладают специальными свойствами и вызываются автоматически в определенных ситуациях,
   что делает их поведение "волшебным" или "магическим" в смысле автоматизации.

Использование магических методов позволяет классам в Python интегрироваться с различными языковыми конструкциями,
 такими как операторы (+, -, *, /),
   функции (len(),
     str(),
       repr()),
         операторы сравнения (==, <, >),
           операторы индексации ([]),
             вызов объекта как функции,
               и другие.


'''
"""

"""

class MyClass:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

obj = MyClass([1, 2, 3, 4, 5])
print(len(obj))  # Вывод: 5

'''
Магические методы в Python предоставляют возможность управлять 
поведением объектов в различных контекстах и взаимодействовать с различными языковыми конструкциями.
 Их использование придает объектам специфичное поведение и позволяет их интеграцию с языковыми функциями.
   Вот несколько причин,
     почему использовать магические методы:

'''