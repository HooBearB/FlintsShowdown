import json
import random
import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, ('json/structures.json'))
structures = json.load(open(filename, "r"))

class format:
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    dim = "\u001b[2m"
    bold = "\u001b[1m"
    end = "\u001b[0m"
    red = "\u001b[31m"
    blue = "\u001b[36m"
    green = "\u001b[32m"

def generateMap(leng, widt):
    mapObj = []
    while len(mapObj) < leng:
        line = []
        while len(line) < widt:
            rand = random.randint(1, 100)
            min = 150
            max = 150
            run = 0
            while not min <= rand <= max:
                tileid = structures["list"][run]
                tiledata = structures[tileid]
                min = tiledata["check"][0]
                max = tiledata["check"][1]
                if run != len(structures["list"]):
                    run = run + 1
            tile = tiledata["display"]
            
            if tiledata["colour"] == "red":
                tile = format.red + tile
            if tiledata["colour"] == "green":
                tile = format.green + tile
            if tiledata["colour"] == "blue":
                tile = format.blue + tile
            tile = tile + format.end
            
            line.append(tile)
        mapObj.append(line)
    return mapObj

def printMap(mapObject):
    runx = 0
    runy = len(mapObject) - 1
    print(format.bold)
    while runy > 0:
        while runx < len(mapObject[runy]):
            print(mapObject[runy][runx], end = "")
            runx = runx + 1
        print()
        runx = 0
        runy = runy - 1
    print(format.end)    
    
map1 = generateMap(25, 25)
printMap(map1)