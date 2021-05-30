#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import datetime
from moviepy.editor import AudioFileClip

finalstr = ""
finalcount = 0

for subdir, dirs, files in sorted(os.walk(".")):
    count = 0
    localstr = "[img=right][/img]\n"
    for file in sorted(files):
        if not file.endswith(".mp3"): continue
        localstr += file.replace(".mp3", "") + "\n"
        audio = AudioFileClip(os.path.join(subdir, file))
        count += audio.duration
    finalcount += count
    finalstr += "[spoiler=\""
    finalstr += subdir.replace("./", "")
    finalstr += " (" + str(datetime.timedelta(seconds=int(count)))
    finalstr += ")\"]\n" + localstr + "[/spoiler]\n"
        
print(finalstr)
print(str(datetime.timedelta(seconds=int(finalcount))))
