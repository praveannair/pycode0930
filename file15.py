# names = ["Rajesh","Akhil","Sireesha","Kesava","Basha"]
# num = [f'{i}-{names[i-1]}' for i in range(1,6) if i!=3]
# print(num)

# names = ["Rajesh","Akhil","Sireesha","Kesava","Basha"]
# num1 = {f'{i}-{names[i-1]}' for i in range(1,6)}
# print(num1)


names = ["Rajesh","Akhil","Sireesha","Kesava","Basha"]
score = [45,66,87,34,88]
num = {names[i-1]:score[i-1] for i in range(1,6)}

# num = {f'{i}-{names[i-1]}' for i in range(1,6)}
print(num)





# 1-PawanKumar
# 2-PawanKumar
# 3-PawanKumar
# 4-PawanKumar
# 5-PawanKumar

# num = [1,2,3,4,5]
# num = []
# for i in range(1,6):
#     num.append(i)
# print(num)


#num1 = [1, 4, 9, 16, 25]
# num1 = []
# for i in range(1,6):
#     num1.append(i*i)
# print(num1)

