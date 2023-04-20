from tkinter import *

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

screen = 0

welcome = Label(window, text="Welcome to Flux!")
welcome.place(x=((windowWidth/2) - welcome.winfo_reqwidth()/2), y=((windowHeight)/2) - welcome.winfo_reqheight())

def startClick():
    welcome.destroy()

    canvas = Canvas(artFrame, height=400, width=800)
    canvas.pack(fill=BOTH, expand=1)

    img = PhotoImage(file="C:\FluxGame\Tester.png")
    canvas.create_image(400, 200, image=img)

    namePrompt = Label(textFrame, text="Enter Player Name: ")
    nameEntry = Entry(textFrame)
    nameButton = Button(textFrame, text="Enter")

    namePrompt.pack(side=TOP)
    nameEntry.pack(side=TOP)
    nameButton.pack(side=TOP)

startButton = Button(text="START")
startButton.place(x=(windowWidth-startButton.winfo_reqwidth()), y=(windowHeight-startButton.winfo_reqheight()))

"""
def nameClicked():
    name = nameEntry.get()
    nameEntry.destroy()
    nameButton.destroy()
    namePrompt.config(text=("Welcome to Flux, " + name))
"""



window.mainloop()