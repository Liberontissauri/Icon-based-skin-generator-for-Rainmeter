import icons

opt = ""
#option
H = ""
#Height
W = ""
#Width
main_folder_name = ""
app_path = ""

print("-"*40)
print("Icon based skin generator for Rainmeter")
print("-"*40)

print("")

print("-"*60)
print("Ensure that all the icons PNG's are into the icon folder ")
print("-"*60)
opt = str(input("insert anything to proceed : "))

print("")

main_folder_name = str(input("Insert a name for the skin: "))
print("creating folder structure...")
icons.createfolderstruct(main_folder_name)
print("folder structure created!")

print("")

print("Insert the informations correspondent to each icon :")

for icon in icons.listicons():
    print("")
    app_path = str(input(icon[0:-4] + " - path: "))
    H = str(input(icon[0:-4] + " - Height (not of the image): "))
    W = str(input(icon[0:-4] + " - Width (not of the image): "))
    print("creating .ini ...")
    icons.createini(H,W,main_folder_name,icon,app_path)
    print(".ini created!")

print("")
print("")
print("All processes are finished")
print("Move the folder {} to the skins folder of Rainmeter".format(main_folder_name))

