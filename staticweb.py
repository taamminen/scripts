#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

template = """
<!DOCTYPE html>
<html>
<head>
	<title>{0}</title>
	<meta name="viewport" content="width=device-width, initial-scale=1" />
    <style>
        * {{line-height:1.5;font-family:monospace;font-size:1rem}}
        h1 {{font-size:2rem}}
        body {{color:white;background:black}}
        main {{max-width:732px;margin:0 auto;padding: 21px 0}}
        a {{color:white}}
    </style>
	<meta name="description" content="" />
	<meta property="og:title" content="" />
	<meta property="og:image" content="" />
</head>
<body>
    <main>
		<h1>{0}</h1>{1}        
    </main>
</body>
</html>
"""

content = ""

for file in os.listdir("./external"):
    if file == "index.html": continue
    ext = file.split(".")[-1]
    content += "\n" + " "*8 + "<a href=\"" + file + "\">" + file.replace("."+ext, "") + "</a><br />"

open("./index.html", "wb").write(template.format("external", content).encode("utf-8"))

content = ""

for file in os.listdir("./taamminen"):
    content += "\n" + " "*8 + "<a href=\"./taamminen/" + file + "\">" + file + "</a><br />"

content += "<a href=\"./taamminen.txt\">taamminen.txt</a>"    

open("index.html", "wb").write(template.format("taamminen", content).encode("utf-8"))

