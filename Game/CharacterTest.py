import io

saveTest = open('fillersave.txt', 'w')
content = []


def loader():
    global content
    if loadSave == "Y":
        saveName = input("What is the name of the file you are trying to load? ")
        save = open(saveName, "r+")
        content = save.readlines()
        name = content[0]
        name = name.rstrip('\n')
        print(content[0])
        print(name)
        character = content[1]
        print(content[1])
        print(character)
        print(f"Hello {name}, you are playing as {character}")

    elif loadSave == "N":
        name = input("What is your name? ")
        character = input("What character would you like to play? ")
        saveName = f"{name}.txt"
        save = open(saveName, "w")
        save.write(name + '\n')
        save.write(character)
        print(f"Hello {name}, you are playing as {character}")


loadSave = input("Would you like to load a save? (Y/N) ")
loader()
print("Your Save:")
print(saveTest)
print(content)


