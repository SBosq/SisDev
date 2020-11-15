# Simple enough, just import everything from tkinter.
import ipcalc
from sympy import *
from sympy import sympify
from sympy.integrals import laplace_transform
from tkinter import *
from scapy.all import *
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import PolynomialFeatures
from pandas import DataFrame
from t1 import data

# Used to check which interfaces are available and which are recognized by npcap

"""print(get_windows_if_list())
print(get_if_list())"""

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Application(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, parent=0):
        Frame.__init__(self, parent, bg="rosy brown")
        self.top_frameL = Frame(self, bg='rosy brown', width=425, height=150)
        self.btm_frameL = Frame(self, bg='rosy brown', width=425, height=150)
        self.top_frameR = Frame(self.btm_frameL, bg='rosy brown', width=425, height=150)

        self.top_frameL.pack()
        self.top_frameR.pack()
        self.btm_frameL.pack(pady=(0, 10))

        # top_frameL is used here

        self.w = Label(self.top_frameL, text="Sniffer", font=("Helvetica", 18, "bold"), bg='rosy brown')
        self.w.pack(pady=(20, 10), side=LEFT)

        self.v = IntVar(self)
        # self.v.set(1)

        languages = [
            ("Ethernet Adapter 1", 1),
            ("Ethernet Adapter 2", 2),
            ("LAN Adapter 1", 3),
            ("LAN Adapter 2", 4),
            ("Wi-Fi Adapter", 5)
        ]

        # top_frameR is used here

        self.L1 = Label(self.top_frameR,
                        text="""Choose where you want to sniff packets from: \n """,
                        justify=LEFT,
                        padx=20, bg='rosy brown', font=("Helvetica", 14)).pack()

        # btm_frameL is used here

        for val, language in enumerate(languages):
            self.R1 = Radiobutton(self.btm_frameL,
                                  text=language,
                                  padx=20,
                                  variable=self.v,
                                  value=val, bg='rosy brown', font=("Helvetica", 14)).pack()

        self.L2 = Label(self.btm_frameL, text="Select TCP, UDP, or ICMP: ", font=("Helvetica", 14), bg='rosy brown')
        self.L2.pack(pady=(20, 0))

        self.Ent = Entry(self.btm_frameL, width=15, font=("Helvetica", 14))
        self.Ent.pack(pady=(10, 10))

        self.btn = Button(self.btm_frameL, text='Begin Scan', command=self.ipdetails, borderwidth=5,
                          font=("Helvetica", 14))  # , command=self.ipdetails
        self.btn.pack(pady=(10, 10), anchor='s')

        self.scrollbar = Scrollbar(self.btm_frameL, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.S2 = Text(self.btm_frameL, height=8, width=60, borderwidth=5, font=("Helvetica", 14))
        self.S2.pack(padx=10, pady=(5, 0), fill=BOTH)
        self.S2.config(state=DISABLED)
        self.S2.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.S2.yview)

        self.w1 = Label(self, text="Which packet do you want more information on: ", font=("Helvetica", 14),
                        bg='rosy brown')
        self.w1.pack(pady=(20, 10))

        self.entry1 = Entry(self, width=15)
        self.entry1.config(font=("Helvetica", 14))
        self.entry1.pack()

        self.btn1 = Button(self, text='Get Info', command=self.moreinfo, borderwidth=5,
                           font=("Helvetica", 14))  # , command=self.moreinfo
        self.btn1.pack(pady=(15, 5), anchor='s')

        self.scrollbar1 = Scrollbar(self, orient="vertical")
        self.scrollbar1.pack(side=RIGHT, fill=Y)

        self.S3 = Text(self, height=8, width=60, borderwidth=5, font=("Helvetica", 14))
        self.S3.pack(padx=10, pady=10, fill=BOTH)
        self.S3.config(state=DISABLED)
        self.S3.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.S3.yview)

        sys.stdout = self
        self.pack()

        # reference to the parent widget, which is the tk window
        self.parent = parent

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Sniffer")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="IP Calculator", command=self.create_window)
        filemenu.add_command(label="Laplace Transforms", command=self.create_window1)
        filemenu.add_command(label="Simple Linear Regression", command=self.create_window2)
        filemenu.add_command(label="Quadratic Linear Regression", command=self.create_window3)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Programs", menu=filemenu)

    def ipdetails(self):
        self.S2.config(state=NORMAL)
        global a
        Val = self.v.get()
        fil = self.Ent.get()
        fill = fil.lower()
        self.S2.delete(END)
        if Val == 0 and fill == "tcp":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", filter="tcp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 0 and fill == "udp":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", filter="udp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 0 and fill == "icmp":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", filter="icmp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 0 and fill == "":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)

        if Val == 1 and fill == "tcp":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", filter="tcp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 1 and fill == "udp":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", filter="udp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 1 and fill == "icmp":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", filter="icmp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 1 and fill == "":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)

        if Val == 2 and fill == "tcp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", filter="tcp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 2 and fill == "udp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", filter="udp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 2 and fill == "icmp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", filter="icmp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 2 and fill == "":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)

        if Val == 3 and fill == "tcp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", filter="tcp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 3 and fill == "udp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", filter="udp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 3 and fill == "icmp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", filter="icmp", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 3 and fill == "":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)

        if Val == 4 and fill == "tcp":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", filter="tcp",
                      count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 4 and fill == "udp":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", filter="udp",
                      count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 4 and fill == "icmp":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", filter="icmp",
                      count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)
        if Val == 4 and fill == "":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", count=25)
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)

    def moreinfo(self):
        self.S3.config(state=NORMAL)
        pos = int(self.entry1.get())
        if pos > 25:
            print("Out of bounds")
            self.S3.config(state=DISABLED)
        else:
            neu = int(pos - 1)
            print(a[neu])
            self.S3.config(state=DISABLED)

    def create_window1(self):
        newWindow1 = Toplevel(self)
        newWindow1.geometry('{}x{}'.format(750, 550))
        newWindow1.resizable(False, False)
        newWindow1.config(bg="rosy brown")
        newWindow1.title('Laplace Transforms')
        self.top_frame1 = Frame(newWindow1, bg='rosy brown', width=425, height=150)
        self.top_frame2 = Frame(newWindow1, bg='rosy brown', width=425, height=150)
        self.top_frame2R = Frame(self.top_frame2, bg='rosy brown')
        self.btm_frame = Frame(newWindow1, bg='rosy brown', width=700, height=450)

        self.top_frame1.pack()
        self.top_frame2.pack()
        self.top_frame2R.pack(side=RIGHT)
        self.btm_frame.pack(anchor='s')

        self.w = Label(self.top_frame1, text="Transformada de Laplace", bg='rosy brown', font=("Helvetica", 18, "bold"))
        self.w.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

        self.btn = Button(self.top_frame2R, text='Calcular!', borderwidth=5, command=self.answers)

        self.w1 = Label(self.top_frame2, text='Ingrese el primer elemento de f(t): ', bg='rosy brown',
                        font=("Helvetica", 15))
        self.w1.pack(padx=(10, 10), anchor='nw', pady=(20, 0))
        self.E1 = Entry(self.top_frame2, width=15)
        self.E1.config(font=("Helvetica", 14))
        self.E1.pack(padx=(10, 10), pady=(5, 5))

        self.w2 = Label(self.top_frame2, text='Ingrese el segundo elemento de f(t): ', bg='rosy brown',
                        font=("Helvetica", 15))
        self.w2.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
        self.E2 = Entry(self.top_frame2, width=15)
        self.E2.config(font=("Helvetica", 14))
        self.E2.pack(padx=(10, 10), pady=(5, 5))

        self.w3 = Label(self.top_frame2, text='Ingrese el tercero elemento de f(t): ', bg='rosy brown',
                        font=("Helvetica", 15))
        self.w3.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
        self.E3 = Entry(self.top_frame2, width=15)
        self.E3.config(font=("Helvetica", 14))
        self.E3.pack(padx=(10, 10), pady=(5, 5))

        self.w4 = Label(self.top_frame2, text='Ingrese el cuarto elemento de f(t): ', bg='rosy brown',
                        font=("Helvetica", 15))
        self.w4.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
        self.E4 = Entry(self.top_frame2, width=15)
        self.E4.config(font=("Helvetica", 14))
        self.E4.pack(padx=(10, 10), pady=(5, 5))

        self.w5 = Label(self.top_frame2, text='Ingrese el quinto elemento de f(t): ', bg='rosy brown',
                        font=("Helvetica", 15))
        self.w5.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
        self.E5 = Entry(self.top_frame2, width=15)
        self.E5.config(font=("Helvetica", 14))
        self.E5.pack(padx=(10, 10), pady=(5, 5))

        # S1 = tk.Scrollbar(top_frame2R)
        self.S2 = Text(self.top_frame2R, height=5, width=35, borderwidth=5)
        # S1.pack(side=tk.RIGHT, fill=tk.Y, pady=(10, 0), anchor='e')
        self.S2.pack(padx=(0, 10), fill=Y)
        self.btn.config(font=("Helvetica", 14))
        self.btn.pack(padx=(75, 75), pady=(50, 0))
        # S1.config(command=S2.yview)
        self.S2.config(font=("Helvetica", 14))  # yscrollcommand=S1.set,

        inst = """Para poder evaluar potencias es necesario    usar (**), 2**4 seria 16. Para multiplicar un       numero con una variable tendras que separar los usando un *. """

        self.S2.insert(END, inst)
        self.S2.config(state=DISABLED)

        self.A1 = Label(self.btm_frame, text='Respuesta: ', bg='rosy brown', font=("Helvetica", 16, "bold"))
        self.A1.pack(anchor='n', pady=(30, 0))

        self.S1 = Scrollbar(self.btm_frame, orient='horizontal')
        self.A2 = Entry(self.btm_frame, width=30)
        self.A2.config(xscrollcommand=self.S1.set)
        self.A2.pack(anchor='n', pady=(15, 0))
        self.S1.config(command=self.A2.xview)
        self.S1.pack(fill=X, anchor='s')

    def create_window2(self):
        newWindow2 = Toplevel(self)
        newWindow2.geometry('{}x{}'.format(750, 650))
        newWindow2.resizable(False, False)
        newWindow2.config(bg="rosy brown")
        newWindow2.title('Regresion Linear Simple')

        self.top_frameL2 = Frame(newWindow2, bg="rosy brown", width=425, height=150)
        self.top_frameR2 = Frame(newWindow2, bg="rosy brown", width=425, height=150)

        self.btm_frameR2 = Frame(newWindow2, bg="rosy brown", width=425, height=150)
        self.btm_frameR3 = Frame(newWindow2, bg="rosy brown", width=425, height=150)

        self.top_frameL2.pack()
        self.top_frameR2.pack()
        self.btm_frameR2.pack(anchor='n', fill=BOTH)
        self.btm_frameR3.pack(anchor='n', fill=BOTH)

        self.w11 = Label(self.top_frameL2, text="Regresion Linear Simple", bg="rosy brown",
                         font=("Helvetica", 18, "bold"))
        self.w11.pack(pady=(20, 0))

        self.btn11 = Button(self.btm_frameR2, text='Respuesta!', borderwidth=5, command=self.solution,
                            font=("Helvetica", 16))
        self.btn11.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

        self.btn111 = Button(self.btm_frameR2, text='CE', borderwidth=5, command=self.otra, font=("Helvetica", 16))
        self.btn111.pack(pady=(30, 0), side=LEFT, anchor='n')

        self.w111 = Label(self.top_frameR2, text="Valores de x: ", bg="rosy brown", font=("Helvetica", 16, "bold"))
        self.w111.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

        self.E111 = Entry(self.top_frameR2, font=("Helvetica", 14), width=50)
        self.E111.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

        self.w211 = Label(self.top_frameR2, text="Valores de y: ", bg="rosy brown", font=("Helvetica", 16, "bold"))
        self.w211.pack(padx=(0, 10), anchor='sw')

        self.E211 = Entry(self.top_frameR2, font=("Helvetica", 14), width=50)
        self.E211.pack(padx=(0, 25), anchor='sw')

        self.w311 = Label(self.btm_frameR3, text="Regresion Linear Simple: ", bg="rosy brown",
                          font=("Helvetica", 16, "bold"))
        self.w311.pack(anchor='n', pady=(25, 0), padx=(20, 0))

        self.listboxF11 = Listbox(self.btm_frameR3, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
        self.listboxF11.pack(padx=(18, 5), pady=(0, 25))

    def create_window(self):
        newWindow = Toplevel(self)
        newWindow.title("IP Calculator")
        newWindow.config(bg='rosy brown')
        newWindow.geometry('{}x{}'.format(775, 675))
        newWindow.resizable(False, False)
        self.top = Frame(newWindow, bg='rosy brown')
        self.top.pack()
        self.top1 = Frame(newWindow, bg='rosy brown')
        self.top1.pack()
        self.mid1 = Frame(newWindow, bg='rosy brown')
        self.mid1.pack()
        self.mid2 = Frame(newWindow, bg='rosy brown')
        self.mid2.pack()
        self.bot = Frame(newWindow, bg='rosy brown')
        self.bot.pack()

        self.Label4 = Label(self.top, text="IP Calculator", font=("Helvetica", 18, "bold"), bg='rosy brown')
        self.Label4.pack(anchor='nw', pady=(10, 0))

        self.Label1 = Label(self.top1, text="Enter Host/Network: ", font=("Helvetica", 14), bg='rosy brown')
        self.Label1.pack(side=LEFT, anchor='nw', pady=(10, 0))

        self.Ent1 = Entry(self.top1, width=15)
        self.Ent1.config(font=("Helvetica", 14))
        self.Ent1.pack(side=LEFT, anchor='ne', pady=(15, 0))

        self.Label2 = Label(self.mid1, text="Enter Netmask: ", font=("Helvetica", 14), bg='rosy brown')
        self.Label2.pack(side=LEFT, anchor='w', pady=(10, 0))

        self.Ent2 = Entry(self.mid1, width=15)
        self.Ent2.config(font=("Helvetica", 14))
        self.Ent2.pack(side=LEFT, anchor='e', pady=(15, 0))

        self.btn3 = Button(self.mid2, text="Calculate", font=("Helvetica", 14), command=self.ipfig)
        self.btn3.pack(pady=(15, 0))

        self.Label3 = Label(self.bot, text="Results: ", font=("Helvetica", 18, 'bold'), bg='rosy brown')
        self.Label3.pack(anchor='n', pady=(10, 0))

        self.S1 = Text(self.bot, height=18, width=21, font=("Helvetica", 14), borderwidth=5)
        self.S1.tag_configure("left", justify="left")
        self.S1.tag_add("left", 1.0, "end")
        self.S1.pack(side=LEFT, padx=(0, 10), pady=(15, 0), fill=BOTH, anchor='w')
        self.S1.config(state=DISABLED)

        self.S4 = Text(self.bot, height=18, width=45, font=("Helvetica", 14), borderwidth=5)
        self.S4.tag_configure("right", justify="right")
        self.S4.tag_add("right", 1.0, "end")
        self.S4.pack(side=LEFT, padx=(0, 5), pady=(15, 0), fill=BOTH, anchor='w')
        self.S4.config(state=DISABLED)

    def create_window3(self):
        newWindow3 = Toplevel(self)
        newWindow3.title("Regresion Linear Cuadratico")
        newWindow3.config(bg='rosy brown')
        newWindow3.geometry('{}x{}'.format(775, 675))
        newWindow3.resizable(False, False)
        self.top3 = Frame(newWindow3, bg='rosy brown')
        self.top13 = Frame(newWindow3, bg='rosy brown')
        self.mid3 = Frame(newWindow3, bg='rosy brown')
        self.mid13 = Frame(newWindow3, bg='rosy brown')

        self.top3.pack()
        self.top13.pack()
        self.mid3.pack(anchor='n', fill=BOTH)
        self.mid13.pack(anchor='n', fill=BOTH)

        self.Label43 = Label(self.top3, text="Regresion Linear Cuadratica", bg="rosy brown",
                             font=("Helvetica", 18, "bold"))
        self.Label43.pack(pady=(20, 0))

        self.btnM3 = Button(self.mid3, text='Respuesta!', borderwidth=5, command=self.solutionM, font=("Helvetica", 16))
        self.btnM3.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

        self.btnM13 = Button(self.mid3, text='CE', borderwidth=5, command=self.otraM, font=("Helvetica", 16))
        self.btnM13.pack(pady=(30, 0), side=LEFT, anchor='n')

        self.Label53 = Label(self.top13, text="Valores de x: ", bg="rosy brown", font=("Helvetica", 16, "bold"))
        self.Label53.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

        self.E33 = Entry(self.top13, font=("Helvetica", 14), width=50)
        self.E33.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

        self.Label63 = Label(self.top13, text="Valores de y: ", bg="rosy brown", font=("Helvetica", 16, "bold"))
        self.Label63.pack(padx=(0, 10), anchor='sw')

        self.E43 = Entry(self.top13, font=("Helvetica", 14), width=50)
        self.E43.pack(padx=(0, 25), anchor='sw')

        self.Label63 = Label(self.mid13, text="Regresion Linear Cuadratica: ", bg="rosy brown",
                             font=("Helvetica", 16, "bold"))
        self.Label63.pack(anchor='n', pady=(25, 0), padx=(20, 0))

        self.listboxM3 = Listbox(self.mid13, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
        self.listboxM3.pack(padx=(18, 5), pady=(0, 25))

    def solutionM(self):
        lista1M = []
        lista2M = []
        lista3M = []
        lista4M = []
        lista5M = []
        lista6M = []
        a = list(map(float, self.E33.get().split()))
        b = list(map(float, self.E43.get().split()))
        x = np.array(a)
        y = np.array(b)
        x1 = np.column_stack((x, y))
        # Calculo de x^2
        for i in range(len(y)):
            lista1M.append(x[i] * x[i])
        lixM = np.array(lista1M)
        # Calculo de x^3
        for i in range(len(y)):
            lista2M.append(x[i] * x[i] * x[i])
        lix2M = np.array(lista2M)
        # Calculo de x^4
        for i in range(len(y)):
            lista3M.append(x[i] * x[i] * x[i] * x[i])
        lix3M = np.array(lista3M)
        # Calculo de xy
        for i in range(len(y)):
            lista4M.append(x[i] * y[i])
        lixyM = np.array(lista4M)
        # Calculo de x^2y
        for i in range(len(y)):
            lista5M.append(x[i] * x[i] * y[i])
        lix2yM = np.array(lista5M)
        # Sumas
        sum1M = x.sum()
        sum2M = y.sum()
        sum3M = lixM.sum()
        sum4M = lix2M.sum()
        sum5M = lix3M.sum()
        sum6M = lixyM.sum()
        sum7M = lix2yM.sum()

        # Metodo crammer
        def sarrus(A):
            val = ((A[0][0] * A[1][1] * A[2][2]) +
                   (A[0][1] * A[1][2] * A[2][0]) +
                   (A[0][2] * A[1][0] * A[2][1])) - \
                  ((A[2][0] * A[1][1] * A[0][2]) +
                   (A[2][1] * A[1][2] * A[0][0]) +
                   (A[2][2] * A[1][0] * A[0][1]))
            return val

        sismat = [[0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0]]
        res = [0.0, 0.0, 0.0]
        sismat[0][0] = len(y)
        sismat[0][1] = sum1M
        sismat[0][2] = sum3M
        sismat[0][3] = sum2M

        sismat[1][0] = sum1M
        sismat[1][1] = sum3M
        sismat[1][2] = sum4M
        sismat[1][3] = sum6M

        sismat[2][0] = sum3M
        sismat[2][1] = sum4M
        sismat[2][2] = sum5M
        sismat[2][3] = sum7M

        mat_x = [[sismat[0][3], sismat[0][1], sismat[0][2]],
                 [sismat[1][3], sismat[1][1], sismat[1][2]],
                 [sismat[2][3], sismat[2][1], sismat[2][2]]]
        mat_y = [[sismat[0][0], sismat[0][3], sismat[0][2]],
                 [sismat[1][0], sismat[1][3], sismat[1][2]],
                 [sismat[2][0], sismat[2][3], sismat[2][2]]]
        mat_z = [[sismat[0][0], sismat[0][1], sismat[0][3]],
                 [sismat[1][0], sismat[1][1], sismat[1][3]],
                 [sismat[2][0], sismat[2][1], sismat[2][3]]]
        det_mat = sarrus(sismat)
        if det_mat == 0:
            self.listboxM3.insert(0, "Determinante de A nulo...")
        else:
            det_matx = sarrus(mat_x)
            det_maty = sarrus(mat_y)
            det_matz = sarrus(mat_z)
            res[0] = det_matx / det_mat
            res[1] = det_maty / det_mat
            res[2] = det_matz / det_mat
            self.listboxM3.insert(0, "P => " + " " + str(res))
        A = res[0]
        b1 = res[1]
        b2 = res[2]
        ##Calculo de ygorrito
        for i in range(len(y)):
            lista6M.append((b2 * lixM[i]) + (b1 * x[i]) + A)
        liygorr = np.array(lista6M)
        pf = PolynomialFeatures(degree=2)
        X = pf.fit_transform(x.reshape(-1, 1))
        regresion_lineal = LinearRegression()
        regresion_lineal.fit(X, y)
        r2 = regresion_lineal.score(X, y)
        self.listboxM3.insert(0, "El modelo de regresion es: " + str(round(b2, 3)) + "x^2" + " + " + str(
            round(b1, 3)) + "x" + " + " + str(
            round(A, 3)))
        self.listboxM3.insert(0, "r2: " + " " + str(round(r2, 3)))
        self.listboxM3.insert(0, "liygorr: " + " " + str(liygorr))
        matri = []
        for i in range(len(b)):
            matri.append([b[i], liygorr[i], abs(round(b[i] - liygorr[i], 3))])
        data = DataFrame(matri, columns=['y', 'ygorr', 'diff'])
        self.listboxM3.insert(0, data)
        poly_reg = PolynomialFeatures(degree=2)
        X_poly = poly_reg.fit_transform(x.reshape(-1, 1))
        lin_reg2 = LinearRegression()
        lin_reg2.fit(X_poly, y.reshape(-1, 1))
        y_pred = lin_reg2.predict(X_poly)
        plt.scatter(x, y, color='red')
        plt.plot(x, y_pred)
        plt.title("Regresion Linear Cuadratica")
        plt.show()

    def solution(self):
        lista3 = []
        lista4 = []
        lista5 = []
        lista6 = []
        lista7 = []
        a = list(map(float, self.E111.get().split()))
        b = list(map(float, self.E211.get().split()))
        x = np.array(a).reshape((-1, 1))
        y = np.array(b)
        # Multiplicacion de X*X guardada en lista3
        for i in range(len(x)):
            lista3.append(x[i] * x[i])
        lix = np.array(lista3)
        # Multiplicacion de Y*Y guardada en lista4
        for i in range(len(y)):
            lista4.append(y[i] * y[i])
        liy = np.array(lista4)
        # Multiplicacion de X*Y guardada en lista4
        for i in range(len(x)):
            lista5.append(x[i] * y[i])
        lixy = np.array(lista5)
        # Calculo de medias
        xmean = x.mean()
        ymean = y.mean()
        # Calculo de sumas
        sum1 = x.sum()
        sum2 = y.sum()
        sum3 = lix.sum()
        sum4 = liy.sum()
        sum5 = lixy.sum()
        per = float(len(x))
        # Calculo de SSxx y SSxy y ssyy
        ssxx = (sum3 - (math.pow(sum1, 2) / per))
        ssyy = (sum4 - (math.pow(sum2, 2) / per))
        ssxy = (sum5 - (sum1 * sum2 / per))
        # Calculo de b0 y b1
        b1 = (ssxy / ssxx)
        b0 = (ymean - (b1 * xmean))
        # Calculo de ygorrito
        for i in range(len(x)):
            lista6.append((b0 + (b1 * a[i])))
        # Calculo de SSE
        for i in range(len(x)):
            lista7.append(math.pow(b[i] - lista6[i], 2))
        lisse = np.array(lista7)
        # suma de SSE
        sum6 = lisse.sum()
        # Calculo de sb0, sb1, tb0 y tb1
        # Paso 1
        var1 = per - 2
        pas1 = (sum6 / var1)
        # Paso 2
        pas2 = (1 / per + (math.pow(xmean, 2) / ssxx))
        sb0 = math.sqrt(pas1 * pas2)
        sb1 = math.sqrt(sum6 / (var1 * ssxx))
        tb0 = b0 / sb0
        tb1 = b1 / sb1
        # Calculo de S, S^2 y R
        s2 = sum6 / var1
        s = math.sqrt(s2)
        r = (ssxy / (math.sqrt(ssxx * ssyy)))
        model = LinearRegression().fit(x, y)
        self.listboxF11.insert(0, "El modelo de regresion es: " + str(round(b0, 3)) + " + " + str(round(b1, 3)) + "x")
        self.listboxF11.insert(0, "r: " + " " + str(round(r, 3)))
        self.listboxF11.insert(0, "s2: " + " " + str(round(s2, 3)))
        self.listboxF11.insert(0, "s: " + " " + str(round(s, 3)))
        self.listboxF11.insert(0, "tb1: " + " " + str(round(tb1, 3)))
        self.listboxF11.insert(0, "tb0: " + " " + str(round(tb0, 3)))
        self.listboxF11.insert(0, "sb1: " + " " + str(round(b1, 3)))
        self.listboxF11.insert(0, "sb0: " + " " + str(round(sb0, 3)))
        self.listboxF11.insert(0, "b1: " + " " + str(round(b1, 3)))
        self.listboxF11.insert(0, "b0: " + " " + str(round(b0, 3)))
        self.E111.config(state=DISABLED)
        self.E211.config(state=DISABLED)
        self.listboxF11.config(state=DISABLED)
        y_pred = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, y_pred, color='red')
        plt.title("Regresion Linear Simple")
        plt.show()

    def otra(self):
        self.E111.config(state=NORMAL)
        self.E211.config(state=NORMAL)
        self.listboxF11.config(state=NORMAL)
        plt.close()
        self.E111.delete(0, 'end')
        self.E211.delete(0, 'end')
        self.listboxF11.delete(0, 'end')
        
    def otraM(self):
        self.E33.config(state=NORMAL)
        self.E43.config(state=NORMAL)
        self.listboxM3.config(state=NORMAL)
        plt.close()
        self.E33.delete(0, 'end')
        self.E43.delete(0, 'end')
        self.listboxM3.delete(0, 'end')

    def ipfig(self):
        self.S1.config(state=NORMAL)
        host = self.Ent1.get()
        ip = ipcalc.IP(host)
        mask = int(self.Ent2.get())
        print("Address: " + host + '\n')
        localnet = ipcalc.Network("%s/%d" % (host, mask))
        ipnm = ipcalc.IP(localnet.netmask())
        ipn = ipcalc.IP(localnet)
        ipbc = ipcalc.IP(localnet.broadcast())
        iphf = ipcalc.IP(localnet.host_first())
        iphl = ipcalc.IP(localnet.host_last())
        print("Netmask: " + str(localnet.netmask()) + '\n')
        print("Network: " + str(localnet) + '\n')
        print("Broadcast: " + str(localnet.broadcast()) + '\n')
        print("HostMin: " + str(localnet.host_first()) + '\n')
        print("HostMax: " + str(localnet.host_last()) + '\n')
        print("Hosts/Net: " + str(int(localnet.size()) - 2) + '\n')
        print("IP version: " + str(ip.version()))
        self.S1.config(state=DISABLED)

        self.S4.config(state=NORMAL)
        print("Bin Address: " + str(ip.bin()))
        print("Hex Address: " + str(ip.hex()) + '\n')

        print("Bin Netmask: " + str(ipnm.bin()))
        print("Hex Netmask: " + str(ipnm.hex()) + '\n')

        print("Bin Network: " + str(ipn.bin()))
        print("Hex Network: " + str(ipn.hex()) + '\n')

        print("Bin Broadcast: " + str(ipbc.bin()))
        print("Hex Broadcast: " + str(ipbc.hex()) + '\n')

        print("Bin HostMin: " + str(iphf.bin()))
        print("Hex HostMin: " + str(iphf.hex()) + '\n')

        print("Bin HostMax: " + str(iphl.bin()))
        print("Hex HostMax: " + str(iphl.hex()) + '\n')
        self.S4.config(state=DISABLED)

    def answers(self):
        global Answ1, Answ2, Answ3, Answ4, Answ5
        s, t, x, y, z = symbols('s t x y z')
        self.A2.delete(0, END)

        if self.E1.get() == '' or self.E1.get() == 0:
            Answ1 = ''
        else:
            if self.E1.index(0) == '-':
                Answ1 = sympify(laplace_transform(self.E1.get(), t, s, noconds=True))
                sig = '-'
                Answ1s = sig + Answ1
                self.A2.insert(0, Answ1s)
            else:
                Answ1 = sympify(laplace_transform(self.E1.get(), t, s, noconds=True))
                self.A2.insert(0, Answ1)

        if self.E2.get() == '' or self.E2.get() == 0:
            Answ2 = ''
        else:
            if self.E2.index(0) == '-':
                Answ2 = sympify(laplace_transform(self.E2.get(), t, s, noconds=True))
                sig = ' - '
                Answ2s = sig + Answ2
                self.A2.insert(END, Answ2s)
            else:
                Answ2 = sympify(laplace_transform(self.E2.get(), t, s, noconds=True))
                self.A2.insert(END, ' + ')
                self.A2.insert(END, Answ2)

        if self.E3.get() == '' or self.E3.get() == 0:
            Answ3 = ''
        else:
            if self.E3.index(0) == '-':
                Answ3 = sympify(laplace_transform(self.E3.get(), t, s, noconds=True))
                sig = ' - '
                Answ3s = sig + Answ3
                self.A2.insert(END, Answ3s)
            else:
                Answ3 = sympify(laplace_transform(self.E3.get(), t, s, noconds=True))
                self.A2.insert(END, ' + ')
                self.A2.insert(END, Answ3)

        if self.E4.get() == '' or self.E4.get() == 0:
            Answ4 = ''
        else:
            if self.E4.index(0) == '-':
                Answ4 = sympify(laplace_transform(self.E4.get(), t, s, noconds=True))
                sig = ' - '
                Answ4s = sig + Answ4
                self.A2.insert(END, Answ4s)
            else:
                Answ4 = sympify(laplace_transform(self.E4.get(), t, s, noconds=True))
                self.A2.insert(END, ' + ')
                self.A2.insert(END, Answ4)

        if self.E5.get() == '' or self.E5.get() == 0:
            Answ5 = ''
        else:
            if self.E5.index(0) == '-':
                Answ5 = sympify(laplace_transform(self.E5.get(), t, s, noconds=True))
                sig = ' - '
                Answ5s = sig + Answ5
                self.A2.insert(END, Answ5s)
            else:
                Answ5 = sympify(laplace_transform(self.E5.get(), t, s, noconds=True))
                self.A2.insert(END, ' + ')
                self.A2.insert(END, Answ5)

        self.A2.config(font=("Helvetica", 15))

    def flush(self):
        pass

    def write(self, txt):
        self.S2.insert(END, str(txt))
        self.S3.insert(END, str(txt))
        self.S1.insert(END, str(txt))
        self.S4.insert(END, str(txt))


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("710x1000")
root.resizable(False, False)

# creation of an instance
app = Application()

# mainloop
mainloop()

##########################################################################################################################
#                                                   t1.py                                                                #
##########################################################################################################################

"""from tkinter import *
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import math
from sklearn.preprocessing import PolynomialFeatures
from pandas import DataFrame
import scipy.stats
from scipy import stats


class Application(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, parent=0):
        Frame.__init__(self, parent, bg="thistle3")

        self.top_frameL = Frame(self, bg="thistle3", width=425, height=150)
        self.top_frameR = Frame(self, bg="thistle3", width=425, height=150)

        self.btm_frameR = Frame(self, bg="thistle3", width=425, height=150)
        self.btm_frameR1 = Frame(self, bg="thistle3", width=425, height=150)

        self.top_frameL.pack()
        self.top_frameR.pack()
        self.btm_frameR.pack(anchor='n', fill=BOTH)
        self.btm_frameR1.pack(anchor='n', fill=BOTH)

        w = Label(self.top_frameL, text="Regresion Linear Simple", bg="thistle3", font=("Helvetica", 18, "bold"))
        w.pack(pady=(20, 0))

        self.btn = Button(self.btm_frameR, text='Respuesta!', borderwidth=5, command=self.solutionS,
                          font=("Helvetica", 16))
        self.btn.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

        self.btn1 = Button(self.btm_frameR, text='CE', borderwidth=5, command=self.otra, font=("Helvetica", 16))
        self.btn1.pack(pady=(30, 0), side=LEFT, anchor='n')

        w1 = Label(self.top_frameR, text="Valores de x: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        w1.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

        self.E1 = Entry(self.top_frameR, font=("Helvetica", 14), width=50)
        self.E1.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

        self.w2 = Label(self.top_frameR, text="Valores de y: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        self.w2.pack(padx=(0, 10), anchor='sw')

        self.E2 = Entry(self.top_frameR, font=("Helvetica", 14), width=50)
        self.E2.pack(padx=(0, 25), anchor='sw')

        self.w3 = Label(self.btm_frameR1, text="Regresion Linear Simple: ", bg="thistle3",
                        font=("Helvetica", 16, "bold"))
        self.w3.pack(anchor='n', pady=(25, 0), padx=(20, 0))

        self.listboxF = Listbox(self.btm_frameR1, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
        self.listboxF.pack(padx=(18, 5), pady=(0, 25))

        sys.stdout = self
        self.pack()

        # reference to the parent widget, which is the tk window
        self.parent = parent

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

        # Creation of init_window

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Regresion Linear")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Regresion Linear Cuadratica", command=self.create_window)
        filemenu.add_command(label="Regresion Linear Multiple", command=self.create_window1)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Programs", menu=filemenu)

    def solutionS(self):
        lista3 = []
        lista4 = []
        lista5 = []
        lista6 = []
        lista7 = []
        a = list(map(float, self.E1.get().split()))
        b = list(map(float, self.E2.get().split()))
        x = np.array(a).reshape((-1, 1))
        y = np.array(b)
        # Multiplicacion de X*X guardada en lista3
        for i in range(len(x)):
            lista3.append(x[i] * x[i])
        lix = np.array(lista3)
        # Multiplicacion de Y*Y guardada en lista4
        for i in range(len(y)):
            lista4.append(y[i] * y[i])
        liy = np.array(lista4)
        # Multiplicacion de X*Y guardada en lista4
        for i in range(len(x)):
            lista5.append(x[i] * y[i])
        lixy = np.array(lista5)
        # Calculo de medias
        xmean = x.mean()
        ymean = y.mean()
        # Calculo de sumas
        sum1 = x.sum()
        sum2 = y.sum()
        sum3 = lix.sum()
        sum4 = liy.sum()
        sum5 = lixy.sum()
        per = float(len(x))
        # Calculo de SSxx y SSxy y ssyy
        ssxx = (sum3 - (math.pow(sum1, 2) / per))
        ssyy = (sum4 - (math.pow(sum2, 2) / per))
        ssxy = (sum5 - (sum1 * sum2 / per))
        # Calculo de b0 y b1
        b1 = (ssxy / ssxx)
        b0 = (ymean - (b1 * xmean))
        # Calculo de ygorrito
        for i in range(len(x)):
            lista6.append((b0 + (b1 * a[i])))
        # Calculo de SSE
        for i in range(len(x)):
            lista7.append(math.pow(b[i] - lista6[i], 2))
        lisse = np.array(lista7)
        # suma de SSE
        sum6 = lisse.sum()
        # Calculo de sb0, sb1, tb0 y tb1
        # Paso 1
        var1 = per - 2
        pas1 = (sum6 / var1)
        # Paso 2
        pas2 = (1 / per + (math.pow(xmean, 2) / ssxx))
        sb0 = math.sqrt(pas1 * pas2)
        sb1 = math.sqrt(sum6 / (var1 * ssxx))
        tb0 = b0 / sb0
        tb1 = b1 / sb1
        # Calculo de S, S^2 y R
        s2 = sum6 / var1
        s = math.sqrt(s2)
        r = (ssxy / (math.sqrt(ssxx * ssyy)))
        model = LinearRegression().fit(x, y)
        self.listboxF.insert(0, "El modelo de regresion es: " + str(round(b0, 3)) + " + " + str(round(b1, 3)) + "x")
        self.listboxF.insert(0, "r: " + " " + str(round(r, 3)))
        self.listboxF.insert(0, "s2: " + " " + str(round(s2, 3)))
        self.listboxF.insert(0, "s: " + " " + str(round(s, 3)))
        self.listboxF.insert(0, "tb1: " + " " + str(round(tb1, 3)))
        self.listboxF.insert(0, "tb0: " + " " + str(round(tb0, 3)))
        self.listboxF.insert(0, "sb1: " + " " + str(round(b1, 3)))
        self.listboxF.insert(0, "sb0: " + " " + str(round(sb0, 3)))
        self.listboxF.insert(0, "b1: " + " " + str(round(b1, 3)))
        self.listboxF.insert(0, "b0: " + " " + str(round(b0, 3)))
        self.E1.config(state=DISABLED)
        self.E2.config(state=DISABLED)
        self.listboxF.config(state=DISABLED)
        y_pred = model.predict(x)
        plt.scatter(x, y)
        plt.plot(x, y_pred, color='red')
        plt.title("Regresion Linear Simple")
        plt.show()

    def solutionM(self):
        lista1M = []
        lista2M = []
        lista3M = []
        lista4M = []
        lista5M = []
        lista6M = []
        a = list(map(float, self.E3.get().split()))
        b = list(map(float, self.E4.get().split()))
        x = np.array(a)
        y = np.array(b)
        x1 = np.column_stack((x, y))
        # Calculo de x^2
        for i in range(len(y)):
            lista1M.append(x[i] * x[i])
        lixM = np.array(lista1M)
        # Calculo de x^3
        for i in range(len(y)):
            lista2M.append(x[i] * x[i] * x[i])
        lix2M = np.array(lista2M)
        # Calculo de x^4
        for i in range(len(y)):
            lista3M.append(x[i] * x[i] * x[i] * x[i])
        lix3M = np.array(lista3M)
        # Calculo de xy
        for i in range(len(y)):
            lista4M.append(x[i] * y[i])
        lixyM = np.array(lista4M)
        # Calculo de x^2y
        for i in range(len(y)):
            lista5M.append(x[i] * x[i] * y[i])
        lix2yM = np.array(lista5M)
        # Sumas
        sum1M = x.sum()
        sum2M = y.sum()
        sum3M = lixM.sum()
        sum4M = lix2M.sum()
        sum5M = lix3M.sum()
        sum6M = lixyM.sum()
        sum7M = lix2yM.sum()

        # Metodo crammer
        def sarrus(A):
            val = ((A[0][0] * A[1][1] * A[2][2]) +
                   (A[0][1] * A[1][2] * A[2][0]) +
                   (A[0][2] * A[1][0] * A[2][1])) - \
                  ((A[2][0] * A[1][1] * A[0][2]) +
                   (A[2][1] * A[1][2] * A[0][0]) +
                   (A[2][2] * A[1][0] * A[0][1]))
            return val

        sismat = [[0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0]]
        res = [0.0, 0.0, 0.0]
        sismat[0][0] = len(y)
        sismat[0][1] = sum1M
        sismat[0][2] = sum3M
        sismat[0][3] = sum2M

        sismat[1][0] = sum1M
        sismat[1][1] = sum3M
        sismat[1][2] = sum4M
        sismat[1][3] = sum6M

        sismat[2][0] = sum3M
        sismat[2][1] = sum4M
        sismat[2][2] = sum5M
        sismat[2][3] = sum7M

        mat_x = [[sismat[0][3], sismat[0][1], sismat[0][2]],
                 [sismat[1][3], sismat[1][1], sismat[1][2]],
                 [sismat[2][3], sismat[2][1], sismat[2][2]]]
        mat_y = [[sismat[0][0], sismat[0][3], sismat[0][2]],
                 [sismat[1][0], sismat[1][3], sismat[1][2]],
                 [sismat[2][0], sismat[2][3], sismat[2][2]]]
        mat_z = [[sismat[0][0], sismat[0][1], sismat[0][3]],
                 [sismat[1][0], sismat[1][1], sismat[1][3]],
                 [sismat[2][0], sismat[2][1], sismat[2][3]]]
        det_mat = sarrus(sismat)
        if det_mat == 0:
            self.listboxM.insert(0, "Determinante de A nulo...")
        else:
            det_matx = sarrus(mat_x)
            det_maty = sarrus(mat_y)
            det_matz = sarrus(mat_z)
            res[0] = det_matx / det_mat
            res[1] = det_maty / det_mat
            res[2] = det_matz / det_mat
            self.listboxM.insert(0, "P => " + " " + str(res))
        A = res[0]
        b1 = res[1]
        b2 = res[2]
        ##Calculo de ygorrito
        for i in range(len(y)):
            lista6M.append((b2 * lixM[i]) + (b1 * x[i]) + A)
        liygorr = np.array(lista6M)
        pf = PolynomialFeatures(degree=2)
        X = pf.fit_transform(x.reshape(-1, 1))
        regresion_lineal = LinearRegression()
        regresion_lineal.fit(X, y)
        r2 = regresion_lineal.score(X, y)
        self.listboxM.insert(0, "El modelo de regresion es: " + str(round(b2, 3)) + "x^2" + " + " + str(
            round(b1, 3)) + "x" + " + " + str(
            round(A, 3)))
        self.listboxM.insert(0, "r2: " + " " + str(round(r2, 3)))
        self.listboxM.insert(0, "liygorr: " + " " + str(liygorr))
        matri = []
        for i in range(len(b)):
            matri.append([b[i], liygorr[i], abs(round(b[i] - liygorr[i], 3))])
        data = DataFrame(matri, columns=['y', 'ygorr', 'diff'])
        self.listboxM.insert(0, data)
        poly_reg = PolynomialFeatures(degree=2)
        X_poly = poly_reg.fit_transform(x.reshape(-1, 1))
        lin_reg2 = LinearRegression()
        lin_reg2.fit(X_poly, y.reshape(-1, 1))
        y_pred = lin_reg2.predict(X_poly)
        plt.scatter(x, y, color='red')
        plt.plot(x, y_pred)
        plt.title("Regresion Linear Cuadratica")
        plt.show()

    def solutionX(self):
        lista2X = []
        lista3X = []
        lista4X = []
        lista5X = []
        lista6X = []
        lista7X = []
        lista8X = []
        lista9X = []
        lista10X = []
        lista11X = []
        a = list(map(float, self.E5.get().split()))
        b = list(map(float, self.E6.get().split()))
        c = list(map(float, self.E7.get().split()))
        x = np.array(a)  # x2
        y = np.array(b)  # x1
        z = np.array(c)  # y
        k = 2
        # Multiplicacion de X1*X1 guardada en lista3
        for i in range(len(x)):
            lista2X.append(x[i] * x[i])
        lix1X = np.array(lista2X)
        # Multiplicacion de X2*X2 guardada en lista3
        for i in range(len(x)):
            lista3X.append(y[i] * y[i])
        lix2X = np.array(lista3X)
        # Multiplicacion de X1*X2 guardada en lista3
        for i in range(len(x)):
            lista4X.append(a[i] * y[i])
        lix1x2X = np.array(lista4X)
        # Multiplicacion de X1*Y guardada en lista3
        for i in range(len(x)):
            lista5X.append(a[i] * z[i])
        lix1yX = np.array(lista5X)
        # Multiplicacion de X2*Y guardada en lista3
        for i in range(len(x)):
            lista6X.append(y[i] * z[i])
        lix2yX = np.array(lista6X)
        # Multiplicacion de Y*Y guardada en lista3
        for i in range(len(x)):
            lista7X.append(z[i] * z[i])
        liyyX = np.array(lista7X)
        # Calculo de sumas
        sum1X = x.sum()
        sum2X = y.sum()
        sum3X = z.sum()
        sum4X = lix1X.sum()
        sum5X = lix2X.sum()
        sum6X = lix1x2X.sum()
        sum7X = lix1yX.sum()
        sum8X = lix2yX.sum()
        sum9X = liyyX.sum()

        ##Regla de cramer
        def sarrus(A):
            val = ((A[0][0] * A[1][1] * A[2][2]) +
                   (A[0][1] * A[1][2] * A[2][0]) +
                   (A[0][2] * A[1][0] * A[2][1])) - \
                  ((A[2][0] * A[1][1] * A[0][2]) +
                   (A[2][1] * A[1][2] * A[0][0]) +
                   (A[2][2] * A[1][0] * A[0][1]))
            return val

        sismat = [[0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0]]
        res = [0.0, 0.0, 0.0]
        sismat[0][0] = len(x)
        sismat[0][1] = sum1X
        sismat[0][2] = sum2X
        sismat[0][3] = sum3X
        sismat[1][0] = sum1X
        sismat[1][1] = sum4X
        sismat[1][2] = sum6X
        sismat[1][3] = sum7X
        sismat[2][0] = sum2X
        sismat[2][1] = sum6X
        sismat[2][2] = sum5X
        sismat[2][3] = sum8X
        mat_x = [[sismat[0][3], sismat[0][1], sismat[0][2]],
                 [sismat[1][3], sismat[1][1], sismat[1][2]],
                 [sismat[2][3], sismat[2][1], sismat[2][2]]]
        mat_y = [[sismat[0][0], sismat[0][3], sismat[0][2]],
                 [sismat[1][0], sismat[1][3], sismat[1][2]],
                 [sismat[2][0], sismat[2][3], sismat[2][2]]]
        mat_z = [[sismat[0][0], sismat[0][1], sismat[0][3]],
                 [sismat[1][0], sismat[1][1], sismat[1][3]],
                 [sismat[2][0], sismat[2][1], sismat[2][3]]]
        det_mat = sarrus(sismat)
        if det_mat == 0:
            self.listboxX.insert(0, "Determinante de A nulo...")
        else:
            det_matx = sarrus(mat_x)
            det_maty = sarrus(mat_y)
            det_matz = sarrus(mat_z)
            res[0] = det_matx / det_mat
            res[1] = det_maty / det_mat
            res[2] = det_matz / det_mat
            self.listboxX.insert(0, "P => " + str(res))
        A = res[0]
        b1 = res[1]
        b2 = res[2]
        self.listboxX.insert(0, "El modelo de regresion es: " + str(round(A, 3)) + " + " + str(round(b1, 3)) + "x1",
                             " + " + str(round(b2, 3)) + "x2")
        # Calculo de ygorrito
        for i in range(len(x)):
            lista8X.append((A + (b1 * x[i]) + (b2 * y[i])))
        liygorrX = np.array(lista8X)
        sum10X = liygorrX.sum()
        # Calculo de SSE
        for i in range(len(x)):
            lista9X.append(math.pow((z[i] - liygorrX[i]), 2))
        liysseX = np.array(lista9X)
        sum11X = liysseX.sum()
        prom = z.mean()
        # Calculo de variacion total
        for i in range(len(x)):
            lista10X.append(math.pow(z[i] - prom, 2))
        livartX = np.array(lista10X)
        # Calculo de variacion Explicada
        for i in range(len(x)):
            lista11X.append(math.pow(lista8X[i] - prom, 2))
        livarexX = np.array(lista11X)
        sum12X = livarexX.sum()
        # Calculo de variacion inexplicada
        livarinX = liysseX
        sum13X = sum11X
        # Calculo de S^2 y S
        s2 = (sum11X / (len(z) - (k + 1)))
        s = math.sqrt(s2)
        # Calculo de Variacion total, r^2, r
        vartotal = sum12X + sum11X
        r2 = sum12X / vartotal
        r = math.sqrt(r2)
        # R ajustada
        var1 = k / (len(x) - 1)
        var2 = ((len(x) - 1) / (len(x) - (k + 1)))
        rajustado = (r2 - var1) * var2
        # Calculo de valores f
        f1 = (sum12X / k)
        f2 = (sum13X / (len(x) - (k + 1)))
        fmodelo = (f1 / f2)

        q = scipy.stats.f.ppf(q=1 - 0.05, dfn=k, dfd=(len(x) - (k + 1)))
        falpha = round(q, 3)

        self.listboxX.insert(0, str(round((stats.t.ppf(1 - 0.025, (len(x) - (k + 1)))), 3)))
        self.listboxX.insert(0, "s2: " + " " + str(round(s2, 3)))
        self.listboxX.insert(0, "s: " + " " + str(round(s, 3)))
        self.listboxX.insert(0, "r2: " + " " + str(round(r2, 3)))
        self.listboxX.insert(0, "r: " + " " + str(round(r, 3)))
        self.listboxX.insert(0, "rajustado: " + str(round(rajustado, 3)))
        self.listboxX.insert(0, "fmodelo: " + str(round(fmodelo, 3)))
        self.listboxX.insert(0, "falpha: " + str(round(falpha, 3)))
        self.listboxX.insert(0, "fmodelo: " + str(round(fmodelo, 3)))

    def create_window(self):
        newWindow = Toplevel(self)
        newWindow.title("Regresion Linear Cuadratico")
        newWindow.config(bg='thistle3')
        newWindow.geometry('{}x{}'.format(775, 675))
        newWindow.resizable(False, False)
        self.top = Frame(newWindow, bg='thistle3')
        self.top1 = Frame(newWindow, bg='thistle3')
        self.mid = Frame(newWindow, bg='thistle3')
        self.mid1 = Frame(newWindow, bg='thistle3')

        self.top.pack()
        self.top1.pack()
        self.mid.pack(anchor='n', fill=BOTH)
        self.mid1.pack(anchor='n', fill=BOTH)

        self.Label4 = Label(self.top, text="Regresion Linear Cuadratica", bg="thistle3", font=("Helvetica", 18, "bold"))
        self.Label4.pack(pady=(20, 0))

        self.btnM = Button(self.mid, text='Respuesta!', borderwidth=5, command=self.solutionM, font=("Helvetica", 16))
        self.btnM.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

        self.btnM1 = Button(self.mid, text='CE', borderwidth=5, command=self.otraM, font=("Helvetica", 16))
        self.btnM1.pack(pady=(30, 0), side=LEFT, anchor='n')

        self.Label5 = Label(self.top1, text="Valores de x: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        self.Label5.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

        self.E3 = Entry(self.top1, font=("Helvetica", 14), width=50)
        self.E3.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

        self.Label6 = Label(self.top1, text="Valores de y: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        self.Label6.pack(padx=(0, 10), anchor='sw')

        self.E4 = Entry(self.top1, font=("Helvetica", 14), width=50)
        self.E4.pack(padx=(0, 25), anchor='sw')

        self.Label6 = Label(self.mid1, text="Regresion Linear Cuadratica: ", bg="thistle3",
                            font=("Helvetica", 16, "bold"))
        self.Label6.pack(anchor='n', pady=(25, 0), padx=(20, 0))

        self.listboxM = Listbox(self.mid1, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
        self.listboxM.pack(padx=(18, 5), pady=(0, 25))

    def create_window1(self):
        newWindow1 = Toplevel(self)
        newWindow1.geometry('{}x{}'.format(750, 750))
        newWindow1.resizable(False, False)
        newWindow1.config(bg="thistle3")
        newWindow1.title('Regresion Linear Multiple')
        self.top_frame1 = Frame(newWindow1, bg='thistle3')
        self.top_frame2 = Frame(newWindow1, bg='thistle3')
        self.btm_frame1 = Frame(newWindow1, bg='thistle3')
        self.btm_frame2 = Frame(newWindow1, bg='thistle3')

        self.top_frame1.pack()
        self.top_frame2.pack()
        self.btm_frame1.pack(anchor='n', fill=BOTH)
        self.btm_frame2.pack(anchor='n', fill=BOTH)

        self.Label7 = Label(self.top_frame1, text="Regresion Linear Multiple", bg="thistle3", font=("Helvetica", 18, "bold"))
        self.Label7.pack(pady=(20, 0))

        self.btnX = Button(self.btm_frame1, text='Respuesta!', borderwidth=5, command=self.solutionX, font=("Helvetica", 16))
        self.btnX.pack(padx=(280, 10), pady=(30, 0), side=LEFT, anchor='n')

        self.btnX1 = Button(self.btm_frame1, text='CE', borderwidth=5, command=self.otraX, font=("Helvetica", 16))
        self.btnX1.pack(pady=(30, 0), side=LEFT, anchor='n')

        self.Label8 = Label(self.top_frame2, text="Valores de x: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        self.Label8.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

        self.E5 = Entry(self.top_frame2, font=("Helvetica", 14), width=50)
        self.E5.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

        self.Label9 = Label(self.top_frame2, text="Valores de x1: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        self.Label9.pack(padx=(0, 10), anchor='nw', pady=(20, 0))

        self.E6 = Entry(self.top_frame2, font=("Helvetica", 14), width=50)
        self.E6.pack(padx=(0, 25), anchor='nw', pady=(0, 20))

        self.Label10 = Label(self.top_frame2, text="Valores de y: ", bg="thistle3", font=("Helvetica", 16, "bold"))
        self.Label10.pack(padx=(0, 10), anchor='sw')

        self.E7 = Entry(self.top_frame2, font=("Helvetica", 14), width=50)
        self.E7.pack(padx=(0, 25), anchor='sw')

        self.Label11 = Label(self.btm_frame2, text="Regresion Linear Multiple: ", bg="thistle3",
                             font=("Helvetica", 16, "bold"))
        self.Label11.pack(anchor='n', pady=(25, 0), padx=(20, 0))

        self.listboxX = Listbox(self.btm_frame2, width=40, height=20, borderwidth=5, font=("Helvetica", 16))
        self.listboxX.pack(padx=(18, 5), pady=(0, 25))

    def otra(self):
        self.E1.config(state=NORMAL)
        self.E2.config(state=NORMAL)
        self.listboxF.config(state=NORMAL)
        plt.close()
        self.E1.delete(0, 'end')
        self.E2.delete(0, 'end')
        self.listboxF.delete(0, 'end')

    def otraM(self):
        self.E3.config(state=NORMAL)
        self.E4.config(state=NORMAL)
        self.listboxM.config(state=NORMAL)
        plt.close()
        self.E3.delete(0, 'end')
        self.E4.delete(0, 'end')
        self.listboxM.delete(0, 'end')

    def otraX(self):
        self.E5.config(state=NORMAL)
        self.E6.config(state=NORMAL)
        self.E7.config(state=NORMAL)
        self.listboxX.config(state=NORMAL)
        plt.close()
        self.E5.delete(0, 'end')
        self.E6.delete(0, 'end')
        self.E7.delete(0, 'end')
        self.listboxX.delete(0, 'end')

    def flush(self):
        pass


root = Tk()
root.geometry("725x650")
root.resizable(False, False)
# creation of an instance
app = Application()
# mainloop
mainloop()
"""

from scapy.all import *
from scapy.utils import hexdump
from collections import Counter
from pandas import DataFrame
import pandas as pd
import numpy as np

packet_counts = Counter()


# Define our Custom Action function

def custom_action(a):
    # Create tuple of Src/Dst in sorted order
    key = tuple(sorted([a[0][1].src, a[0][1].dst]))
    packet_counts.update([key])
    return f"Packet #{sum(packet_counts.values())}: {a[0][1].src} ==> {a[0][1].dst}"


a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", count=25, prn=custom_action)
list = []
for key, count in packet_counts.items():
    list.append(str(f"{f'{key[0]} <--> {key[1]}'}: {count}"))
x = list[0].split(' ')
list1 = []
for i in range(len(list)):
    list1.append(list[i].split(' '))
data = DataFrame(list1, columns=['SRC', '<-->', 'DST', ' Count'])
del data['<-->']
print()
print(data)
print()
list2 = []
for i in range(len(data)):
    sss = data.iat[i, 2]
    list2.append(sss)
print()
sas = hexdump(a[24])
ipdeets = open("IP_Details.txt", "w+")
list1 = np.array(list1).reshape(1, -1)
ipdeets.write(str(list1))
ipdeets.write("\n")
ipdeets.write(str(data))
ipdeets.write("\n")
ipdeets.write(str(sas))
