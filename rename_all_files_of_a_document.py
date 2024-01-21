import os

i = 0
newname = "icon_"
directory = r'D:\AndroidProjects\RESOURCES\digitalmcq icons'

for filename in os.listdir(directory):
    src = directory + "\\" + filename
    dst = directory + "\\" + newname + filename # + ".png"  str(i) + ".jpg"
    i += 1
    os.rename(src, dst)
