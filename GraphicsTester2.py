from tkinter import *
root =Tk()
root.geometry("800x800")

frame_image = Frame(root)
frame_image.pack(side=TOP, fill="x")

frame_image.picture = PhotoImage(file="C:\FluxGame\MarioFanArt.png")
frame_image.label = Label(frame_image, image=frame_image.picture)
frame_image.label.pack()

button = Button(frame_image, text="Button")
button.pack()

mainloop()