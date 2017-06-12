from __future__ import print_function

import tkinter as tk
from tkinter.ttk import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import StringVar
from LoanMortgageCalculator import LoanMortgageCalculator

LARGE_FONT = ("Verdana", 14)


class LoanMortgageCalculatorGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = InputPage(container, self)

        self.frames[InputPage] = frame

        frame.grid(row=0, column=0, sticky="news")

        self.show_frame(InputPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class InputPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        tk.Label(self, text="Loan amount: $", font=LARGE_FONT).grid(row=0, column=0,  sticky="NW")
        tk.Label(self, text="Down-payment amount: $", font=LARGE_FONT).grid(row=1, column=0, sticky="NW")
        tk.Label(self, text="Interest rate: (%)", font=LARGE_FONT).grid(row=2, column=0, sticky="NW")
        tk.Label(self, text="Number of years: ", font=LARGE_FONT).grid(row=3, column=0, sticky="NW")

        self.entryLoanAmountValue = StringVar()
        self.entryLoanAmountValue.set("0.00")
        self.entryDownPaymentAmountValue = StringVar()
        self.entryDownPaymentAmountValue.set("0.00")
        self.entryInterestRateValue = StringVar()
        self.entryInterestRateValue.set("0.00")
        self.entryNumberOfYearsValue = StringVar()
        self.entryNumberOfYearsValue.set("0")

        entry_Loan_Amt = tk.Entry(self, width=12, textvariable=self.entryLoanAmountValue)
        entry_Loan_Amt.grid(row=0, column=1, sticky="NW")
        entry_Downpayment_Amt = tk.Entry(self, width=12, textvariable=self.entryDownPaymentAmountValue)
        entry_Downpayment_Amt.grid(row=1, column=1, sticky="NW")
        entry_Interest_Rate = tk.Entry(self, width=5, textvariable=self.entryInterestRateValue)
        entry_Interest_Rate.grid(row=2, column=1, sticky="NW")
        entry_Number_Of_Years = tk.Entry(self, width=2, textvariable=self.entryNumberOfYearsValue)
        entry_Number_Of_Years.grid(row=3, column=1, sticky="NW")

        tk.Button(self, text="Calculate", font=LARGE_FONT, command=lambda: self.calculate()).grid(row=4, column=0,
                                                                                                  sticky="S")
        tk.Button(self, text="Visualize", font=LARGE_FONT, command=lambda: self.graph_it()).grid(row=4, column=1,
                                                                                                 sticky="S")

    def calculate(self):
        lmc = self.create_loan_mortgage_calculator()
        balances, interests, principals = lmc.generate_monthly_breakdowns()
        mortgage_payment = lmc.monthly_payment()
        dataPage =  DataPage(self.parent, self.controller, mortgage_payment, balances, interests, principals)
        self.controller.frames[DataPage] = dataPage
        dataPage.grid(row=0, column=0, sticky="news")
        self.controller.show_frame(DataPage)

    def create_loan_mortgage_calculator(self):
        la = float(self.entryLoanAmountValue.get())
        dp = float(self.entryDownPaymentAmountValue.get())
        ir = float(self.entryInterestRateValue.get())
        piy = int(self.entryNumberOfYearsValue.get())
        lmc = LoanMortgageCalculator(la, dp, ir, piy)
        return lmc

    def graph_it(self):
        lmc = self.create_loan_mortgage_calculator()
        balances, interests, principals = lmc.generate_monthly_breakdowns()
        graph_page = GraphPage(self.parent, self.controller, lmc.number_of_monthly_periods,
                               balances, interests, principals)
        self.controller.frames[GraphPage] = graph_page
        graph_page.grid(row=0, column=0, sticky="news")
        self.controller.show_frame(GraphPage)


class DataPage(tk.Frame):
    def __init__(self, parent, controller, mortgage_payment, balances, interests, principals):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Button(self, text="Back", font=LARGE_FONT, command=lambda: controller.show_frame(InputPage)).grid(
            row=0, column=0, sticky="N")
        tk.Label(self, text="Mortgage Payment: $").grid(row=0, column=1, sticky="N")
        tk.Label(self, text=str(mortgage_payment)).grid(row=0, column=2, sticky="N")
        self.treeView = Treeview(self)
        self.treeView["columns"] = ("balance", "interest", "principal")
        self.treeView.heading("#0", text="Month", anchor="w")
        self.treeView.column("#0", anchor="w")
        self.treeView.heading("balance", text="Loan Balance $")
        self.treeView.heading("interest", text="Interest Paid $")
        self.treeView.heading("principal", text="Principal Paid $")

        month = 1

        for balance, interest, principal in zip(balances, interests, principals):
            self.treeView.insert('', 'end', text=str(month), values=(str(balance), str(interest), str(principal)))
            month += 1

        self.treeView.grid(sticky="NSEW")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class GraphPage(tk.Frame):
    def __init__(self, parent, controller, number_of_months, balances, interests, principals):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Mortgage Visualization", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Button(self, text="Back", command=lambda: controller.show_frame(InputPage)).pack()

        months = list()

        i = 1
        while i <= number_of_months:
            months.append(i)
            i = i + 1

        f = Figure()
        f.subplots_adjust(left=0.15, right=0.95, wspace=0.25, hspace=0.75)
        a = f.add_subplot(211)
        plot1, = a.plot(months, interests,'r')
        plot2, = a.plot(months, principals,'g')

        b = f.add_subplot(212)
        plot3 = b.plot(months, balances, 'b')

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



app = LoanMortgageCalculatorGUI()
app.title("Fixed Loan Mortgage Calculator App")
app.mainloop()
