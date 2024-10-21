class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        print("Good Morning")
        
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
    def area(self):
        print("Good Evening")
a=Square(4)
a.area()

b=Shape("John")
b.area()