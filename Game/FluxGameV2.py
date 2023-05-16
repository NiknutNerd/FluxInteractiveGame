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

    """
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
    """


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


boFont = font.Font(family="Courier", size=12)
brandonFont = font.Font(family="Times", size=12)
blueFont = font.Font(family="Helvetica", size=12)
overviewFont = font.Font(family="Courier", size=14)


characterPrompt = Label(window, text="Choose Your Character:")
boButton = Button(buttonFrame, text="Bo", fg="red", font=boFont)
brandonButton = Button(buttonFrame, text="Brandon", font=brandonFont)
blueButton = Button(buttonFrame, text="Blue", fg="blue", font=blueFont)

overviewButton = Button(buttonFrame, text="Overview", font=overviewFont)


def overviewClicked(event):
    overviewMainPage()



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

    overviewButton.grid(row=2, column=1, padx=20, ipadx=20, ipady=20)

    boButton.bind("<Button-1>", boClicked)
    brandonButton.bind("<Button-1>", brandonClicked)
    blueButton.bind("<Button-1>", blueClicked)
    overviewButton.bind("<Button->", overviewClicked)


# Bo's Story
boText1 = Label(textFrame, font=boFont)
boText2 = Label(textFrame, font=boFont)
boText3 = Label(textFrame, font=boFont)
boText4 = Label(textFrame, font=boFont)
boText5 = Label(textFrame, font=boFont)
boClickButton = Button(textFrame, font=boFont)
boOptionButton = Button(textFrame, font=boFont)

def boPage4():
    updatePageNumber(4)

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()
    overviewButton.destroy()

    boText1.config(text="You are an 8 year old boy named Bo")
    boText2.config(text="You have a 4 year old brother named Kaz and your dad is named Hal")
    boText3.config(text="You are half-Korean from your Mom's side")
    boText4.config(text="Your favorite tv show is an 80's detective show called Raider")
    boText5.config(text="You, Kaz, and your dad are in the car. It is a few days before Christmas")
    boClickButton.config(text="Continue")
    boClickButton.bind("<Button-1>", bo5Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)

def bo5Click(event):
    boPage5()
def boPage5():
    updatePageNumber(5)

    boText1.config(text="Kaz breaks a long silence, asking: Did Umma make dinner?")
    boText2.config(text="You and your dad tense up. After a few moments your dad responds")
    boText3.config(text="Dad: I'll make you something when we get home | Kaz: Grilled cheeses")
    boText4.config(text="Dad spoke in Korean, which he almost never does")
    boText5.config(text="After a few long minutes Kaz asks again: Is Umma making dinner soon?")
    boClickButton.config(text="- C L I C K -")
    boClickButton.bind("<Button-1>", bo6Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)

def bo6Click(event):
    boPage6()

def boPage6():
    updatePageNumber(6)

    degree = chr(176)

    boText1.config(text="Season 2 Episode 2: The Mighty and the Weak")
    boText2.config(text="Jacket Guy's commanding officer wants to send him to Little China")
    boText3.config(text=f"to investigate a homicide of a baby girl left in a dumpster when it was 9{degree}F")
    boText4.config(text="Jacket guy needs to get the parents to open up about what happened.")
    boText5.config(text="He has a name, but you know him as Jacket Guy for the jacket he wears every day")
    boClickButton.config(text="Continue")
    boClickButton.bind("<Button-1>", bo7Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)


def bo7Click(event):
    boPage7()


def boPage7():
    updatePageNumber(7)

    boText1.config(text="Jacket guy enters a store in Little China. There is an old man at the counter")
    boText2.config(text="He addresses the man but he doesn't speak English. His son enters the shop")
    boText3.config(text="Jacket Guy asks for the parents of the baby Hui-Ling Tao, knowing that is the son")
    boText4.config(text="After some back and forth Jacket Guy addresses the son by his name, Jiao-Long")
    boText5.config(text="but Jiao-Long is not interested and orders Jacket Guy out of his shop")
    boClickButton.config(text="- C L I C K -")
    boClickButton.bind("<Button-1>", bo8Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)


def bo8Click(event):
    boPage8()


def boPage8():
    updatePageNumber(8)

    boText1.config(text="When you get home Kaz decides he is not hungry and starts to find something on tv")
    boText2.config(text="You don't like looking after Kaz, especially at school where people can see")
    boText3.config(text="Kaz always wants to play pretend and you don't want Annamarie Watkins to see")
    boText4.config(text="Annamarie had told you about the trip her family was going on for the holidays")
    boText5.config(text="Your family never travels for holidays but you like hearing her talk about it")
    boClickButton.config(text="Continue")
    boClickButton.bind("<Button-1>", bo9Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)


def bo9Click(event):
    boPage9()


def boPage9():
    boText1.config(text="Instead of grilled cheese you have cereal for dinner. No-one talks for a while")
    boText2.config(text="Dad breaks the silence telling you and Kaz to go straight to bed after dinner.")
    boText3.config(text="Kaz: Umma always reads me a book before bed.")
    boText4.config(text="Your dad suggests that you read to Kaz, but Kaz again insists that Umma does it")
    boText5.config(text="Kaz throws a tantrum, pounding away at the table until he tires himself out")
    boClickButton.config(text="- C L I C K -")
    boClickButton.bind("<Button-1>", bo10Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)


def bo10Click(event):
    boPage10()


def boPage10():
    updatePageNumber(10)
    # Page 69
    boText1.config(text="Jacket Guy is looking for the mom of Hui-Ling Tao and clues for the case")
    boText2.config(text="He eventually finds her entering the shop, but despite his pleading she won't talk")
    boText3.config(text="Jacket Guy: Your daughter deserves justice")
    boText4.config(text="The woman says if they go to the police they get deported and leaves")
    boText5.config(text="Jacket Guy realizes that he has lost his witness and he won't solve the case")
    boClickButton.config(text="- C L I C K -")
    boClickButton.bind("<Button-1>", bo11Click)
    boText1.pack(side=TOP)
    boText2.pack(side=TOP)
    boText3.pack(side=TOP)
    boText4.pack(side=TOP)
    boText5.pack(side=TOP)
    boClickButton.pack(side=TOP)


def bo11Click(event):
    boPage11()


def boPage11():
    updatePageNumber(11)

"""
boOptionButton.config(command=lambda: bo7Click(True))
boClickButton.config(command=lambda: bo7Click(False))
"""



brandonText1 = Label(textFrame, font=brandonFont)
brandonText2 = Label(textFrame, font=brandonFont)
brandonText3 = Label(textFrame, font=brandonFont)
brandonText4 = Label(textFrame, font=brandonFont)
brandonText5 = Label(textFrame, font=brandonFont)
brandonClickButton = Button(textFrame, font=brandonFont)
brandonOptionButton = Button(textFrame, font=brandonFont)

score = 0

def brandonPage4():
    updatePageNumber(4)

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()
    overviewButton.destroy()

    brandonText1.config(text="Your name is Brandon. You are a 28 year old Korean American")
    brandonText2.config(text="You work in marketing at a magazine called Metropol")
    brandonText3.config(text="You have a boyfriend named Gil, who also happens to be your boss")
    brandonText4.config(text="Your favorite TV show is a detective show from the 80s called Raider")
    brandonText5.config(text="The day before our story starts there was a blackout of the whole east coast")
    brandonClickButton.config(text="Continue")
    brandonClickButton.bind("<Button-1>", brandon5Click)
    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonText5.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon5Click(event):
    brandonPage5()
def brandonPage5():
    updatePageNumber(5)
    brandonText1.config(text="You wake up next to Gil. As you get up Gil begs you to go back to sleep.")
    brandonText2.config(text="You start getting ready and Gil asks you if you want any breakfast")
    brandonText3.config(text="You remind him that you will be late if you have breakfast. He starts to protest.")
    brandonText4.config(text="You are thinking about your plans for the rest of the day, like going to the gym after work")
    brandonText5.config(text="One last time Gil begs you to stay")
    brandonClickButton.config(text="Go To Work")
    brandonOptionButton.config(text="Stay With Gil")
    brandonClickButton.bind("<Button-1>", brandon6Click)
    brandonOptionButton.bind("<Button-1>", brandon6Option)
    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonText5.pack(side=TOP)
    brandonClickButton.pack(side=TOP)
    brandonOptionButton.pack(side=TOP)


def brandon6Click(event):
    brandonPage6()


def brandon6Option(event):
    brandonPage6B()


def brandonPage6():
    updatePageNumber(6)
    brandonOptionButton.forget()
    brandonText1.config(text="You leave for work, taking the trash out with you. You arrive at the building where Metropol's offices are")
    brandonText2.config(text="In the elevator you run into a woman that you work with. You can't remember her name, is it Lee(?)")
    brandonText3.config(text="Gil calls you into his office. He tells you that Metropol had been bought out and the whole marketing departmet is being fired")
    brandonText4.config(text="Gil: I know it's tough so close to Christmas. They can give you 8 weeks severance pay | He hands you an envelope with a letter and a check")
    brandonText5.config(text="Gil tries to offer comfort but you don't want to hear it. You pack up your things and leave your office for the last time")
    brandonClickButton.config(text="Leave")
    brandonClickButton.bind("<Button-1>", brandon7Click)
    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonText5.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandonPage6B():
    updatePageNumber(6)

    brandonOptionButton.forget()
    brandonText1.config(text="You stay with Gil as he makes breakfast. He starts to talk about work which you usually try to avoid")
    brandonText2.config(text="Gil: Metropol is being bought by another company. We are having to lay off a lot of employees")
    brandonText3.config(text="You realize what he is saying as he rummages through his briefcase and pulls out a piece of paper")
    brandonText4.config(text="Gil: I wanted to tell you before so that you were prepared. Management has prepared severance checks")
    brandonText5.config(text="This was not the path of the book, so you will return to the story as intended")
    brandonClickButton.config(text="Return To Story")
    brandonClickButton.bind("<Button-1>", )
    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonText5.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


def brandon7Click(event):
    brandonPage7()


def brandonPage7():
    updatePageNumber(7)

    brandonText1.config(text="After you leave the office building you go into the first expensive store you can find")
    brandonText2.config(text="You are greeted by a girl holding at least 10k worth of scarves. She introduces herself as Min")
    brandonText3.config(text="Min, what do you sell most of here? | She tells you about their wallets, but what you really need is a bag for the stuff from your desk")
    brandonText4.config(text="She shows you a wall of bags and picks out a beltbag for you. Though it looks like a fanny pack she assures you its in fashion")
    brandonText5.config(text="You use your severance check to pay for the bag. Min notices the TERMINATION label and tells you about the boots she bought after a breakup")
    brandonClickButton.config(text="Ask Her Out")
    brandonOptionButton.config(text="Don't Ask Her Out")
    brandonClickButton.bind("<Button-1>", brandon8Click)
    brandonOptionButton.bind("<Button-1>", brandon8Option)
    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonText5.pack(side=TOP)
    brandonClickButton.pack(side=TOP)
    brandonOptionButton.pack(side=TOP)


def brandon8Click(event):
    brandonText1.config(text="I'm sorry your boyfriend broke up with you. Do you want to get dinner with me tonight?")
    brandonText2.config(text="Min thinks for a while but eventually says no")
    brandonPage8()


def brandon8Option(event):
    brandonText1.config(text="I'm sorry your boyfriend broke up with you.")
    brandonText2.config(text="Min: Thanks")
    brandonPage8()


def brandonPage8():
    updatePageNumber(8)

    brandonOptionButton.forget()
    brandonText3.config(text="You leave the boutique. You start to get wrapped up in your own thoughts. What was the blackout last night?")
    brandonText4.config(text="Where are you gonna go after this? Home doesn't feel right. Maybe you'll walk around and listen to music")
    brandonText5.config(text="You press the button for the elevator. The door opens and you step inside. Suddenly you find yourself falling")
    brandonClickButton.config(text=". . .")
    brandonClickButton.bind("<Button-1>", )
    brandonText1.pack(side=TOP)
    brandonText2.pack(side=TOP)
    brandonText3.pack(side=TOP)
    brandonText4.pack(side=TOP)
    brandonText5.pack(side=TOP)
    brandonClickButton.pack(side=TOP)


blueText1 = Label(textFrame, font=blueFont)
blueText2 = Label(textFrame, font=blueFont)
blueText3 = Label(textFrame, font=blueFont)
blueText4 = Label(textFrame, font=blueFont)
blueText5 = Label(textFrame, font=blueFont)
blueClickButton = Button(textFrame, font=blueFont)
blueOptionButton = Button(textFrame, font=blueFont)
def bluePage4():
    updatePageNumber(4)

    namePrompt.destroy()
    characterPrompt.destroy()
    boButton.destroy()
    brandonButton.destroy()
    blueButton.destroy()
    overviewButton.destroy()

    blueText1.config(text="You are a 48 year old half-Korean man named Blue")
    blueText2.config(text="You lost the ability to speak at age 29 due to a stroke")
    blueText3.config(text="Years ago you worked for a company called Flux owned by Io Emsworth")
    blueText4.config(text="You are preparing to be a part of a TV special about Flux")
    blueText5.config(text="")
    blueClickButton.config(text="Continue")
    blueClickButton.bind("<Button-1>", blue5Click)
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def blue5Click(event):
    bluePage5()
def bluePage5():
    updatePageNumber(5)
    blueText1.config(text="You walk up to the freight entrance of a large glass tower downtown")
    blueText2.config(text="You are greeted by Tor - your contact from the tv studio -  and a young woman")
    blueText3.config(text="Assuming that the girl is an interpreter, you sign towards her, but she is confused")
    blueText4.config(text="Tor: We don't have an interpreter today. You won't need it soon anyways")
    blueText5.config(text="You follow them into an elevator, rocketting towards the top of the tower")
    blueClickButton.config(text="Top of Tower")
    blueClickButton.bind("<Button-1>", blue6Click)
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def blue6Click(event):
    bluePage6()


def bluePage6():
    updatePageNumber(6)
    blueText1.config(text="The plan for today is to get prepared for the interview and meet the light and makeup crew")
    blueText2.config(text="A young technician approaches you with a gun-like instrument. He cleans a spot on your neck")
    blueText3.config(text="Tech: Are you good with needles? | You shrug and he lines up the instrument with your neck.")
    blueText4.config(text="With a loud pop and a pinch a device was implanted in your neck.")
    blueText5.config(text="The technician tells you to repeat after him: I've seen things you people wouldn't believe")
    blueClickButton.config(text="I've seen things you people wouldn't believe")
    blueClickButton.bind("<Button-1>", blue7Click)
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def blue7Click(event):
    bluePage7()


def bluePage7():
    updatePageNumber(7)
    blueText1.config(text="For the first time in 20 years you can speak. It is not the voice you remember, and the implant vibrates as you talk")
    blueText2.config(text="The tech has you repeat a few more phrases. He tells you it is a short term implant that will disengage in a month")
    blueText3.config(text="Once you finish up and move on to makeup, the tech asks you about meeting Io Emsworth")
    blueText4.config(text="Thinking back to your time at Flux, you tell him that you only met her once or twice")
    blueText5.config(text="Tor reappears and walks over to you")
    blueClickButton.config(text="Talk to Tor")
    blueOptionButton.config(text="Learn more about Flux")
    blueClickButton.bind("<Button-1>", blue8Click)
    blueOptionButton.bind("<Button-1>", blue8Option)
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)
    blueOptionButton.pack(side=TOP)

def blue8Click(event):
    bluePage8()

def blue8Option(event):
    bluePage8B()


def bluePage8B():
    updatePageNumber(8)
    blueOptionButton.forget()
    blueText1.config(text="Flux was an energy company founded by 25 year old Io Emsworth.")
    blueText2.config(text="She had come up with an idea for perpetual energy.")
    blueText3.config(text="One of Flux's Lifetime batteries could power a device for longer than the life of the hardware itself")
    blueText4.config(text="It all came crashing down after multiple employees died due to Flux's experiments")
    blueText5.config(text="You were lucky enough to survive, and went on to testify against her in court.")
    blueClickButton.config(text="")
    blueClickButton.bind("<Button-1>", blue8Click)
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def bluePage8():
    updatePageNumber(8)
    blueOptionButton.forget()
    blueText1.config(text="You ask Tor: Why couldn't we use an interpreter? | Tor tells you that ASL interpreters kill engagement")
    blueText2.config(text="The makeup team buzzes around you for an hour, getting rid of the gray hairs and a scar above your eye")
    blueText3.config(text="They pitch a fit when Tor explains that they will have to do it all out of a van on site.")
    blueText4.config(text="In a few days you are going to walk through Flux Headquarters with the cameras and tell your stories")
    blueText5.config(text="Tor tells you that they will pick you up the day after Christmas to take you to F1. With that you are free to go")
    blueClickButton.config(text="Head Home")
    blueClickButton.bind("<Button-1>", blue9Click)
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def blue9Click(event):
    bluePage9()


def bluePage9():
    updatePageNumber(9)
    blueText1.config(text="You call your daughter as you leave. At first you don't speak")
    blueText2.config(text="After a moment she asks: Care to explain the point of calling me?")
    blueText3.config(text="In her whole life you have never called her, as there is no point when you can't speak")
    blueText4.config(text="You respond: Just wanted you to hear me before I come by")
    blueText5.config(text="She tells you to pick up some cognac before coming over for dinner tonight, and hangs up.")
    blueClickButton.config(text="Continue")
    blueClickButton.bind("<Button-1>", )
    blueText1.pack(side=TOP)
    blueText2.pack(side=TOP)
    blueText3.pack(side=TOP)
    blueText4.pack(side=TOP)
    blueText5.pack(side=TOP)
    blueClickButton.pack(side=TOP)


def blue10Click(event):
    bluePage10()


def bluePage10():
    updatePageNumber(10)


# Overview

authorButton = Button(buttonFrame, text="Author", font=overviewFont)
themeButton = Button(buttonFrame, text="Theme", font=overviewFont)

overviewText1 = Label(artFrame, font=overviewFont)
overviewText2 = Label(artFrame, font=overviewFont)
overviewText3 = Label(artFrame, font=overviewFont)
overviewText4 = Label(artFrame, font=overviewFont)
overviewText5 = Label(artFrame, font=overviewFont)
overviewText6 = Label(artFrame, font=overviewFont)
overviewText7 = Label(artFrame, font=overviewFont)
overviewText8 = Label(artFrame, font=overviewFont)
overviewText9 = Label(artFrame, font=overviewFont)
overviewText10 = Label(artFrame, font=overviewFont)
overviewText11 = Label(artFrame, font=overviewFont)
overviewText12 = Label(artFrame, font=overviewFont)
overviewText13 = Label(artFrame, font=overviewFont)
overviewText14 = Label(artFrame, font=overviewFont)
overviewText15 = Label(artFrame, font=overviewFont)


def overviewMainPage():
    namePrompt.destroy()
    characterPrompt.destroy()
    overviewButton.destroy()

    authorButton.grid(row=0, column=0)
    themeButton.grid(row=0, column=2)
    boButton.grid(row=1, column=0)
    brandonButton.grid(row=1, column=1)
    blueButton.grid(row=1, column=2)

    authorButton.bind("<Button-1>", authorOverview)
    themeButton.bind("<Button-1>", themeOverview)
    boButton.bind("<Button-1>", boOverview)
    brandonButton.bind("<Button-1>", brandonOverview)
    blueButton.bind("<Button-1>", blueOverview)


def authorOverview(event):
    overviewText1.config(text="")
    overviewText2.config(text="")
    overviewText3.config(text="")
    overviewText4.config(text="")
    overviewText5.config(text="")
    overviewText6.config(text="Jinwoo Chong is an Asian American author living in New York")
    overviewText7.config(text="He has written many short stories, but Flux was his first novel")
    overviewText8.config(text="Chong has a masters from Columbia University")
    overviewText9.config(text="There is very little information about Chong that I was able to find")
    overviewText10.config(text="")
    overviewText11.config(text="")
    overviewText12.config(text="")
    overviewText13.config(text="")
    overviewText14.config(text="")
    overviewText15.config(text="")

    overviewText1.pack()
    overviewText2.pack()
    overviewText3.pack()
    overviewText4.pack()
    overviewText5.pack()
    overviewText6.pack()
    overviewText7.pack()
    overviewText8.pack()
    overviewText9.pack()
    overviewText10.pack()
    overviewText11.pack()
    overviewText12.pack()
    overviewText13.pack()
    overviewText14.pack()
    overviewText15.pack()


def themeOverview(event):
    overviewText1.config(text="With three stories there are many themes present in this book")
    overviewText2.config(text="But the thing they all have in common is the human response to trauma")
    overviewText3.config(text="")
    overviewText4.config(text="Bo responds to the loss of his mother in my opinion better than his family")
    overviewText5.config(text="While Bo wants to have an open dialogue about his mom, his dad")
    overviewText6.config(text="refuses to talk about her and his brother pretends she never died")
    overviewText7.config(text="")
    overviewText8.config(text="When Brandon loses his job, he immediately tries to spend his trauma away")
    overviewText9.config(text="by buying an expensive bag with his severance check.")
    overviewText10.config(text="He then suffers a second trauma of falling down an elevator")
    overviewText11.config(text="He accepts a sketchy job from a guy that rescues him")
    overviewText12.config(text="")
    overviewText13.config(text="Blue's trauma happened to him 20 years in the past, but he finally deals")
    overviewText14.config(text="with it by using a TV interview to get back into F1 to drink 1% milk")
    overviewText15.config(text="to travel back in time to stop the initial trauma that defined his life")

    overviewText1.pack()
    overviewText2.pack()
    overviewText3.pack()
    overviewText4.pack()
    overviewText5.pack()
    overviewText6.pack()
    overviewText7.pack()
    overviewText8.pack()
    overviewText9.pack()
    overviewText10.pack()
    overviewText11.pack()
    overviewText12.pack()
    overviewText13.pack()
    overviewText14.pack()
    overviewText15.pack()


def boOverview(event):
    overviewText1.config(text="Bo is an 8 year old boy growing up in the early 2000's")
    overviewText2.config(text="He is half Korean from his Mom's side")
    overviewText3.config(text="He has a 4 year old brother named Kaz")
    overviewText4.config(text="")
    overviewText5.config(text="After losing his mother in a tragic accident, Bo finds himself")
    overviewText6.config(text="at odds with his father and brother over how to deal with the loss")
    overviewText7.config(text="His dad refuses to talk about their mom, while his brother is continuing")
    overviewText8.config(text="on as if she never went away.")
    overviewText9.config(text="")
    overviewText10.config(text="Eventually Bo snaps, yelling at his brother that their mom is dead")
    overviewText11.config(text="His dad grounds him and Bo runs away. He ends up running so far he gets lost")
    overviewText12.config(text="He falls and seriously injures his hand, and has no idea how to get home")
    overviewText13.config(text="")
    overviewText14.config(text="Bo is rescued by what appears to be the main character of Raider")
    overviewText15.config(text="Raider takes him home and he is taken to the hospital")

    overviewText1.pack()
    overviewText2.pack()
    overviewText3.pack()
    overviewText4.pack()
    overviewText5.pack()
    overviewText6.pack()
    overviewText7.pack()
    overviewText8.pack()
    overviewText9.pack()
    overviewText10.pack()
    overviewText11.pack()
    overviewText12.pack()
    overviewText13.pack()
    overviewText14.pack()
    overviewText15.pack()


def brandonOverview(event):
    overviewText1.config(text="Brandon is a 28 year old Korean American man in our modern day")
    overviewText2.config(text="He worked for a magazine, but he got fired")
    overviewText3.config(text="")
    overviewText4.config(text="He spends his severance pay on a bag at a boutique where he meets Min")
    overviewText5.config(text="")
    overviewText6.config(text="After buying the bag he falls down an elevator shaft")
    overviewText7.config(text="")
    overviewText8.config(text="When he wakes up he meets Lev who gets him a job for a tech startup")
    overviewText9.config(text="")
    overviewText10.config(text="This startup is Flux, founded by Io Emsworth who had come up with an")
    overviewText11.config(text="idea for perpetual energy. After working for Flux for a while he")
    overviewText12.config(text="finds out that the perpetual energy was actually time travel")
    overviewText13.config(text="")
    overviewText14.config(text="Flux's research ends up killing 3 people and causes you to have")
    overviewText15.config(text="a stroke that puts you in a coma and you lose the ability to speak")

    overviewText1.pack()
    overviewText2.pack()
    overviewText3.pack()
    overviewText4.pack()
    overviewText5.pack()
    overviewText6.pack()
    overviewText7.pack()
    overviewText8.pack()
    overviewText9.pack()
    overviewText10.pack()
    overviewText11.pack()
    overviewText12.pack()
    overviewText13.pack()
    overviewText14.pack()
    overviewText15.pack()


def blueOverview(event):
    overviewText1.config(text="Blue is a 48 year old half-Korean man about 20 years in the future")
    overviewText2.config(text="He has a daughter named Jem with his ex-wife Min")
    overviewText3.config(text="")
    overviewText4.config(text="20 years ago Blue worked for an energy company named Flux")
    overviewText5.config(text="Flux's research into perpetual energy ended up killing 3 people")
    overviewText6.config(text="and caused Blue to have a stroke that took away his ability to speak")
    overviewText7.config(text="")
    overviewText8.config(text="Blue agrees to do a TV special about Flux to get himself into F1,")
    overviewText9.config(text="Flux's headquarters where he used to work")
    overviewText10.config(text="The special arranges for him to get an implant to let him speak")

    """
    overviewText11.config(text="")
    overviewText12.config(text="During the interview he gets into his old office to get the 1% milk")
    overviewText13.config(text="that lets him travel through time back to save his mother")
    overviewText14.config(text="He gets stuck in the past knowing he has broken the loop")
    overviewText15.config(text="")
    """
    overviewText11.config(text="")
    overviewText12.config(text="")
    overviewText13.config(text="")
    overviewText14.config(text="")
    overviewText15.config

    overviewText1.pack()
    overviewText2.pack()
    overviewText3.pack()
    overviewText4.pack()
    overviewText5.pack()
    overviewText6.pack()
    overviewText7.pack()
    overviewText8.pack()
    overviewText9.pack()
    overviewText10.pack()
    overviewText11.pack()
    overviewText12.pack()
    overviewText13.pack()
    overviewText14.pack()
    overviewText15.pack()


window.mainloop()
