import json

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

print(format.clear)
print("   ______")
print("  /______|" + format.end + format.red + " _____" + format.end + format.blue + " _____" + format.end + format.green + " _____" + format.end)
print("    | |" + format.end + format.red + "   / ___/" + format.end + format.blue + "/ ___/" + format.end + format.green + "/ ___/" + format.end)
print("    | |" + format.end + format.red + "  / /__" + format.end + format.blue + " / ___/" + format.end + format.green + "/___ /" + format.end)
print("    |_|" + format.end + format.red + " /____/" + format.end + format.blue + "/_/   " + format.end + format.green + "/____/" + format.end)
print()
print(format.bold + "    CustomFliSh" + format.end)
print("    Compatable with FliSh v0.2.0")
print()
decision = ask("", 2, ["Create CFS file", "Open CFS file"])