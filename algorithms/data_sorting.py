import tkinter as tk
from tkinter.ttk import *
import time

LARGE_FONT = ("Verdana", 14)

class SortingAnimator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.canvas_width = 1200
        self.canvas_height = 500

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.listValues = tk.StringVar()
        self.listValues.set("")

        tk.Entry(container, width=20, textvariable=self.listValues, justify='right').grid(row=0, column=0, sticky="n")
        tk.Button(container, text="bubble sort", command=lambda: self.bubble_sort()).grid(row=0, column=1, sticky="n")
        tk.Button(container, text="merge sort", command=lambda: self.merge_sort()).grid(row=1, column=1, sticky="n")
        tk.Button(container, text="quick sort", command=lambda: self.quick_sort()).grid(row=2, column=1, sticky="n")

        frame = Frame(container)
        frame.grid(row=3, column=0, sticky="s")
        self.canvas = tk.Canvas(frame, width=self.canvas_width, height=self.canvas_height)

        self.shapes = list()

        self.canvas.pack()

    # Sorting algorithms
    # Bubble sort -start
    def bubble_sort(self):
        self.organize_data()
        swapped = False
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.swap(self.data[j], self.data[j + 1])
                    self.swap_shapes(j, j+1)
                    swapped = True

            if not swapped:
                break

        print("After bubble sort: "+str(self.data))
    # Bubble sort - end

    # Merge sort - start
    def merge_sort(self):
        self.organize_data()
        self.data = self.merge_sort_subset(self.data)
        print("After merge sort: "+str(self.data))

    def merge_sort_subset(self, data_list):
        print(str(data_list))
        if len(data_list) <= 1:
            return data_list
        list1 = self.merge_sort_subset(data_list[:(len(data_list)//2)])
        list2 = self.merge_sort_subset(data_list[(len(data_list)//2):])
        return self.merge_lists(list1, list2)

    def merge_lists(self, list1, list2):
        result =  list()

        while len(list1) > 0 and len(list2) > 0:
            if list1[0] > list2[0]:
                result.append(list2[0])
                list2 = list2[1:]
            else:
                result.append(list1[0])
                list1 = list1[1:]

        while len(list1) > 0:
            result.append(list1[0])
            list1 = list1[1:]

        while len(list2) > 0:
            result.append(list2[0])
            list2 = list2[1:]

        self.reorder_shapes(result)
        return result
    # Merge sort - end

    # Quick sort - start
    def quick_sort(self):
        self.organize_data()
        self.quick_sort_subset(0, len(self.data) - 1)
        print("After quick sort: "+str(self.data))

    def quick_sort_subset(self, left, right):
        if right - left <= 0:
            return
        else:
            pivot = self.data[right]
            partition = self.partition(left, right, pivot)
            self.quick_sort_subset(left, partition - 1)
            self.quick_sort_subset(partition + 1, right)

    def partition(self, left, right, pivot_value):
        left_index = left
        right_index = right - 1

        while True:
            while self.data[left_index] < pivot_value:
                left_index += 1

            while right_index > 0 and self.data[right_index] > pivot_value:
                right_index -= 1

            if left_index >= right_index:
                break
            else:
                # Swap left and right index
                self.data[left_index], self.data[right_index] = self.swap(self.data[left_index], self.data[right_index])
                self.swap_shapes(left_index, right_index)
                time.sleep(1)

        self.data[left_index], self.data[right] = self.swap(self.data[left_index], self.data[right])
        self.swap_shapes(left_index, right)
        return left_index

    def swap(self, left, right):
        tmp = left
        left = right
        right = tmp
        return left, right

    # Quick sort - end

    def draw_rectangle(self, x, y, length, breadth, color):
        return self.canvas.create_rectangle(x, y, x + length, y + breadth, fill=color)

    def swap_shapes(self, i, j):
        self.canvas.itemconfigure(self.shapes[i], text=str(self.data[i]), fill="red")
        self.canvas.itemconfigure(self.shapes[j], text=str(self.data[j]), fill="red")
        self.canvas.update()
        time.sleep(0.225)
        self.canvas.itemconfigure(self.shapes[i], fill="black")
        self.canvas.itemconfigure(self.shapes[j], fill="black")
        self.canvas.update()

    def reorder_shapes(self, sub_list):
        for i in range(len(sub_list)):
            self.canvas.itemconfigure(self.shapes[i], text=str(sub_list[i]), fill="red")
            self.canvas.update()
            time.sleep(0.225)
            self.canvas.itemconfigure(self.shapes[i], fill="black")
            self.canvas.update()

    def organize_data(self):
        self.data = self.listValues.get().split()

        try:
            self.data = [int(val) for val in self.data]
        except:
            print("Data is non-numeric..")

        # curate the data - convert them to numbers

        print(self.data)

        # Initialize the canvas
        self.canvas.delete("all")
        del self.shapes[:]
        xspan = self.canvas_width - 50
        cell_xspan = xspan / len(self.data)

        xval = cell_xspan/2 + 5
        yval = 100

        for i in range(len(self.data)):
            self.draw_rectangle(xval - cell_xspan/2, yval - 20, cell_xspan - 5, 40, color="white")
            shape = self.canvas.create_text(xval, yval, text=str(self.data[i]), fill="black")
            self.shapes.append(shape)
            xval += cell_xspan


app = SortingAnimator()
app.title("Sorting")
app.mainloop()
