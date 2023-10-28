class hello:
    """в классе привет"""
    def __init__(self,item):
        self.item = item
    def __str__(self):
        return 'привет'



a = hello(10)
print(a)
    