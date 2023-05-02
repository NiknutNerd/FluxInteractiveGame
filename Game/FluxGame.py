from tkinter import *
import tkinter.font as font

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
    makeImage("C:\FluxGame\Tester.png")
    makeConstants()

    if character == "Bo":
        if page == 4:
            boPage4()
        elif page == 5:
            boPage5()
        elif page == 6:
            boPage6()
        elif page == 7:
            boPage7()
    elif character == "Brandon":
        if page == 4:
            brandonPage4()



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


def updatePageNumber(page):
    global pageCounter
    pageCounter = page
    screen.config(text=f'Page {pageCounter}')


# Page 2 Name entry, prompt,
def makePage2():
    updatePageNumber(2)

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

    makeConstants()
    makeImage("C:\FluxGame\Tester.png")

    saveUpdate()
    boPage4()


def brandonClicked(event):
    global character
    global pageCounter
    global save

    character = "Brandon"
    pageCounter = 4

    makeConstants()
    makeImage("C:\FluxGame\Tester.png")

    saveUpdate()
    brandonPage4()


def blueClicked(event):
    global character
    global pageCounter

    character = "Blue"
    pageCounter = 4

    makeConstants()
    makeImage("C:\FluxGame\Tester.png")

    saveUpdate()
    bluePage4()


# Page 3 Welcome message, character choice
def makePage3():
    updatePageNumber(3)

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
boFont = font.Font(family="Courier", size=14)
boText1 = Label(textFrame, font=boFont)
boText2 = Label(textFrame, font=boFont)
boText3 = Label(textFrame, font=boFont)
boText4 = Label(textFrame, font=boFont)
boClickButton = Button(textFrame, font=boFont)
boOptionButton = Button(textFrame, font=boFont)

def boPage4():
    updatePageNumber(4)

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()

    boText1.config(text="You are in the car with your Dad, Hal and brother, Kaz")
    boText2.config(text="It is around Christmastime. There is snow on the side of the road.")
    boText3.config(text="No one has talked for the whole ride")
    boText4.config(text="")
    boClickButton.config(text="Continue")
    boClickButton.bind("<Button-1>", bo5Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boClickButton.pack(side=TOP)

def bo5Click(event):
    boPage5()
def boPage5():
    updatePageNumber(5)

    boText1.config(text="Kaz: Did Umma make dinner?")
    boText2.config(text="Dad: No, Kazzie, I'll make you something when we're home.")
    boText3.config(text="Kaz: Grilled cheeses.")
    boText4.config(text="")
    boClickButton.config(text="Continue")
    boClickButton.bind("<Button-1>", bo6Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boClickButton.pack(side=TOP)

def bo6Click(event):
    boPage6()
def boPage6():
    updatePageNumber(6)

    boText1.config(text="You realize that your right shoe is missing")
    boText2.config(text="The bottom of your sock has gotten very dirty")
    boText3.config(text="")
    boText4.config(text="")
    boOptionButton.config(text="Look for shoe")
    boClickButton.config(text="Don't look for shoe")
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boOptionButton.pack(side=LEFT)
    boClickButton.pack(side=LEFT)
    boOptionButton.config(command=lambda: bo7Click(True))
    boClickButton.config(command=lambda: bo7Click(False))


def bo7Click(event, shoe=False):
    boPage7(shoe)
def boPage7(shoe=False):
    updatePageNumber(7)
    boOptionButton.forget()
    if shoe:
        boText1.config(text="You look around for your shoe, but you can't find it.")
    else:
        boText1.config(text="You do not look for the shoe.")
    boText2.config(text="Kaz: Is Umma making dinner?")
    boText3.config(text="You and your dad both tense up at Kaz's words")
    boText4.config(text="")
    boClickButton.config(text="- C L I C K -")
    boClickButton.bind("<Button-1>", bo8Click)

    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boClickButton.pack(side=TOP)

def bo8Click(event):
    boPage8()
def boPage8():
    updatePageNumber(8)

    boText1.config(text="Raider")
    boText2.config(text="")
    boText3.config(text="")
    boText4.config(text="")
    boClickButton.config(text="")
    boClickButton.bind("<Button-1>", bo9Click)

    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boClickButton.pack(side=TOP)


def bo9Click(event):
    boPage9()
def boPage9():
    updatePageNumber(9)

    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boClickButton.pack(side=TOP)



brandonFont = font.Font(family="Times", size=14)
brandonText1 = Label(textFrame, font=brandonFont)
brandonText2 = Label(textFrame, font=brandonFont)
brandonText3 = Label(textFrame, font=brandonFont)
brandonText4 = Label(textFrame, font=brandonFont)
brandonClickButton = Button(textFrame, font=brandonFont)
brandonOptionButton = Button(textFrame, font=brandonFont)

def brandonPage4():
    updatePageNumber(4)

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()

    brandonText1.config(text="You wake up next to your boyfriend, Gil")
    brandonText2.config(text="Gil: Too early, go back to sleep.")
    brandonText3.config(text="")
    brandonText4.config(text="")
    brandonClickButton.config(text="What?")
    brandonClickButton.bind("<Button-1>", brandon5Click)

    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon5Click(event):
    brandonPage5()
def brandonPage5():
    updatePageNumber(5)
    brandonText1.config(text="Gil: You're not sleeping.")
    brandonText2.config(text="The first snow of the year is on the ground outside")
    brandonText3.config(text="If it sticks around for a few days there might be a white Christmas")
    brandonText4.config(text="Gil: Want any breakfast?")
    brandonClickButton.config(text="I'll be late if I do")
    brandonClickButton.bind("<Button-1>", brandon6Click)

    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon6Click(event):
    brandonPage6()
def brandonPage6():
    updatePageNumber(6)

    brandonText1.config(text="Gil: Just be late")
    brandonText2.config(text="You leave for work, taking the trash with you")
    brandonText3.config(text="")
    brandonText4.config(text="")
    brandonClickButton.config(text="Go to Work")
    brandonClickButton.bind("<Button-1>", brandon7Click)

    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon7Click(event):
    brandonPage7()
def brandonPage7():
    updatePageNumber(7)

    brandonText1.config(text="You take the subway to Memorial Park")
    brandonText2.config(text="Up ahead there is a large glass building that houses the headquarters of an old newspaper company.")
    brandonText3.config(text="That newspaper company is the parent company of Metropol, a dying magazine")
    brandonText4.config(text="")
    brandonClickButton.config(text="Enter")
    brandonClickButton.bind("<Button-1>", brandon8Click)

    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon8Click(event):
    brandonPage8()
def brandonPage8():
    updatePageNumber(8)
    brandonText1.config(text="In the elevator is a woman that works with you")
    brandonText2.config(text="What is her name again? You can never seem to remember. Maybe its Lee?")
    brandonText3.config(text="You give each other small smiles in greeting")
    brandonText4.config(text="Lee(?): Happy holidays")
    brandonClickButton.config(text="To you, too")
    brandonClickButton.bind("<Button-1>", brandon9Click)

    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon9Click(event):
    brandonPage9()
def brandonPage9():
    updatePageNumber(9)
    brandonText1.config(text="You continue making awkward small talk with Lee(?)")
    brandonText2.config(text="You go to work, but get distracted reading the past couple issues of Metropol")
    brandonText3.config(text="After a while your boss Gil(Same Guy) walks up")
    brandonText4.config(text="Gil: Hey    Let's talk")
    brandonClickButton.config(text="")
    brandonClickButton.bind("<Button-1>")



blueFont = font.Font(family="Helvetica", size=14)
blueText1 = Label(textFrame, font=blueFont)
blueText2 = Label(textFrame, font=blueFont)
blueText3 = Label(textFrame, font=blueFont)
blueText4 = Label(textFrame, font=blueFont)
blueClickButton = Button(textFrame, font=blueFont)
blueOptionButton = Button(textFrame, font=blueFont)
def bluePage4():
    updatePageNumber(4)

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()

    blueText1.config(text="You walk up to the freight entrance of a nondescript glass tower")
    blueText2.config(text="A young woman and a man named Tor are waiting for you")
    blueText3.config(text="Tor: You're late.")
    blueText4.config(text="")
    blueOptionButton.config(text="Address the woman")
    blueClickButton.config(text="Address Tor")

    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueOptionButton.pack(side=LEFT)
    blueClickButton.pack(side=LEFT)
    blueOptionButton.config(command=lambda: blue5Click(True))
    blueClickButton.config(command=lambda: blue5Click(False))



def blue5Click(event, address=False):
    bluePage5(address)
def bluePage5(address=False):
    updatePageNumber(5)
    blueOptionButton.forget()
    if address:
        blueText1.config(text="You sign   Train got stopped on the way   to the woman")
    else:
        blueText1.config(text="You sign   Train got stopped on the way   to Tor")
    blueText2.config(text="The woman looks confused and flustered")
    blueText3.config(text="Tor: Relax, we don't have an interpretter today. You won't need it in a couple minutes anyway.")
    blueText4.config(text="")
    blueClickButton.config(text="Continue")
    blueClickButton.bind("<Button-1>", blue6Click)

    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def blue6Click(event):
    bluePage6()
def bluePage6():
    updatePageNumber(6)
    blueText1.config(text="Woman: Right this way Mr. Blue")
    blueText2.config(text="Tor: Don't call him that, its not even his name")
    blueText3.config(text="You follow Tor and the woman into the elevator and rocket upwards")
    blueText4.config(text="")
    blueClickButton.config(text="Continue 2")
    blueClickButton.bind("<Button-1>", blue7Click)

    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueClickButton.pack(side=TOP)

def blue7Click(event):
    bluePage7()
def bluePage7():
    updatePageNumber(7)

    blueText1.config(text="")
    blueText2.config(text="")
    blueText3.config(text="")
    blueText4.config(text="")
    blueClickButton.config(text="")
    blueClickButton.bind("<Button-1>")

    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueClickButton.pack(side=TOP)


window.mainloop()