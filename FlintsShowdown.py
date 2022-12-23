#   _____  __     _____   __   __  _____  __  _____      _____  __  __  ______  __    __  ____    ______  __    __  __   __ 
#  / ___/ / /    /_  _/  /  | / / /_  _/ /_/ /  __/     /  __/ / /_/ / / __  / / /__ / / / __ |  / __  / / /__ / / /  | / /
# / ___/ / /___  _/ /_  / /||/ /   / /      /__  /     /__  / / __  / / /_/ / / // // / / /_/ / / /_/ / / // // / / /||/ /
#/_/    /_____/ /____/ /_/ |__/   /_/      /____/     /____/ /_/ /_/ /_____/ /_______/ /_____/ /_____/ /_______/ /_/ |__/
version = "0.3.0"
dateRelease = "December 25, 2022"
#Project start: Jan 23, 2022
#Current release push: December 25, 2022

'''
TO DO:
- Dialogue
- Hunger system
- Appendage system, getting wounded affects combat, etc
- Medical supplies, maybe having different items heal different parts
- Crafting (Maybe?)
- Factions/grouping
    - Group meetups
    - Group combat
    - Inter-person dialogue (Custom support?)
- More items
- Improved NPCs
'''

import random
import os
import time
import json
import MOOSERecoded as moose

# Attempts to load individual json files that are used by the program
directory = os.path.dirname(__file__)
filename = os.path.join(directory, (r'usersettings.json'))
usr = json.load(open(filename, "r"))

filename = os.path.join(directory, (r'json/items.json'))
items = json.load(open(filename, "r"))
filename = os.path.join(directory, (r'json/npcs.json'))
npc = json.load(open(filename, "r"))
filename = os.path.join(directory, (r'json/dialogue.json'))
dialogue = json.load(open(filename, "r"))
usedmods = []
usedmodtitles = []



"""
   __ __  _____  _____  __    _____  _____  _  __
  / // / /_  _/ /_  _/ / /   /_  _/ /_  _/ | |/ /
 / // /   / /  _/ /_  / /__  _/ /_   / /    / /
/____/   /_/  /____/ /____/ /____/  /_/    /_/
"""
# Defines ANSI format codes to be used later on
# Make sure your terminal supports ANSI before filing a bug report
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

def checkAnsi():
    if usr["ansiCompat"] == None:
        print("Running first time setup...\n")
        onColour = moose.askOption("Does weird text show up here? --->" + "\u001b[0m", ["Yes", "No"])
        if onColour == 1:
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
            usr["ansiCompat"] = False
        else:
            usr["ansiCompat"] = True
        moose.jason.saveFile(r'usersettings', usr)

# Pulls a list of characters from the living character set for use in other functions
def generateCharacterList(number):
    # The returned list, empty at the start
    charList = []
    # List of those living, used to gather characters for charList
    livingCharacters = []
    # Opens loop
    x = 0
    while x < len(characterNames):
        # Checks to see if the read character is dead
        if characterNames[x] not in deadCharacters:
            # Adds read character to the livingCharacters if it is alive
            livingCharacters.append(x)
        x = x + 1
    # Checks to see if the requested number of characters is greater than the amount living
    if number > len(livingCharacters):
        # Returns full list of livingCharacters if so
        return livingCharacters
    else:
        # Returns partial list of livingCharacters if not
        while len(charList) < number:
            rand = random.randint(0, len(characterNames) - 1)
            if rand not in charList:
                if characterNames[rand] not in deadCharacters:
                    charList.append(rand)
    # Returns list of characters
    return charList

# Generates a list of events for the day depending on the initial amount of characters
def generateEvents():
    # Determines the amount of events happening for this day depending on the amount of characters at start
    eventNum = random.randint(1, int(len(characterNames) / 2))
    # Opens list of events
    eventList = []
    # Adds an airdrop to the start of the event list every 3 days
    if days % 3 == 0:
        eventList.append("airdrop")
    # Defines a list of event codes
    events = ["saw_participant", "heard_participant", "trace", "attacked", "looting"]
    # Loops checks to see if the length of events meets the required number for that day
    while len(eventList) < eventNum:
        # Finds and adds a random event from the list of event codes
        eventList.append(random.choice(events))
    return eventList

# Checks to see if a character file's data is up to date with the current build
def checkRelint(data, filename):
    # Opens issue list
    issues = []
    try:
        # Attempts to find version value
        version = data["version"]
        # If listed version is not equal to program version, adds version correction to the list of issues
        if data["version"] != version:
            issues.append(data["version"])
    # If version is not found in the file, add it to the list of issues
    except:
        issues.append("version")
    try:
        # Attempts to find character dialogue
        dialoguePlan = data["1"]["dialogue"]
    # If dialogue is not found in the character file, add it to the list of issues
    except:
        issues.append("dialogue")
    # If there are issues within the list, send it to the relint() function
    if len(issues) > 0:
        relintedData = relint(data, issues, filename)
        return relintedData

def relint(data, issues, filename):
    # Asks user if they want the program to change the file
    print(format.clear)
    decision = moose.askOption("This data file is out of date, and this can cause issues.\n  Would you like to have to program modify it and have it be used anyway?\n", ["Yes", "No"])
    # If they decide yes, run through issues list
    if decision == 1:
        run = 0
        # Runs through issues
        while run < len(issues):
            # If "version" tag is in list, add current version to the version tag
            if issues[run] == "version":
                data["version"] = version
            if issues[run] == "dialogue":
                leng = data["length"]
                dialogRun = 0
                while dialogRun < leng:
                    data[str(dialogRun)]["dialogue"] = "basic"
                    dialogRun = dialogRun + 1
            run = run + 1
        run = 0
        # Opens dict type for saving
        newData = {}
        # Adds preliminary info
        newData["length"] = data["length"]
        newData["version"] = version
        newData["creationmode"] = data["creationmode"]
        # Adds info for each character 
        while run < data["length"]:
            # Opens character dict
            newData[str(run)] = {}
            newData[str(run)]["name"] = data[str(run)]["name"]
            newData[str(run)]["plan"] = data[str(run)]["plan"]
            newData[str(run)]["dialogue"] = data[str(run)]["dialogue"]
            newData[str(run)]["melee"] = data[str(run)]["melee"]
            newData[str(run)]["ranged"] = data[str(run)]["ranged"]
            newData[str(run)]["endurance"] = data[str(run)]["endurance"]
            newData[str(run)]["strength"] = data[str(run)]["strength"]
            newData[str(run)]["communication"] = data[str(run)]["communication"]
            run = run + 1
        # Finds root directory
        directory = os.path.dirname(__file__)
        # Navigates to characterSaves folder within directory
        foldername = os.path.join(directory, ('characterSaves/'))
        # Finds file path
        filename = os.path.join(foldername, filename)
        # Opens file for writing
        file = open(filename, "w")
        # Dumps all data
        json.dump(newData, file, separators = (', ', ': '), indent = 4)
        # Prints out relint statement and waits for user
        print()
        moose.scrollingText("Data was relinted without any issues.")
        print()
        moose.askToContinue()
        # Returns and stores relinted data
        return newData
    # Returns to menu if the user chooses not to have the program change file
    if decision == 2:
        mainMenu()

# Determines, processes, and prints out loot given to characters
def runLoot(characters):
    # Globalizes the lists of items, their durabilities, and character armour values, all affected by loot gained in this function
    global characterItems
    global characterItemDurabilities
    global characterArmour
    
    # Grabs a random item from the item table
    lootItem = random.choice(items["lootable"])
    # Checks to see if the gained item is armour
    if items[lootItem]["type"] == "Armour":
        # Adds the armour value to the current character's armour
        characterArmour[characters[0]] = characterArmour[characters[0]] + items[lootItem]["ap"]
        # Prints out the armour pickup message
        if items[lootItem]["uncap"] == True:
            moose.scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".")
        else:
            moose.scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"] + format.end + ".")
    # If item is not armour...
    else:
        # If character is over capacity...
        if len(characterItems[characters[0]]) > 3:
            # Compare gained item grade over the currently equipped item
            if items[lootItem]["grade"] >= items[characterItems[characters[0]][0]]["grade"]:
                # Checks the uncap value for the currently equipped item
                if items[characterItems[characters[0]][0]]["uncap"] == True:
                    if items[lootItem]["uncap"] == True:
                        # Both lower
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"].lower() + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"].lower() + format.end + ".")
                    else:
                        # Current lower, loot upper
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"].lower() + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"] + format.end + ".")
                else:
                    if items[lootItem]["uncap"] == True:
                        # Current upper, loot lower
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"] + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"].lower() + format.end + ".")
                    else:
                        # Both upper
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"] + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"] + format.end + ".")
                # Appends event to log
                event = {"day": days, "type": "loot", "chars": [characterNames[characters[0]]], "event": characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".", "item": lootItem}
                log.append(event)
                
                characterItems[characters[0]][0] = lootItem
                characterItemDurabilities[characters[0]][0] = items[lootItem]["durability"]
            else:
                if items[characterItems[characters[0]][0]]["uncap"] == True:
                    if items[lootItem]["uncap"] == True:
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"].lower() + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"].lower() + format.end + ".")
                    else:
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"].lower() + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"] + format.end + ".")
                else:
                    if items[lootItem]["uncap"] == True:
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"] + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"].lower() + format.end + ".")
                    else:
                        moose.scrollingText(characterNames[characters[0]] + " drops their " + format.red + items[characterItems[characters[0]][0]]["name"] + format.end + " to pick up the cache's " + format.green + items[lootItem]["name"] + format.end + ".")
        else:
            characterItems[characters[0]].append(lootItem)
            characterItemDurabilities[characters[0]].append(items[lootItem]["durability"])
            if items[lootItem]["uncap"] == True:
                moose.scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"].lower() + format.end + ".")
                event = {"day": days, "type": "loot", "chars": [characterNames[characters[0]]], "event": characterNames[characters[0]] + " picked up the " + items[lootItem]["name"].lower() + ".", "item": lootItem}
                log.append(event)
            else:
                moose.scrollingText(characterNames[characters[0]] + " picks up the " + format.green + items[lootItem]["name"] + format.end + ".")
                event = {"day": days, "type": "loot", "chars": [characterNames[characters[0]]], "event": characterNames[characters[0]] + " picked up the " + items[lootItem]["name"]  + ".", "item": lootItem}
                log.append(event)

# Checks to see if an item in a character's inventory has broken or not 
def checkBreak(character):
    if len(characterItems[character]) > 0:
        if characterItemDurabilities[character][0] <= 0:
            moose.scrollingText(format.red + characterNames[character] + items[characterItems[character][0]]["break"] + format.end)
            characterItems[character].pop(0)
            characterItemDurabilities[character].pop(0)
            if len(characterItems[character]) > 0:
                moose.scrollingText(format.blue + characterNames[character] + " switches to their " + items[characterItems[character][0]]["name"] + "." + format.end)
            else:
                moose.scrollingText(format.blue + characterNames[character] + " drops it." + format.end)

def filterLog(setfilters, readlog):
    returnlog = readlog
    filterrun = 0
    while filterrun < len(setfilters):
        instruction = setfilters[filterrun][0]
        if instruction == "char":
            logrun = 0
            while logrun < len(readlog):
                if not setfilters[filterrun][1] in log[logrun]["chars"]:
                    log.pop(logrun)
                logrun = logrun + 1
        if instruction == "loot":
            if len(setfilters[filterrun]) > 1:
                logrun = 0
                while logrun < len(readlog):
                    if log[logrun]["type"] == "loot":
                        if setfilters[filterrun][1] != log[logrun]["item"]:
                            log.pop(logrun)
                    logrun = logrun + 1
            else:
                logrun = 0
                while logrun < len(readlog):
                    if log[logrun]["type"] != "loot":
                        log.pop(logrun)
                    logrun = logrun + 1
        if instruction == "combat":
            logrun = 0
            while logrun < len(readlog):
                if log[logrun]["type"] != "combat":
                    log.pop(logrun)
                logrun = logrun + 1
        if instruction == "escape":
            logrun = 0
            while logrun < len(readlog):
                if log[logrun]["type"] != "escape":
                    log.pop(logrun)
                logrun = logrun + 1
        if instruction == "trace":
            logrun = 0
            while logrun < len(readlog):
                if log[logrun]["type"] != "trace":
                    log.pop(logrun)
                logrun = logrun + 1
        if instruction == "day":
            logrun = 0
            while logrun < len(readlog):
                if log[logrun]["day"] != setfilters[filterrun][1]:
                    log.pop(logrun)
                logrun = logrun + 1
        filterrun = filterrun + 1
    return returnlog

def stringFilters(filters):
    filterstrings = []
    run = 0
    while run < len(filters):
        if filters[run][0] == "loot":
            if len(filters[run]) > 1:
                string = "Filter by item looted: " + filters[run][1]
            else:
                string = "Filter by loot event"
        if filters[run][0] == "combat":
            string = "Filter by combat event"
        if filters[run][0] == "escape":
            string = "Filter by escape event"
        if filters[run][0] == "trace":
            string = "Filter by trace event"
        if filters[run][0] == "char":
            string = "Filter by character: " + characterNames[filters[run][1]]
        if filters[run][0] == "day":
            string = "Filter by day: " + filters[run][1]
        filterstrings.append(string)
        run = run + 1
    return filterstrings

def combat(characters, decision, ran):
    global deadCharacters
    determination = [10, 10]
    if decision == 1:
        print()
    if len(characterItems[characters[0]]) > 0:
        aGrade = items[characterItems[characters[0]][0]]["grade"]
    else:
        aGrade = 0
    if len(characterItems[characters[1]]) > 0:
        bGrade = items[characterItems[characters[1]][0]]["grade"]
    else:
        bGrade = 0
    gradediff = []
    gradediff.append(aGrade - bGrade)
    gradediff.append(bGrade - aGrade)
    if npc[characterPlans[characters[0]]]["attacked"] == "flee" or characterHealth[characters[0]] < 50 or gradediff[0] < 0:
        rand = random.randint(1, 4 + (characterAttributes[characters[1]][3] - characterAttributes[characters[0]][3]))
        if decision == 1:
            print()
            moose.scrollingText(format.blue + characterNames[characters[0]] + " attempts to run away." + format.end)
        if rand == 6:
            if decision != 1:
                print()
            moose.scrollingText(format.green + characterNames[characters[0]] + " runs away." + format.end)
            print()
            event = {"day": days, "type": "escape", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[0]] + " ran away from " + characterNames[characters[1]] + "."}
            log.append(event)
            ran = True
        else:
            if decision == 1:
                moose.scrollingText(format.red + characterNames[characters[0]] + " fails to run away." + format.end)
                determination[0] = determination[0] - 1
    charA = 1
    charB = 0
    if ran != True:
        ran = False
        while characterHealth[characters[0]] > 0 and characterHealth[characters[1]] > 0 and ran != True:
            if characterItems[characters[charA]] == []:
                rand = random.randint(1, 3)
                hits = ["punches", "hits", "kicks", "knees"]
                if rand != 3:
                    rand = random.randint(3, (characterAttributes[characters[charA]][4] * 2) + 3)
                    if characterArmour[characters[charB]] > 0:
                        if characterArmour[characters[charB]] - rand > 0:
                            characterArmour[characters[charB]] = characterArmour[characters[charB]] - rand
                        else:
                            rand = rand - characterArmour[characters[charB]]
                            characterArmour[characters[charB]] = 0
                            characterHealth[characters[charB]] = characterHealth[characters[charB]] - rand
                    else:
                        characterHealth[characters[charB]] = characterHealth[characters[charB]] - rand
                    if decision == 1:
                        moose.scrollingText(characterNames[characters[charA]] + " " + random.choice(hits) + " " + characterNames[characters[charB]] + ".   " + format.red + "-" + str(rand) + format.end)
                else:
                    if decision == 1:
                        moose.scrollingText(characterNames[characters[charA]] + " misses their shot.")
                        determination[charA] = determination[charA] - 1
            else:
                if decision == 1:
                    moose.scrollingText(characterNames[characters[charA]] + items[characterItems[characters[charA]][0]]["ready"])
                rand = random.randint(1, 100)
                weapon = items[characterItems[characters[charA]][0]]
                if decision == 1:
                    moose.scrollingText(characterNames[characters[charA]] + items[characterItems[characters[charA]][0]]["attack"] + characterNames[characters[charB]] + ".")
                if weapon["type"] == "Melee":
                    rand = rand + (characterAttributes[characters[charA]][1] * 5)
                if weapon["type"] == "Ranged":
                    rand = rand + (characterAttributes[characters[charA]][2] * 5)
                if rand <= weapon["accuracy"]:
                    dam = weapon["damage"]
                    if weapon["type"] == "Melee":
                        dam = dam + random.randint(0, characterAttributes[characters[charA]][1] * 5)  + random.randint(0, characterAttributes[characters[charA]][4] * 5)
                    if weapon["type"] == "Ranged":
                        dam = dam + random.randint(-10 , 10)
                    origDam = dam
                    determination[charB] = determination[charB] - (dam / 100)
                    if characterArmour[characters[charB]] > 0:
                        if characterArmour[characters[charB]] - dam > 0:
                            characterArmour[characters[charB]] = characterArmour[characters[charB]] - dam
                        else:
                            dam = dam - characterArmour[characters[charB]]
                            characterArmour[characters[charB]] = 0
                            characterHealth[characters[charB]] = characterHealth[characters[charB]] - dam
                    else:
                        characterHealth[characters[charB]] = characterHealth[characters[charB]] - dam
                    characterItemDurabilities[characters[charA]][0] = characterItemDurabilities[characters[charA]][0] - 1
                    if decision == 1:
                        moose.scrollingText("The shot connects.   " + format.red + "-" + str(origDam) + format.end)
                else:
                    if decision == 1:
                        moose.scrollingText("The shot misses.")
                    if items[characterItems[characters[charA]][0]]["faildamage"] == True:
                        characterItemDurabilities[characters[charA]][0] = characterItemDurabilities[characters[charA]][0] - 1
            checkBreak(characters[charA])
            if decision == 1:
                time.sleep(0.25)
            if charA == 1:
                charA = 0
                charB = 1
            else:
                charA = 1
                charB = 0
            if ran == True or characterHealth[characters[charA]] <= 0 or characterHealth[characters[charB]] <= 0:
                if characterHealth[characters[charA]] <= 0:
                    print()
                    moose.scrollingText(characterNames[characters[charA]] + " succumbs to their wounds, and dies.")
                    charactersKilled[characters[charB]].append(characterNames[characters[charA]])
                    killedBy[characters[charA]] = characterNames[characters[charB]]
                    if characterItems[characters[charB]] != []:
                        if items[characterItems[characters[charB]][0]]["uncap"] == True:
                            event = {"day": days, "type": "death", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with a " + items[characterItems[characters[charB]][0]]["name"].lower() +  "."}
                            log.append(event)
                        else:
                            event = {"day": days, "type": "death", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with a " + items[characterItems[characters[charB]][0]]["name"] +  "."}
                            log.append(event)
                    else:
                        event = {"day": days, "type": "death", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charA]] + " was killed by " + characterNames[characters[charB]] + " with their" + format.italic + " fists." + format.end}
                        log.append(event)
                    characterKills[characters[charB]] = characterKills[characters[charB]] + 1
                    print()
                    deadCharacters.append(characterNames[characters[charA]])
                if characterHealth[characters[charB]] <= 0:
                    moose.scrollingText(characterNames[characters[charB]] + " succumbs to their wounds, and dies.")
                    charactersKilled[characters[charA]].append(characterNames[characters[charB]])
                    killedBy[characters[charB]] = characterNames[characters[charA]]
                    if characterItems[characters[charA]] != []:
                        if items[characterItems[characters[charA]][0]]["uncap"] == True:
                            event = {"day": days, "type": "death", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with a " + items[characterItems[characters[charA]][0]]["name"].lower() +  "."}
                            log.append(event)
                        else:
                            event = {"day": days, "type": "death", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with a " + items[characterItems[characters[charA]][0]]["name"] +  "."}
                            log.append(event)
                    else:
                        event = {"day": days, "type": "death", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charB]] + " was killed by " + characterNames[characters[charA]] + " with their" + format.italic + " fists." + format.end}
                        log.append(event)
                    characterKills[characters[charA]] = characterKills[characters[charA]] + 1
                    print()
                    deadCharacters.append(characterNames[characters[charB]])
                break
            rand = random.randint(1, 6)
            if rand == 1 or characterHealth[characters[charB]] < 50 or gradediff[charB] < 0 or determination[charB] <= 0:
                rand = random.randint(1, 4 + (characterAttributes[characters[charB]][3] - characterAttributes[characters[charA]][3]))
                if decision == 1:
                    moose.scrollingText(format.blue + characterNames[characters[charB]] + " attempts to run away." + format.end)
                if rand == 6 or determination[charA] < 5:
                    if determination[charA] < 5:
                        moose.scrollingText(format.green + characterNames[characters[charA]] + " lets " + characterNames[characters[charB]] + " get away." + format.end)
                    else:
                        moose.scrollingText(format.green + characterNames[characters[charB]] + " runs away." + format.end)
                    characterNames[characters[0]] + " saw " + characterNames[characters[1]] + "."
                    event = {"day": days, "type": "escape", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[charB]] + " ran away from " + characterNames[characters[charA]] + "."}
                    log.append(event)
                    ran = True
                else:
                    if decision == 1:
                        moose.scrollingText(format.red + characterNames[characters[charB]] + " fails to run away." + format.end)
                        determination[charB] = determination[charB] - 1



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
    print("          ╵-╵   " + format.end + format.bold + format.blue + " /____/ /_/ /_/ /_____/ /_______/ /_____/ /_____/ /_______/ /_/ |__/" + format.end + format.italic + format.bold)
    print()
    moose.scrollingText("v" + version + " / " + dateRelease + " build" + format.end)
    decision = moose.askOption("", ["Start new game", "Create characters", "Enable/disable mods", "Settings", "Exit"], delay = 0.02)
    if decision == 1:
        startSim()
    if decision == 2:
        selectSimMode()
        createCharacters()
    if decision == 3:
        loadMods()
    if decision == 4:
        settings()
    if decision == 5:
        raise Exception("Exited game... I think.")

def startSim():
    global creationMode
    global characterNames
    global characterPlans
    global characterDialogue
    global characterAttributes
    global characterHealth
    global characterItems
    global characterItemDurabilities
    global days
    global deadCharacters
    global characterKills
    global charactersKilled
    global killedBy
    global characterArmour
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
        characterSaves.append("Back to main manu")
        filenumber = moose.askOption("Load characters:", characterSaves)
        if characterSaves[filenumber - 1] != "Back to main manu":
            file = os.path.join(foldername, os.path.join(characterSaves[filenumber - 1]))
            data = json.load(open(file, "r"))
            checkRelint(data, characterSaves[filenumber - 1])
            creationMode = data["creationmode"]
            characterNames = []
            characterPlans = []
            characterDialogue = []
            characterAttributes = []
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
            mainMenu()
    else:
        print()
        moose.scrollingText("Directory is empty!")
        print()
        moose.askToContinue()
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
    charactersKilled = []
    while len(charactersKilled) <= len(characterNames):
        charactersKilled.append([])
    killedBy = []
    while len(killedBy) <= len(characterNames):
        killedBy.append("n/a")
    characterArmour = []
    while len(characterArmour) <= len(characterNames):
        characterArmour.append(0)
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
    moose.scrollingText(format.bold + format.blue + format.italic + "Day " + str(days) + "." + format.end)
    time.sleep(0.5)
    print()
    if len(characterNames) - len(deadCharacters) > 1:
        runEvents(generateEvents())
        time.sleep(0.5)
        print()
        moose.scrollingText(format.bold + format.blue + format.italic + "Night falls." + format.end)
        print()
        nightfall()
    else:
        printWinner()

def runEvents(eventList):
    run = 0
    while run < len(eventList):
        if len(deadCharacters) < len(characterNames) - 1:
            if eventList[run] == "saw_participant":
                sawParticipant()
            if eventList[run] == "heard_participant":
                heardParticipant()
            if eventList[run] == "trace":
                trace()
            if eventList[run] == "attacked":
                attacked()
                moose.askToContinue()
                print(format.clear)
            if eventList[run] == "looting":
                looting()
            if eventList[run] == "airdrop":
                airdrop()
            run = run + 1

def sawParticipant():
    characters = generateCharacterList(2)
    moose.scrollingText(characterNames[characters[0]] + " sees " + characterNames[characters[1]] + ".")
    event = {"day": days, "type": "trace", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[0]] + " saw " + characterNames[characters[1]] + "."}
    log.append(event)
    time.sleep(0.5)
    if npc[characterPlans[characters[0]]]["saw_participant"] == "loud":
        attack(characters)
    if npc[characterPlans[characters[0]]]["saw_participant"] == "stealth":
        rand = random.randint(1, 6)
        if rand == 6:
            attacked(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " hides.")
    if npc[characterPlans[characters[0]]]["saw_participant"] == "flee":
        rand = random.randint(1, 8)
        if rand == 4:
            attacked(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " runs away.")
    if npc[characterPlans[characters[0]]]["saw_participant"] == "communicate":
        moose.scrollingText(format.blue + characterNames[characters[0]] + " attempts to negotiate with " + characterNames[characters[1]] + "." + format.end)
        rand = random.randint(1, 4)
        if rand == 4:
            moose.scrollingText(format.red + characterNames[characters[1]] + " didn't like that." + format.end)
            attacked(characters)
        else:
            moose.scrollingText(format.green + characterNames[characters[0]] + " successfully negotiates with " + characterNames[characters[1]] + "." + format.end)
    print()
    moose.askToContinue()
    print(format.clear)

def heardParticipant():
    characters = generateCharacterList(2)
    moose.scrollingText(characterNames[characters[0]] + " hears something.")
    event = {"day": days, "type": "trace", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[0]] + " heard something."}
    log.append(event)
    time.sleep(0.5)
    if npc[characterPlans[characters[0]]]["heard_participant"] == "loud":
        rand = random.randint(1, 4)
        if rand == 4:
            moose.scrollingText(characterNames[characters[0]] + " finds " + characterNames[characters[1]] + ".")
            attack(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " searches the area, but doesn't find anyone.")
    if npc[characterPlans[characters[0]]]["heard_participant"] == "stealth":
        rand = random.randint(1, 6)
        if rand == 6:
            moose.scrollingText(characterNames[characters[1]] + " finds " + characterNames[characters[0]] + ".")
            attacked(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " hides.")
    if npc[characterPlans[characters[0]]]["heard_participant"] == "seek":
        rand = random.randint(1, 2)
        if rand == 2:
            moose.scrollingText(characterNames[characters[0]] + " finds " + characterNames[characters[1]] + ".")
            attack(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " fails to find anyone.")
    if npc[characterPlans[characters[0]]]["heard_participant"] == "flee":
        moose.scrollingText(characterNames[characters[0]] + " runs away.")
    print()
    moose.askToContinue()
    print(format.clear)

def trace():
    characters = generateCharacterList(2)
    moose.scrollingText(characterNames[characters[0]] + " notices footprints in the mud.")
    event = {"day": days, "type": "trace", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[0]] + " noticed a trace of someone."}
    log.append(event)
    time.sleep(0.5)
    if npc[characterPlans[characters[0]]]["trace"] == "loud":
        rand = random.randint(1, 10)
        if rand == 10:
            moose.scrollingText(characterNames[characters[0]] + " finds " + characterNames[characters[1]] + ".")
            attack(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " fails to find anyone.")
    if npc[characterPlans[characters[0]]]["trace"] == "stealth":
        rand = random.randint(1, 16)
        if rand == 16:
            moose.scrollingText(characterNames[characters[1]] + " finds " + characterNames[characters[0]] + ".")
            attacked(characters)
        else:
            moose.scrollingText(characterNames[characters[0]] + " hides.")
    print()
    moose.askToContinue()
    print(format.clear)
        
def attacked(characters = []):
    if characters == []:
        characters = generateCharacterList(2)
    if len(characters) == 1:
        characters.append(generateCharacterList(1))
    ran = False
    moose.scrollingText(format.bold + format.red + characterNames[characters[1]] + " engages " + characterNames[characters[0]] + "." + format.end)
    if len(characterItems[characters[1]]) > 0:
        if items[characterItems[characters[1]][0]]["uncap"] == True:
            moose.scrollingText(characterNames[characters[1]] + " has a " + items[characterItems[characters[1]][0]]["name"].lower() + ".")
        else:
            moose.scrollingText(characterNames[characters[1]] + " has a " + items[characterItems[characters[1]][0]]["name"] + ".")
    else:
        moose.scrollingText(characterNames[characters[1]] + " is using their fists.")
    if len(characterItems[characters[0]]) > 0:
        if items[characterItems[characters[0]][0]]["uncap"] == True:
            moose.scrollingText(characterNames[characters[0]] + " has a " + items[characterItems[characters[0]][0]]["name"].lower() + ".")
        else:
            moose.scrollingText(characterNames[characters[0]] + " has a " + items[characterItems[characters[0]][0]]["name"] + ".")
    else:
        moose.scrollingText(characterNames[characters[0]] + " is using their fists.")
    event = {"day": days, "type": "combat", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[0]] + " got attacked by " + characterNames[characters[1]] + "."}
    log.append(event)
    print()
    decision = moose.askOption("Would you like to view this combat turn by turn?", ["Turn by turn", "Skip to result"])
    combat(characters, decision, ran)

def attack(characters = []):
    if characters == []:
        characters = generateCharacterList(2)
    if len(characters) == 1:
        characters.append(generateCharacterList(1))
    ran = False
    moose.scrollingText(format.bold + format.red + characterNames[characters[0]] + " attacks " + characterNames[characters[1]] + "." + format.end)
    if len(characterItems[characters[0]]) > 0:
        if items[characterItems[characters[0]][0]]["uncap"] == True:
            moose.scrollingText(characterNames[characters[0]] + " has a " + items[characterItems[characters[0]][0]]["name"].lower() + ".")
        else:
            moose.scrollingText(characterNames[characters[0]] + " has a " + items[characterItems[characters[0]][0]]["name"] + ".")
    else:
        moose.scrollingText(characterNames[characters[0]] + " is using their fists.")
    if len(characterItems[characters[1]]) > 0:
        if items[characterItems[characters[1]][0]]["uncap"] == True:
            moose.scrollingText(characterNames[characters[1]] + " has a " + items[characterItems[characters[1]][0]]["name"].lower() + ".")
        else:
            moose.scrollingText(characterNames[characters[1]] + " has a " + items[characterItems[characters[1]][0]]["name"] + ".")
    else:
        moose.scrollingText(characterNames[characters[1]] + " is using their fists.")
    event = {"day": days, "type": "combat", "chars": [characterNames[characters[0]], characterNames[characters[1]]], "event": characterNames[characters[0]] + " attacked " + characterNames[characters[1]] + "."}
    log.append(event)
    print()
    decision = moose.askOption("Would you like to view this combat turn by turn?", ["Turn by turn", "Skip to result"])
    newCharacters = []
    run = len(characters) - 1
    while run >= 0:
        newCharacters.append(characters[run])
        run = run - 1
    combat(newCharacters, decision, ran)

def looting():
    characters = generateCharacterList(2)
    moose.scrollingText(characterNames[characters[0]] + " notices a cache near their location.")
    if npc[characterPlans[characters[0]]]["looting"] == "loud":
        rand = random.randint(1, 6)
        if rand == 1:
            attacked(characters)
        else:
            runLoot(characters)
    if npc[characterPlans[characters[0]]]["looting"] == "stealth":
        runLoot(characters)
    if npc[characterPlans[characters[0]]]["looting"] == "seek":
        rand = random.randint(1, 8)
        if rand == 1:
            attack(characters)
        else:
            runLoot(characters)
    print()
    moose.askToContinue()
    print(format.clear)

def airdrop():
    characters = generateCharacterList(random.randint(1, int((len(characterNames) - len(deadCharacters) / 5))))
    run = 0
    moose.scrollingText(format.bold + "Airdrops descend on the showdown's arena." + format.end)
    print()
    while run < len(characters):
        tempChar = []
        tempChar.append(characters[run])
        runLoot(tempChar)
        run = run + 1
    print()
    moose.askToContinue()
    print(format.clear)

def nightfall():
    decision = moose.askOption("Nightfall actions:", ["View characters", "View log", "Continue to day"], delay = 0.05)
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
        moose.scrollingText("Character [" + format.red + "Health" + format.end + "] (" + format.green + "Equipped item" + format.end + ") {" + format.blue + "Kills" + format.end + "}")
        moose.scrollingText(format.red + "Dead character" + format.end + " {" + format.blue + "Kills" + format.end + "}")
        print()
        decision = moose.askOption("View character:\n", options, delay = 0.05)
        view = decision - 1
        print()
        if options[decision - 1] != "Exit":
            moose.scrollingText(format.bold + characterNames[view] + format.end)
            moose.scrollingText("Health: " + format.red + format.bold + str(characterHealth[view]) + format.end)
            if characterArmour[view] > 0:
                moose.scrollingText("Armour: " + format.blue + format.bold + str(characterArmour[view]) + format.end)
            if characterNames[view] in deadCharacters:
                moose.scrollingText("Killed by: " + killedBy[view])
            moose.scrollingText("Kills: " + str(characterKills[view]))
            if len(charactersKilled[view]) > 0:
                run = 0
                while run < len(charactersKilled[view]):
                    moose.scrollingText(str(run + 1) + ". " + charactersKilled[view][run])
                    run = run + 1
            print()
            moose.scrollingText("Inventory:")
            run = 0
            while run < len(characterItems[view]):
                currItem = items[characterItems[view][run]]
                moose.scrollingText(format.bold + currItem["name"] + format.end)
                moose.scrollingText(format.green + str(characterItemDurabilities[view][run]) + format.end + "/" + format.blue + str(currItem["durability"]) + format.end)
                linerun = 1
                while linerun <= 5:
                    if currItem[str(linerun)] != "":
                        print("  ", end = "")
                        print(currItem[str(linerun)])
                    linerun = linerun + 1
                print()
                run = run + 1
            if len(characterItems[view]) == 0:
                moose.scrollingText(format.bold + format.italic + "Inventory is empty!" + format.end)
        print(format.clear)
    nightfall()

def viewLog():
    print(format.clear)
    option = moose.askOption("Viewing log:", ["View with filter", "View full log", "Exit log viewer"])
    if option == 1:
        filters = []
        filteredlog = []
        option = 0
        while option != 3:
            print(format.clear)
            if len(filters) == 0:
                print("Add a filter to view the log!")
            else:
                if len(filteredlog) == 0:
                    moose.scrollingText("Filters didn't return anything! Remove some filters to see more.")
                else:
                    run = 0
                    while run < len(filteredlog):
                        filteredlog[run]["event"]
                        run = run + 1
            outoption = 0
            while outoption != 5:
                print(format.clear)
                outoption = moose.askOption("", ["Sort by character", "Sort by type", "Sort by day", "Remove filters", "Exit"])
                print(format.clear)
                if len(filters) == 0:
                    print("Add a filter to view the log!")
                else:
                    if len(filteredlog) == 0:
                        moose.scrollingText("Filters didn't return anything! Remove some filters to see more.")
                    else:
                        run = 0
                        while run < len(filteredlog):
                            filteredlog[run]["event"]
                            run = run + 1
                if outoption == 1:
                    print()
                    option = moose.askOption("Select character", characterNames)
                    filters.append(["char", option - 1])
                if outoption == 2:
                    print()
                    option = moose.askOption("Select filter type", ["Item found", "Combat", "Escape", "Trace", "None"])
                    if option == 1:
                        print()
                        option = moose.askOption("Filter by specific item or show all looting events?", ["Filter by item", "Show all", "None"])
                        if option == 1:
                            print()
                            itemid = moose.askOption("Choose item to filter by:", items["lootable"])
                            filters.append(["loot", items["lootable"][itemid]])
                        if option == 2:
                            filters.append(["loot"])
                    if option == 2:
                        filters.append(["combat"])
                    if option == 3:
                        filters.append(["escape"])
                    if option == 4:
                        filters.append(["trace"])
                if outoption == 3:
                    print()
                    filters.append(["day", moose.askOpen("Filter by day: (1 - " + str(days) + ")", min = 1, max = days)])
                if outoption == 4:
                    filterstrings = stringFilters(filters)
                    filters.pop(moose.askOption("Choose a filter to remove", filterstrings) - 1)
                filteredlog = filterLog(filters, log)
                
    if option == 2:
        print(format.clear)
        print("Viewing full log:\n")
        run = 0
        while run < len(log):
            print(log[run]["event"])
            time.sleep(0.05)
            run = run + 1
        print()
        moose.askToContinue()
    nightfall()

def healAll():
    run = 0
    while run < len(characterHealth):
        if characterHealth[run] > 0:
            if characterHealth[run] + 10 <= 100:
                characterHealth[run] = characterHealth[run] + 10
            else:
                characterHealth[run] = 100
        run = run + 1

def printWinner():
    run = 0
    while characterNames[run] in deadCharacters:
        run = run + 1
    print(format.clear)
    moose.scrollingText(format.green + characterNames[run] + format.end + " is the last one alive.")
    moose.scrollingText("They win.")
    print()
    moose.scrollingText("           Kills: " + str(characterKills[run]))
    if len(characterItems[run]) > 0:
        moose.scrollingText("Last used weapon: " + items[characterItems[run][0]]["name"])
    else:
        moose.scrollingText("Last used weapon: Fists")
    print()
    moose.askToContinue()
    mainMenu()

def selectSimMode():
    global creationMode
    global characterNames
    global characterDialogue
    global characterPlans
    global characterAttributes
    print(format.clear)
    time.sleep(0.5)
    moose.scrollingText("Detailed showdown")
    time.sleep(0.3)
    moose.scrollingText("- Full simulation", indent = 4, delay = 0.01)
    moose.scrollingText("- Choose NPC plan", indent = 4, delay = 0.01)
    moose.scrollingText("- Custom attributes", indent = 4, delay = 0.01)
    time.sleep(0.3)
    print()
    moose.scrollingText("Adaptable simulation")
    time.sleep(0.3)
    moose.scrollingText("- Full simulation", indent = 4, delay = 0.01)
    moose.scrollingText("- Random NPC plan", indent = 4, delay = 0.01)
    moose.scrollingText("- Custom attributes", indent = 4, delay = 0.01)
    time.sleep(0.3)
    print()
    moose.scrollingText("Simple logic")
    time.sleep(0.3)
    moose.scrollingText("- Partial simulation", indent = 4, delay = 0.01)
    moose.scrollingText("- Random NPC plan", indent = 4, delay = 0.01)
    moose.scrollingText("- All have same attributes", indent = 4, delay = 0.01)
    time.sleep(0.5)
    print()
    decision = moose.askOption("Select a creation mode:", ["Detailed", "Adaptable", "Simple", "Back to main manu"])
    if decision == 1:
        creationMode = "det"
    if decision == 2:
        creationMode = "ada"
    if decision == 3:
        creationMode = "sim"
    if decision == 4:
        mainMenu()
    characterNames = ["Joe Generic"]
    characterPlans = ["offensive"]
    characterDialogue = ["basic"]
    characterAttributes = [[0, 0, 0, 0, 0]]

def createCharacters(currentCharacter = 0):
    global characterNames
    global characterPlans
    global characterDialogue
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
            methods.append("Dialogue")
            methods.append("Attributes")
        if creationMode == "ada":
            methods.append("Name")
            methods.append("Dialogue")
            methods.append("Attributes")
        if creationMode == "sim":
            methods.append("Name")
        methods.append("Switch character")
        methods.append("New character")
        methods.append("Delete character")
        methods.append("Import/export character set")
        methods.append("Exit")
        moose.scrollingText("CHARACTER CREATION", delay = 0.025)
        print()
        moose.scrollingText("Name: " + characterNames[currentCharacter])
        moose.scrollingText("Plan: " + npc[characterPlans[currentCharacter]]["name"])
        moose.scrollingText("Dialogue plan: " + dialogue[characterDialogue[currentCharacter]]["name"])
        moose.scrollingText("Current character: #" + str(currentCharacter + 1))
        print()
        print("          Melee: " + str(characterAttributes[currentCharacter][0]))
        print("         Ranged: " + str(characterAttributes[currentCharacter][1]))
        print("      Endurance: " + str(characterAttributes[currentCharacter][2]))
        print("       Strength: " + str(characterAttributes[currentCharacter][3]))
        print("  Communication: " + str(characterAttributes[currentCharacter][4]))
        print()
        decision = moose.askOption("Character editor:", methods)
        if methods[decision - 1] == "Name":
            changeCharacterName(currentCharacter)
        if methods[decision - 1] == "NPC plan":
            changeCharacterPlan(currentCharacter)
        if methods[decision - 1] == "Dialogue":
            changeCharacterDialogue(currentCharacter)
        if methods[decision - 1] == "Attributes":
            changeCharacterAttributes(currentCharacter)
        if methods[decision - 1] == "Switch character":
            currentCharacter = switchCharacter(currentCharacter, characterNames)
        if methods[decision - 1] == "New character":
            currentCharacter = newCharacter(characterNames)
        if methods[decision - 1] == "Delete character":
            currentCharacter = deleteCharacter(currentCharacter)
        if methods[decision - 1] == "Import/export character set":
            saveLoadCharacters()
    print(format.clear)
    moose.scrollingText("Are you sure you want to exit?")
    decision = moose.askOption("Make sure you have your sheet saved before exiting.", ["Save sheet", "Back to character creation", "Exit"])
    if decision == 1:
        directToSave()
        mainMenu()
    if decision == 2:
        createCharacters(currentCharacter)
    if decision == 3:
        mainMenu()

def changeCharacterName(curChar):
    print()
    characterNames[curChar] = moose.askString("Choose character name:")
    print(format.clear)

def changeCharacterPlan(curChar):
    global characterPlans
    print()
    npclist = []
    run = 0
    while run < len(npc["npclist"]):
        npclist.append(npc[npc["npclist"][run]]["name"])
        run = run + 1
    decision = moose.askOption("Choose character's NPC plan", npclist)
    print(format.clear)
    print(npc[npc["npclist"][decision - 1]]["triangle1"])
    print(npc[npc["npclist"][decision - 1]]["triangle2"])
    print(npc[npc["npclist"][decision - 1]]["triangle3"])
    print(npc[npc["npclist"][decision - 1]]["triangle4"])
    print(npc[npc["npclist"][decision - 1]]["triangle5"])
    print()
    moose.scrollingText(npc[npc["npclist"][decision - 1]]["description"])
    flow = moose.askOption("", ["Set this as character plan", "Return to plan selection"], delay = 0.05)
    if flow == 1:
        characterPlans[curChar] = npc["npclist"][decision - 1]
    else:
        print(format.clear)
        changeCharacterPlan(curChar)
    print(format.clear)

def changeCharacterDialogue(curChar):
    global characterDialogue
    print()
    dialoguelist = []
    run = 0
    while run < len(dialogue["packs"]):
        dialoguelist.append(dialogue[dialogue["packs"][run]]["name"])
        run = run + 1
    decision = moose.askOption("Choose character's NPC plan", dialoguelist)
    characterDialogue[curChar] = dialogue["packs"][decision - 1]
    print(format.clear)

def changeCharacterAttributes(curChar):
    print(format.clear)
    print("          Melee: " + str(characterAttributes[curChar][0]))
    print("         Ranged: " + str(characterAttributes[curChar][1]))
    print("      Endurance: " + str(characterAttributes[curChar][2]))
    print("       Strength: " + str(characterAttributes[curChar][3]))
    print("  Communication: " + str(characterAttributes[curChar][4]))
    decision = moose.askOption("", ["Change melee", "Change ranged", "Change endurance", "Change strength", "Change communication", "Exit"])
    while decision != 6:
        if decision == 1:
            print()
            characterAttributes[curChar][0] = moose.askOpen("Choose value for melee:")
        if decision == 2:
            print()
            characterAttributes[curChar][1] = moose.askOpen("Choose value for ranged:")
        if decision == 3:
            print()
            characterAttributes[curChar][2] = moose.askOpen("Choose value for endurance:")
        if decision == 4:
            print()
            characterAttributes[curChar][3] = moose.askOpen("Choose value for strength:")
        if decision == 5:
            print()
            characterAttributes[curChar][4] = moose.askOpen("Choose value for communication:")
        print(format.clear)
        print("          Melee: " + str(characterAttributes[curChar][0]))
        print("         Ranged: " + str(characterAttributes[curChar][1]))
        print("      Endurance: " + str(characterAttributes[curChar][2]))
        print("       Strength: " + str(characterAttributes[curChar][3]))
        print("  Communication: " + str(characterAttributes[curChar][4]))
        decision = moose.askOption("", ["Change melee", "Change ranged", "Change endurance", "Change strength", "Change communication", "Exit"])
    print(format.clear)

def switchCharacter(curChar, currentCharacters):
    print(format.clear)
    print("  ")
    switch = moose.askOption("Current characters:", currentCharacters, lookingFor = [curChar])
    switch = switch - 1
    print(format.clear)
    return switch

def newCharacter(currentCharacters):
    print(format.clear)
    characterNames.append("Unnamed character")
    characterPlans.append("defensive")
    characterDialogue.append("basic")
    characterAttributes.append([0, 0, 0, 0, 0])
    newCharacter = len(currentCharacters) - 1
    return newCharacter

def deleteCharacter(currChar):
    global characterNames
    global characterPlans
    global characterDialogue
    global characterAttributes

    print()
    decision = moose.askOption("Would you really like to delete this character?", ["Yes", "No"], delay = 0.05)
    if decision == 1:
        characterNames.pop(currChar)
        characterPlans.pop(currChar)
        characterDialogue.pop(currChar)
        characterAttributes.pop(currChar)
        currChar = currChar - 1
    return currChar

def saveLoadCharacters():
    global characterNames
    global characterPlans
    global characterDialogue
    global characterAttributes
    global creationMode

    print()
    decision = moose.askOption("What do you want to do with this character sheet?", ["Load", "Save", "Copy characters to new file", "Back to character creation"])
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
            filenumber = moose.askOption("Load characters:", characterSaves)
            if characterSaves[filenumber - 1] != "Exit":
                file = os.path.join(foldername, os.path.join(characterSaves[filenumber - 1]))
                data = json.load(open(file, "r"))
                if data["creationmode"] != creationMode:
                    print()
                    decision = moose.askOption("This file was created in a different mode, would you like to switch to the file's mode?", ["Change mode to file", "Back to character creation"])
                    if decision == 1:
                        creationMode = data["creationmode"]
                    if decision == 2:
                        createCharacters()
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
                saveLoadCharacters()
        else:
            print()
            print("  Directory is empty!")
            print()
            moose.askToContinue()
            print(format.clear)
    if decision == 2:
        run = 0
        data = {}
        data["length"] = len(characterNames)
        data["creationmode"] = creationMode
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
        filename = moose.askString("Name this character set:")
        filename = os.path.join(foldername, filename + r'.json')
        file = open(filename, "w")
        json.dump(data, file, separators = (', ', ': '), indent = 4)
    if decision == 3:
        selected = []
        charList = characterNames
        charList.append("Complete copy")
        charList.append("Cancel copy")
        print(format.clear)
        decision = 0
        while charList[decision] != "Complete copy" and charList[decision] != "Cancel copy":
            decision = moose.askOption("Choose characters to copy:", charList, lookingFor = selected) - 1
            if charList[decision] != "Complete copy" and charList[decision] != "Cancel copy":
                selected.append(decision)
            print(format.clear)
        if charList[decision] == "Complete copy":
            data = {}
            data["length"] = len(selected)
            data["creationmode"] = creationMode
            run = 0
            while run < len(selected):
                data[str(run)] = {}
                data[str(run)]["name"] = characterNames[selected[run]]
                data[str(run)]["plan"] = characterPlans[selected[run]]
                data[str(run)]["dialogue"] = characterDialogue[selected[run]]
                data[str(run)]["melee"] = characterAttributes[selected[run]][0]
                data[str(run)]["ranged"] = characterAttributes[selected[run]][1]
                data[str(run)]["endurance"] = characterAttributes[selected[run]][2]
                data[str(run)]["strength"] = characterAttributes[selected[run]][3]
                data[str(run)]["communication"] = characterAttributes[selected[run]][4]
                run = run + 1
            print()
            directory = os.path.dirname(__file__)
            foldername = os.path.join(directory, ('characterSaves/'))
            filename = moose.askString("Name the new character set:")
            filename = os.path.join(foldername, filename + r'.json')
            file = open(filename, "w")
            json.dump(data, file, separators = (', ', ': '), indent = 4)
            file.close()
            data = json.load(open(filename, "r"))
            characterNames = []
            characterPlans = []
            characterDialogue = []
            characterAttributes = []
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
    filename = moose.askString("Name this character set:")
    filename = os.path.join(foldername, filename + r'.json')
    file = open(filename, "w")
    json.dump(data, file, separators = (', ', ': '), indent = 4)
    print(format.clear)

def loadMods():
    global items
    global npc
    global dialogue
    global usedmods
    global usedmodtitles

    print(format.clear)
    directory = os.path.dirname(__file__)
    dirname = os.path.join(directory, (r'json/mods/'))
    dirlist = os.listdir(dirname)
    openlist = []
    opendir = []
    x = 0
    while x < len(dirlist):
        dir = moose.jason.openFile(r'mods/' + dirlist[x], omitType = True)
        opendir.append(dir)
        openlist.append(dir["modname"])
        x = x + 1
    openlist.append("Reset to default")
    openlist.append("Return to main menu")
    if len(openlist) <= 1:
        moose.scrollingText("You have no mods in the folder!")
        moose.scrollingText("Place mod files in the /json/mods/ folder to have them show up here.\n")
        moose.askToContinue()
    else:
        mod = 1
        while openlist[mod - 1] != "Return to main menu":
            print(format.clear)
            mod = moose.askOption("Choose a mod to load:", openlist, lookingFor = usedmods)
            if openlist[mod - 1] == "Reset to default":
                directory = os.path.dirname(__file__)
                filename = os.path.join(directory, (r'json/items.json'))
                items = json.load(open(filename, "r"))
                filename = os.path.join(directory, (r'json/npcs.json'))
                npc = json.load(open(filename, "r"))
                filename = os.path.join(directory, (r'json/dialogue.json'))
                dialogue = json.load(open(filename, "r"))
                usedmods = []
                usedmodtitles = []
            else:
                if openlist[mod - 1] != "Return to main menu":
                    openmod = opendir[mod - 1]
                    category = openmod["category"]
                    if category == "items":
                        if openmod["overwrite"]:
                            items = mod
                        else:
                            nowLoot = items["lootable"]
                            newLoot = openmod["lootable"]
                            items.update(openmod)
                            items["lootable"] = nowLoot + newLoot
                    if category == "npc":
                        if openmod["overwrite"]:
                            npc = mod
                        else:
                            nowPlan = npc["npclist"]
                            newPlan = openmod["npclist"]
                            npc.update(openmod)
                            npc["npclist"] = nowPlan + newPlan
                    if category == "dialogue":
                        if openmod["overwrite"]:
                            dialogue = mod
                        else:
                            nowPack = dialogue["packs"]
                            newPack = openmod["packs"]
                            dialogue.update(openmod)
                            dialogue["packs"] = nowPack + newPack
                    usedmods.append(mod - 1)
                    usedmodtitles.append(openmod["modname"])
    mainMenu()

def settings():
    global format
    print(format.clear)
    moose.scrollingText("SETTINGS", delay = 0.025)
    print()
    print("  Display mode: " + format.mode)
    print()
    decision = moose.askOption("Change settings:", ["Change display mode", "Back to main menu"])
    if decision == 1:
        print()
        newmode = moose.askOption("Set display mode:", ["Colourmatic", "Markdown formatting", "Plain text"])
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



moose.displayLogo()
time.sleep(1)
checkAnsi()
mainMenu()