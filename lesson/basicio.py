# Basic File IO

import os

# Check current working directory
cwd = os.getcwd()
print(cwd)

# Straightforward way of opening then closing file
#myfile = open("lesson/basicio.txt")
#lines = myfile.readlines()
#print(lines)
#myfile.close()

with open("lesson/basicio.txt") as myfile:
  lines = myfile.readlines()
  print(lines)
  # autoclose file
print(lines)