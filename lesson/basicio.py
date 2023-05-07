# Basic File IO

import os
import locale
import time

# Check current working directory
cwd = os.getcwd()
print(cwd)

# Check Locale
print(locale.getpreferredencoding())

# Straightforward way of opening then closing file
#myfile = open("lesson/basicio.txt")
#lines = myfile.readlines()
#print(lines)
#myfile.close()

# Open file for reading
with open("lesson/basicio.txt", mode="r", encoding="UTF-8") as myfile:
  lines = myfile.readlines()
  print(lines)
  # myfile.write("xxx") # io.UnsupportedOperation: not writable
  # autoclose file
print(lines)

# Open file for writing (append mode)
with open("lesson/basicio.txt", mode="a", encoding="UTF-8") as myfile:
  #myfile.write("\n")
  myfile.write(str(time.gmtime(0)) + "\n")