## Test files used
import os
import hashlib

os.system("touch test.txt")

file = open("test.txt", "a")
file.write("this is a test file")
file.close()

should_fail = hashlib.md5(b'What will happend')
