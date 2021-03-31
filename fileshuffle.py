#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys
from random import randrange

try:
    folder = sys.argv[1]
    length = int(sys.argv[2])
except:
    sys.exit('Arguments should be <folder> and <length num>')

def random_string(length=7):
    result = ""
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    for i in range(0, length):
        result += chars[randrange(0, len(chars)-1)]
    return result

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.find(".") > -1:
            new_filename = random_string(length) + "." + file.split(".")[-1]
        else: new_filename = random_string(length)
        os.rename(os.path.join(root, file), os.path.join(root, new_filename))
