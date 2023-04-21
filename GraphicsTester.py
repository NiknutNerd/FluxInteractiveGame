from tkinter import *
import random


window = Tk()
window.title("Graphics")
window.geometry("800x600")
canvas = Canvas(window)
canvas.pack(fill=BOTH, expand=1)

image = Frame(window)
image.pack()
image.picture = PhotoImage(file="C:\FluxGame\MarioFanArt.png")

window.update()
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


r = str(hex(random.randint(0, 255)))
g = str(hex(random.randint(0, 255)))
b = str(hex(random.randint(0, 255)))

r = r[2:]
g = g[2:]
b = b[2:]
#if length = 1, add a 0 in front

if len(r) == 1:
    r = "0" + r
if len(g) == 1:
    g = "0" + g
if len(b) == 1:
    b = "0" + b

rgb = "#" + r + g + b
print(rgb)

canvas.create_rectangle(0, 0, 100, 100, fill=rgb)

pixelSize = 8
for x1 in range(0, width, pixelSize):
    for y1 in range(0, 400, pixelSize):
        print(str(x1) + ", " + str(y1))

        r = str(hex(random.randint(0, 255)))
        g = str(hex(random.randint(0, 255)))
        b = str(hex(random.randint(0, 255)))

        r = r[2:]
        g = g[2:]
        b = b[2:]

        if len(r) == 1:
            r = "0" + r
        if len(g) == 1:
            g = "0" + g
        if len(b) == 1:
            b = "0" + b

        rgb = "#" + r + g + b
        print(rgb)

        print("x1, y1, x2, y2: " + str(x1) + ", " + str(y1) + ", " + str(x1 + pixelSize) + ", " + str(y1 + pixelSize))
        canvas.create_rectangle(x1, y1, (x1 + pixelSize), (y1 + pixelSize), fill=rgb)
        print("Rect created")


        """
        if y1 >= 100 and y1 < 200:
            r = str(hex(random.randint(0, 255)))
            g = str(hex(random.randint(0, 255)))
            b = str(hex(random.randint(0, 255)))

            r = r[2:]
            g = g[2:]
            b = b[2:]

            if len(r) == 1:
                r = "0" + r
            if len(g) == 1:
                g = "0" + g
            if len(b) == 1:
                b = "0" + b

            rgb = "#" + r + g + b
            print(rgb)

            print("x1, y1, x2, y2: " + str(x1) + ", " + str(y1) + ", " + str(x1 + pixelSize) + ", " + str(y1 + pixelSize))
            canvas.create_rectangle(x1, y1, (x1 + pixelSize), (y2 + pixelSize), fill=rgb)
            """
window.mainloop()