class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
    def __getitem__(self, item):
        if item>len(self.marks) and item<0:
            raise IndexError('индекс недопустим')
        else:
            return self.marks[item]
    def __setitem__(self,key, item):
        self.marks[key]=item
    def __delitem__(self, item):
        del self.marks[item]
   
s1 = Student('Сергей', [5, 5, 3, 2, 5])
    
print(s1[4])
s1[0] = 10
del s1[2]
print(s1.marks)

