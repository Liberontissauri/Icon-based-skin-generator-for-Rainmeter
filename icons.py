import os
from shutil import copy2

def geticonpath(icon_name):
    curD = os.getcwd()
    return curD + "\icon\{}".format(icon_name)

def listicons():

    return os.listdir(os.getcwd() + "\icon")

def createfolderstruct(main_folder_name):
    os.mkdir(main_folder_name)
    os.mkdir(os.getcwd() +"\{}".format(main_folder_name)+"\@Resources")
    for icon in listicons():
        icon = icon[0:-4]
        os.mkdir(os.getcwd() +"\{}".format(main_folder_name)+"\{}".format(icon))
        copy2(geticonpath(icon+".png"),os.getcwd()+"\{}".format(main_folder_name)+"\{}".format("@resources"))

def createini(H,W,main_folder_name,icon_name,app_path):
    f = open(os.getcwd()+"\{}".format(main_folder_name)+"\{}".format(icon_name[0:-4])+"\{}".format(icon_name[0:-4] + ".ini"),"w")
    f.writelines(["[Rainmeter]\n",
    "Update=1000\n",
    "\n",
    "[{}]".format(icon_name[0:-4])+"\n",
    "Meter=Image\n",
    "ImageName=#@#\{}".format(icon_name)+"\n",
    "H={}".format(str(H))+"\n",
    "W={}".format(str(W))+"\n",
    'LeftMouseUpAction=["{}"]'.format(app_path)
    ])
    f.close()
