import os
from PIL import Image


#os.system("backgroundremover -i './photo/test/IMG_6357.JPG' -m 'u2netp' -o 'output4.png'")
#os.system("backgroundremover -i '" + x + "' -m 'u2netp' -o './photo/test/output" + str(y) + ".png'")
import glob

ls =(glob.glob("/Users/apple/remove_bg/*"))

y=0

#picture = Image.open("./photo/test/output1.png")

# Rotate Image By 180 Degree
#picture.rotate(270).save('./photo/test/examcover_rotated90.png')


for x in ls:
    y=y+1
    #os.system("backgroundremover -i '" + x + "' -a -ae 15 -o './photo/test/output/1output"+ str(y) +".png'")
    os.system("backgroundremover -i '" + x + "' -m 'u2netp' -o '/Users/apple/remove_bg/output/" + str(y) + ".png'")
