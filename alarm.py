# File: alarm.py (run this)
# By: Huy2007Chuck
# Mini project Alarm Clock

from datetime import datetime as dt
import time
import tkinter as tk
from tkinter.simpledialog import askinteger as askint

# Constants
SM_FT = ("Consolas", 16)
LG_FT = ("Consolas", 20)


class Prompt(tk.Tk):
    def __init__(self):
        super().__init__()

        self.set_active()

        units = ("hour", "minute", "second")
        lbls = []
        self.ents = []
        btns = []

        name_lbl = tk.Label(self, text="Alarm name", font=SM_FT)
        name_lbl.grid(row=3, column=0, padx=5, pady=5)

        name_ent = tk.Entry(self, font=SM_FT, width="10")
        name_ent.insert(0, "Unnamed")
        name_ent.grid(row=3, column=1, padx=5, pady=5)

        self.ents.append(name_ent)

        for i in range(len(units)):
            l = tk.Label(self, text=units[i].capitalize(), font=SM_FT)
            l.grid(row=i, column=0, padx=5, pady=5)
            lbls.append(l)

            e = tk.Entry(self, font=SM_FT, width="5")
            e.config(state="normal")
            e.insert(0, "00")
            e.config(state="readonly")
            e.grid(row=i, column=1, padx=5, pady=5)
            self.ents.append(e)

            b = tk.Button(self, text="Input...", font=SM_FT, command=lambda i=i: self.input_time(units, i))
            b.grid(row=i, column=2, padx=5, pady=5)
            btns.append(b)

        cbtn = tk.Button(self, text="Done", font=SM_FT, command=self.done)
        cbtn.grid(row=4, column=2, padx=5, pady=5)


    def set_active(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()


    def input_time(self, units, i):
        m = [0, 0]

        if units[i] == "hour": m = [0, 24]
        else: m = [0, 60]

        t = askint("Input", "Please enter " + units[i], minvalue=m[0], maxvalue=m[1])

        self.ents[i].config(state="normal")
        self.ents[i].delete(0, tk.END)
        self.ents[i].insert(0, str(t))
        self.ents[i].config(state="readonly")

        self.set_active()


    def done(self):
        global root
        l = [e.get() for e in self.ents]
        print(l)

        self.destroy()

        root.destroy()
        root = App()
        root.title("Alarm Clock")
        root.alarm_add(l)
        root.mainloop()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.t = tk.StringVar()

        current_time = tk.Label(self, text="CURRENT TIME", font=SM_FT)
        current_time.pack(padx=5, pady=5)

        self.time_lbl = tk.Label(self, textvariable=self.t, font=LG_FT)
        self.time_lbl.pack(padx=5, pady=5)

        self.set_btn = tk.Button(self, text="Create new alarm", font=SM_FT, command=self.prompt)
        self.set_btn.pack(padx=5, pady=5)

        self.update_time()


    def set_active(self):
        self.lift()
        self.focus_force()
        self.grab_set()
        self.grab_release()


    def update_time(self):
        text = str(dt.now().time())[:-7]
        self.t.set(text)

        self.time_lbl.after(1000, self.update_time)


    def prompt(self):
        p = Prompt()
        p.title("Create new alarm")


    def alarm_add(self, alarm):
        new_btn = tk.Label(self, text=":".join(alarm), font=SM_FT)
        new_btn.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = App()
    root.title("Alarm Clock")
    root.mainloop()
