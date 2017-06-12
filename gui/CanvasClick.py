import tkinter as tk
from tkinter.ttk import *
from tkinter import StringVar

LARGE_FONT = ("Verdana", 14)



class CanvasClick(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Setup basic variables
        self.canvas_width = 800
        self.canvas_height = 500
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        frame = Frame(container)
        frame.grid(row=1, column=0, sticky="s")
        self.canvas = tk.Canvas(frame, width=self.canvas_width, height=self.canvas_height)
        self.canvas.bind("<B1-Motion>", self.track_and_draw_line)
        self.canvas.bind("<Button-1>", self.draw_circle)
        self.canvas.bind("<Button-2>", self.draw_cross)
        self.canvas.pack()

        self.x1y1 = (-1,-1)
        self.x2y2 = (-1,-1)

    def track_and_draw_line(self, event):
        if self.x1y1[0] == -1 and self.x2y2[0] == -1:
            self.x1y1 = (event.x, event.y)
        else:
            self.x2y2 = (event.x, event.y)
            self.draw_line_and_reset_coordinates()

    def draw_line_and_reset_coordinates(self):
        self.canvas.create_line(self.x1y1, self.x2y2)
        self.x1y1 = (-1, -1)
        self.x2y2 = (-1, -1)

    def draw_circle(self, event):
        print("o drawn at ("+str(event.x)+","+str(event.y)+")")
        self.canvas.create_oval(event.x, event.y, event.x + 20, event.y + 20, fill="green")



    def draw_cross(self, event):
        print("x drawn at ("+str(event.x)+","+str(event.y)+")")
        self.canvas.create_line(event.x, event.y, event.x + 20, event.y + 20, fill="red")
        self.canvas.create_line(event.x, event.y + 20, event.x + 20, event.y, fill="red")


app = CanvasClick()
app.title("Events")
app.mainloop()
