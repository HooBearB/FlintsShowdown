import json
import os

directory = os.path.dirname(__file__)
filename = os.path.join(directory, ('json/items.json'))
items = json.load(open(filename, "r"))

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

while 1 == 1:
    item = input("\nItem?\n")
    item = item.lower()
    if item in items:
        print()
        print(format.bold + items[item]["name"] + format.end)
        print("        Damage: " + str(items[item]["damage"]))
        print("      Accuracy: " + str(items[item]["accuracy"]))
        print("    Durability: " + str(items[item]["durability"]))
        print("Damage on fail: " + str(items[item]["faildamage"]))
        print()
        print("Player A" + items[item]["ready"])
        print("Player A" + items[item]["attack"] + "Player B.")
        print("Player A" + items[item]["break"])
        print()
        if items[item]["1"] != "":
            print(items[item]["1"])
        if items[item]["2"] != "":
            print(items[item]["2"])
        if items[item]["3"] != "":
            print(items[item]["3"])
        if items[item]["4"] != "":
            print(items[item]["4"])
        if items[item]["5"] != "":
            print(items[item]["5"])
    else:
        print("Not a valid item ID!")