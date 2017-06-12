import tkinter as tk
from tkinter.ttk import *
from tkinter import StringVar

LARGE_FONT = ("Verdana", 14)

class CalculatorGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.calculatorInputValue = StringVar()
        self.calculatorInputValue.set("0")

        frame = Frame(container)
        frame.grid(row=1, column=0, sticky="s")

        #----Define components
        tk.Entry(container, width=20, textvariable=self.calculatorInputValue, justify='right').grid(row=0, column=0, sticky="n")

        #---Row 1 Buttons
        tk.Button(frame, text="7", command=lambda: self.set_value("7", False)).grid(row=0, column=0)
        tk.Button(frame, text="8", command=lambda: self.set_value("8", False)).grid(row=0, column=1)
        tk.Button(frame, text="9", command=lambda: self.set_value("9", False)).grid(row=0, column=2)
        tk.Button(frame, text="+", command=lambda: self.set_operand1_and_operator("+")).grid(row=0, column=3)
        tk.Button(frame, text='MOD', command=lambda: self.set_operand1_and_operator("%")).grid(row=0, column=4)

        #---Row 2 Buttons
        tk.Button(frame, text="4", command=lambda: self.set_value("4", False)).grid(row=1, column=0)
        tk.Button(frame, text="5", command=lambda: self.set_value("5", False)).grid(row=1, column=1)
        tk.Button(frame, text="6", command=lambda: self.set_value("6", False)).grid(row=1, column=2)
        tk.Button(frame, text="-", command=lambda: self.set_operand1_and_operator("-")).grid(row=1, column=3)
        tk.Button(frame, text='x ^ y', command=lambda: self.set_operand1_and_operator("^")).grid(row=1, column=4)

        #---Row 3 Buttons
        tk.Button(frame, text="1", command=lambda: self.set_value("1", False)).grid(row=2, column=0)
        tk.Button(frame, text="2", command=lambda: self.set_value("2", False)).grid(row=2, column=1)
        tk.Button(frame, text="3", command=lambda: self.set_value("3", False)).grid(row=2, column=2)
        tk.Button(frame, text="x", command=lambda: self.set_operand1_and_operator("x")).grid(row=2, column=3)
        tk.Button(frame, text="=", command=lambda: self.set_operand2_and_evaluate()).grid(row=2, column=4)

        #---Row 4 Buttons
        tk.Button(frame, text="0", command=lambda: self.set_value("0", False)).grid(row=3, column=0)
        tk.Button(frame, text=".", command=lambda: self.set_value(".", False)).grid(row=3, column=1)
        tk.Button(frame, text="C", command=lambda: self.set_value("0", True)).grid(row=3, column=2)
        tk.Button(frame, text='/', command=lambda: self.set_operand1_and_operator("/")).grid(row=3, column=3)

        container.tkraise()

    def set_value(self, value, clear_entry):
        if self.calculatorInputValue.get() == "0" and value != ".":
            clear_entry = True

        if "." in self.calculatorInputValue.get() and value == ".":
            return

        if clear_entry or self.clear_value:
            self.calculatorInputValue.set(value)
            self.clear_value = False
        else:
            self.calculatorInputValue.set(self.calculatorInputValue.get() + value)

    def set_operand1_and_operator(self, op):
        self.operand1 = float(self.calculatorInputValue.get())
        self.operator = op
        self.clear_value = True

    def set_operand2_and_evaluate(self):
        self.operand2 = float(self.calculatorInputValue.get())

        try:
            if self.operator == 'x':
                self.calculatorInputValue.set(self.operand1 * self.operand2)
            elif self.operator == '/':
                self.calculatorInputValue.set(self.operand1 / self.operand2)
            elif self.operator == '%':
                self.calculatorInputValue.set(self.operand1 % self.operand2)
            elif self.operator == '+':
                self.calculatorInputValue.set(self.operand1 + self.operand2)
            elif self.operator == '-':
                self.calculatorInputValue.set(self.operand1 - self.operand2)
            elif self.operator == '^':
                self.calculatorInputValue.set(self.operand1 ** self.operand2)

        except:
            self.calculatorInputValue.set('Error')

        self.operand1 = 0
        self.operand2 = 0
        self.operator = ''



app = CalculatorGUI()
app.title("Calculator")
app.mainloop()
