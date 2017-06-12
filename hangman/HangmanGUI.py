import tkinter as tk
from tkinter.ttk import *
from tkinter import StringVar
import random

LARGE_FONT = ("Verdana", 14)

class HangmanGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.guesses = 0
        self.word_choices = ['hard', 'soft', 'brittle', 'mettle', 'gobble', 'broad', 'wiring', 'bring', 'short']
        self.selected_word = self.word_choices[random.randint(0,8)]

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.guessInputValue = StringVar()
        self.guessInputValue.set("")

        frame = Frame(container)
        frame.grid(row=1, column=0, sticky="s")

        #----Define components
        tk.Entry(container, width=20, textvariable=self.guessInputValue, justify='right').grid(row=0, column=0, sticky="n")
        tk.Button(container, text="check", command=lambda: self.check_guess()).grid(row=0, column=1, sticky="n")
        tk.Button(container, text="reset", command=lambda: self.clear_figure()).grid(row=0, column=2, sticky="n")

        self.canvas = tk.Canvas(frame, width=500, height=300)
        self.status = self.display_message("")
        self.draw_scaffold()

        self.canvas.pack()

    def draw_scaffold(self):
        self.canvas.create_line(25, 10, 60, 10)
        self.canvas.create_line(25, 10, 25, 150)
        self.canvas.create_line(60,10, 60, 20)
        self.canvas.create_rectangle(15, 150, 75, 160, fill="blue")

    def draw_head(self):
        return self.canvas.create_oval(50, 20, 70, 40, fill="blue")

    def draw_neck(self):
        return self.canvas.create_line(60, 40, 60, 50)

    def draw_left_arm(self):
        return self.canvas.create_line(40, 50, 60, 50)

    def draw_right_arm(self):
        return self.canvas.create_line(60, 50, 80, 50)

    def draw_torso(self):
        return self.canvas.create_line(60, 50, 60, 90)

    def draw_left_leg(self):
        return self.canvas.create_line(60, 90, 40, 120)

    def draw_right_leg(self):
        return self.canvas.create_line(60, 90, 80, 120)

    def clear_figure(self):
        self.guesses = 0
        self.canvas.delete(self.status)
        self.canvas.delete(self.head)
        self.canvas.delete(self.neck)
        self.canvas.delete(self.left_arm)
        self.canvas.delete(self.right_arm)
        self.canvas.delete(self.torso)
        self.canvas.delete(self.left_leg)
        self.canvas.delete(self.right_leg)

    def display_message(self, message):
        try:
            self.canvas.delete(self.status)
        except:
            print()
        self.status =  self.canvas.create_text(150, 200, text=message)

    def check_guess(self):
        if self.guessInputValue.get() == self.selected_word:
            self.status = self.display_message("Congratulations !!!")
        else:
            self.guesses += 1

            if self.guesses == 1:
                self.head = self.draw_head()
                self.display_message("Guess again...")
            elif self.guesses == 2:
                self.neck = self.draw_neck()
                self.display_message("Guess again...")
            elif self.guesses == 3:
                self.left_arm = self.draw_left_arm()
                self.display_message("Guess again... It is a "+str(len(self.selected_word))+" letter word")
            elif self.guesses == 4:
                self.right_arm = self.draw_right_arm()
                self.display_message("Guess again... It starts with "+self.selected_word[:1])
            elif self.guesses == 5:
                self.torso = self.draw_torso()
                self.display_message("Guess again... It ends with "+self.selected_word[-1:])
            elif self.guesses == 6:
                self.left_leg = self.draw_left_leg()
                self.display_message("Guess again...")
            elif self.guesses == 7:
                self.right_leg = self.draw_right_leg()
                self.display_message("Game over. You lost...Answer is "+self.selected_word)

app = HangmanGUI()
app.title("Hangman")
app.mainloop()

