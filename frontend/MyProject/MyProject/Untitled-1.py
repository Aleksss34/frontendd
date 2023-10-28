from typing import Any


class counter:
    def __init__(self):
        self.__counter=0
        

    def __call__(self, *args, **aargs):
        print('привет')
        self.__counter+=1
        return self.__counter
    def __getattr__(self, item):
        raise ValueError('Ошибка нет обьекта')
    # def __getattribute__(self, item):
    #     if item == 'x':
    #         raise ValueError('Доступ запрещен')
a = counter()
a1 = counter()
a()
a()
a1()
res=a()
res2 = a1()
print(a.x)
print(res, res2)
