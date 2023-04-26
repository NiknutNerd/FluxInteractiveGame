from tkinter import *

from Game.Blue import Blue
from Game.Bo import Bo
from Game.Brandon import Brandon

pageCounter = 1
name = ""
character = ""
saveFile = None
save = None


def increaseCounter(event):
    global pageCounter
    pageCounter += 1
    screen.config(text=str("Page " + str(pageCounter)))


def decreaseCounter(event):
    global pageCounter
    pageCounter -= 1
    screen.config(text=str("Page " + str(pageCounter)))


def loadPage(page):
    page = int(page)
    makeImage("C:\FluxGame\Tester.png")
    if page == 2:
        print("Loading Page 2")
        makePage2()
    elif page == 3:
        makePage3()


def makeImage(image):
    artFrame.picture = PhotoImage(file=image)
    artFrame.label = Label(artFrame, image=artFrame.picture)
    artFrame.label.pack()


window = Tk()
window.title("Flux Interactive Game")
window.geometry("800x600")

window.update()
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()

artFrame = Frame(window, width=800, height=400)
textFrame = Frame(window)
buttonFrame = Frame(window)

artFrame.pack()
textFrame.pack()
buttonFrame.pack()

nextButton = Button(window, text="Next ->")
nextButton.place(x=(windowWidth - nextButton.winfo_reqwidth()),
                 y=(windowHeight - nextButton.winfo_reqheight()))
nextButton.bind("<Button-1>", increaseCounter)

backButton = Button(window, text="<- Back")
backButton.place(x=(windowWidth - nextButton.winfo_reqwidth() - backButton.winfo_reqwidth()),
                 y=(windowHeight - backButton.winfo_reqheight()))
backButton.bind("<Button-1>", decreaseCounter)

screen = Label(window, text=("Page " + str(pageCounter)))
screen.place(x=0, y=(windowHeight - screen.winfo_reqheight()))

# Page 1 Welcome page, greeting and start button

welcome = Label(window, text="Welcome to Flux!")
welcome.place(x=((windowWidth / 2) - welcome.winfo_reqwidth() / 2), y=((windowHeight) / 2) - welcome.winfo_reqheight())


def startClick(event):
    screen.config(text=("Page " + str(pageCounter)))
    makeImage("C:\FluxGame\Tester.png")
    makePage2()


startButton = Button(window, text="Start")
startButton.pack()
startButton.bind("<Button-1>", startClick)


def loadClick(event):
    loadPrompt.pack()
    loadSaveEntry.pack()
    continueSave.pack()

    continueSave.bind("<Button-1>", continueSaveClick)


def continueSaveClick(event):
    global name
    name = loadSaveEntry.get()

    global saveFile
    saveFile = open(f"{name}.txt", "r+")

    global save
    save = saveFile.readlines()

    global character
    global pageCounter

    try:
        name = save[0]
        name = name.rstrip('\n')
        character = save[1]
        character = character.rstrip('\n')
        pageCounter = save[2]
        pageCounter = pageCounter.rstrip('\n')
    except:
        print("An Error Has Occured, Check Save")
        window.quit()


    print(name)
    print(character)
    print(pageCounter)

    destroyPage1()
    loadPage(pageCounter)


loadButton = Button(window, text="Load")
loadButton.pack()
loadButton.bind("<Button-1>", loadClick)

loadPrompt = Label(window, text="Enter Save Name:")
loadSaveEntry = Entry(window)
continueSave = Button(window, text="Load Save")


def nameClicked(event):
    global name
    name = nameEntry.get()
    global saveFile
    saveFile = open(f"{name}.txt", "w")
    saveFile.write(name)
    saveFile.write("\n")
    saveFile.write(character)
    saveFile.write('\n')
    saveFile.write(str(pageCounter))

    namePrompt.config(text=("Welcome to Flux, " + name))
    makePage3()


namePrompt = Label(textFrame, text="Enter Player Name: ")
nameEntry = Entry(textFrame)
nameButton = Button(textFrame, text="Enter")


def saveClicked(event):
    saveFile.write()


def destroyPage1():
    welcome.destroy()
    startButton.destroy()
    loadButton.destroy()
    loadPrompt.destroy()
    loadSaveEntry.destroy()
    continueSave.destroy()


# Page 2 Name entry, prompt,
def makePage2():
    global pageCounter
    pageCounter = 2
    screen.config(text=str("Page " + str(pageCounter)))

    welcome.destroy()
    startButton.destroy()

    namePrompt.pack(side=TOP)
    nameEntry.pack(side=TOP)
    nameButton.pack(side=TOP)

    nameButton.bind("<Button-1>", nameClicked)


characterPrompt = Label(textFrame, text="Choose Your Character:")
boButton = Button(buttonFrame, text="Bo", fg="red")
brandonButton = Button(buttonFrame, text="Brandon")
blueButton = Button(buttonFrame, text="Blue", fg="blue")


def boClicked(event):
    print("Bo")
    global character
    character = "Bo"


def brandonClicked(event):
    print("Brandon")
    global character
    character = "Brandon"


def blueClicked(event):
    print("Blue")
    global character
    character = "Blue"


# Page 3 Welcome message, character choice
def makePage3():
    global pageCounter
    pageCounter = 3
    screen.config(text=str("Page " + str(pageCounter)))

    nameEntry.destroy()
    nameButton.destroy()
    characterPrompt.pack(side=TOP)
    boButton.grid(row=1, column=0, padx=20, ipadx=((brandonButton.winfo_reqwidth()-boButton.winfo_reqwidth())/2))
    brandonButton.grid(row=1, column=1, padx=20)
    blueButton.grid(row=1, column=2, padx=20, ipadx=((brandonButton.winfo_reqwidth()-blueButton.winfo_reqwidth())/2))

    boButton.bind("<Button-1>", boClicked)
    brandonButton.bind("<Button-1>", brandonClicked)
    blueButton.bind("<Button-1>", blueClicked)


window.mainloop()