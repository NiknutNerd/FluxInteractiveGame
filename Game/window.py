from tkinter import *
screen = 0

window = Tk()
window.title("Flux Interactive Game")
window.geometry("800x600")

window.update()
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()

artFrame = Frame(window, width=800, height=400)
textFrame = Frame(window)

artFrame.pack()
textFrame.pack()



"""
canvas = Canvas(artFrame, height=400, width=800)
canvas.pack(fill=BOTH, expand=1)


img = PhotoImage(file="C:\FluxGame\Tester.png")
canvas.create_image(400, 200, image=img)
"""
"""
canvas = Canvas(artFrame, height=400, width=800)
canvas.pack(fill=BOTH, expand=1)
def makeImage(image):
    img = PhotoImage(file=image)
    canvas.create_image(400, 200, image=img)
    
"""
"""
artFrame.picture = PhotoImage(file="C:\FluxGame\Tester.png")
artFrame.label = Label(artFrame, image=artFrame.picture)
artFrame.label.pack()
"""

def makeImage(image):
    artFrame.picture = PhotoImage(file=image)
    artFrame.label = Label(artFrame, image=artFrame.picture)
    artFrame.label.pack()

nextButton = Button(text="Next ->")
nextButton.place(x=(800 - nextButton.winfo_reqwidth()), y=(600 - nextButton.winfo_reqheight()))

makeImage("C:\FluxGame\Tester.png")
def nameClicked():
    name = nameEntry.get()
    nameEntry.destroy()
    nameButton.destroy()
    namePrompt.config(text=("Welcome to Flux, " + name))

namePrompt = Label(textFrame, text="Enter Player Name: ")
nameEntry = Entry(textFrame)
nameButton = Button(textFrame, text="Enter", command=nameClicked)

namePrompt.pack(side=TOP)
nameEntry.pack(side=TOP)
nameButton.pack(side=TOP)

window.mainloop()
