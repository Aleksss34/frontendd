class clock:
    def __init__(self, time: int):
        if type(time)!=int:
            raise ValueError('Нужно вписать целое число')
        if time!=abs(time):
            raise ValueError('Время должно быть положительным')
        self.__time=time
    def get_clock(self):
        day = self.__time//86400
        hour = (self.__time-day*86400)//3600
        minutes = (self.__time-hour*3600)//60
        sec = (self.__time-hour*3600-minutes*60)
        return f'{self.__get_zero(day)}:{self.__get_zero(hour)}:{self.__get_zero(minutes)}:{self.__get_zero(sec)} '
    @classmethod
    def __get_zero(cls, x):
        return str(x).rjust(2, '0')
    def __add__(self, others):
        if type(others)!=int:
            raise ValueError('Нужно вписать целое число')
        return __class__(self.__time+others)

a = clock(int(input('введите время в секундах:')))
print(a.get_clock())
while True:
    print('хотите добавить немного времени?')
    if input()=='да' or 'yes':


        a+=int(input('введите сколько секунд вы хотите добавить:'))
        print(a.get_clock())
    else:
        print('хорошо')
        break