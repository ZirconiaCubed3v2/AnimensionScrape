import os
try:
    os.mkdir("outfiles")
except FileExistsError:
    pass
epList = open("episodeslist.txt", 'r')
lines = epList.readlines()
for x in range(0, len(lines) - 1):
    if ("mp4" in lines[x].strip()):
        continue
    os.system("wget \"%s\" -O \"outfiles/%s\"" % (lines[x].strip(), lines[x - 1].strip()))