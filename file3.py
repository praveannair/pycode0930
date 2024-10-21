# from collections import Counter
# names=["john","cathy","john","ria","john"]
# mycounter = Counter(names)
# print(mycounter)
# print(mycounter.most_common(1))

# from collections import namedtuple
# fruits = ['orange','mange','apple']
# Price = namedtuple('Price',fruits)
# p = Price(23,43,47)
# print(p)
# print(p.orange)


# from collections import defaultdict
# d = defaultdict(int) #try float
# d['a']=34
# d['b']=45
# print(d['a'])
# print(d['r'])


# from collections import deque
# d=deque([3,5,1])
# d.append(6)
# d.appendleft(9)
# d.pop()
# d.popleft()
# d.clear()
# d.extend([4,5,7])
# d.extendleft([3,1])
# d.rotate(2)
# print(d)

# from collections import ChainMap
# obj1={'a':4,'b':7}
# obj2={'c':9,'d':0}
# obj = ChainMap(obj1,obj2)
# print(c)
# print(obj['d'])

# for i,j in obj.items():
#     print(i,j)


from collections import UserList
class MyList(UserList):
	def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")
L = MyList([1, 2, 3, 4])
print(L)
L.pop()
print(L)



