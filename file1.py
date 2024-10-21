# f=open("story.txt","r")
# s = f.read()
# print(s)
# f.close()

# #file is not closed after the operation
# for line in open("story.txt"): 
#     print(line, end="") 


# #file will be closed automatically – predefined cleanup
with open("story.txt") as f: 
    for line in f: 
        print(line, end="") 
