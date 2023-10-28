class Point:
    def __init__(self, number):
        self.__number = number
    @property
    def private(self):
        return self.__number
    @private.setter
    def private(self, item):
        self.__number=item
a = Point(20)
a.private =  10
print(a.private)