class Point():
    def __init__(self, number):
        if type(number)!=int:
            raise ValueError('введенное значение должно быть целым числом')
        self.__number = number
    def verification(self, other):
        if type(other)==Point or type(other)==int:
            sc = other
            if type(other)==Point:
                sc = other.__number
            return sc   
        else:
            raise ValueError('Добавить можно только целое число либо обьект класса')
    def __add__(self, other):
        return self.__number+self.verification(other)
    def __radd__(self, other):
        return self.__number+self.verification(other)
    def __sub__(self, other):
        return self.__number-self.verification(other)
    def __rsub__(self, other):
        return self.verification(other)-self.__number
    def __mul__(self, other):
        return self.__number*self.verification(other)
    def __rmul__(self, other):
        return self.__number*self.verification(other)
    def __truediv__(self, other):
        return self.__number/self.verification(other)
    def __rtruediv__(self, other): 
        return self.__number/self.verification(other)
    def __abs__(self, other):
        return abs(other.__number)
    def __len__(self, other):
        return len(other.__number)
n1 = Point(10)
n2 = Point(-20)
n3 = abs(n2+n2+n2+n2)
print(n3)