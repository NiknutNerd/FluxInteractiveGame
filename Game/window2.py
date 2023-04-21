from tkinter import *

from Game.Bo import Bo
from Game.Brandon import Brandon
from Game.Blue import Blue

counter = 0


def increaseCounter(event):
    global counter
    counter += 1
    screen.config(text=str("Page " + str(counter)))


def decreaseCounter(event):
    global counter
    counter -= 1
    screen.config(text=str("Page " + str(counter)))


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

artFrame = Frame(window)
textFrame = Frame(window)

artFrame.pack()
textFrame.pack()

nextButton = Button(window, text="Next ->")
nextButton.place(x=(windowWidth - nextButton.winfo_reqwidth()),
                 y=(windowHeight - nextButton.winfo_reqheight()))
nextButton.bind("<Button-1>", increaseCounter)

backButton = Button(window, text="<- Back")
backButton.place(x=(windowWidth - nextButton.winfo_reqwidth() - backButton.winfo_reqwidth()),
                 y=(windowHeight - backButton.winfo_reqheight()))
backButton.bind("<Button-1>", decreaseCounter)

screen = Label(window, text=("Page " + str(counter)))
screen.place(x=0, y=(windowHeight - screen.winfo_reqheight()))

# Page 1 Welcome page, greeting and start button

welcome = Label(window, text="Welcome to Flux!")
welcome.place(x=((windowWidth / 2) - welcome.winfo_reqwidth() / 2), y=((windowHeight) / 2) - welcome.winfo_reqheight())


def startClick(event):
    global counter
    counter = 1
    screen.config(text=("Page " + str(counter)))
    makeImage("C:\FluxGame\Tester.png")
    makePage2()


startButton = Button(window, text="Start")
startButton.pack()
startButton.bind("<Button-1>", startClick)


def nameClicked(event):
    name = nameEntry.get()
    namePrompt.config(text=("Welcome to Flux, " + name))


namePrompt = Label(textFrame, text="Enter Player Name: ")
nameEntry = Entry(textFrame)
nameButton = Button(textFrame, text="Enter")


# Page 2 Name entry, prompt,

def makePage2():
    welcome.destroy()
    startButton.destroy()

    namePrompt.pack(side=TOP)
    nameEntry.pack(side=TOP)
    nameButton.pack(side=TOP)

    nameButton.bind("<Button-1>", nameClicked)


characterPrompt = Label(textFrame, text="Choose Your Character: ")


# Page 3 Welcome message, character choice
def makePage3():
    nameEntry.destroy()
    nameButton.destroy()
    characterPrompt.pack(side=TOP)


window.mainloop()
