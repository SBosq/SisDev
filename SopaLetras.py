from tkinter import *
from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel
import sys


class Display(Frame):

    def __init__(self, parent=0):
        Frame.__init__(self, parent, bg='light blue')
        self.w = Label(self, text="Sopa de letras", bg='light blue', font=("Helvetica", 18, "bold"))
        self.w.pack(pady=(20, 0))

        self.w1 = Label(self, text='Dimensiones deseadas: ', bg='light blue', font=("Helvetica", 15))
        self.w1.pack(pady=(5, 0))
        self.entry1 = Entry(self, width=15)
        self.entry1.config(font=("Helvetica", 14))
        self.entry1.pack()

        self.w2 = Label(self, text='Primera palabra: ', bg='light blue', font=("Helvetica", 15))
        self.w2.pack(pady=(5, 0))
        self.entry2 = Entry(self, width=15)
        self.entry2.config(font=("Helvetica", 14))
        self.entry2.pack()

        self.w3 = Label(self, text='Segunda palabra: ', bg='light blue', font=("Helvetica", 15))
        self.w3.pack(pady=(5, 0))
        self.entry3 = Entry(self, width=15)
        self.entry3.config(font=("Helvetica", 14))
        self.entry3.pack()

        self.w4 = Label(self, text='Tercera palabra: ', bg='light blue', font=("Helvetica", 15))
        self.w4.pack(pady=(5, 0))
        self.entry4 = Entry(self, width=15)
        self.entry4.config(font=("Helvetica", 14))
        self.entry4.pack()

        self.w5 = Label(self, text='Cuarta palabra: ', bg='light blue', font=("Helvetica", 15))
        self.w5.pack(pady=(5, 0))
        self.entry5 = Entry(self, width=15)
        self.entry5.config(font=("Helvetica", 14))
        self.entry5.pack()

        self.w6 = Label(self, text='Quinta palabra: ', bg='light blue', font=("Helvetica", 15))
        self.w6.pack(pady=(5, 0))
        self.entry6 = Entry(self, width=15)
        self.entry6.config(font=("Helvetica", 14))
        self.entry6.pack()

        self.btn = Button(self, text='Crear', borderwidth=5, command=self.crear_sopa)
        self.btn.config(font=("Helvetica", 14))
        self.btn.pack(padx=(75, 75), pady=(25, 25))

        self.S2 = Text(self, height=15, width=50)
        self.S2.pack(padx=(0, 3), pady=(5, 0), fill=BOTH)
        sys.stdout = self
        self.pack()

    def crear_sopa(self):
        words = [self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get(), self.entry6.get()]
        ndim = int(self.entry1.get())
        result = create_panel(height=ndim, width=ndim, words_value_list=words)
        print(display_panel(result.get('panel')))

    def flush(self):
        pass

    def write(self, txt):
        self.S2.insert(END, str(txt))


if __name__ == '__main__':
    Display().mainloop()
