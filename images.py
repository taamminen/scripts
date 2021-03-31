#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys
from PIL import Image


try:
    folder = sys.argv[1]
    output_folder = sys.argv[2]
    max_size = int(sys.argv[3])
except:
    sys.exit('Arguments are <folder>, <output folder> and <max size in pixels>')

if not os.path.exists(folder): sys.exit('Folder does not exists')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
            new_filename = os.path.join(output_folder, file)
            img = Image.open(os.path.join(root, file))
            w, h = img.width, img.height
            if w > h:
                neww = max_size
                newh = int(max_size * h / w)
            else:
                newh = max_size
                neww = int(max_size * w / h)
            img = img.resize((neww, newh), Image.ANTIALIAS)
            img.save(os.path.join(output_folder, file))

