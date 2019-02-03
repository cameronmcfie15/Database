import os
info = ''
file = open('Converter.bat', 'w+')
dirList = os.listdir()
for f in dirList:
    if ".ui" in f:
        remove = f.replace(".ui", "")
        noType = remove+".py"
        if noType not in dirList:
            print("Converting "+f+" to a .py file")
            info = str("pyuic5 -x "+str(f)+" -o "+str(remove)+".py \n")


file.write(info)
file.close()
os.system("Converter.bat")
