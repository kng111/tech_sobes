''' В питоне есть оператор with. 
 Размещенный внутри код выполняется с особенностью: 
 до и после гарантированно срабатывают события входа в блок withи выхода из него. 
 Объект, который определяет эту логику,
   называется контекстным менеджером.'''


# Пример реализации своего контекстного менеджера на основе класса:
# Определение класса Printable
class Printable:
    # Метод, вызываемый при входе в блок with
    def __enter__(self):
        print('enter')
        return 123

    # Метод, вызываемый при выходе из блока with
    def __exit__(self, exc_type, exc_value, traceback):
        # type, value и traceback предоставляют информацию об исключении, если оно произошло внутри блока with
        # Если исключение не произошло, они будут равны None
        
        if exc_type is not None:
            print(f'Исключение типа {exc_type} с сообщением: {exc_value}')
        print('exit')
        return True  # Если нужно подавить исключение, верните True, иначе оно будет передано дальше


# Использование контекстного менеджера
        
# with Printable() as printer: # В языке программирования Python ключевое слово as используется в контексте оператора with для присвоения результатов выражения
#                                         # , возвращаемого методом __enter__ контекстного менеджера, переменной.
#     # Код внутри блока with
#     print(printer)
#     print('внутри блока with')


with Printable(): # Заходим в блок
    print('внутри блока with')
    raise ValueError('Пример исключения') # raise Возбуждает указанное исключение. 
    

# Когда блок завершается, вызывается метод __exit__




#
         # Пример реализации своего контекстного менеджера с использованием встроенной библиотеки contextlib

# from contextlib import contextmanager

# @contextmanager
# def printable():
#     print('enter')
#     try:
#       yield
#     finally:
#       print('exit')



# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.file = None

#     def __enter__(self):
#         try:
#             self.file = open(self.filename, self.mode, encoding='utf-8')
#             return self.file
#         except FileNotFoundError:
#             print("Error: File not found")
#             raise

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()


# with FileManager("test.txt", "r") as f:
#     if f:
#         print(f.read())


