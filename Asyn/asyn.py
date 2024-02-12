# import time


# def fun1(x):
#     print(x**2)
#     time.sleep(3)
#     print('fun1 завершена')


# def fun2(x):
#     print(x**0.5)
#     time.sleep(3)
#     print('fun2 завершена')


# def main():
#     fun1(4)
#     fun2(4)


# print(time.strftime('%X'))

# main()

# print(time.strftime('%X'))



"""
Асинхронность в Python используется для эффективного управления выполнением кода,
 особенно в сценариях,
   где есть блокирующие операции,
     такие как ввод/вывод (I/O)
"""


"""
 За неимением многопоточности мы можем использвовать асинхронность в Python,
   тем самым мы запускаем функции в асинхронном порядке и не дожидаясь завершения одной можем получить другую функцию.

   Это полезно когда у нас много операций связанных с вводом и выводом с помощью функций
"""
import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))