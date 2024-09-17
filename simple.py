import os

os.system("touch test.txt")


file = open("test.txt", "a")
file.write("this is a test file")
file.close()
