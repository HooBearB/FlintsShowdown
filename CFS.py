import json
import os

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

def ask(message, indent, options, lookingFor = ""):
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    runline = 0
    while runline < len(options):
        if runline == lookingFor:
            print("  - ", end = "")
        else:
            run = 0
            while run <= indent + 1:
                print(" ", end = "")
                run = run + 1
        print(str(runline + 1) + ". " + options[runline])
        runline = runline + 1
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    while type(decision) != int:
        try:
            decision = int(decision)
        except:
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            print("Invalid input!")
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            decision = input("> ")
    while decision < 1 or decision > len(options):
        run = 0
        while run <= indent:
            print(" ", end = "")
            run = run + 1
        print("Invalid input!")
        run = 0
        while run <= indent:
            print(" ", end = "")
            run = run + 1
        decision = input("> ")
        while type(decision) != int:
            try:
                decision = int(decision)
            except:
                run = 0
                while run <= indent:
                    print(" ", end = "")
                    run = run + 1
                print("Invalid input!")
                run = 0
                while run <= indent:
                    print(" ", end = "")
                    run = run + 1
                decision = input("> ")
    return decision

def askOpen(message, indent):
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    while type(decision) != int:
        try:
            decision = int(decision)
        except:
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            print("Invalid input!")
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            decision = input("> ")
    return decision

def askString(message, indent):
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    return decision

def mainMenu():
    print(format.red + format.bold + "   ______" + format.end + format.bold + format.green + "  ______" + format.end + format.bold + format.blue + "  ______" + format.end)
    print(format.red + format.bold + "  / ____/" + format.end + format.bold + format.green + " / ____/" + format.end + format.bold + format.blue + " / ____/" + format.end)
    print(format.red + format.bold + " / /___" + format.end + format.bold + format.green + "  / ____/" + format.end + format.bold + format.blue + " /___  /" + format.end)
    print(format.red + format.bold + "/_____/" + format.end + format.bold + format.green + " /_/    " + format.end + format.bold + format.blue + " /_____/" + format.end)
    print()
    decision = ask("For Flint's Showdown 0.2.5\n", 0, ["Start new mod file", "Open mod file"])
    if decision == 1:
        createCFS()
    if decision == 2:
        openCFS()

def createCFS():
    modname = askString("What would you like to name this CFS folder?", 0)
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
        decision = ask("Which file should be opened?", 0, dirList)
        followCFS(dirList(decision))
    else:
        print("No CFS folders in directory!")
        decision = ask("Would you like to create a CFS folder?", 0, ["Yes", "No"])
        if decision == 1:
            createCFS()
        if decision == 2:
            mainMenu()

def followCFS(folder):

mainMenu()