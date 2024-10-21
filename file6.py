from collections import UserString

class MyStr(UserString):
    def upper(self, s = None):
        raise RuntimeError("Deletion not allowed")
        
s = MyStr("Hello")

print(s)

s.upper()
