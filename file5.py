from collections import UserDict

class custdict(UserDict):
    def pop(self, s = None):
            raise RuntimeError("Deletion not allowed")

mydict = custdict({'a': 2, 'b': 33})
print(mydict['a'])
mydict.pop('b')
print(mydict.data)
