from tkinter import *


window = Tk()
window.title("Graphics")
window.geometry("800x600")
canvas = Canvas(window)
canvas.pack(fill=BOTH, expand=1)

image = Frame(window)
image.pack()
image.picture = PhotoImage(file="C:\FluxGame\MarioFanArt.png")

width = window.winfo_width()
height = window.winfo_height()
print(window.winfo_geometry())

print(width)
print(height)

x1 = 0
y1 = 400
x2 = 800
y2 = 400

canvas.create_line(x1, y1, x2, y2, width=5)

window.mainloop()