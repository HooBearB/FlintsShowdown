import json
import os
import textwrap

class format:
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

def menu():
    print(format.clear)
    print("   " + "           |\\")
    print("   " + " __________| |")
    print("   " + "|_________|  |")
    print("   " + "           |_|")
    print("     " + format.end + format.red + " _____" + format.end + format.blue + " _____" + format.end + format.green + " _____" + format.end)
    print("  " + format.end + format.red + "   / ___/" + format.end + format.blue + "/ ___/" + format.end + format.green + "/ ___/" + format.end)
    print("  " + format.end + format.red + "  / /__" + format.end + format.blue + " / ___/" + format.end + format.green + "/___ /" + format.end)
    print("  " + format.end + format.red + " /____/" + format.end + format.blue + "/_/   " + format.end + format.green + "/____/" + format.end)
    print()
    print(format.bold + "    CustomFliSh" + format.end)
    print(format.italic + "    Mod making tool for Flint's Showdown" + format.end)
    print("    Compatable with FliSh v0.2.0")
    print()
    decision = ask("CFS is currently a work in progress, please bear with me on this.", 2, ["Create CFS folder", "Open CFS folder", "Learn about CFS"])
    if decision == 1:
        createCFS()
    if decision == 2:
        openCFS()
    if decision == 3:
        learnCFS()

def createCFS():
    print(format.clear)
    filename = askString("What would you like the mod folder to be named?", 2)
    directory = os.path.dirname(__file__)
    foldername = os.path.join(directory, ('contentPacks/'))
    os.makedirs(os.path.join(foldername, filename))
    foldername = os.path.join(foldername, filename)
    os.makedirs(os.path.join(foldername, 'json/'))
    jsonname = os.path.join(foldername, 'json/')
    infoFile = os.path.join(foldername, 'packInfo.json')
    file = open(infoFile, "w")
    infoData = {}
    infoData["name"] = askString("What would you like the pack to be named?", 2)
    authors = []
    decision = ""
    while decision != "1":
        decision = askString("What authors made this content pack? (Type 1 to exit and move on.)", 2)
        if decision != "1":
            authors.append(decision)
    infoData["authors"] = authors
    infoData["id"] = infoData["name"]
    infoData["status"] = "Unfinished"
    description = askString("Add a description for what you want the pack to be.", 2)
    infoData["description"] = textwrap.wrap(description, 65)
    infoData["content"] = []
    json.dump(infoData, file, separators = (',', ':'), indent = 4)
    openCFS(infoFile, jsonname)

def openCFS(infoFile, jsonDir):
    print(format.clear)
    methods = []
    methods.append("Edit info file")
    if "items.json" in os.listdir(jsonDir):
        methods.append("Open items")
    else:
        methods.append("Create items file")
    if "npcs.json" in os.listdir(jsonDir):
        methods.append("Open NPCs")
    else:
        methods.append("Create NPC file")
    if "dialogue.json" in os.listdir(jsonDir):
        methods.append("Open dialogue")
    else:
        methods.append("Create dialogue file")
    decision = ask("File creation menu", 2, methods)
    if methods[decision - 1] == "Edit info file":
        editInfo()
    if methods[decision - 1] == "Open items":
        createItems()
    if methods[decision - 1] == "Open NPCs":
        createNPCs()
    if methods[decision - 1] == "Open dialogue":
        createDialogue()
    if methods[decision - 1] == "Create items file":
        file = open(os.path.join(jsonDir, "items.json"), "w")
        info = json.load(open(infoFile, "r"))
        info["content"].append("items")
        json.dump(info, open(infoFile, "w"), separators = (',', ':'), indent = 4)
        createItems(file)
    if methods[decision - 1] == "Create NPC file":
        file = open(os.path.join(jsonDir, "npcs.json"), "w")
        info = json.load(open(infoFile, "r"))
        info["content"].append("npcs")
        json.dump(info, open(infoFile, "w"), separators = (',', ':'), indent = 4)
        createNPCs(file)
    if methods[decision - 1] == "Create dialogue file":
        file = open(os.path.join(jsonDir, "dialogue.json"), "w")
        info = json.load(open(infoFile, "r"))
        info["content"].append("dialogue")
        json.dump(info, open(infoFile, "w"), separators = (',', ':'), indent = 4)
        createDialogue(file)

menu()