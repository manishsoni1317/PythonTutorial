import os
path1 = os.path.abspath(os.getcwd())
print(path1)

f = open("write.txt", "w")
f.write("Hello, World!\n")
f.write("This is a file write example.\n")
f.close()