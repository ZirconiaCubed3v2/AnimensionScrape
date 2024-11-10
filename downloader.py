import os
epList = open("episodeslist.txt", 'r')
lines = epList.readlines()
for x in range(0, len(lines)):
    if ("mp4" in lines[x].strip()[-3:]):
        continue
    os.system("wget \"%s\" -O \"%s\"" % (lines[x].strip(), lines[x - 1].strip()))