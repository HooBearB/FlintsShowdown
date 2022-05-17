import json
import os
import MOOSERecoded as moose

class format:
    mode = "Colourmatic"
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    strikethrough = "\u001b[29m"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    dim = "\u001b[2m"
    bold = "\u001b[1m"
    end = "\u001b[0m"
    red = "\u001b[31m"
    blue = "\u001b[36m"
    green = "\u001b[32m"

def mainMenu():
    print(format.blue + format.bold + "   ______" + format.end + format.bold + format.red + "  ______" + format.end + format.bold + format.green + "  ______" + format.end)
    print(format.blue + format.bold + "  / ____/" + format.end + format.bold + format.red + " / ____/" + format.end + format.bold + format.green + " / ____/" + format.end)
    print(format.blue + format.bold + " / /___" + format.end + format.bold + format.red + "  / ____/" + format.end + format.bold + format.green + " /___  /" + format.end)
    print(format.blue + format.bold + "/_____/" + format.end + format.bold + format.red + " /_/    " + format.end + format.bold + format.green + " /_____/" + format.end)
    print()
    decision = moose.askOption("For Flint's Showdown 0.2.5\n", ["Start new mod file", "Open mod file"])
    if decision == 1:
        createCFS()
    if decision == 2:
        openCFS()

def createCFS():
    modname = moose.askString("What would you like to name this CFS folder?", 0)
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, (r'json/cfs/'))
    dirName = os.path.join(filename + modname)
    os.makedirs(dirName)
    followCFS(dirName)

def openCFS():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, (r'json/cfs/'))
    dirList = os.listdir(filename)
    print("")
    if len(dirList) != 0:
        decision = moose.askOption("Which file should be opened?", dirList)
        followCFS(dirList(decision))
    else:
        print("No CFS folders in directory!")
        decision = moose.askOption("Would you like to create a CFS folder?", ["Yes", "No"])
        if decision == 1:
            createCFS()
        if decision == 2:
            mainMenu()

def followCFS(folder):
    x = x + 1

print()
moose.ansiTest()
print(format.clear)
mainMenu()