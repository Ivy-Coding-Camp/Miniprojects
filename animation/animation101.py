import tkinter as tk
from tkinter.ttk import *
import random


LARGE_FONT = ("Verdana", 14)

class Animation101(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        frame = Frame(container)
        frame.grid(row=1, column=0, sticky="s")
        self.canvas = tk.Canvas(frame, width=500, height=500)
        self.canvas.pack()
        self.x = 200
        self.y = 200
        size = 20
        self.red_circle = self.draw_circle(self.x, self.y, size, "red")
        self.blue_circle = self.draw_circle(self.x+20, self.y+20, size+5, "blue")
        self.orange_circle = self.draw_circle(self.x+20, self.y+20, size+10, "orange")
        self.green_circle = self.draw_circle(self.x+20, self.y+20, size+15, "green")
        self.canvas.after(0, self.animate_circles)

    def animate_circles(self):
        range = 2
        x1 = random.randint(-range, range)
        y1 = random.randint(-range, range)
        x2 = random.randint(-range, range)
        y2 = random.randint(-range, range)
        x3 = random.randint(-range, range)
        y3 = random.randint(-range, range)
        x4 = random.randint(-range, range)
        y4 = random.randint(-range, range)
        self.canvas.move(self.red_circle, x1, y1)
        self.canvas.move(self.blue_circle, x2, y2)
        self.canvas.move(self.orange_circle, x3, y3)
        self.canvas.move(self.green_circle, x4, y4)
        # self.canvas.update()
        self.canvas.after(10, self.animate_circles)

    def draw_circle(self, x, y, size, color):
        return self.canvas.create_oval(x, y, x + size, y + size, fill=color)

app = Animation101()
app.title("Crazy balls")
app.mainloop()