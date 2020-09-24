Hypotenuse Calculator
#################################################################################

from tkinter import *
import math


def show_answer():
    comp1 = num1.get()
    comp2 = num2.get()
    Ans1 = math.pow(int(comp1), 2) + math.pow(int(comp2), 2)
    Ans2 = math.sqrt(Ans1)
    label_result.config(text="Length of Hypotenuse: %.4f" % Ans2)
    return


main = Tk()
main.geometry('400x225')
main.resizable(False, False)
main.config(bg="skyblue")
main.title('Hypotenuse Calculator')
Label(main, text="Length of side A: ").grid(row=0, pady=(25, 25), padx=(45, 0))
Label(main, text="Length of side B: ").grid(row=1, pady=(25, 25), padx=(45, 0))

num1 = Entry(main)
num2 = Entry(main)

label_result = Label(main)
label_result.grid(row=3, column=1, pady=(25, 25), padx=(45, 0))

num1.grid(row=0, column=1, pady=(25, 25), padx=(45, 0))
num2.grid(row=1, column=1, pady=(25, 25), padx=(45, 0))

Button(main, text='Calculate!', command=show_answer).grid(row=3, column=0, pady=(25, 25), padx=(75, 25))

mainloop()

#################################################################################

Area Calculator
#################################################################################

from tkinter import *
import math


def show_answer_rect():
    comp1 = num1.get()
    comp2 = num2.get()
    Ans1 = int(comp1) * int(comp2)
    label_result_rect.config(text="Area: %2d" % Ans1)
    return


def show_answer_para():
    comp3 = num1.get()
    comp4 = num2.get()
    Ans2 = int(comp3) * int(comp4)
    label_result_para.config(text="Area: %2d" % Ans2)
    return


def show_answer_tri():
    comp1 = num1.get()
    comp2 = num2.get()
    Ans3 = ((int(comp1) * int(comp2)) / 2)
    label_result_tri.config(text="Area: %2d" % Ans3)
    return


def show_answer_cube():
    comp1 = num1.get()
    comp2 = num2.get()
    Ans4 = (int(comp1) * int(comp2)) * 6
    label_result_cube.config(text="Area: %2d" % Ans4)
    return


def show_answer_pyra():
    comp1 = num1.get()
    comp2 = num2.get()
    Ans5 = ((2 * int(comp1) * int(comp2)) + math.pow(int(comp1), 2))
    label_result_pyra.config(text="Area: %2d" % Ans5)
    return


main = Tk()
main.geometry('700x560')
main.resizable(False, False)
main.config(bg="grey")
main.title('Area Formulas')
Label(main, text="Base: ", bg="grey", font=("Helvetica", 16)).grid(row=0, column=2, pady=(25, 15), padx=(45, 0))
Label(main, text="Height: ", bg="grey", font=("Helvetica", 16)).grid(row=1, column=2, pady=(15, 25), padx=(45, 0))

Label(main, text="Enter the base and height,", bg="grey", font=("Helvetica", 16)).grid(row=0, column=0, padx=(45, 0))
Label(main, text="then select a geometric shape. ", bg="grey", font=("Helvetica", 16)).grid(row=1, column=0, padx=(45, 0))

num1 = Entry(main)
num2 = Entry(main)

label_result_rect = Label(main)
label_result_para = Label(main)
label_result_tri = Label(main)
label_result_cube = Label(main)
label_result_pyra = Label(main)

label_result_rect.grid(row=3, column=3, pady=(25, 25), padx=(15, 0), sticky=E)
label_result_para.grid(row=4, column=3, pady=(25, 25), padx=(15, 0), sticky=E)
label_result_tri.grid(row=5, column=3, pady=(25, 25), padx=(15, 0), sticky=E)
label_result_cube.grid(row=6, column=3, pady=(25, 25), padx=(15, 0), sticky=E)
label_result_pyra.grid(row=7, column=3, pady=(25, 25), padx=(15, 0), sticky=E)

num1.grid(row=0, column=3, pady=(25, 25), padx=(45, 0))
num2.grid(row=1, column=3, pady=(25, 25), padx=(45, 0))

Button(main, text='Rectangle', command=show_answer_rect, borderwidth=5).grid(row=3, column=0, pady=(25, 25), padx=(75, 25), sticky=W)
Button(main, text='Parallelogram', command=show_answer_para, borderwidth=5).grid(row=4, column=0, pady=(25, 25), padx=(75, 25), sticky=W)
Button(main, text='Triangle', command=show_answer_tri, borderwidth=5).grid(row=5, column=0, pady=(25, 25), padx=(75, 25), sticky=W)
Button(main, text='Cube', command=show_answer_cube, borderwidth=5).grid(row=6, column=0, pady=(25, 25), padx=(75, 25), sticky=W)
Button(main, text='Pyramid', command=show_answer_pyra, borderwidth=5).grid(row=7, column=0, pady=(25, 25), padx=(75, 25), sticky=W)

mainloop()

#################################################################################

Interest Calculator
#################################################################################

from tkinter import *
import math


def show_answer_simp():
    comp1 = num1.get()
    comp2 = num2.get()
    comp3 = num3.get()
    rate = float(int(comp2) / 100)
    Ans1 = 1 + (float(comp3) * rate)
    Ans2 = int(comp1) * Ans1
    label_result_simp.config(text="%.4f" % Ans2)
    return


def show_answer_comp():
    comp3 = num1.get()
    comp4 = num2.get()
    comp5 = num3.get()
    rate = float(int(comp4) / 100)
    Ans3 = int(comp3) * math.pow(1 + rate, int(comp5))
    label_result_comp.config(text="%.4f" % Ans3)
    return


main = Tk()
main.geometry('550x300')
main.resizable(False, False)
main.config(bg="light grey")
main.title('Interest Comparison')
Label(main, text="Principal: ", bg="light grey", font=("Helvetica", 16)).grid(row=0, column=0, pady=(25, 0), padx=(25, 0))
Label(main, text="Rate: ", bg="light grey", font=("Helvetica", 16)).grid(row=0, column=1, pady=(25, 0), sticky=W)
Label(main, text="Years: ", bg="light grey", font=("Helvetica", 16)).grid(row=0, column=2, pady=(25, 0), padx=(45, 0),
                                                                          sticky=W)

num1 = Entry(main)
num2 = Entry(main)
num3 = Entry(main)

label_result_simp = Label(main)
label_result_comp = Label(main)

num1.grid(row=1, column=0, pady=(5, 25), padx=(30, 0))
num2.grid(row=1, column=1, pady=(5, 25), padx=(0, 10), sticky=W)
num3.grid(row=1, column=2, pady=(5, 25), padx=(15, 0), sticky=E)

label_result_simp.grid(row=3, column=2, pady=(25, 25), padx=(15, 0), sticky=E)
label_result_comp.grid(row=4, column=2, pady=(25, 25), padx=(15, 0), sticky=E)

Button(main, text='Simple Interest', command=show_answer_simp, borderwidth=5).grid(row=3, column=0, pady=(25, 25), padx=(75, 25), sticky=W)
Button(main, text='Compound Interest', command=show_answer_comp, borderwidth=5).grid(row=4, column=0, pady=(25, 25), padx=(75, 25), sticky=W)

mainloop()

#################################################################################

Runners Calculator
#################################################################################

from tkinter import *
import math


def show_answer():
    comp1 = float(num1.get())
    comp2 = num2.get()
    rate = float(float(comp2) / float(comp1))
    label_result.config(bg="light green", font=("Helvetica", 10), text="Minutes per mile: %.4f" % rate)
    return


main = Tk()
main.geometry('350x175')
main.resizable(False, False)
main.config(bg="light green")
main.title('Runners Calculator')
Label(main, text="Number of miles ran: ", bg="light green", font=("Helvetica", 10)).grid(row=0, column=0, pady=(25, 0), padx=(25, 0))
Label(main, text="Finishing time in minutes: ", bg="light green", font=("Helvetica", 10)).grid(row=0, column=1, pady=(25, 0), padx=(15, 0),sticky=W)


num1 = Entry(main)
num2 = Entry(main)

label_result = Label(main)

num1.grid(row=1, column=0, pady=(5, 25), padx=(30, 0))
num2.grid(row=1, column=1, pady=(5, 25), padx=(25, 10), sticky=W)

label_result.grid(row=3, column=1, pady=(25, 25), padx=(0, 25), sticky=E)

Button(main, text='Running Speed', command=show_answer, borderwidth=5).grid(row=3, column=0, pady=(25, 25), padx=(25, 25), sticky=W)

mainloop()

#################################################################################

Grade Percentages
#################################################################################

from tkinter import *
import math


def show_answer():
    comp1 = num1.get()
    comp2 = num2.get()
    comp3 = num3.get()
    comp4 = num4.get()
    grade = float(comp1) + float(comp2) + float(comp3)
    per = float(float(grade) + float(comp4))
    ans1 = float(per/550) * 100
    label_result.config(bg="pink", font=("Helvetica", 8, "bold"), text="Total Percentage: %.2f" % ans1)
    return


main = Tk()
main.geometry('350x225')
main.resizable(False, False)
main.config(bg="pink")
main.title('Grade Percentages')
Label(main, text="First Exam: ", bg="pink", font=("Helvetica", 12)).grid(row=0, column=0, pady=(25, 0), padx=(25, 25))
Label(main, text="Second Exam: ", bg="pink", font=("Helvetica", 12)).grid(row=0, column=1, pady=(25, 0), sticky=W)
Label(main, text="Third Exam: ", bg="pink", font=("Helvetica", 12)).grid(row=1, column=0, pady=(30, 0), padx=(25, 25))
Label(main, text="Assignment Points: ", bg="pink", font=("Helvetica", 12)).grid(row=1, column=1, pady=(30, 0), padx=(0, 0), sticky=W)

num1 = Entry(main)
num2 = Entry(main)
num3 = Entry(main)
num4 = Entry(main)

label_result = Label(main)

num1.grid(row=1, column=0, pady=(5, 25), padx=(30, 30))
num2.grid(row=1, column=1, pady=(5, 25), padx=(0, 10), sticky=W)
num3.grid(row=2, column=1, pady=(5, 25), padx=(0, 10), sticky=W)
num4.grid(row=2, column=0, pady=(5, 25), padx=(30, 30))

label_result.grid(row=3, column=1, pady=(0, 25), padx=(0, 75), sticky=W)

Button(main, text='Show Percentage', command=show_answer, borderwidth=5).grid(row=3, column=0, pady=(5, 25), padx=(0, 25))

mainloop()

#################################################################################

Hello World (4 Button Option)
#################################################################################

from tkinter import *


def show_green():
    main.config(bg='green')
    Label(main, text="Hello World ", bg="light green", font=("Helvetica", 16)).grid(row=0, pady=(15, 15), padx=(35, 0))
    return


def show_red():
    main.config(bg='red')
    Label(main, text="Hello World ", bg="#FF6969", font=("Helvetica", 16)).grid(row=0, pady=(15, 15), padx=(35, 0))
    return


def show_yellow():
    main.config(bg='yellow')
    Label(main, text="Hello World ", bg="#FFFD96", font=("Helvetica", 16)).grid(row=0, pady=(15, 15), padx=(35, 0))
    return


def show_blue():
    main.config(bg='blue')
    Label(main, text="Hello World ", bg="light blue", font=("Helvetica", 16)).grid(row=0, pady=(15, 15), padx=(35, 0))
    return


main = Tk()
main.geometry('225x250')
main.resizable(False, False)
main.config(bg="white")
main.title('Button Color Options')
Label(main, text="Hello World ", bg="white", font=("Helvetica", 16)).grid(row=0, pady=(15, 15), padx=(35, 0))
Button(main, text='Click for message in Green', command=show_green, borderwidth=5).grid(row=1, column=0, pady=(5, 5), padx=(35, 0))
Button(main, text='Click for message in Red', command=show_red, borderwidth=5).grid(row=2, column=0, pady=(5, 5), padx=(35, 0))
Button(main, text='Click for message in Yellow', command=show_yellow, borderwidth=5).grid(row=3, column=0, pady=(5, 5), padx=(35, 0))
Button(main, text='Click for message in Blue', command=show_blue, borderwidth=5).grid(row=4, column=0, pady=(5, 5), padx=(35, 0))

mainloop()

#################################################################################

Addition Program
#################################################################################

from tkinter import *


def show_answer():
    comp1 = E1.get()
    comp2 = E2.get()
    answ1 = float(comp1) + float(comp2)
    ans1.config(bg="light gray", font=("Helvetica", 12), text="%.2f" % answ1)
    return


root = Tk()
root.geometry('300x300')
root.resizable(False, False)
root.config(bg="light gray")
root.title('Addition Program')

w = Label(root, text="Addition Program", pady=10, bg="light gray", font=("Helvetica", 16, "bold"))
w.pack()
w = Label(root, text="Enter first number:", bg="light gray", font=("Helvetica", 12))
w.pack()
E1 = Entry(root, width=20)
E1.pack()
w = Label(root, text="Enter second number:", bg="light gray", font=("Helvetica", 12))
w.pack()
E2 = Entry(root, width=20)
E2.pack()
w = Label(root, pady=5, bg="light gray")
w.pack()
btn = Button(root, text="Add", bg="light gray", pady=5, padx=15, command=show_answer)
btn.pack()
w = Label(root, pady=2, bg="light gray")
w.pack()
w = Label(root, text="Sum:", bg="light gray", font=("Helvetica", 12))
ans1 = Label(root, bg="light gray", font=("Helvetica", 12))
w.pack()
ans1.pack()

mainloop()

#################################################################################

Binary Conversion Program
#################################################################################

from tkinter import *


def show_answer():
    comp1 = num1.get()
    comp2 = str(num1.get())
    answ1 = ord(comp1)
    res = ' '.join(format(ord(i), 'b') for i in comp2)
    label_result1.config(width=9, bg="black", fg="light green", font=("Helvetica", 20, "bold"), text="0%s" % res)
    label_result.config(width=5, bg="black", fg="light green", font=("Helvetica", 16, "bold"), text="%d" % answ1)
    return


main = Tk()
main.geometry('{}x{}'.format(700, 350))
main.resizable(False, False)
main.config(bg="light gray")
main.title('Binary Conversion Program')
top_frame = Frame(main, bg="light gray", width=700, height=40)
mid_frame = Frame(main, bg="light gray", width=700, height=10)
btm_frame = Frame(main, bg="light gray", width=700, height=50)

main.grid_rowconfigure(1, weight=1)
main.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
mid_frame.grid(row=1, sticky="ew")
btm_frame.grid(row=2, sticky="ew")

Label(top_frame, text="Binary Conversion Program", bg="light gray", font=("Helvetica", 16, "bold")).grid(row=0, padx=(210, 0), pady=(15, 15), sticky='w')
Label(top_frame, text="Enter a character from the  keyboard into the text box on the left. When you click the Convert ", bg="light gray", font=("Helvetica", 10)).grid(row=1, padx=(75, 0))
Label(top_frame, text="button it will display the ASCII value that is used to represent it in binary and decimal form.", bg="light gray", font=("Helvetica", 10)).grid(row=2, padx=(55, 0))

num1 = Entry(mid_frame, width=3, justify=CENTER)
num1.grid(row=0, column=0, pady=(0, 25), padx=(15, 15), sticky='nw', ipady=10)

Button(mid_frame, text='Convert', command=show_answer, borderwidth=5).grid(row=0, column=1, pady=(5, 5), padx=(0, 25),
                                                                           sticky='nw')
Label(mid_frame, text=" 128  64  32  16  8  4  2  1 ", bg="light gray", font=("Helvetica", 12)).grid(row=0, column=2, padx=(117, 0), sticky='w')
label_result1 = Label(mid_frame, bg="light gray")
label_result1.grid(row=1, column=2, sticky='w', padx=(131, 0))

Label(btm_frame, text="Decimal Representation", bg="light gray", font=("Helvetica", 12)).grid(row=0, column=2, padx=(259, 0), sticky='nw')
label_result = Label(btm_frame, bg="light gray")
label_result.grid(row=1, column=2, sticky='w', padx=(312, 0), pady=(0, 20))

mainloop()

#################################################################################

Film Inventory Search Program
#################################################################################

from tkinter import *

title_list = ["Casablanca", "Citizen Kane", "E.T.", "Finding Nemo", "Gone with the Wind", "It's a "
                                                                                                         "Wonderful "
                                                                                                         "Life",
                             "Jaws", "Jurassic Park", "King Kong", "Lawrence of Arabia", "Lord of the Rings",
                             "Psycho", "Schindler's List", "Shrek", "Star Wars", "Terminator II", "The Godfather",
                             "The Graduate", "Vertigo", "Wizard of Oz"]


def sequential():
    comp1 = str(E1.get())
    location = title_list.index(comp1) + 1
    del title_list[location:]
    for k in title_list:
        listboxF.insert(END, k)
    listboxF.insert(END, comp1.upper() + " FOUND!")
    listboxF.insert(END, str(location) + " comparisons were made")
    return


def binary():
    return


main = Tk()
main.geometry('{}x{}'.format(700, 550))
main.resizable(False, False)
main.config(bg="light gray")
main.title('Binary Conversion Program')
top_frameL = Frame(main, bg="light gray", width=425, height=150)
top_frameR = Frame(main, bg="light gray", width=425, height=150)

btm_frameL = Frame(main, bg="light gray", width=350, height=450)
btm_frameR = Frame(main, bg="light gray", width=350, height=150)

top_frameL.pack()
top_frameR.pack()
btm_frameL.pack(side=LEFT, anchor='n', fill=BOTH, padx=(25, 0))
btm_frameR.pack(side=LEFT, anchor='n', fill=BOTH)

w = Label(top_frameL, text="Film Inventory Search", bg="light gray", font=("Helvetica", 16, "bold"))
w.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

btn = Button(top_frameL, text='Sequential Search', command=sequential, borderwidth=5)
btn.pack(side=RIGHT, padx=(75, 75), pady=(20, 0))

w1 = Label(top_frameR, text="Enter a film name", bg="light gray", font=("Helvetica", 14))
w1.pack(side=LEFT, padx=(0, 10), anchor='e', pady=(20, 0))

E1 = Entry(top_frameR, width=25)
E1.pack(side=LEFT, padx=(0, 110), pady=(20, 0))

btn1 = Button(top_frameR, text='Binary Search', command=binary, borderwidth=5)
btn1.pack(padx=(0, 125), pady=(5, 0), side=LEFT)

w1 = Label(btm_frameL, text="List of names", bg="light gray", font=("Helvetica", 13))
w1.pack(anchor='nw', pady=(25, 0), padx=(5, 5))

listboxE = Listbox(btm_frameL, width=40, height=100, borderwidth=5)
listboxE.pack(pady=(0, 25), padx=(5, 5))

for i in title_list:
    listboxE.insert(END, i)

w1 = Label(btm_frameR, text="Search log", bg="light gray", font=("Helvetica", 13))
w1.pack(anchor='nw', pady=(25, 0), padx=(5, 5))

listboxF = Listbox(btm_frameR, width=60, height=100, borderwidth=5)
listboxF.pack(padx=(0, 5), pady=(0, 25))

mainloop()

#################################################################################

Sorting Program
#################################################################################

