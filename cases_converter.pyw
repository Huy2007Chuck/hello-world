# File: main.pyw (run this)
# By Huy2007Chuck
# Converts normal text into different available cases
# Main module of the Cases Converter project

import tkinter as tk
import pyperclip
import random

# Constants
FT = ("Consolas", 20)
SM_FT = ("Consolas", 10)

SEPS = [
    "", # 0
    " ", # 1
    "_", # 2
    "-", # 3
    ".", # 4
    ",", # 5
    "/", # 6
    "\\", # 7
    "|", # 8
    ":", # 9
    ";" # 10
]

CASES = [
    "SpongeBob", # 0
    "Camel", # 1
    "Pascal", # 2
    "Snake", # 3
    "Kebab", # 4
    "Flat", # 5
    "Upper Flat", # 6
    "Constant", # 7
    "Train", # 8
    "Camel Snake", # 9
    "Cobol", # 10
    "Upper", # 11
    "Lower", # 12
    "JoJo", # 13
    "Random", # 14
    "BAO", # 15
    "Sentence", # 16
    "Toggle", # 17
    "Capitalize Each Word", # 18
    "Spacing", # 19
    "Ascii" # 20
]


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.clicked = tk.StringVar()
        self.clicked.set(random.choice(CASES))

        self.lbl = tk.Label(self, text="Input text:", font=FT)
        self.lbl.pack(padx=20, pady=10)

        self.ent = tk.Entry(self, font=FT)
        self.ent.focus()
        self.ent.pack(padx=20, pady=10)

        self.drop = tk.OptionMenu(self, self.clicked, *CASES)
        self.drop.config(font=SM_FT, width=30)
        self.drop.pack(padx=20, pady=10)

        self.btn = tk.Button(self, text="Convert", font=FT, command=lambda: self.convert(self.clicked.get(), self.ent.get()))
        self.btn.pack(padx=20, pady=10)

        self.new_lbl = tk.Entry(self, font=FT)
        self.new_lbl.configure(state="readonly")
        self.new_lbl.pack(padx=20, pady=10)

        self.copy_btn = tk.Button(self, text="Copy to clipboard", font=FT, command=lambda: self.copy(self.new_lbl.get()))
        self.copy_btn.pack(padx=20, pady=10)

        self.bind("<Return>", lambda x: self.convert(self.clicked.get(), self.ent.get()))


    def convert(self, case, string):
        if case == CASES[0]:
            text = self.spongebob(string)
        elif case == CASES[1]:
            text = self.camel(string)
        elif case == CASES[2]:
            text = self.pascal(string)
        elif case == CASES[3]:
            text = self.snake(string)
        elif case == CASES[4]:
            text = self.kebab(string)
        elif case == CASES[5]:
            text = self.flat(string)
        elif case == CASES[6]:
            text = self.upper_flat(string)
        elif case == CASES[7]:
            text = self.constant(string)
        elif case == CASES[8]:
            text = self.train(string)
        elif case == CASES[9]:
            text = self.camel_snake(string)
        elif case == CASES[10]:
            text = self.cobol(string)
        elif case == CASES[11]:
            text = self.upper(string)
        elif case == CASES[12]:
            text = self.lower(string)
        elif case == CASES[13]:
            text = self.jojo(string)
        elif case == CASES[14]:
            text = self.random(string)
        elif case == CASES[15]:
            text = self.bao(string)
        elif case == CASES[16]:
            text = self.sentence(string)
        elif case == CASES[17]:
            text = self.toggle(string)
        elif case == CASES[18]:
            text = self.capitalize_each_word(string)
        elif case == CASES[19]:
            text = self.spacing(string)
        elif case == CASES[20]:
            text = self.ascii(string)
        else:
            text = string

        print(case + ": " + string + " --> " + text)

        self.new_lbl.configure(state="normal")
        self.new_lbl.delete(0, tk.END)
        self.new_lbl.insert(0, text)
        self.new_lbl.configure(state="readonly")


    def copy(self, text):
        pyperclip.copy(text)


    def spongebob(self, string):
        char_list = [char.lower() for char in string]
        new_char_list = []
        index = 0

        for char in char_list:
            if char.isalpha():
                index += 1
                if index % 2 == 0:
                    new_char_list.append(char.upper())
                else:
                    new_char_list.append(char)
            else:
                new_char_list.append(char)

        new_string = SEPS[0].join(new_char_list)

        return new_string


    def camel(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = []

        for word in word_list:
            if word_list.index(word) == 0:
                new_word_list.append(word)
            else:
                new_word_list.append(word.capitalize())

        new_string = SEPS[0].join(new_word_list)

        return new_string


    def pascal(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.capitalize() for word in word_list]
        new_string = SEPS[0].join(new_word_list)

        return new_string


    def snake(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.lower() for word in word_list]
        new_string = SEPS[2].join(new_word_list)

        return new_string


    def kebab(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.lower() for word in word_list]
        new_string = SEPS[3].join(new_word_list)

        return new_string


    def flat(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.lower() for word in word_list]
        new_string = SEPS[0].join(new_word_list)

        return new_string


    def upper_flat(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.upper() for word in word_list]
        new_string = SEPS[0].join(new_word_list)

        return new_string


    def constant(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.upper() for word in word_list]
        new_string = SEPS[2].join(new_word_list)

        return new_string


    def train(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.capitalize() for word in word_list]
        new_string = SEPS[3].join(new_word_list)

        return new_string


    def camel_snake(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.capitalize() for word in word_list]
        new_string = SEPS[2].join(new_word_list)

        return new_string


    def cobol(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.upper() for word in word_list]
        new_string = SEPS[3].join(new_word_list)

        return new_string


    def upper(self, string):
        new_char_list = [char.upper() for char in string]
        new_string = SEPS[0].join(new_char_list)

        return new_string


    def lower(self, string):
        new_char_list = [char.lower() for char in string]
        new_string = SEPS[0].join(new_char_list)

        return new_string


    def jojo(self, string):
        new_char_list = []
        
        for char in string:
            if char.upper() == "J":
                new_char_list.append(char.upper())
            else:
                new_char_list.append(char)

        new_string = SEPS[0].join(new_char_list)

        return new_string


    def random(self, string):
        new_char_list = []

        for char in string:
            if char in SEPS:
                new_char_list.append(random.choice(SEPS))
            else:
                n = random.randint(0, 1)
                if n == 0:
                    new_char_list.append(char.lower())
                else:
                    new_char_list.append(char.upper())

        new_string = SEPS[0].join(new_char_list)

        return new_string


    def bao(self, string):
        new_char_list = [char.upper() for char in string.replace(" ", "")]
        new_string = SEPS[4].join(new_char_list)

        return new_string


    def sentence(self, string):
        word_list = string.split(SEPS[1])
        word_list[0] = word_list[0].capitalize()
        new_string = SEPS[1].join([*word_list])
        new_string_2 = SEPS[0].join([new_string, "."])

        return new_string_2


    def toggle(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.capitalize() for word in word_list]
        new_word_list_2 = [word.swapcase() for word in new_word_list]
        new_string = SEPS[1].join(new_word_list_2)

        return new_string


    def capitalize_each_word(self, string):
        word_list = string.split(SEPS[1])
        new_word_list = [word.capitalize() for word in word_list]
        new_string = SEPS[1].join(new_word_list)

        return new_string


    def spacing(self, string):
        new_char_list = [char.lower() for char in string.replace(" ", "")]
        new_string = SEPS[1].join(new_char_list)

        return new_string


    def ascii(self, string):
        new_char_list = [str(ord(char)) for char in string]
        new_string = SEPS[1].join(new_char_list)
        
        return new_string


if __name__ == "__main__":
    root = App()
    #print(root.sentence("hi convert thiis pleaseeae"))
    root.title("Cases Converter")
    root.mainloop()
