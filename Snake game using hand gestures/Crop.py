from PIL import Image
import os
from bs4 import BeautifulSoup
from xml.dom import minidom
print("Shrink images in the folder")
folder = input("folder: ")
xmlfolder = input("folder: ")
#wtop = int(input("wtop: "))
#htop = int(input("htop: "))
#wdown = int(input("wdown: "))
#hdown = int(input("hdown: "))
#for i in os.listdir(folder):
#    file = f"{folder}\\{i}"
#    im = Image.open(file)
#    im = im.crop((wtop, htop, wdown, hdown))
#    im.save(file)

for i in os.listdir(folder):
    #file = f"{folder}\\{i}"
    file =i
    #print(file)
    for j in os.listdir(xmlfolder):
        #xmlfile = f"{folder}\\{i}"
        #with open(str(j),'r') as f:
        #    data = f.read()
        #xmldata = BeautifulSoup(data,"xml")
        #print(j)
        xmldata = minidom.parse(xmlfolder+j)
        fname=xmldata.getElementsByTagName('filename')
        if(fname[0].firstChild.data==file):
            print(fname[0].firstChild.data)
            im = Image.open(folder+file)
            xmin = xmldata.getElementsByTagName('xmin')
            wtop = int(xmin[0].firstChild.data)
            #print(wtop)

            ymin = xmldata.getElementsByTagName('ymin')
            htop = int(ymin[0].firstChild.data)

            xmax = xmldata.getElementsByTagName('xmax')
            wdown = int(xmax[0].firstChild.data)

            ymax = xmldata.getElementsByTagName('ymax')
            hdown = int(ymax[0].firstChild.data)
            #print(wtop,htop,wdown,hdown)
            im = im.crop((wtop, htop, wdown, hdown))
            print("1")
            im.save(file)