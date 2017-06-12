import tkinter as tk
from tkinter.ttk import *
import time


LARGE_FONT = ("Verdana", 14)

class Hanoi(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Setup basic variables
        self.canvas_width = 800
        self.canvas_height = 500
        self.number_of_disks = 9
        self.spindle_offset = 100   # how far apart the spindles need to be
        self.max_disk_length = 100  # what is the size of the biggest disk
        self.disk_differential = 5  # by how much do we decrease each disk's size (on each side) as we go up the stack
        self.disk_width = 10        # what is the thickness or width of each disk
        self.disk_color = "red"

        self.disks = list()         # this will contain the actual disk components to move around
        self.source = list()        # this is the representation of the source stack
        self.destination = list()
        self.auxiliary = list()

        self.initialize_stacks()

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        tk.Button(container, text="start", command=lambda: self.do_hanoi()).grid(row=0, column=0, sticky="n")
        tk.Button(container, text="reset", command=lambda: self.reset_canvas()).grid(row=0, column=1, sticky="n")

        frame = Frame(container)
        frame.grid(row=1, column=0, sticky="s")
        self.canvas = tk.Canvas(frame, width=self.canvas_width, height=self.canvas_height)
        self.draw_spindles()
        self.draw_stack()
        self.canvas.pack()

    def do_hanoi(self):
        self.reset_canvas()
        print("disks = "+str(self.disks))
        print("source = "+str(self.source))
        print("auxiliary = "+str(self.auxiliary))
        print("destination = "+str(self.destination))

        self.hanoi(self.source[len(self.source) - 1], self.source, self.destination, self.auxiliary)

        print("source = "+str(self.source))
        print("auxiliary = "+str(self.auxiliary))
        print("destination = "+str(self.destination))


    def initialize_stacks(self):
        # self.source.clear()
        # self.auxiliary.clear()
        # self.destination.clear()
        del self.source[:]
        del self.auxiliary[:]
        del self.destination[:]
        for i in range(self.number_of_disks):
            self.source.append(i)

    def hanoi(self, disk, src, dest, aux):
        if disk == 0:
            self.transfer_disk(disk, src, dest)
        else:
            self.hanoi(disk - 1, src, aux, dest)
            self.transfer_disk(disk, src, dest)
            self.hanoi(disk - 1, aux, dest, src)

    def transfer_disk(self, disk, src, dest):
        print("==============================================")
        print("disk = "+str(disk))
        self.move_disk(disk, src, dest)
        src.remove(disk)
        dest.insert(0, disk)

    def move_disk(self, disk_index, src, dest):
        d = self.disks[disk_index]
        xincr = 0
        if src == self.source and dest == self.destination:
            print("Moving "+str(disk_index)+" from source to destination")
            self.canvas.itemconfigure(self.move_msg, text="Moving from Source to Destination")
            xincr = 2*(self.max_disk_length + 50)
        elif src == self.auxiliary and dest == self.destination:
            print("Moving "+str(disk_index)+" from auxiliary to destination")
            self.canvas.itemconfigure(self.move_msg, text="Moving from Auxiliary to Destination")
            xincr = self.max_disk_length + 50
        elif src == self.destination and dest == self.auxiliary:
            print("Moving "+str(disk_index)+" from destination to auxiliary")
            self.canvas.itemconfigure(self.move_msg, text="Moving from Destination to Auxiliary")
            xincr = -(self.max_disk_length + 50)
        elif src == self.destination and dest == self.source:
            print("Moving "+str(disk_index)+" from destination to source")
            self.canvas.itemconfigure(self.move_msg, text="Moving from Destination to Source")
            xincr = -2*(self.max_disk_length + 50)
        elif src == self.source and dest == self.auxiliary:
            print("Moving "+str(disk_index)+" from source to auxiliary")
            self.canvas.itemconfigure(self.move_msg, text="Moving from Source to Auxiliary")
            xincr = self.max_disk_length + 50
        elif src == self.auxiliary and dest == self.source:
            print("Moving "+str(disk_index)+" from auxiliary to source")
            self.canvas.itemconfigure(self.move_msg, text="Moving from Auxiliary to Source")
            xincr = -(self.max_disk_length + 50)

        y_target_coords = self.canvas.coords(self.spindle1_base)[1] - self.disk_width * (len(dest) + 1)
        src_disk_coords = self.canvas.coords(d)

        print("Y-Coordinates of source = "+str(src_disk_coords[1]))
        print("Y-Coordinates of target = "+str(y_target_coords))

        yincr = y_target_coords - src_disk_coords[1]

        print("xincr = "+str(xincr))
        print("yincr = "+str(yincr))

        self.canvas.move(d, xincr, yincr)
        self.canvas.update()
        time.sleep(0.1)

    def reset_canvas(self):
        self.canvas.delete("all")
        self.initialize_stacks()
        self.draw_spindles()
        self.draw_stack()

    def draw_rectangle(self, x, y, length, breadth, color):
        return self.canvas.create_rectangle(x, y, x + length, y + breadth, fill=color)

    def draw_stack(self):
        # self.disks.clear()
        del self.disks[:]
        for i in range(self.number_of_disks):
            disk = self.draw_rectangle(self.spindle_offset + (i*self.disk_differential),
                                (self.canvas_width/10) + self.disk_width * (self.number_of_disks - i),
                                self.max_disk_length - 2*(i*self.disk_differential),
                                self.disk_width,
                                self.disk_color)
            self.disks.insert(0, disk)

    def draw_spindles(self):
        self.xh1 = self.spindle_offset - 10
        self.yh1 = (self.canvas_width/10) + self.disk_width * (self.number_of_disks + 1)

        self.xh2 = self.spindle_offset + self.max_disk_length + 10
        self.yh2 = (self.canvas_width/10) + self.disk_width * (self.number_of_disks + 1)

        self.xv1 = (2 * self.spindle_offset + self.max_disk_length) / 2
        self.yv1 = self.canvas_width / 10

        self.xv2 = (2 * self.spindle_offset + self.max_disk_length) / 2
        self.yv2 = (self.canvas_width / 10) + self.disk_width * (self.number_of_disks + 1)


        # Draw spindle 1 - src
        self.spindle1_base = self.canvas.create_line(self.xh1,
                                self.yh1,
                                self.xh2,
                                self.yh2,
                                fill="black")
        self.canvas.create_line(self.xv1,
                                self.yv1,
                                self.xv2,
                                self.yv2,
                                fill="black")
        self.canvas.create_text((self.xh1 + self.xh2)/2, self.yh1 + 10, text="Source")

        # Draw spindle 2 - aux
        self.spindle2_base = self.canvas.create_line(self.xh1 + self.max_disk_length + 50,
                                self.yh1,
                                self.xh2 + self.max_disk_length + 50,
                                self.yh2,
                                fill="black")
        self.canvas.create_line(self.xv1 + self.max_disk_length + 50,
                                self.yv1,
                                self.xv2 + self.max_disk_length + 50,
                                self.yv2,
                                fill="black")
        self.canvas.create_text((self.xh1 + self.xh2)/2 + (self.max_disk_length + 50), self.yh1 + 10, text="Auxiliary")

        #
        # # Draw spindle 3 - dest
        self.spindle3_base = self.canvas.create_line(self.xh1 + 2 * (self.max_disk_length + 50),
                                self.yh1,
                                self.xh2 + 2 * (self.max_disk_length + 50),
                                self.yh2,
                                fill="black")
        self.canvas.create_line(self.xv1 + 2 * (self.max_disk_length + 50),
                                self.yv1,
                                self.xv2 + 2 * (self.max_disk_length + 50),
                                self.yv2,
                                fill="black")
        self.canvas.create_text((self.xh1 + self.xh2)/2 + 2*(self.max_disk_length + 50), self.yh1 + 10, text="Destination")

        self.move_msg = self.canvas.create_text((self.xh1 + self.xh2)/2 + (self.max_disk_length + 50), self.yh1 + 50, text="")

app = Hanoi()
app.title("Hanoi")


app.mainloop()