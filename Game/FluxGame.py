from tkinter import *

pageCounter = 1
name = ""
character = ""
saveFile = open('fillersave.txt', 'w+')
save = [name, character, pageCounter]


def saveUpdate():
    global saveFile
    global save

    if save != [name, character, str(pageCounter)]:
        save = [name, character, str(pageCounter)]
        for i in range(len(save)):
            save[i] = save[i] + '\n'
    saveFile.writelines(save)
    print("Debugger Save Update")
    print(f"File Name: {saveFile.name}")
    print(f"Name: {name}")
    print(f"Character: {character}")
    print(f"Page: {pageCounter}")
    print(f"Save: {save}")


def loadPage(page):
    page = int(page)
    makeConstants()

    if character == "Bo" :
        if page == 4:
            makeBoPage4()
    elif character == "Brandon":
        if page == 4:
            makeBrandonPage4()


def makeConstants():
    saveAndQuitButton.place(x=(windowWidth - quitButton.winfo_reqwidth() - saveAndQuitButton.winfo_reqwidth()),
                            y=(windowHeight - saveAndQuitButton.winfo_reqheight()))
    saveButton.place(x=(
                windowWidth - quitButton.winfo_reqwidth() - saveAndQuitButton.winfo_reqwidth() - saveButton.winfo_reqwidth()),
                     y=(windowHeight - saveButton.winfo_reqheight()))

    saveAndQuitButton.bind("<Button-1>", saveAndQuitClick)
    saveButton.bind("<Button-1>", saveClick)


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

def makeImage(image):
    artFrame.picture = PhotoImage(file=image)
    artFrame.label = Label(artFrame, image=artFrame.picture)
    artFrame.label.pack()


# Save, Save and Quit, and Quit Button Methods
def saveClick(event):
    saveUpdate()


def saveAndQuitClick(event):
    saveUpdate()
    window.quit()


def quitClick(event):
    window.quit()


# Save and Quit Buttons
quitButton = Button(window, text="Quit")
quitButton.place(x=(windowWidth - quitButton.winfo_reqwidth()),
                 y=(windowHeight - quitButton.winfo_reqheight()))
quitButton.bind("<Button-1>", quitClick)

saveAndQuitButton = Button(window, text="Save + Quit")

saveButton = Button(window, text="Save")
"""
saveButton.place(x=(windowWidth - nextButton.winfo_reqwidth() - saveButton.winfo_reqwidth()),
                 y=(windowHeight - saveButton.winfo_reqheight()))
saveButton.bind("<Button-1>", saveClick())
"""


screen = Label(window, text=("Page " + str(pageCounter)))
screen.place(x=0, y=(windowHeight - screen.winfo_reqheight()))

# Page 1 Welcome page, greeting and start button

welcome = Label(window, text="Welcome to Flux!")
welcome.place(x=((windowWidth / 2) - welcome.winfo_reqwidth() / 2), y=((windowHeight) / 2) - welcome.winfo_reqheight())


def startClick(event):
    screen.config(text=("Page " + str(pageCounter)))
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
    global character
    global pageCounter
    global saveFile
    global save

    name = loadSaveEntry.get()

    try:
        saveFile = open(f"{name}.txt", "r+")
    except:
        loadPrompt.config(text='No Save Found')
        return

    save = saveFile.readlines()

    try:
        name = save[0]
        name = name.rstrip('\n')
        character = save[1]
        character = character.rstrip('\n')
        pageCounter = save[2]
        pageCounter = pageCounter.rstrip('\n')

        pageCounter = int(pageCounter)
    except:
        loadPrompt.config(text="Incorrect File Format")
        return

    if pageCounter > 3:
        destroyPage1()
        loadPage(pageCounter)
    else:
        loadPrompt.config(text="Invalid Page State")


loadButton = Button(window, text="Load")
loadButton.pack()
loadButton.bind("<Button-1>", loadClick)

loadPrompt = Label(window, text="Enter Save Name:")
loadSaveEntry = Entry(window)
continueSave = Button(window, text="Load Save")


def nameClicked(event):
    global name
    global saveFile
    global save

    name = nameEntry.get()
    saveFile = open(f"{name}.txt", "w+")

    namePrompt.config(text=("Welcome to Flux, " + name))
    makePage3()


namePrompt = Label(window, text="Enter Player Name: ")
nameEntry = Entry(window)
nameButton = Button(window, text="Enter")


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

    destroyPage1()

    nameEntry.place(x=((windowWidth / 2) - nameEntry.winfo_reqwidth() / 2),
                    y=((windowHeight) / 2) - nameEntry.winfo_reqheight())
    namePrompt.place(x=((windowWidth /2) - namePrompt.winfo_reqwidth() / 2),
                     y=((windowHeight) / 2) - nameEntry.winfo_reqheight() - namePrompt.winfo_reqheight())
    nameButton.place(x=((windowWidth / 2) - nameButton.winfo_reqwidth()/2),
                     y=(windowHeight/2))

    nameButton.bind("<Button-1>", nameClicked)


characterPrompt = Label(window, text="Choose Your Character:")
boButton = Button(buttonFrame, text="Bo", fg="red")
brandonButton = Button(buttonFrame, text="Brandon")
blueButton = Button(buttonFrame, text="Blue", fg="blue")


def boClicked(event):
    global character
    global pageCounter

    character = "Bo"
    pageCounter = 4

    saveUpdate()
    makeBoPage4()


def brandonClicked(event):
    global character
    global pageCounter
    global save

    character = "Brandon"
    pageCounter = 4

    saveUpdate()
    makeBrandonPage4()


def blueClicked(event):
    global character
    global pageCounter

    character = "Blue"
    pageCounter = 4

    saveUpdate()
    makeBluePage4()


# Page 3 Welcome message, character choice
def makePage3():
    global pageCounter
    pageCounter = 3
    screen.config(text=str("Page " + str(pageCounter)))

    nameEntry.destroy()
    nameButton.destroy()
    namePrompt.place(x=(windowWidth/2)-(namePrompt.winfo_reqwidth()/2))
    characterPrompt.place(x=((windowWidth/2) - (characterPrompt.winfo_reqwidth()/2)),
                          y=((windowHeight/2)))
    boButton.grid(row=1, column=0, padx=20, ipadx=(((brandonButton.winfo_reqwidth()-boButton.winfo_reqwidth())/2)+20), ipady=20)
    brandonButton.grid(row=1, column=1, padx=20, ipadx=20, ipady=20)
    blueButton.grid(row=1, column=2, padx=20, ipadx=(((brandonButton.winfo_reqwidth()-blueButton.winfo_reqwidth())/2)+20), ipady=20)

    boButton.bind("<Button-1>", boClicked)
    brandonButton.bind("<Button-1>", brandonClicked)
    blueButton.bind("<Button-1>", blueClicked)

# Bo's Story
boText1 = Label(textFrame, font=("Courier", 14))
boText2 = Label(textFrame, font=("Courier", 14))
boText3 = Label(textFrame, font=("Courier", 14))
boClickButton = Button(textFrame)

def toBo5(click):
    makeBoPage5()
def makeBoPage4():
    global pageCounter
    pageCounter = 4

    makeConstants()
    makeImage("C:\FluxGame\Tester.png")
    screen.config(text=f'Page {pageCounter}')

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()

    boText1.config(text="You are in the car with your Dad, Hal and brother, Kaz")
    boText2.config(text="No one has talked for the whole ride")
    boClickButton.bind("<Button-1>", toBo5)
    boText1.pack()
    boText2.pack()
    boClickButton.pack()


def makeBoPage5():
    global pageCounter
    pageCounter = 5
    screen.config(text=f'Page {pageCounter}')

    boText1.config(text="Kaz: Did Umma make dinner?")


brandonText1 = Label(textFrame, font=("Times", 14))
def makeBrandonPage4():
    global pageCounter
    pageCounter = 4

    makeConstants()
    makeImage("C:\FluxGame\Tester.png")
    screen.config(text=f"Page {pageCounter}")

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()


blueText1 = Label(textFrame, font=("Helvetica", 14))
def makeBluePage4():
    global pageCounter
    pageCounter = 4

    makeConstants()
    makeImage("C:\FluxGame\Tester.png")
    screen.config(text=f"Page {pageCounter}")

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()


window.mainloop()