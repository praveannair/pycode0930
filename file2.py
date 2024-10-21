import os
# os.mkdir('temp')
# os.chdir('d:/batches/0930batch/pycode/temp')
# f=open('story.txt','w')
# f.write("Hello World")
# f.close()

os.chdir('d:/batches/0930batch/pycode/temp')
os.remove('story.txt')
os.chdir('../')
os.rmdir('temp')
print(os.listdir())


