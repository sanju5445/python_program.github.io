f=open("demofile","rt")
# print(f.read())
# for x in f:
#     words=x.split()
#     txt=''.join(reversed(words))
#     print(txt)
f.close()
f=open("demofile","a")
f.write("now the file has more content")
f.close()
f=open("demofile")
# print(f.read())
f.close()

p=open("demofile","w")
p.write("oopss!!! i have deleted the content")
p.close()

op=open("demofile","r")
print(op.read())
op.close()

# new=open("who","x")
# new.write("the quick brown fox jumps over the lazy dog,,, the quick brown fox jumps over the lazy dog")
# new.close()
# n=open("myfile")
# print(n.read())

# new=open("who","rt")
# print(new.read())
# new.close()
import os
# if os.path.exists("who"):
#     os.remove("who")
# else:
#     print("the file doesn't exist")
try:
    os.remove("who")
except:
    print("the file you want to delete doesn't exist")




# os.remove("xx")
# os.rmdir("xxx")
x=open("demofile")
print(x.read())
x.close()

f=open("demofile","r",encoding="utf-8")
# print(f.read())
print(f.tell())
print(f.seek(0))

current_directory=os.getcwd()
print(current_directory)
# os.mkdir("test")
# os.rmdir("test")
# os.rename('test',"local")
# os.rmdir("local ")