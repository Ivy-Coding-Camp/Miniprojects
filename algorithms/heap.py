import tkinter as tk
from tkinter.ttk import *
import time

LARGE_FONT = ("Verdana", 14)

class HeapAnimator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.canvas_width = 1200
        self.canvas_height = 500
        # self.heap_root = HeapNode.populate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        # self.heap_root = HeapNode(6, left=HeapNode(7, left=HeapNode(10), right=HeapNode(15)), right=HeapNode(12, left=HeapNode(17)))
        self.data = list()

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.listValues = tk.StringVar()
        self.listValues.set("")

        tk.Entry(container, width=20, textvariable=self.listValues, justify='right').grid(row=0, column=0, sticky="n")
        tk.Button(container, text="visualize", command=lambda: self.visualize()).grid(row=0, column=1, sticky="n")
        tk.Button(container, text="max heap", command=lambda: self.max_heap()).grid(row=1, column=1, sticky="n")

        frame = Frame(container)
        frame.grid(row=3, column=0, sticky="s")
        self.canvas = tk.Canvas(frame, width=self.canvas_width, height=self.canvas_height)

        self.shapes = list()

        self.canvas.pack()

    def visualize(self):
        self.canvas.delete("all")
        self.data = self.listValues.get().split()
        self.heap_root = HeapNode.populate(self.data)
        self.heap_root.draw(self.canvas, self.heap_root, 200, 100)
        self.canvas.update()


    # def buildheap(self):
    #     k = len(self.data)//2
    #     while k > 0:
    #         print()
    #
    # def percolatingdown(self, k):
    #     tmp = self.data[k]
    #     k = 0
    #     child = 0
    #     while k <= len(self.data):
    #         child = 2*k
    #         if


class HeapNode:
    def __init__(self, value, *args, **kwargs):
        self.value = value
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)

    def level(self, child):
        if child == self:
            return 1
        elif child == self.left or child == self.right:
            return 2
        elif self.left is not None:
            return self.level(self) + self.left.level(child)
        elif self.right is not None:
            return self.level(self) + self.right.level(child)
        else:
            return 0


    @staticmethod
    def populate(data):
        if len(data) == 0:
            return None
        elif len(data) == 1:
            return HeapNode.populate2(data[0], None, None)
        elif len(data) == 2:
            return HeapNode.populate2(data[0], HeapNode(data[1]), None)
        elif len(data) == 3:
            return HeapNode.populate2(data[0], HeapNode(data[1]), HeapNode(data[2]))
        else:
            return HeapNode.populate2(data[0], HeapNode.populate(data[1:(len(data) // 2)]), HeapNode.populate(data[(len(data)//2):]))

    @staticmethod
    def populate2(rootval, left, right):
        print("rootval = "+str(rootval))
        result = HeapNode(rootval)
        print(str(result))
        if left is not None:
            result.left = left
        if right is not None:
            result.right = right
        return result

    def __str__(self):
        result = ""
        result += "("+str(self.value)
        if self.left is not None:
            result += ",("
            result += self.left.__str__()
            result += ")"
        if self.right is not None:
            result += ",("
            result += self.right.__str__()
            result += ")"
        result += ")"
        return result

    def draw(self, canvas, root, x, y):
        rootxy = (x,y)
        lxy = (x-(40 + 70/root.level(self)), y+40)
        rxy = (x+(40 + 70/root.level(self)), y+40)

        canvas.create_oval(rootxy[0], rootxy[1], rootxy[0]+20, rootxy[1]+20, fill="white")
        canvas.create_text(rootxy[0]+10, rootxy[1]+10, text=str(self.value))

        if self.left is not None:
            self.left.draw(canvas, root, lxy[0], lxy[1])
            canvas.create_line(x+10, y+20, lxy[0]+10, lxy[1])

        if self.right is not None:
            self.right.draw(canvas, root, rxy[0], rxy[1])
            canvas.create_line(x+10, y+20, rxy[0]+10, rxy[1])


app = HeapAnimator()
app.title("Heap visualization")
app.mainloop()
