#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, sys, os

listpath = sys.argv[1]
outputpath = sys.argv[2]
listcontent = open(listpath, "rb").read().decode("utf-8")
lines = listcontent.splitlines()

for i, line in enumerate(lines):
    if not line.startswith("http"): continue
    if lines[i-1] != "" and not lines[i-1].startswith("http"):
        title = lines[i-1] + "." + line.split(".")[-1]
    else: title = line.split("/")[-1]
    r = requests.get(line)
    if (not os.path.exists(os.path.join(outputpath, title))) \
        or (os.path.exists(os.path.join(outputpath, title))
        and os.path.getsize(os.path.join(outputpath, title)) <= 16):
        with open(os.path.join(outputpath, title), "wb") as f:
            f.write(r.content)
            print(title + " has been download")

