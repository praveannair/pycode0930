def add(x, y, z = 0):  #method overloading
    if z==0:
        print("Good Morning")
    else:
        print("Good Evening")

print(add(2, 3))

print(add(2, 3, 4))