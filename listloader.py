#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, sys, os

try:
    listpath = sys.argv[1]
    outputpath = sys.argv[2]
except:
    sys.exit('Arguments should be <list.txt> and <output_folder>')

try:
    listcontent = open(listpath, "rb").read().decode("utf-8")
except:
    sys.exit('list of files does not exists')

lines = listcontent.splitlines()

for i, line in enumerate(lines):
    if not line.startswith("http"): continue
    if lines[i-1] != "" and not lines[i-1].startswith("http"):
        title = lines[i-1].replace("/", "-") + "." + line.split(".")[-1]
    else: title = line.split("/")[-1]
    if (not os.path.exists(os.path.join(outputpath, title))) \
        or (os.path.exists(os.path.join(outputpath, title))
        and os.path.getsize(os.path.join(outputpath, title)) <= 16):
        r = requests.get(line)
        with open(os.path.join(outputpath, title), "wb") as f:
            f.write(r.content)
            print(title + " has been downloaded")
    else:
        print(title + " has been skipped")
