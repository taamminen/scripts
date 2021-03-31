#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys
from moviepy.editor import VideoFileClip, AudioFileClip
from datetime import datetime

try:
    folder_of_files = sys.argv[1]
    timecodes_file = sys.argv[2]
except:
    sys.exit('Arguments should be <folder> and <txt file>')

if not os.path.exists(folder_of_files):
    sys.exit('Folder does not exists')

st = ""
count = 0

for filename in sorted(os.listdir(folder_of_files)):
    if not (filename.endswith(".mp4") or filename.endswith(".mp3")): continue
    if filename.endswith(".mp4"):
        clip = VideoFileClip(os.path.join(folder_of_files, filename))
    elif filename.endswith(".mp3"):
        clip = AudioFileClip(os.path.join(folder_of_files, filename))
    else: continue
    st += datetime.fromtimestamp(count).strftime("%H:%M:%S") + " " + filename + "\n"
    count += clip.duration

st += "\n    Total time: " + datetime.fromtimestamp(count).strftime("%H:%M:%S")

open(timecodes_file, "wb").write(st.encode("utf-8"))
