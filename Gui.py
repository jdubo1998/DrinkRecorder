import tkinter as tk
from tkinter import ttk, Label, Button, Menubutton, Menu, Entry
from datetime import datetime
import Game
import Graphs

class GameGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.activePlayers = Game.getPlayers()

        self.title("Alcohol Game")
        self.resizable(width=False, height=False)
        self.geometry('750x320')

        self.calc_label = Label(self, text="Calculations", font="lucida 11 bold")
        self.calc_label.place(x=20, y=10)

        # --- Participants Multiple Selection Combobox ---
        # Label
        self.label1 = Label(self, text="Participants:")
        self.label1.place(x=10, y=40)

        # Multiple selection combobox
        self.player_combobox = Menubutton(self, text="_______", borderwidth=1, indicatoron=True)
        self.player_combobox_values = Menu(self.player_combobox, tearoff=False)
        self.player_combobox.configure(menu=self.player_combobox_values)
        self.player_combobox.place(x=90, y=40)
        self.players = {}
        for player in Game.getPlayers():
            self.players[player] = tk.IntVar(value=1)
            self.player_combobox_values.add_checkbutton(label=player, variable=self.players[player],
                    onvalue=1, offvalue=0, command=self.setActivePlayers)

        # ---   Date1 to Date2 Seleciton   ---
        self.date1 = tk.StringVar()
        self.date1.set("4/20/20")
        self.date2 = tk.StringVar()
        self.date2.set(datetime.today().strftime("%#m/%#d/%y"))
        # Date1
        self.date1_entry = Entry(self, textvariable=self.date1)
        self.date1_entry.place(x=10, y=70, width=60)
        # Date2
        self.date2_entry = Entry(self, textvariable=self.date2)
        self.date2_entry.place(x=90, y=70, width=60)
        # Labels
        self.label2 = Label(self, text="to")
        self.label2.place(x=72, y=70)

        # ---   Submit Button   ---
        self.submit_btn1 = Button(self, text="Submit", command=self.submitData)
        self.submit_btn1.place(x=90, y=100)

        # Seperator
        self.seperator = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.seperator.place(x=10, y=145, width=180)

        # ---   Add Score   ---
        self.date = tk.StringVar()
        self.name = tk.StringVar()
        self.pct = tk.StringVar()
        self.oz = tk.StringVar()
        # Labels
        self.score_label = Label(self, text="Add Score", font="lucida 11 bold")
        self.score_label.place(x=20, y=160)
        self.label4 = Label(self, text="Date: ")
        self.label4.place(x=10, y=190)
        self.label5 = Label(self, text="Name: ")
        self.label5.place(x=10, y=220)
        self.label6 = Label(self, text="Pct: ")
        self.label6.place(x=10, y=250)
        self.label7 = Label(self, text="Oz: ")
        self.label7.place(x=85, y=250)
        # Name
        self.name_entry = Entry(self, textvariable=self.date)
        self.name_entry.place(x=52, y=190)
        self.date_entry = Entry(self, textvariable=self.name)
        self.date_entry.place(x=60, y=220)
        self.pct_entry = Entry(self, textvariable=self.pct)
        self.pct_entry.place(x=45, y=250, width=30)
        self.oz_entry = Entry(self, textvariable=self.oz)
        self.oz_entry.place(x=115, y=250, width=30)

        # ---   Submit Button   ---
        self.submit_btn2 = Button(self, text="Submit", command=self.submitScore)
        self.submit_btn2.place(x=90, y=280)

    def setActivePlayers(self):
        self.activePlayers.clear()
        for player, active in self.players.items():
            if (active.get() == 1):
                self.activePlayers.append(player)

    def submitData(self):
        Graphs.createFigures(self.activePlayers, self.date1.get(), self.date2.get())

    def submitScore(self):
        Game.insertScore(self.name.get(), self.date.get(), float(self.pct.get()), float(self.oz.get()))

if __name__ == "__main__":
    root = GameGUI()
    root.mainloop()

# root = GameGUI()
# root.mainloop()
