from scapy.layers.inet import IP, ICMP, TCP, UDP
from tkinter import *
from scapy.all import *
import sys


def ip_details():
    listboxF.delete(0, END)
    ans = []
    comp1 = str(E1.get())
    p = sr1(IP(dst=comp1, src="192.168.1.10") / TCP())
    for i in p:
        ans.append(i)
    for k in ans[:]:
        listboxF.insert(END, k)
    listboxF.insert(END, "Vea consola para más información")
    r = p.show2()
    file = open("IP_Details.txt", "w")
    q = sniff(filter="ip", prn=lambda pkt: "%s: %s" % (pkt.sniffed_on, pkt.show2()), count=10)
    file.write(str(q))
    file.write('\n' + str(p)) //using r yields a "None" in the .txt file therefore we switch it to write p instead
    return


# p = sr1(IP(dst="www.slashdot.org", src="192.168.1.10") / ICMP() / "Hello")
# p.show()

main = Tk()
main.geometry('{}x{}'.format(650, 550))
main.resizable(False, False)
main.config(bg="light gray")
main.title('Pseudo Sniffer')

top_frameL = Frame(main, bg="light gray", width=425, height=150)
top_frameR = Frame(main, bg="light gray", width=425, height=150)

btm_frameR = Frame(main, bg="light gray", width=425, height=150)

top_frameL.pack()
top_frameR.pack()
btm_frameR.pack(side=LEFT, anchor='n', fill=BOTH)

w = Label(top_frameL, text="IP Address Sniffer", bg="light gray", font=("Helvetica", 16, "bold"))
w.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

btn = Button(top_frameL, text='Begin Scan', command=ip_details, borderwidth=5)
btn.pack(side=RIGHT, padx=(217, 0), pady=(30, 0), anchor='e')

w1 = Label(top_frameR, text="Enter an IP/Web Address: ", bg="light gray", font=("Helvetica", 12))
w1.pack(side=LEFT, padx=(0, 10), anchor='e', pady=(20, 0))

E1 = Entry(top_frameR, width=35)
E1.pack(side=LEFT, padx=(0, 110), pady=(20, 0))

w1 = Label(btm_frameR, text="IP Details", bg="light gray", font=("Helvetica", 15))
w1.pack(anchor='nw', pady=(25, 0), padx=(18, 5))

scrollbar = Scrollbar(btm_frameR, orient="horizontal")
scrollbar.pack(side=BOTTOM, fill=X)

listboxF = Listbox(btm_frameR, width=100, height=100, borderwidth=5)
listboxF.pack(padx=(18, 5), pady=(0, 25), expand=1)
listboxF.config(xscrollcommand=scrollbar.set)
scrollbar.config(command=listboxF.xview)

mainloop()
