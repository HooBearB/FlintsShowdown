"""
   _____________  ________  ________  _________  _________
  /  __   __   / /  __   / /  __   / /  ______/ /  ______/
 /  / /  / /  / /  /_/  / /  /_/  / /______  / /  ______/
/__/ /__/ /__/ /_______/ /_______/ /________/ /________/
    ____                      __         __
   / __ \___  _________  ____/ /__  ____/ /
  / /_/ / _ \/ ___/ __ \/ __  / _ \/ __  /
 / _  _/  __/ /__/ /_/ / /_/ /  __/ /_/ /
/_/ |_|\___/\___/\____/\____/\___/\____/
"""
#v0.1
#Created by: Flint
#Maintained and added to by: (Insert the name of the guy I'm gonna bribe into looking at my shitty code)

import time
import os
import json

class format:
    mode = "Colour"
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    strikethrough = "\u001b[29m"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    bold = "\u001b[1m"
    dim = "\u001b[2m"
    red = "\u001b[31m"
    magenta = "\u001b[35m"
    blue = "\u001b[36m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    end = "\u001b[0m"

#Prints out logo for use in intro screens and such
def displayLogo():
    msg = """
MADE WITH
   _____________  ________  ________  _________  _________
  /  __   __   / /  __   / /  __   / /  ______/ /  ______/
 /  / /  / /  / /  /_/  / /  /_/  / /______  / /  ______/
/__/ /__/ /__/ /_______/ /_______/ /________/ /________/
    ____                      __         __
   / __ \___  _________  ____/ /__  ____/ /
  / /_/ / _ \/ ___/ __ \/ __  / _ \/ __  /
 / _  _/  __/ /__/ /_/ / /_/ /  __/ /_/ /
/_/ |_|\___/\___/\____/\____/\___/\____/

v0.1
"""
    print(format.clear)
    time.sleep(1)
    print(format.dim)
    print(msg)
    time.sleep(0.1)
    print(format.clear)
    print(format.end)
    print(msg)
    time.sleep(3)
    print(format.clear)
    print(format.dim)
    print(msg)
    time.sleep(0.1)
    print(format.end)
    print(format.clear)

#Prints out all included ANSI values with respective tags
def ansiTest():
    print(format.strikethrough + "Strikethrough" + format.end)
    print(format.italic + "Italic" + format.end)
    print(format.bold + "Bold" + format.end)
    print(format.dim + "Dimmed" + format.end)
    print(format.red + "Red" + format.end)
    print(format.magenta + "Magenta" + format.end)
    print(format.blue + "Blue" + format.end)
    print(format.green + "Green" + format.end)
    print(format.yellow + "Yellow" + format.end)

#Prints out a string bit by bit, giving the impression of text that scrolls across the screen
#   message: What to print out in the beginning (String)
#   indent: How far from the edge of the terminal printing should begin, in spaces (Positive integer, default 2)
#   increment: How many letters should print out in one loop (Positive integer, default 1)
#   delay: How long to wait between loops (Positive float, default 0.02)
def scrollingText(message, indent = 2, increment = 1, delay = 0.02):
    #Prints out indent from edge
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    #Prints out every letter in given message, pausing between every increment
    run = 0
    while run < len(message):
        print(message[run : run + increment], end = "")
        time.sleep(delay)
        run = run + increment
    print("")


#Asks for user input given a list of options
#   message: What to print out in the beginning (String)
#   options: What to print out in list form for the player to choose from (String table)
#   indent: How far from the edge of the terminal to start printing objects (Positive integer, default 2)
#   delay: How long to wait between printing list objects (Positive float, default 0)
#   lookingFor: What line to print a special string that indicates a selected object (Positive integer, default [-1] to prevent usage)
def askOption(message, options, indent = 2, delay = 0, lookingFor = [-1]):
    #Prints out indent
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    #Prints out initial message
    print(message)
    runline = 0
    while runline < len(options):
        #Checks if running line corresponds to the line that the program is looking for
        if runline in lookingFor:
            #Prints selection indicator and makes the line bold
            print("  - " + format.bold, end = "")
        else:
            #Prints list indent
            run = 0
            while run <= indent + 1:
                print(" ", end = "")
                run = run + 1
        #Prints out list object
        print(str(runline + 1) + ". " + options[runline])
        print(format.end, end = "")
        #Waits between loops
        time.sleep(delay)
        #Moves to next line in list
        runline = runline + 1
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    #Asks for user input
    decision = input("> ")
    #Checks if input is a usable int
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
    #Checks if input is within list range
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
    #Returns user decision
    return decision

#Prints out plain list of objects
#   message: What to print out in the beginning (String)
#   options: What to print out in list form for the player to choose from (String table)
#   indent: How far from the edge of the terminal to start printing objects (Positive integer, default 2)
#   delay: How long to wait between printing list objects (Positive float, default 0)
def listOption(message, options, indent = 2, delay = 0, lookingFor = -1):
    #Prints out indent
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    #Prints out initial message
    print(message)
    runline = 0
    while runline < len(options):
        #Checks if running line corresponds to the line that the program is looking for
        if runline == lookingFor:
            #Prints selection indicator and makes the line bold
            print("  - " + format.bold, end = "")
        else:
            #Prints list indent
            run = 0
            while run <= indent + 1:
                print(" ", end = "")
                run = run + 1
        #Prints out list object
        print(str(runline + 1) + ". " + options[runline])
        print(format.end, end = "")
        #Waits between loops
        time.sleep(delay)
        #Moves to next line in list
        runline = runline + 1

#Asks for open integer value without lists
#   message: What to print out in the beginning (String)
#   min: Lower limit of range, must be less than max, if given (Integer, default "N/A" to prevent usage) 
#   max: Upper limit of range, must be greater than min, if given (Integer, default "N/A" to prevent usage)
#   indent: How far from the edge of the terminal to start printing objects (Positive integer, default 2)
def askOpen(message, min = "N/A", max = "N/A", indent = 2):
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
    #Checks if decision is greater than minimum
    if min != "N/A" and max == "N/A":
        while decision < min:
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
    #Checks if decision is less than maximum
    if max != "N/A" and min == "N/A":
        while decision > max:
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
    #Checks if decision is greater than minimum and less than maximum
    if max != "N/A" and min != "N/A":
        while decision > max or decision < min:
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
    #Returns input
    return decision

#Asks for a string from user
#   message: What to print out in the beginning (String)
#   indent: How far from the edge of the terminal to start printing objects (Positive integer, default 2)
def askString(message, indent = 2):
    #Prints indent and message
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    #Asks for input
    decision = str(input("> "))
    return decision

#Pauses program to ask for input to continue
def askToContinue():
    #Asks to continue, x is an unused variable
    x = input("  Press " + format.bold + "enter" + format.end + " to continue.   ")

class jason:
    #Opens a file and dumps the JSON data into a dictionary object
    #   file: Path from the current file's directory (String, path-like)
    def openFile(file, omitType = False):
        #Finds root directory of running file
        directory = os.path.dirname(__file__)
        #Gets file path to file in /json/ folder that is found in root directory
        if omitType:
            filename = os.path.join(directory, (r'json/' + file))
        else:
            filename = os.path.join(directory, (r'json/' + file + r'.json'))
        #Attempts to find file in /json/ folder found in root directory
        try:
            items = json.load(open(filename, "r"))
        #Print error message if failure is inevitably encountered
        except:
            print(format.red + format.bold + "Error: Could not find json file at " + filename + " using JSONHandler.py" + format.end)
            items = "None"
        #Returns JSON content within file
        return items

    #Saves data to a given folder under a set file name
    #   name: What to save the file under (String)
    #   folder: Where to save the file (String)
    #   data: What to write in the file (Any type of data that can be stored in a JSON file)
    def saveFile(name, data, folder = r''):
        #Finds root directory of running file
        directory = os.path.dirname(__file__)
        #Gets file path to file in /json/ folder that is found in root directory
        filename = os.path.join(directory, (folder + name + r'.json'))
        #Opens file
        file = open(filename, "w")
        #Dumps data into file
        json.dump(data, file, separators = (',', ': '), indent = 4)

    #Tries to grab a value from a given dictionary
    #   root: The root object to pull from (Dictionary)
    #   find: What you want to attempt to pull from the root (String)
    #   setTo: What to use as the value to if there is no given value in the root (Any)
    def tryGrab(root, find, setTo):
        try:
            x = root[find]
        except:
            x = setTo
        return x