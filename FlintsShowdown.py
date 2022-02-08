#FLINT'S SHOWDOWN
"""
A fun little project for me to do,
this is kinda like those hunger games
simulations you can find online that
you can put all your friends into.
"""
#Project start: Jan 23, 2022
#JSON finished: February 1st, 2022
#Character building finished: February 7th, 2022

import random
import os
import time
import json

directory = os.path.dirname(__file__)
filename = os.path.join(directory, ('json/items.json'))
items = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/npcs.json'))
npc = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/events.json'))
events = json.load(open(filename, "r"))



"""
   __ __  _____  _____  __    _____  _____  _  __
  / // / /_  _/ /_  _/ / /   /_  _/ /_  _/ | |/ /
 / // /   / /  _/ /_  / /__  _/ /_   / /    / /
/____/   /_/  /____/ /____/ /____/  /_/    /_/
"""
class format:
    mode = "Colourmatic"
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    dim = "\u001b[2m"
    bold = "\u001b[1m"
    end = "\u001b[0m"
    red = "\u001b[31m"
    blue = "\u001b[36m"
    green = "\u001b[32m"

def scrollingText(message, indent, delay):
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    run = 0
    while run < len(message):
        print(message[run : run + 1], end = "")
        time.sleep(delay)
        run = run + 1
    print("")

def ask(message, indent, options, delay, lookingFor = ""):
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
        time.sleep(delay)
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

def askToContinue():
    x = input("  Press " + format.bold + "enter" + format.end + " to continue")
    print(format.clear)



"""
    _____  __ __  __   __  _____  _____  _____  ______  __   __  _____
   / ___/ / // / /  | / / / ___/ /_  _/ /_  _/ / __  / /  | / / /  __/
  / ___/ / // / / /||/ / / /__    / /  _/ /_  / /_/ / / /||/ / /__  /
 /_/    /____/ /_/ |__/ /____/   /_/  /____/ /_____/ /_/ |__/ /____/
"""
def mainMenu():
    print(format.clear)
    print("     _____  __    _____   __   __  _____  __  _____")
    print("    / ___/ / /   /_  _/  /  | / / /_  _/ /_/ /  __/")
    print("   / ___/ / /__  _/ /_  / /||/ /   / /      /__  /")
    print("  /_/    /____/ /____/ /_/ |__/   /_/      /____/")
    print("                 _____  __  __  ______  __    __  ____    ______  __    __  __   __")
    print("                /  __/ / /_/ / / __  / / /__ / / / __ |  / __  / / /__ / / /  | / /")
    print("               /__  / / __  / / /_/ / / // // / / /_/ / / /_/ / / // // / / /||/ /")
    print("              /____/ /_/ /_/ /_____/ /_______/ /_____/ /_____/ /_______/ /_/ |__/")
    print()
    scrollingText("v0.1 DEMO | Feb 14, 2022 build", 2, 0.02)
    decision = ask("", 2, ["Start new game", "Create characters", "Settings", "Exit"], 0.03)
    if decision == 1:
        startSim()
    if decision == 2:
        selectSimMode()
        createCharacters()
    if decision == 3:
        settings()
    if decision == 4:
        raise Exception("Exited game.")

def startSim():
    global creationMode
    global characterNames
    global characterPlans
    global characterAttributes
    global characterHealth
    global characterItems
    global days

    directory = os.path.dirname(__file__)
    foldername = os.path.join(directory, ('characterSaves/'))
    characterSaves = os.listdir(foldername)
    print()
    run = 0
    while run < len(characterSaves):
        if characterSaves[run].endswith(r'.json') != True:
            characterSaves.pop(run)
        run = run + 1
    if len(characterSaves) != 0:
        filenumber = ask("Load characters:", 2, characterSaves, 0.01)
        file = os.path.join(foldername, os.path.join(characterSaves[filenumber - 1]))
        data = json.load(open(file, "r"))
        creationMode = data["creationmode"]
        characterNames = []
        characterPlans = []
        characterAttributes = []
        run = 0
        while run < data["length"]:
            characterNames.append(data[str(run)]["name"])
            characterPlans.append(data[str(run)]["plan"])
            templist = []
            templist.append(data[str(run)]["melee"])
            templist.append(data[str(run)]["ranged"])
            templist.append(data[str(run)]["endurance"])
            templist.append(data[str(run)]["strength"])
            templist.append(data[str(run)]["communication"])
            characterAttributes.append(templist)
            run = run + 1
    else:
        print()
        scrollingText("Directory is empty!", 2, 0.01)
        askToContinue()
        mainMenu()
    characterHealth = []
    while len(characterHealth) <= len(characterNames):
        characterHealth.append(100)
    characterItems = []
    while len(characterItems) <= len(characterNames):
        characterItems.append([])
    days = 1
    sim()

def sim():
    printDayGUI()

def generateEvents():
    eventNum = random.randint(1, 5)
    eventList = []
    while len(eventList) < eventNum:
        cardinal = random.randint(0, len(events["rootEvents"]) - 1)
        eventList.append(events["rootEvents"][cardinal])
    return eventList

def printDayGUI():
    print(format.clear)
    time.sleep(0.25)
    scrollingText("Day " + str(days) + ".", 2, 0.01)
    time.sleep(0.25)
    runEvents(generateEvents())

def runEvents(eventList):
    run = 0
    while run < len(eventList):
        curEvent = events[eventList[run]]
        participants = []
        participantsID = []
        while len(participants) < curEvent["participants"]:
            addChar = random.randint(0, len(characterNames) - 1)
            participantsID.append(addChar)
            participants.append(characterNames[addChar])
        while curEvent != "return" and curEvent != "combat":
            if len(participants) == 1:
                scrollingText(participants[0] + " " + curEvent["openmessage"][random.randint(0, len(curEvent["openmessage"]) - 1)], 2, 0.01)
            if len(participants) == 2:
                scrollingText(participants[0] + " " + curEvent["openmessage"][random.randint(0, len(curEvent["openmessage"]) - 1)] + " " + participants[1] + ".", 2, 0.01)
            outcomeList = curEvent[npc[characterPlans[participantsID[0]]][eventList[run]]]
            curEvent = events[outcomeList[random.randint(0, len(outcomeList) - 1)]]
            askToContinue()
        run = run + 1

def generateCharacterList(number):
    charList = []
    while len(charList) < number:
        charList.append(random.choice(characterNames))
    return charList

def selectSimMode():
    global creationMode
    global characterNames
    global characterPlans
    global characterAttributes
    print(format.clear)
    time.sleep(0.5)
    scrollingText(";showdown.detailed", 2, 0.01)
    time.sleep(0.3)
    scrollingText("- Full simulation", 4, 0.01)
    scrollingText("- Choose NPC plan", 4, 0.01)
    scrollingText("- Custom attributes", 4, 0.01)
    time.sleep(0.3)
    print()
    scrollingText(";showdown.adaptable", 2, 0.01)
    time.sleep(0.3)
    scrollingText("- Full simulation", 4, 0.01)
    scrollingText("- Random NPC plan", 4, 0.01)
    scrollingText("- Custom attributes", 4, 0.01)
    time.sleep(0.3)
    print()
    scrollingText(";showdown.simple", 2, 0.01)
    time.sleep(0.3)
    scrollingText("- Partial simulation", 4, 0.01)
    scrollingText("- Random NPC plan", 4, 0.01)
    scrollingText("- All have same attributes", 4, 0.01)
    time.sleep(0.5)
    print()
    decision = ask("Select a creation mode:", 2, ["Detailed", "Adaptable", "Simple"], 0.01)
    if decision == 1:
        creationMode = "det"
    if decision == 2:
        creationMode = "ada"
    if decision == 3:
        creationMode = "sim"
    characterNames = ["Joe Generic"]
    characterPlans = ["offensive"]
    characterAttributes = [[0, 0, 0, 0, 0]]

def createCharacters(currentCharacter = 0):
    global characterNames
    global characterPlans
    global characterAttributes

    print(format.clear)
    methods = []
    if creationMode == "det":
        methods.append("Name")
        methods.append("NPC plan")
        methods.append("Attributes")
    if creationMode == "ada":
        methods.append("Name")
        methods.append("Attributes")
    if creationMode == "sim":
        methods.append("Name")
    methods.append("Switch character")
    methods.append("New character")
    methods.append("Import/export character set")
    methods.append("Exit")

    decision = 1
    while methods[decision - 1] != "Exit":
        print(format.clear)
        methods = []
        if creationMode == "det":
            methods.append("Name")
            methods.append("NPC plan")
            methods.append("Attributes")
        if creationMode == "ada":
            methods.append("Name")
            methods.append("Attributes")
        if creationMode == "sim":
            methods.append("Name")
        methods.append("Switch character")
        methods.append("New character")
        methods.append("Import/export character set")
        methods.append("Exit")
        scrollingText("CHARACTER CREATION", 2, 0.015)
        print()
        scrollingText("Name: " + characterNames[currentCharacter], 2, 0.01)
        scrollingText("Plan: " + npc[characterPlans[currentCharacter]]["name"], 2, 0.01)
        scrollingText("Current character: #" + str(currentCharacter + 1), 2, 0.01)
        print()
        print("          Melee: " + str(characterAttributes[currentCharacter][0]))
        print("         Ranged: " + str(characterAttributes[currentCharacter][1]))
        print("      Endurance: " + str(characterAttributes[currentCharacter][2]))
        print("       Strength: " + str(characterAttributes[currentCharacter][3]))
        print("  Communication: " + str(characterAttributes[currentCharacter][4]))
        print()
        decision = ask("Character editor:", 2, methods, 0.01)
        if methods[decision - 1] == "Name":
            changeCharacterName(currentCharacter)
        if methods[decision - 1] == "NPC plan":
            changeCharacterPlan(currentCharacter)
        if methods[decision - 1] == "Attributes":
            changeCharacterAttributes(currentCharacter)
        if methods[decision - 1] == "Switch character":
            currentCharacter = switchCharacter(currentCharacter, characterNames)
        if methods[decision - 1] == "New character":
            currentCharacter = newCharacter(characterNames)
        if methods[decision - 1] == "Import/export character set":
            saveLoadCharacters()
    print(format.clear)
    scrollingText("Are you sure you want to exit?", 2, 0.01)
    decision = ask("Make sure you have your sheet saved before exiting.", 2, ["Save sheet", "Back to character creation", "Exit"], 0.01)
    if decision == 1:
        directToSave()
        mainMenu()
    if decision == 2:
        createCharacters(currentCharacter)
    if decision == 3:
        mainMenu()

def changeCharacterName(curChar):
    print()
    characterNames[curChar] = askString("Choose character name:", 2)
    print(format.clear)

def changeCharacterPlan(curChar):
    global characterPlans
    print()
    npclist = []
    run = 0
    while run < len(npc["npclist"]):
        npclist.append(npc[npc["npclist"][run]]["name"])
        run = run + 1
    decision = ask("Choose character's NPC plan", 2, npclist, 0.01)
    characterPlans[curChar] = npc["npclist"][decision - 1]
    print(format.clear)

def changeCharacterAttributes(curChar):
    print(format.clear)
    print("          Melee: " + str(characterAttributes[curChar][0]))
    print("         Ranged: " + str(characterAttributes[curChar][1]))
    print("      Endurance: " + str(characterAttributes[curChar][2]))
    print("       Strength: " + str(characterAttributes[curChar][3]))
    print("  Communication: " + str(characterAttributes[curChar][4]))
    decision = ask("", 2, ["Change melee", "Change ranged", "Change endurance", "Change strength", "Change communication", "Exit"], 0.01)
    while decision != 6:
        if decision == 1:
            print()
            characterAttributes[curChar][0] = askOpen("Choose value for melee:", 2)
        if decision == 2:
            print()
            characterAttributes[curChar][1] = askOpen("Choose value for ranged:", 2)
        if decision == 3:
            print()
            characterAttributes[curChar][2] = askOpen("Choose value for endurance:", 2)
        if decision == 4:
            print()
            characterAttributes[curChar][3] = askOpen("Choose value for strength:", 2)
        if decision == 5:
            print()
            characterAttributes[curChar][4] = askOpen("Choose value for communication:", 2)
        print(format.clear)
        print("          Melee: " + str(characterAttributes[curChar][0]))
        print("         Ranged: " + str(characterAttributes[curChar][1]))
        print("      Endurance: " + str(characterAttributes[curChar][2]))
        print("       Strength: " + str(characterAttributes[curChar][3]))
        print("  Communication: " + str(characterAttributes[curChar][4]))
        decision = ask("", 2, ["Change melee", "Change ranged", "Change endurance", "Change strength", "Change communication", "Exit"], 0.01)
    print(format.clear)

def switchCharacter(curChar, currentCharacters):
    print(format.clear)
    print("  ")
    switch = ask("Current characters:", 2, currentCharacters, 0.01, curChar)
    switch = switch - 1
    print(format.clear)
    return switch

def newCharacter(currentCharacters):
    print(format.clear)
    characterNames.append("Unnamed character")
    characterPlans.append("defensive")
    characterAttributes.append([0, 0, 0, 0, 0])
    newCharacter = len(currentCharacters) - 1
    return newCharacter

def saveLoadCharacters():
    global characterNames
    global characterPlans
    global characterAttributes
    global creationMode

    print()
    decision = ask("Load or save characters?", 2, ["Load", "Save", "Back to character creation"], 0.01)
    if decision == 1:
        directory = os.path.dirname(__file__)
        foldername = os.path.join(directory, ('characterSaves/'))
        characterSaves = os.listdir(foldername)
        print()
        run = 0
        while run < len(characterSaves):
            if characterSaves[run].endswith(r'.json') != True:
                characterSaves.pop(run)
            run = run + 1
        if len(characterSaves) != 0:
            filenumber = ask("Load characters:", 2, characterSaves, 0.01)
            file = os.path.join(foldername, os.path.join(characterSaves[filenumber - 1]))
            data = json.load(open(file, "r"))
            if data["creationmode"] != creationMode:
                print()
                decision = ask("This file was created in a different mode, would you like to switch to the file's mode?", 2, ["Change mode to file", "Back to character creation"], 0.01)
                if decision == 1:
                    creationMode = data["creationmode"]
                if decision == 2:
                    createCharacters()
            characterNames = []
            characterPlans = []
            characterAttributes = []
            run = 0
            while run < data["length"]:
                characterNames.append(data[str(run)]["name"])
                characterPlans.append(data[str(run)]["plan"])
                templist = []
                templist.append(data[str(run)]["melee"])
                templist.append(data[str(run)]["ranged"])
                templist.append(data[str(run)]["endurance"])
                templist.append(data[str(run)]["strength"])
                templist.append(data[str(run)]["communication"])
                characterAttributes.append(templist)
                run = run + 1
        else:
            print()
            print("  Directory is empty!")
            askToContinue()
    if decision == 2:
        run = 0
        data = {}
        data["length"] = len(characterNames)
        data["creationmode"] = creationMode
        while run < len(characterNames):
            data[str(run)] = {}
            data[str(run)]["name"] = characterNames[run]
            data[str(run)]["plan"] = characterPlans[run]
            data[str(run)]["melee"] = characterAttributes[run][0]
            data[str(run)]["ranged"] = characterAttributes[run][1]
            data[str(run)]["endurance"] = characterAttributes[run][2]
            data[str(run)]["strength"] = characterAttributes[run][3]
            data[str(run)]["communication"] = characterAttributes[run][4]
            run = run + 1
        print()
        directory = os.path.dirname(__file__)
        foldername = os.path.join(directory, ('characterSaves/'))
        filename = askString("Name this character set:", 2)
        filename = os.path.join(foldername, filename + '.json')
        file = open(filename, "w")
        json.dump(data, file, separators = (',', ':'), indent = 4)
    print(format.clear)

def directToSave():
    run = 0
    data = {}
    data["length"] = len(characterNames)
    data["creationmode"] = creationMode
    while run < len(characterNames):
        data[str(run)] = {}
        data[str(run)]["name"] = characterNames[run]
        data[str(run)]["plan"] = characterPlans[run]
        data[str(run)]["melee"] = characterAttributes[run][0]
        data[str(run)]["ranged"] = characterAttributes[run][1]
        data[str(run)]["endurance"] = characterAttributes[run][2]
        data[str(run)]["strength"] = characterAttributes[run][3]
        data[str(run)]["communication"] = characterAttributes[run][4]
        run = run + 1
    print()
    directory = os.path.dirname(__file__)
    foldername = os.path.join(directory, ('characterSaves/'))
    filename = askString("Name this character set:", 2)
    filename = os.path.join(foldername, filename + '.json')
    file = open(filename, "w")
    json.dump(data, file, separators = (',', ':'), indent = 4)
    print(format.clear)

def settings():
    global format
    print(format.clear)
    scrollingText("SETTINGS", 2, 0.015)
    print()
    print("  Display mode: " + format.mode)
    print()
    decision = ask("Change settings:", 2, ["Change display mode"], 0.01)
    if decision == 1:
        print()
        newmode = ask("Set display mode:", 2, ["Colourmatic", "Markdown formatting", "Plain text"], 0.01)
        if newmode == 1:
            class format:
                mode = "Colourmatic"
                clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                underline = "\u001b[4m"
                italic = "\u001b[3m"
                dim = "\u001b[2m"
                bold = "\u001b[1m"
                end = "\u001b[0m"
                red = "\u001b[31m"
                blue = "\u001b[36m"
                green = "\u001b[32m"
        if newmode == 2:
            class format:
                mode = "Markdown"
                clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                underline = "\u001b[4m"
                italic = "\u001b[3m"
                dim = "\u001b[2m"
                bold = "\u001b[1m"
                end = "\u001b[0m"
                red = ""
                blue = ""
                green = ""
        if newmode == 3:
            class format:
                mode = "Plain text"
                clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                underline = ""
                italic = ""
                dim = ""
                bold = ""
                end = ""
                red = ""
                blue = ""
                green = ""
    mainMenu()



#selectSimMode()
"""
creationMode = "det"
characterNames = ["Joe Generic"]
characterPlans = ["defensive"]
characterAttributes = [[0, 0, 0, 0, 0]]
createCharacters()
"""
mainMenu()