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
        self.S2.config(state=DISABLED)

    def flush(self):
        pass

    def write(self, txt):
        self.S2.insert(END, str(txt))


if __name__ == '__main__':
    Display().mainloop()

###################################################################################################################################
#Codigo hecho usando JSON para la sopa de letras
###################################################################################################################################

from word_search_puzzle.utils import display_panel
from word_search_puzzle.algorithms import create_panel
from tkinter import *
import tkinter as tk
import json


def crear_sopa():
    words = [E2.get(), E3.get(), E4.get(), E5.get(), E6.get()]
    ndim = int(E1.get())
    result = create_panel(height=ndim, width=ndim, words_value_list=words,
                          as_dict=TRUE)  # , as_dict=TRUE
    with open('SopaLetras.txt', 'w') as outfile:
        json.dump(result, outfile)
    #
    # display_panel(result.get('panel'))
    # S2.insert(tk.END, r)
    with open('SopaLetras.txt', 'r') as inside:
        data = json.load(inside)
        data1 = json.dumps(data, indent=4, sort_keys=TRUE)
    S2.insert('1.0', str(data1))
    S2.config(state=DISABLED)


"""def imprimir_sopa(self, txt):
    self.output.insert(tk.END, str(txt))
    self.update_idletasks()"""


def imprimir_sopa():
    for k in json.dumps:
        S2.insert(tk.END, '{} = {} \n'.format(k, json.dumps))


main = tk.Tk()
main.geometry('{}x{}'.format(750, 550))
main.resizable(False, False)
main.config(bg="light blue")
main.title('Sopa de Letras')

top_frame1 = Frame(main, bg='light blue', width=425, height=150)
top_frame2 = Frame(main, bg='light blue', width=425, height=150)
top_frame2R = Frame(top_frame2, bg='light blue')

top_frame1.pack()
top_frame2.pack()
top_frame2R.pack(side=RIGHT)

w = Label(top_frame1, text="Sopa de letras", bg='light blue', font=("Helvetica", 18, "bold"))
w.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

btn = Button(top_frame2R, text='Crear', borderwidth=5, command=crear_sopa)
btn.config(font=("Helvetica", 14))
btn.pack(padx=(75, 75), pady=(50, 0))

"""btn1 = Button(top_frame2R, text='Imprimir', borderwidth=5, command=imprimir_sopa)
btn1.config(font=("Helvetica", 14))
btn1.pack(padx=(75, 75), pady=(50, 0))"""

w1 = Label(top_frame2, text='Dimensiones deseadas: ', bg='light blue', font=("Helvetica", 15))
w1.pack(padx=(10, 10), anchor='nw', pady=(20, 0))
E1 = Entry(top_frame2, width=15)
E1.config(font=("Helvetica", 14))
E1.pack(padx=(10, 10), pady=(5, 5))

w2 = Label(top_frame2, text='Primera palabra: ', bg='light blue', font=("Helvetica", 15))
w2.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E2 = Entry(top_frame2, width=15)
E2.config(font=("Helvetica", 14))
E2.pack(padx=(10, 10), pady=(5, 5))

w3 = Label(top_frame2, text='Tercera palabra: ', bg='light blue', font=("Helvetica", 15))
w3.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E3 = Entry(top_frame2, width=15)
E3.config(font=("Helvetica", 14))
E3.pack(padx=(10, 10), pady=(5, 5))

w4 = Label(top_frame2, text='Cuarta palabra: ', bg='light blue', font=("Helvetica", 15))
w4.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E4 = Entry(top_frame2, width=15)
E4.config(font=("Helvetica", 14))
E4.pack(padx=(10, 10), pady=(5, 5))

w5 = Label(top_frame2, text='Quinta palabra: ', bg='light blue', font=("Helvetica", 15))
w5.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E5 = Entry(top_frame2, width=15)
E5.config(font=("Helvetica", 14))
E5.pack(padx=(10, 10), pady=(5, 5))

w6 = Label(top_frame2, text='Quinta palabra: ', bg='light blue', font=("Helvetica", 15))
w6.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E6 = Entry(top_frame2, width=15)
E6.config(font=("Helvetica", 14))
E6.pack(padx=(10, 10), pady=(5, 5))

S1 = tk.Scrollbar(top_frame2R)
S1.pack(side=tk.RIGHT, fill=tk.Y, pady=(10, 0), anchor='e')
S2 = Text(top_frame2R, height=15, width=35)
S2.pack(padx=(0, 3), pady=(5, 0), fill=tk.BOTH)
S1.config(command=S2.yview)
S2.config(yscrollcommand=S1.set, font=("Helvetica", 14))

mainloop()
