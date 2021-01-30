import os
import random

# name of folder we will make
DIR = "random/"
# name a file we will make. File name is random
FILE = f"File_{random.randint(0, 100000)}.txt"

# make the directory that will contain FILE
os.makedirs(DIR, exist_ok=True)

# create the file and put some data in it
f = open(DIR + "/" + FILE, "w+")
f.write("Hello World!");
f.close()




