
'''

декоратор может поменять входные и выходные данные

Пример с пистолетом и грулителем где декоратор выступает в роли глушителя он меняет поведение нашей функции
    с использованием декоратора мы получаем совсем другой результат на выходе

'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()



