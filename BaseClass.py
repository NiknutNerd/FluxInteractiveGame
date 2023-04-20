class User:
    name = ""
    character = ""

player = User()
player.name = input("Enter Player Name: ")
player.character = input("Which Character Would You Like To Play? ")

print(player.name)
print(player.character)
