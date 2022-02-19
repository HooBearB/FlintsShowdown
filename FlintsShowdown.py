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
#Event flow finished: February 11th, 2022
currentVersion = "v0.2.0"



import random
import os
import time
import json
import glob

class contentPacks:
    items = "Default pack"
    npc = "Default pack"
    dialogue = "Default pack"
directory = os.path.dirname(__file__)
filename = os.path.join(directory, ('json/items.json'))
items = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/npcs.json'))
npc = json.load(open(filename, "r"))
filename = os.path.join(directory, ('json/dialogue.json'))
dialogue = json.load(open(filename, "r"))



"""
   __ __  _____  _____  __    _____  _____  _  __
  / // / /_  _/ /_  _/ / /   /_  _/ /_  _/ | |/ /
 / // /   / /  _/ /_  / /__  _/ /_   / /    / /
/____/   /_/  /____/ /____/ /____/  /_/    /_/
"""
class format:
    mode = "Colourmatic"
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    strikethrough = "\u001b[29m"
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

def scrollingDialogue(character, line, indent, delay):
    run = 0
    message = character + " says " + line
    while run < indent:
        print(" ", end = "")
        run = run + 1
    run = 0
    print("\"", end = "")
    while run < len(message):
        print(message[run : run + 1], end = "")
        time.sleep(delay)
        run = run + 1
    print("\"")

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
    x = input("  Press " + format.bold + "enter" + format.end + " to continue.   ")
    print(format.clear)

def generateCharacterList(number):
    charList = []
    while len(charList) < number:
        rand = random.randint(0, len(characterNames) - 1)
        if rand not in charList:
            if characterNames[rand] not in deadCharacters:
                charList.append(rand)
    return charList

def generateEvents():
    eventNum = random.randint(1, int(len(characterNames) / 2))
    eventList = []
    while len(eventList) < eventNum:
        events = ["saw_participant", "heard_participant", "trace", "attacked", "looting", "looting", "looting"]
        eventList.append(random.choice(events))
    return eventList

def fetchDialogue(target, prompt):
    templist = dialogue[target][prompt]
    dialoguechoice = random.choice(templist)
    return dialoguechoice



"""
    _____  __ __  __   __  _____  _____  _____  ______  __   __  _____
   / ___/ / // / /  | / / / ___/ /_  _/ /_  _/ / __  / /  | / / /  __/
  / ___/ / // / / /||/ / / /__    / /  _/ /_  / /_/ / / /||/ / /__  /
 /_/    /____/ /_/ |__/ /____/   /_/  /____/ /_____/ /_/ |__/ /____/
"""
def mainMenu():
    print(format.clear)
    print(format.green + format.bold)
    print("     _____  __    _____   __   __  _____  __  _____" + format.end + format.red + format.bold + "         _________________________" + format.end + format.bold + format.green)
    print("    / ___/ / /   /_  _/  /  | / / /_  _/ /_/ /  __/" + format.end + format.red + format.bold + "  ______/   ▅▅▅  _________________|" + format.end + format.bold + format.green)
    print("   / ___/ / /__  _/ /_  / /||/ /   / /      /__  /" + format.end + format.red + format.bold + "  |     _________|_╷_╷_╷_╷_╷_/" + format.end + format.bold + format.green)
    print("  /_/    /____/ /____/ /_/ |__/   /_/      /____/" + format.end + format.red + format.bold + "   |____/(_/" + format.end + format.bold + format.red)
    print("           _    " + format.end + format.bold + format.blue + "    _____  __  __  ______  __    __  ____    ______  __    __  __   __" + format.end + format.bold + format.red)
    print("  ________| |__ " + format.end + format.bold + format.blue + "   /  __/ / /_/ / / __  / / /__ / / / __ |  / __  / / /__ / / /  | / /" + format.end + format.bold + format.red)
    print("  \_╷_╷_╷_|  __|" + format.end + format.bold + format.blue + "  /__  / / __  / / /_/ / / // // / / /_/ / / /_/ / / // // / / /||/ /" + format.end + format.bold + format.red)
    print("          ╵-╵   " + format.end + format.bold + format.blue + " /____/ /_/ /_/ /_____/ /_______/ /_____/ /_____/ /_______/ /_/ |__/" + format.end + format.italic + format.dim)
    print()
    scrollingText(fetchDialogue("program", "menu") + format.end, 2, 0.01)
    scrollingText(format.bold + format.italic + "v0.2.0 DEMO / Feb 20, 2022 build" + format.end, 2, 0.02)
    decision = ask("", 2, ["Start new game", "Create characters", "Open content pack", "Settings", "Exit"], 0.03)
    if decision == 1:
        startSim()
    if decision == 2:
        selectSimMode()
        createCharacters()
    if decision == 3:
        openPack()
    if decision == 4:
        settings()
    if decision == 6:
        raise Exception("Exited game.")

def startSim():
    global creationMode
    global characterNames
    global characterPlans
    global characterAttributes
    global characterHealth
    global characterItems
    global characterItemDurabilities
    global days
    global deadCharacters
    global characterKills
    global log

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
        characterSaves.append("Exit")
        filenumber = ask("Load characters:", 2, characterSaves, 0.01)
        if characterSaves[filenumber - 1] != "Exit":
            file = os.path.join(foldername, os.path.join(characterSaves[filenumber - 1]))
            data = json.load(open(file, "r"))
            attempt = False
            try:
                npcFile = data["npcPack"]
                dialogueFile = data["dialoguePack"]
                attempt = True
            except:
                print()
                scrollingText("This file was made before v0.2.0. You can manually update this file", 2, 0.01)
                scrollingText("to match a current file, or make a new file in the program.", 2, 0.01)
                print()
                askToContinue()
                mainMenu()
            if attempt:
                if npcFile == contentPacks.npc and dialogueFile == contentPacks.dialogue:
                    attempt = False
                    try: 
                        fileVersion = data["version"]
                        attempt = True
                    except:
                        print()
                        scrollingText("This file was made before v0.2.0. You can manually update this file", 2, 0.01)
                        scrollingText("to match a current file, or make a new file in the program.", 2, 0.01)
                        print()
                        askToContinue()
                        mainMenu()
                    if attempt:
                        if fileVersion == currentVersion:
                            creationMode = data["creationmode"]
                            characterNames = []
                            characterPlans = []
                            characterAttributes = []
                            characterDialogue = []
                            run = 0
                            while run < data["length"]:
                                characterNames.append(data[str(run)]["name"])
                                characterPlans.append(data[str(run)]["plan"])
                                characterDialogue.append(data[str(run)]["dialogue"])
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
                            scrollingText("This file was created with a previous version of FliSh. You can ", 2, 0.01)
                            scrollingText("can manually update this file to match a current file, or make a new file in the program.", 2, 0.01)
                            print()
                            askToContinue()
                            mainMenu()
                else:
                    scrollingText("Sorry, this character file was made with a different set of content packs.", 2, 0.01)
                    if data["npcPack"] != contentPacks.npc:
                        scrollingText("This file takes an npc content pack with the ID of " + data["npcPack"] + " while you have " + contentPacks.npc + " currently enabled.")
                    if data["dialoguePack"] != contentPacks.dialogue:
                        scrollingText("This file takes a dialogue content pack with the ID of " + data["dialoguePack"] + " while you have " + contentPacks.dialogue + " currently enabled.")
        else:
            mainMenu()
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
    characterItemDurabilities = []
    while len(characterItemDurabilities) <= len(characterNames):
        characterItemDurabilities.append([])
    characterKills = []
    while len(characterKills) <= len(characterNames):
        characterKills.append(0)
    days = 1
    deadCharacters = []
    log = []
    sim()

def sim():
    global days
    while len(deadCharacters) < len(characterNames) - 1:
        printDayGUI()
        healAll()
        days = days + 1
    printWinner()

def printDayGUI():
    print(format.clear)
    time.sleep(0.5)
    scrollingText(format.bold + format.blue + format.italic + "Day " + str(days) + "." + format.end, 2, 0.01)
    time.sleep(0.5)
    print()
    runEvents(generateEvents())
    time.sleep(0.5)
    print()
    scrollingText(format.bold + format.blue + format.italic + "Night falls." + format.end, 2, 0.01)
    print()
    nightfall()

def runEvents(eventList):
    run = 0
    while run < len(eventList):
        if eventList[run] == "saw_participant":
            sawParticipant()
        if eventList[run] == "heard_participant":
            heardParticipant()
        if eventList[run] == "trace":
            trace()
        if eventList[run] == "attacked":
            attacked()
        if eventList[run] == "looting":
            looting()
        askToContinue()
        run = run + 1

def sawParticipant():
    characters = generateCharacterList(2)
    scrollingText(characterNames[characters[0]] + " sees " + characterNames[characters[1]] + ".", 2, 0.01)
    log.append(str(days) + ". " + characterNames[characters[0]] + " saw " + characterNames[characters[1]] + ".")
    time.sleep(0.5)
    if npc[characterPlans[characters[0]]]["saw_participant"] == "loud":
        attack(characters)
    if npc[characterPlans[characters[0]]]["saw_participant"] == "stealth":
        rand = random.randint(1, 6)
        if rand == 6:
            attacked(characters)
        else:
            scrollingText(characterNames[characters[0]] + " hides.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["saw_participant"] == "flee":
        rand = random.randint(1, 8)
        if rand == 4:
            attacked(characters)
        else:
            scrollingText(characterNames[characters[0]] + " runs away.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["saw_participant"] == "communicate":
        scrollingText(characterNames[characters[0]] + " attempts to negotiate with " + characterNames[characters[1]] + ".", 2, 0.01)
        rand = random.randint(1, 4)
        if rand == 4:
            scrollingText(characterNames[characters[1]] + " didn't like that.", 2, 0.01)
            attacked(characters)
        else:
            scrollingText(characterNames[characters[0]] + " successfully negotiates with " + characterNames[characters[1]] + ".", 2, 0.01)

def heardParticipant():
    characters = generateCharacterList(2)
    scrollingText(characterNames[characters[0]] + " hears something.", 2, 0.01)
    log.append(str(days) + ". " + characterNames[characters[0]] + " heard something.")
    randCheck = random.randint(1, 7)
    if randCheck == 1:
        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "heard"), 2, 0.01)
    time.sleep(0.5)
    if npc[characterPlans[characters[0]]]["heard_participant"] == "loud":
        rand = random.randint(1, 4)
        if rand == 4:
            scrollingText(characterNames[characters[0]] + " finds " + characterNames[characters[1]] + ".", 2, 0.01)
            attack(characters)
        else:
            scrollingText(characterNames[characters[0]] + " searches the area, but doesn't find anyone.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["heard_participant"] == "stealth":
        rand = random.randint(1, 6)
        if rand == 6:
            scrollingText(characterNames[characters[1]] + " finds " + characterNames[characters[0]] + ".", 2, 0.01)
            attacked(characters)
        else:
            scrollingText(characterNames[characters[0]] + " hides.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["heard_participant"] == "seek":
        rand = random.randint(1, 2)
        if rand == 2:
            scrollingText(characterNames[characters[0]] + " finds " + characterNames[characters[1]] + ".", 2, 0.01)
            attack(characters)
        else:
            scrollingText(characterNames[characters[0]] + " fails to find anyone.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["heard_participant"] == "flee":
        scrollingText(characterNames[characters[0]] + " runs away.", 2, 0.01)

def trace():
    characters = generateCharacterList(2)
    scrollingText(characterNames[characters[0]] + " notices footprints in the mud.", 2, 0.01)
    log.append(str(days) + ". " + characterNames[characters[0]] + " noticed a trace of someone.")
    randCheck = random.randint(1, 5)
    if randCheck == 1:
        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "trace"), 2, 0.01)
    time.sleep(0.5)
    if npc[characterPlans[characters[0]]]["trace"] == "loud":
        rand = random.randint(1, 10)
        if rand == 10:
            scrollingText(characterNames[characters[0]] + " finds " + characterNames[characters[1]] + ".", 2, 0.01)
            attack(characters)
        else:
            scrollingText(characterNames[characters[0]] + " fails to find anyone.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["trace"] == "stealth":
        rand = random.randint(1, 16)
        if rand == 16:
            scrollingText(characterNames[characters[1]] + " finds " + characterNames[characters[0]] + ".", 2, 0.01)
            attacked(characters)
        else:
            scrollingText(characterNames[characters[0]] + " hides.", 2, 0.01)
        
def attacked(characters = []):
    global deadCharacters
    if characters == []:
        characters = generateCharacterList(2)
    if len(characters) == 1:
        characters.append(generateCharacterList(1))
    ran = False
    scrollingText(format.bold + characterNames[characters[1]] + " engages " + characterNames[characters[0]] + "." + format.end, 2, 0.01)
    randCheck = random.randint(1, 4)
    if randCheck == 1:
        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "attacked"), 2, 0.01)
    if len(characterItems[characters[1]]) > 0:
        scrollingText(characterNames[characters[1]] + " has a " + items[characterItems[characters[1]][0]]["name"].lower() + ".", 2, 0.01)
    else:
        scrollingText(characterNames[characters[1]] + " has is using their fists.", 2, 0.01)
    if len(characterItems[characters[0]]) > 0:
        scrollingText(characterNames[characters[0]] + " has a " + items[characterItems[characters[0]][0]]["name"].lower() + ".", 2, 0.01)
    else:
        scrollingText(characterNames[characters[0]] + " has is using their fists.", 2, 0.01)
    log.append(str(days) + ". " + characterNames[characters[0]] + " got attacked by " + characterNames[characters[1]] + ".")
    print()
    decision = ask("Would you like to view this combat turn by turn?", 2, ["Turn by turn", "Skip to result"], 0.01)
    print()
    if npc[characterPlans[characters[0]]]["attacked"] == "flee":
        rand = random.randint(1, 6)
        if decision == 1:
            scrollingText(characterNames[characters[0]] + " attempts to run away.", 2, 0.01)
        if rand == 6:
            scrollingText(characterNames[characters[0]] + " runs away.", 2, 0.01)
            log.append(str(days) + ". " + characterNames[characters[0]] + " ran away.")
            ran = True
        else:
            if decision == 1:
                scrollingText(characterNames[characters[0]] + " fails to run away.", 2, 0.01)
    charA = 1
    charB = 0
    if ran != True:
        ran = False
        while characterHealth[characters[0]] > 0 and characterHealth[characters[1]] > 0:
            if characterItems[characters[charA]] == []:
                rand = random.randint(1, 3)
                if rand != 3:
                    if decision == 1:
                        scrollingText(characterNames[characters[charA]] + " punches " + characterNames[characters[charB]] + ".", 2, 0.01)
                    rand = random.randint(3, 5)
                    characterHealth[characters[charB]] = characterHealth[characters[charB]] - rand
                else:
                    if decision == 1:
                        scrollingText(characterNames[characters[charA]] + " misses their shot.", 2, 0.01)
                randCheck = random.randint(1, 8)
                if randCheck == 1:
                    scrollingDialogue(characters[charA], fetchDialogue(characterDialogue[characters[charA]], "combat"), 2, 0.01)
            else:
                if decision == 1:
                    scrollingText(characterNames[characters[charA]] + items[characterItems[characters[charA]][0]]["ready"], 2, 0.01)
                rand = random.randint(1,100)
                if decision == 1:
                    scrollingText(characterNames[characters[charA]] + items[characterItems[characters[charA]][0]]["attack"] + characterNames[characters[charB]] + ".", 2, 0.01)
                if rand <= items[characterItems[characters[charA]][0]]["accuracy"]:
                    if decision == 1:
                        scrollingText("The shot connects.", 2, 0.01)
                    characterHealth[characters[charB]] = characterHealth[characters[charB]] - items[characterItems[characters[charA]][0]]["damage"]
                    characterItemDurabilities[characters[charA]][0] = characterItemDurabilities[characters[charA]][0] - 1
                else:
                    if decision == 1:
                        scrollingText("The shot misses.", 2, 0.01)
                    if items[characterItems[characters[charA]][0]]["faildamage"] == True:
                        characterItemDurabilities[characters[charA]][0] = characterItemDurabilities[characters[charA]][0] - 1
                randCheck = random.randint(1, 8)
                if randCheck == 1:
                    scrollingDialogue(characters[charA], fetchDialogue(characterDialogue[characters[charA]], "combat"), 2, 0.01)
            if decision == 1:
                time.sleep(0.25)
            if decision == 1:
                time.sleep(0.5)
            if charA == 1:
                charA = 0
                charB = 1
            else:
                charA = 1
                charB = 0
            if ran == True or characterHealth[characters[charA]] <= 0 or characterHealth[characters[charB]] <= 0:
                if characterHealth[characters[charA]] <= 0:
                    scrollingText(characterNames[characters[charA]] + " succumbs to their wounds, and dies.", 2, 0.01)
                    if characterItems[characters[charB]] != []:
                        log.append(str(days) + ". " + characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with a " + items[characterItems[characters[charB]][0]]["name"].lower() +  ".")
                    else:
                        log.append(str(days) + ". " + characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with their" + format.italic + " fists." + format.end)
                    characterKills[characters[charB]] = characterKills[characters[charB]] + 1
                    print()
                    deadCharacters.append(characterNames[characters[charA]])
                if characterHealth[characters[charB]] <= 0:
                    scrollingText(characterNames[characters[charB]] + " succumbs to their wounds, and dies.", 2, 0.01)
                    if characterItems[characters[charA]] != []:
                        log.append(str(days) + ". " + characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with a " + items[characterItems[characters[charA]][0]]["name"].lower() +  ".")
                    else:
                        log.append(str(days) + ". " + characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with their" + format.italic + " fists." + format.end)
                    characterKills[characters[charA]] = characterKills[characters[charA]] + 1
                    print()
                    deadCharacters.append(characterNames[characters[charB]])
                break
            rand = random.randint(1, 6)
            if rand == 1:
                rand = random.randint(1, 8)
                if decision == 1:
                    scrollingText(characterNames[characters[charB]] + " attempts to run away.", 2, 0.01)
                if rand == 6:
                    scrollingText(characterNames[characters[charB]] + " runs away.", 2, 0.01)
                    log.append(str(days) + ". " + characterNames[characters[charB]] + " ran away.")
                    randCheck = random.randint(1, 5)
                    if randCheck == 1:
                        scrollingDialogue(characters[charA], fetchDialogue(characterDialogue[characters[charA]], "chasing"), 2, 0.01)
                    ran = True
                else:
                    if decision == 1:
                        scrollingText(characterNames[characters[charB]] + " fails to run away.", 2, 0.01)

def attack(characters = []):
    global deadCharacters
    if characters == []:
        characters = generateCharacterList(2)
    if len(characters) == 1:
        characters.append(generateCharacterList(1))
    ran = False
    scrollingText(format.bold + characterNames[characters[0]] + " attacks " + characterNames[characters[1]] + "." + format.end, 2, 0.01)
    randCheck = random.randint(1, 4)
    if randCheck == 1:
        scrollingDialogue(characters[1], fetchDialogue(characterDialogue[characters[1]], "attacked"), 2, 0.01)
    if len(characterItems[characters[0]]) > 0:
        scrollingText(characterNames[characters[0]] + " has a " + items[characterItems[characters[0]][0]]["name"].lower() + ".", 2, 0.01)
    else:
        scrollingText(characterNames[characters[0]] + " has is using their fists.", 2, 0.01)
    if len(characterItems[characters[1]]) > 0:
        scrollingText(characterNames[characters[1]] + " has a " + items[characterItems[characters[1]][0]]["name"].lower() + ".", 2, 0.01)
    else:
        scrollingText(characterNames[characters[1]] + " has is using their fists.", 2, 0.01)
    log.append(str(days) + ". " + characterNames[characters[0]] + " attacked " + characterNames[characters[1]] + ".")
    print()
    decision = ask("Would you like to view this combat turn by turn?", 2, ["Turn by turn", "Skip to result"], 0.01)
    print()
    if npc[characterPlans[characters[1]]]["attacked"] == "flee":
        rand = random.randint(1, 6)
        if decision == 1:
            scrollingText(characterNames[characters[1]] + " attempts to run away.", 2, 0.01)
        if rand == 6:
            scrollingText(characterNames[characters[1]] + " runs away.", 2, 0.01)
            log.append(str(days) + ". " + characterNames[characters[1]] + " ran away.")
            ran = True
        else:
            if decision == 1:
                scrollingText(characterNames[characters[1]] + " fails to run away.", 2, 0.01)
    charA = 0
    charB = 1
    if ran != True:
        ran = False
        while characterHealth[characters[0]] > 0 and characterHealth[characters[1]] > 0:
            if characterItems[characters[charA]] == []:
                rand = random.randint(1, 3)
                if rand != 3:
                    if decision == 1:
                        scrollingText(characterNames[characters[charA]] + " punches " + characterNames[characters[charB]] + ".", 2, 0.01)
                    rand = random.randint(3, 5)
                    characterHealth[characters[charB]] = characterHealth[characters[charB]] - rand
                else:
                    if decision == 1:
                        scrollingText(characterNames[characters[charA]] + " misses their shot.", 2, 0.01)
                randCheck = random.randint(1, 8)
                if randCheck == 1:
                    scrollingDialogue(characters[charA], fetchDialogue(characterDialogue[characters[charA]], "combat"), 2, 0.01)
            else:
                if decision == 1:
                    scrollingText(characterNames[characters[charA]] + items[characterItems[characters[charA]][0]]["ready"], 2, 0.01)
                rand = random.randint(1,100)
                if decision == 1:
                    scrollingText(characterNames[characters[charA]] + items[characterItems[characters[charA]][0]]["attack"] + characterNames[characters[charB]] + ".", 2, 0.01)
                if rand <= items[characterItems[characters[charA]][0]]["accuracy"]:
                    if decision == 1:
                        scrollingText("The shot connects.", 2, 0.01)
                    characterHealth[characters[charB]] = characterHealth[characters[charB]] - items[characterItems[characters[charA]][0]]["damage"]
                    characterItemDurabilities[characters[charA]][0] = characterItemDurabilities[characters[charA]][0] - 1
                else:
                    if decision == 1:
                        scrollingText("The shot misses.", 2, 0.01)
                    if items[characterItems[characters[charA]][0]]["faildamage"] == True:
                        characterItemDurabilities[characters[charA]][0] = characterItemDurabilities[characters[charA]][0] - 1
                randCheck = random.randint(1, 8)
                if randCheck == 1:
                    scrollingDialogue(characters[charA], fetchDialogue(characterDialogue[characters[charA]], "combat"), 2, 0.01)
            if decision == 1:
                time.sleep(0.25)
            if decision == 1:
                time.sleep(0.5)
            if charA == 1:
                charA = 0
                charB = 1
            else:
                charA = 1
                charB = 0
            if ran == True or characterHealth[characters[charA]] <= 0 or characterHealth[characters[charB]] <= 0:
                if characterHealth[characters[charA]] <= 0:
                    scrollingText(characterNames[characters[charA]] + " succumbs to their wounds, and dies.", 2, 0.01)
                    if characterItems[characters[charB]] != []:
                        log.append(str(days) + ". " + characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with a " + items[characterItems[characters[charB]][0]]["name"].lower() +  ".")
                    else:
                        log.append(str(days) + ". " + characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with their" + format.italic + " fists." + format.end)
                    characterKills[characters[charB]] = characterKills[characters[charB]] + 1
                    print()
                    deadCharacters.append(characterNames[characters[charA]])
                if characterHealth[characters[charB]] <= 0:
                    scrollingText(characterNames[characters[charB]] + " succumbs to their wounds, and dies.", 2, 0.01)
                    if characterItems[characters[charA]] != []:
                        log.append(str(days) + ". " + characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with a " + items[characterItems[characters[charA]][0]]["name"].lower() +  ".")
                    else:
                        log.append(str(days) + ". " + characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with their" + format.italic + " fists." + format.end)
                    characterKills[characters[charA]] = characterKills[characters[charA]] + 1
                    print()
                    deadCharacters.append(characterNames[characters[charB]])
                break
            rand = random.randint(1, 6)
            if rand == 1:
                rand = random.randint(1, 8)
                if decision == 1:
                    scrollingText(characterNames[characters[charB]] + " attempts to run away.", 2, 0.01)
                if rand == 6:
                    scrollingText(characterNames[characters[charB]] + " runs away.", 2, 0.01)
                    log.append(str(days) + ". " + characterNames[characters[charB]] + " ran away.")
                    randCheck = random.randint(1, 5)
                    if randCheck == 1:
                        scrollingDialogue(characters[charA], fetchDialogue(characterDialogue[characters[charA]], "chasing"), 2, 0.01)
                    ran = True
                else:
                    if decision == 1:
                        scrollingText(characterNames[characters[charB]] + " fails to run away.", 2, 0.01)

def looting():
    characters = generateCharacterList(2)
    scrollingText(characterNames[characters[0]] + " notices a cache near their location.", 2, 0.01)
    if npc[characterPlans[characters[0]]]["looting"] == "loud":
        rand = random.randint(1, 6)
        if rand == 1:
            attacked(characters)
        else:
            lootItem = random.choice(items["lootable"])
            if len(characterItems[characters[0]]) == 0:
                characterItems[characters[0]].append(lootItem)
                characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
                scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".", 2, 0.01)
                log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                randCheck = random.randint(1, 4)
                if randCheck == 1:
                    if items[lootItem]["type"] == "Melee":
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                    if items[lootItem]["type"] == "Ranged":
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
            else:
                if len(characterItems[characters[0]]) > 3:
                    if items[lootItem]["grade"] >= items[characterItems[characters[0]][0]]["grade"]:
                        scrollingText(characterNames[characters[0]] + " drops their " + items[characterItems[characters[0]][0]]["name"].lower() + " to pick up the cache's " + items[lootItem]["name"].lower() + ".", 2, 0.01)
                        log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                        characterItems[characters[0]][0] = lootItem
                        characterItemDurabilities[characters[0]][0] = items[lootItem]["durability"]
                        randCheck = random.randint(1, 4)
                        if randCheck == 1:
                            if items[lootItem]["type"] == "Melee":
                                scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                            if items[lootItem]["type"] == "Ranged":
                                scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
                    else:
                        scrollingText(characterNames[characters[0]] + "'s " + items[characterItems[characters[0]][0]]["name"].lower() + " is better than the " + items[lootItem]["name"].lower() + ".", 2, 0.01)
                        randCheck = random.randint(1, 4)
                        if randCheck == 1:
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "havebetter"), 2, 0.01)
                else:
                    characterItems[characters[0]].append(lootItem)
                    characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
                    scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".", 2, 0.01)
                    log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                    randCheck = random.randint(1, 4)
                    if randCheck == 1:
                        if items[lootItem]["type"] == "Melee":
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                        if items[lootItem]["type"] == "Ranged":
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
    if npc[characterPlans[characters[0]]]["looting"] == "stealth":
        lootItem = random.choice(items["lootable"])
        if len(characterItems[characters[0]]) == 0:
            characterItems[characters[0]].append(lootItem)
            characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
            scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".", 2, 0.01)
            log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
            randCheck = random.randint(1, 4)
            if randCheck == 1:
                if items[lootItem]["type"] == "Melee":
                    scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                if items[lootItem]["type"] == "Ranged":
                    scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
        else:
            if len(characterItems[characters[0]]) > 3:
                if items[lootItem]["grade"] >= items[characterItems[characters[0]][0]]["grade"]:
                    scrollingText(characterNames[characters[0]] + " drops their " + items[characterItems[characters[0]][0]]["name"].lower() + " to pick up the cache's " + items[lootItem]["name"].lower() + ".", 2, 0.01)
                    log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                    characterItems[characters[0]][0] = lootItem
                    characterItemDurabilities[characters[0]][0] = items[lootItem]["durability"]
                    randCheck = random.randint(1, 4)
                    if randCheck == 1:
                        if items[lootItem]["type"] == "Melee":
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                        if items[lootItem]["type"] == "Ranged":
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
                else:
                    scrollingText(characterNames[characters[0]] + "'s " + items[characterItems[characters[0]][0]]["name"].lower() + " is better than the " + items[lootItem]["name"].lower() + ".", 2, 0.01)
                    randCheck = random.randint(1, 4)
                    if randCheck == 1:
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "havebetter"), 2, 0.01)
            else:
                characterItems[characters[0]].append(lootItem)
                characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
                scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".", 2, 0.01)
                log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                randCheck = random.randint(1, 4)
                if randCheck == 1:
                    if items[lootItem]["type"] == "Melee":
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                    if items[lootItem]["type"] == "Ranged":
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
    if npc[characterPlans[characters[0]]]["looting"] == "seek":
        rand = random.randint(1, 8)
        if rand == 1:
            attack(characters)
        else:
            lootItem = random.choice(items["lootable"])
            if len(characterItems[characters[0]]) == 0:
                characterItems[characters[0]].append(lootItem)
                characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
                scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".", 2, 0.01)
                log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                randCheck = random.randint(1, 4)
                if randCheck == 1:
                    if items[lootItem]["type"] == "Melee":
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                    if items[lootItem]["type"] == "Ranged":
                        scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
            else:
                if len(characterItems[characters[0]]) > 3:
                    if items[lootItem]["grade"] >= items[characterItems[characters[0]][0]]["grade"]:
                        scrollingText(characterNames[characters[0]] + " drops their " + items[characterItems[characters[0]][0]]["name"].lower() + " to pick up the cache's " + items[lootItem]["name"].lower() + ".", 2, 0.01)
                        log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                        characterItems[characters[0]][0] = lootItem
                        characterItemDurabilities[characters[0]][0] = items[lootItem]["durability"]
                        randCheck = random.randint(1, 4)
                        if randCheck == 1:
                            if items[lootItem]["type"] == "Melee":
                                scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                            if items[lootItem]["type"] == "Ranged":
                                scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)
                    else:
                        scrollingText(characterNames[characters[0]] + "'s " + items[characterItems[characters[0]][0]]["name"].lower() + " is better than the " + items[lootItem]["name"].lower() + ".", 2, 0.01)
                        randCheck = random.randint(1, 4)
                        if randCheck == 1:
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "havebetter"), 2, 0.01)
                else:
                    characterItems[characters[0]].append(lootItem)
                    characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
                    scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".", 2, 0.01)
                    log.append(str(days) + ". " + characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".")
                    randCheck = random.randint(1, 4)
                    if randCheck == 1:
                        if items[lootItem]["type"] == "Melee":
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "meleegot"), 2, 0.01)
                        if items[lootItem]["type"] == "Ranged":
                            scrollingDialogue(characters[0], fetchDialogue(characterDialogue[characters[0]], "rangedgot"), 2, 0.01)

def nightfall():
    decision = ask("Nightfall actions:", 2, ["View characters", "View log", "Continue to day"], 0.05)
    if decision == 1:
        viewCharacters()
    if decision == 2:
        viewLog()

def viewCharacters():
    decision = 1
    options = []
    run = 0
    while len(options) < len(characterNames):
        if characterHealth[run] > 0:
            if len(characterItems[run]) > 0:
                options.append(characterNames[run] + " [" + format.red + str(characterHealth[run]) + format.end + "] (" + format.green + items[characterItems[run][0]]["name"] + format.end + ") {" + format.blue + str(characterKills[run]) + format.end + "}")
            else:
                options.append(characterNames[run] + " [" + format.red + str(characterHealth[run]) + format.end + "] (" + format.green + "Fists" + format.end + ") {" + format.blue + str(characterKills[run]) + format.end + "}")
        else:
            options.append(format.red + format.strikethrough + characterNames[run] + format.end + " {" + format.blue + str(characterKills[run]) + format.end + "}")
        run = run + 1
    options.append("Exit")
    while options[decision - 1] != "Exit":
        print()
        decision = ask("View character:", 2, options, 0.05)
        view = decision - 1
        print()
        if options[decision - 1] != "Exit":
            scrollingText(format.bold + characterNames[view] + format.end, 2, 0.01)
            scrollingText("Health: " + str(characterHealth[view]), 2, 0.01)
            scrollingText(" Kills: " + str(characterKills[view]), 2, 0.01)
            print()
            scrollingText("Inventory:", 2, 0.01)
            run = 0
            while run < len(characterItems[view]):
                currItem = items[characterItems[view][run]]
                scrollingText(currItem["name"], 2, 0.01)
                linerun = 1
                while linerun <= 5:
                    if currItem[str(linerun)] != "":
                        print("  ", end = "")
                        print(currItem[str(linerun)])
                    linerun = linerun + 1
                print()
                run = run + 1
            if len(characterItems[view]) == 0:
                scrollingText(format.bold + format.italic + "Inventory is empty!" + format.end, 2, 0.01)
    nightfall()

def viewLog():
    run = 0
    print()
    while run < len(log):
        scrollingText(log[run], 2, 0.01)
        run = run + 1
    askToContinue()
    nightfall()

def healAll():
    run = 0
    while run < len(characterHealth):
        if characterHealth[run] > 0:
            if characterHealth[run] + 20 <= 100:
                characterHealth[run] = characterHealth[run] + 20
            else:
                characterHealth[run] = characterHealth[run] + (100 - characterHealth[run])
        run = run + 1

def printWinner():
    run = 0
    while characterNames[run] in deadCharacters:
        run = run + 1
    print(format.clear)
    scrollingText(format.green + characterNames[run] + format.end + " is the last one alive.", 2, 0.01)
    scrollingText("They win.", 2, 0.01)
    print()
    scrollingText("           Kills: " + str(characterKills[run]), 2, 0.01)
    scrollingText("Last used weapon: " + characterItems[run][0], 2, 0.01)
    askToContinue()
    mainMenu()

def selectSimMode():
    global creationMode
    global characterNames
    global characterPlans
    global characterAttributes
    global characterDialogue

    print(format.clear)
    time.sleep(0.5)
    scrollingText(";showdown.detailed", 2, 0.01)
    time.sleep(0.05)
    scrollingText("- Full simulation", 4, 0.01)
    scrollingText("- Choose NPC plan", 4, 0.01)
    scrollingText("- Custom attributes", 4, 0.01)
    time.sleep(0.05)
    print()
    scrollingText(";showdown.adaptable", 2, 0.01)
    time.sleep(0.05)
    scrollingText("- Full simulation", 4, 0.01)
    scrollingText("- Random NPC plan", 4, 0.01)
    scrollingText("- Custom attributes", 4, 0.01)
    time.sleep(0.05)
    print()
    scrollingText(";showdown.simple", 2, 0.01)
    time.sleep(0.05)
    scrollingText("- Partial simulation", 4, 0.01)
    scrollingText("- Random NPC plan", 4, 0.01)
    scrollingText("- All have same attributes", 4, 0.01)
    time.sleep(0.1)
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
    characterDialogue = ["cynic"]

def createCharacters(currentCharacter = 0):
    global characterNames
    global characterPlans
    global characterAttributes
    global characterDialogue

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
    methods.append("Delete character")
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
            methods.append("Dialogue")
        if creationMode == "ada":
            methods.append("Name")
            methods.append("Attributes")
            methods.append("Dialogue")
        if creationMode == "sim":
            methods.append("Name")
        methods.append("Switch character")
        methods.append("New character")
        methods.append("Delete character")
        methods.append("Import/export character set")
        methods.append("Exit")
        scrollingText("CHARACTER CREATION", 2, 0.015)
        print()
        scrollingText("Name: " + characterNames[currentCharacter], 2, 0.01)
        scrollingText("Plan: " + npc[characterPlans[currentCharacter]]["name"], 2, 0.01)
        scrollingText("Dialogue: " + dialogue[characterDialogue[currentCharacter]]["name"], 2, 0.01)
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
        if methods[decision - 1] == "Dialogue":
            changeCharacterDialogue(currentCharacter)
        if methods[decision - 1] == "Switch character":
            currentCharacter = switchCharacter(currentCharacter, characterNames)
        if methods[decision - 1] == "New character":
            currentCharacter = newCharacter(characterNames)
        if methods[decision - 1] == "Delete character":
            currentCharacter = deleteCharacter(currentCharacter)
        if methods[decision - 1] == "Import/export character set":
            saveLoadCharacters()
    print(format.clear)
    scrollingText("Are you sure you want to exit?", 2, 0.01)
    decision = ask("Make sure you have your sheet saved before exiting.", 2, ["Save sheet", "Back to character creation", "Exit without saving"], 0.01)
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
    decision = ask("Choose character's NPC plan:", 2, npclist, 0.01)
    print(format.clear)
    print(npc[npc["npclist"][decision - 1]]["triangle1"])
    print(npc[npc["npclist"][decision - 1]]["triangle2"])
    print(npc[npc["npclist"][decision - 1]]["triangle3"])
    print(npc[npc["npclist"][decision - 1]]["triangle4"])
    print(npc[npc["npclist"][decision - 1]]["triangle5"])
    print()
    scrollingText(npc[npc["npclist"][decision - 1]]["description"], 2, 0.01)
    flow = ask("", 2, ["Set this as character plan", "Return to plan selection"], 0.05)
    if flow == 1:
        characterPlans[curChar] = npc["npclist"][decision - 1]
    else:
        print(format.clear)
        changeCharacterPlan(curChar)
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

def changeCharacterDialogue(curChar):
    global characterDialogue
    list = []
    run = 0
    while run < len(dialogue["list"]):
        list.append(dialogue[dialogue["list"][run]]["name"])
        run = run + 1
    print()
    decision = ask("Choose character's dialogue set:", 2, list, 0.05)
    characterDialogue[curChar] = dialogue["list"][decision - 1]
    createCharacters(curChar)

def switchCharacter(curChar, currentCharacters):
    print(format.clear)
    print("  ")
    switch = ask("Current characters:", 2, currentCharacters, 0.01, lookingFor = curChar)
    switch = switch - 1
    print(format.clear)
    return switch

def newCharacter(currentCharacters):
    print(format.clear)
    characterNames.append("Unnamed character")
    characterPlans.append("defensive")
    characterAttributes.append([0, 0, 0, 0, 0])
    characterDialogue.append("cynic")
    newCharacter = len(currentCharacters) - 1
    return newCharacter

def deleteCharacter(currChar):
    global characterNames
    global characterPlans
    global characterAttributes

    print()
    decision = ask("Would you really like to delete this character?", 2, ["Yes", "No"], 0.05)
    if decision == 1:
        characterNames.pop(currChar)
        characterPlans.pop(currChar)
        characterAttributes.pop(currChar)
        currChar = currChar - 1
    return currChar

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
            characterSaves.append("Exit")
            filenumber = ask("Load characters:", 2, characterSaves, 0.01)
            if characterSaves[filenumber - 1] != "Exit":
                file = os.path.join(foldername, os.path.join(characterSaves[filenumber - 1]))
                data = json.load(open(file, "r"))
                attempt = False
                try:
                    npcFile = data["npcPack"]
                    dialogueFile = data["dialoguePack"]
                    attempt = True
                except:
                    print()
                    scrollingText("This file was made before v0.2.0. You can manually update this file", 2, 0.01)
                    scrollingText("to match a current file, or make a new file in the program.", 2, 0.01)
                    print()
                    askToContinue()
                    mainMenu()
                if attempt:
                    if npcFile == contentPacks.npc and dialogueFile == contentPacks.dialogue:
                        attempt = False
                        try: 
                            fileVersion = data["version"]
                            attempt = True
                        except:
                            print()
                            scrollingText("This file was made before v0.2.0. You can manually update this file", 2, 0.01)
                            scrollingText("to match a current file, or make a new file in the program.", 2, 0.01)
                            print()
                            askToContinue()
                            mainMenu()
                        if attempt:
                            if fileVersion == currentVersion:
                                creationMode = data["creationmode"]
                                characterNames = []
                                characterPlans = []
                                characterAttributes = []
                                characterDialogue = []
                                run = 0
                                while run < data["length"]:
                                    characterNames.append(data[str(run)]["name"])
                                    characterPlans.append(data[str(run)]["plan"])
                                    characterDialogue.append(data[str(run)]["dialogue"])
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
                                scrollingText("This file was created with a previous version of FliSh. You can ", 2, 0.01)
                                scrollingText("can manually update this file to match a current file, or make a new file in the program.", 2, 0.01)
                                print()
                                askToContinue()
                                mainMenu()
                    else:
                        scrollingText("Sorry, this character file was made with a different set of content packs.", 2, 0.01)
                        if data["npcPack"] != contentPacks.npc:
                            scrollingText("This file takes an npc content pack with the ID of " + data["npcPack"] + " while you have " + contentPacks.npc + " currently enabled.")
                        if data["dialoguePack"] != contentPacks.dialogue:
                            scrollingText("This file takes a dialogue content pack with the ID of " + data["dialoguePack"] + " while you have " + contentPacks.dialogue + " currently enabled.")
            else:
                mainMenu()
        else:
            print()
            scrollingText("Directory is empty!", 2, 0.01)
            askToContinue()
            mainMenu()
    if decision == 2:
        run = 0
        data = {}
        data["length"] = len(characterNames)
        data["creationmode"] = creationMode
        data["version"] = currentVersion
        data["npcPack"] = contentPacks.npc
        data["dialoguePack"] = contentPacks.dialogue
        while run < len(characterNames):
            data[str(run)] = {}
            data[str(run)]["name"] = characterNames[run]
            data[str(run)]["plan"] = characterPlans[run]
            data[str(run)]["dialogue"] = characterDialogue[run]
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
    data["version"] = currentVersion
    data["npcPack"] = contentPacks.npc
    data["dialoguePack"] = contentPacks.dialogue
    while run < len(characterNames):
        data[str(run)] = {}
        data[str(run)]["name"] = characterNames[run]
        data[str(run)]["plan"] = characterPlans[run]
        data[str(run)]["dialogue"] = characterDialogue[run]
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

def openPack():
    global items
    global npc
    global dialogue

    directory = os.path.dirname(__file__)
    foldername = os.path.join(directory, ('contentPacks/*'))
    contentFolders = glob.glob(foldername)
    display = []
    run = 0
    while len(display) < len(contentFolders):
        currFileName = os.path.join(contentFolders[run], "packInfo.json")
        try:
            infoFile = json.load(open(currFileName, "r"))
            display.append(infoFile["name"])
        except:
            print()
            scrollingText("One of these folders doesn't have a packInfo.json, make sure it has one in", 2, 0.01)
            scrollingText("the original download, or write one yourself using CFS.", 2, 0.01)
            display.append(format.red + "Invalid content pack" + format.end)
        run = run + 1
    display.append("Default pack")
    display.append("Exit")
    print()
    decision = ask("Choose content pack:", 2, display, 0.05)
    print()
    if display[decision - 1] != "Exit":
        if display[decision - 1] != "Default pack":
            packDirectory = os.path.join(foldername, contentFolders[decision - 1])
            loadingFile = os.path.join(packDirectory, "packInfo.json")
            infoFile = json.load(open(loadingFile, "r"))
            print(format.clear)
            display.append(infoFile["name"])
            run = 0
            if infoFile["status"] == "Unfinished":
                print()
                scrollingText(format.underline + format.bold + format.red + infoFile["name"] + format.end, 2, 0.01)
            if infoFile["status"] == "In progress":
                print()
                scrollingText(format.underline + format.bold + format.blue + infoFile["name"] + format.end, 2, 0.01)
            if infoFile["status"] == "Finished":
                print()
                scrollingText(format.underline + format.bold + format.green + infoFile["name"] + format.end, 2, 0.01)
            authList = infoFile["authors"][0]
            run = 1
            while run < len(infoFile["authors"]):
                authList = authList + ", " + infoFile["authors"][run]
                run = run + 1
            scrollingText("Author(s): " + authList, 2, 0.01)
            while run < len(infoFile["description"]):
                scrollingText(infoFile["description"][run], 2, 0.01)
                run = run + 1
            if "items" in infoFile["content"]:
                scrollingText("This pack includes " + format.red + "items" + format.end + ".", 2, 0.01)
            if "npcs" in infoFile["content"]:
                scrollingText("This pack includes " + format.blue + "NPCs" + format.end + ".", 2, 0.01)
            if "dialogue" in infoFile["content"]:
                scrollingText("This pack includes " + format.green + "dialogue" + format.end + ".", 2, 0.01)
            print()
            decision = ask("Load this package?", 2, ["Yes", "No"], 0.05)
            print()
            if decision == 1:
                if "items" in infoFile["content"]:
                    try:
                        filename = os.path.join(packDirectory, ('json/items.json'))
                        items = json.load(open(filename, "r"))
                        contentPacks.items = infoFile["id"]
                        scrollingText("Items JSON file loaded from " + infoFile["name"] + ".", 2, 0.01)
                    except:
                        print()
                        scrollingText("Sorry, we couldn't load the items file from this content pack.", 2, 0.01)
                        scrollingText("Make sure the packInfo.json is filled out properly!", 2, 0.01)
                        print()
                        askToContinue()
                        openPack()
                if "npcs" in infoFile["content"]:
                    try:
                        filename = os.path.join(packDirectory, ('json/npcs.json'))
                        npc = json.load(open(filename, "r"))
                        contentPacks.npc = infoFile["id"]
                        scrollingText("NPC JSON file loaded from " + infoFile["name"] + ".", 2, 0.01)
                    except:
                        print()
                        scrollingText("Sorry, we couldn't load the NPC file from this content pack.", 2, 0.01)
                        scrollingText("Make sure the packInfo.json is filled out properly!", 2, 0.01)
                        print()
                        askToContinue()
                        openPack()
                if "dialogue" in infoFile["content"]:
                    try:
                        filename = os.path.join(packDirectory, ('json/dialogue.json'))
                        dialogue = json.load(open(filename, "r"))
                        contentPacks.dialogue = infoFile["id"]
                        scrollingText("Dialogue JSON file loaded from " + infoFile["name"] + ".", 2, 0.01)
                    except:
                        print()
                        scrollingText("Sorry, we couldn't load the dialogue file from this content pack.", 2, 0.01)
                        scrollingText("Make sure the packInfo.json is filled out properly!", 2, 0.01)
                        print()
                        askToContinue()
                        openPack()
                scrollingText("All listed content from " + infoFile["name"] + " loaded.", 2, 0.01)
                print()
                askToContinue()
            else:
                print(format.clear)
                openPack()
        else:
            directory = os.path.dirname(__file__)
            filename = os.path.join(directory, ('json/items.json'))
            items = json.load(open(filename, "r"))
            scrollingText("Items JSON file loaded from default.", 2, 0.01)
            filename = os.path.join(directory, ('json/npcs.json'))
            npc = json.load(open(filename, "r"))
            scrollingText("NPC JSON file loaded from default.", 2, 0.01)
            filename = os.path.join(directory, ('json/dialogue.json'))
            dialogue = json.load(open(filename, "r"))
            scrollingText("Dialogue JSON file loaded from default.", 2, 0.01)
            contentPacks.items = "Default pack"
            contentPacks.npc = "Default pack"
            contentPacks.dialogue = "Default pack"
            askToContinue()
        mainMenu()
    else:
        mainMenu()

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
                clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                strikethrough = "\u001b[29m"
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
                clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                strikethrough = "\u001b[29m"
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
                clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                strikethrough = ""
                underline = ""
                italic = ""
                dim = ""
                bold = ""
                end = ""
                red = ""
                blue = ""
                green = ""
    mainMenu()



mainMenu()