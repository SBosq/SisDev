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
