loadSave = input("Would you like to load a save? (Y/N) ")
if loadSave == "Y":
    saveName = input("What is the name of the file you are trying to load? ")
    save = open(saveName, "r+")
    content = save.readlines()
    name = content[0]
    name = name.rstrip('\n')
    character = content[1]
    print(f"Hello {name}, you are playing as {character}")

elif loadSave == "N":
    name = input("What is your name? ")
    character = input("What character would you like to play? ")
    saveName = f"{name}.txt"
    save = open(saveName, "w")
    save.write(name + '\n')
    save.write(character)
    print(f"Hello {name}, you are playing as {character}")