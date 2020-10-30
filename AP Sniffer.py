##########################################################################################################################################
# There are two codes that need to be used in order for this program to work properly on is named t1.py and the other, which is the main #
# on is called world.py, however you can change the name of these programs just make sure to also change the import of t1.py because     #
# this program is crucial for several functions of the main application                                                                  #
##########################################################################################################################################

####################################
#             t1.py                #
####################################

from scapy.all import *
from scapy.utils import hexdump
from collections import Counter
from pandas import DataFrame
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
data = DataFrame(list1, columns=['SRC', '<-->', 'DSTT', ' Count'])
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

####################################
#             world.py             #
####################################

import tkinter as tk
from collections import Counter
from tkinter import *
from pandas import DataFrame
from scapy.all import *
from t1 import custom_action, data

packet_counts = Counter()

# Used to check which interfaces are available and which are recognized by npcap

"""print(get_windows_if_list())
print(get_if_list())"""


class Application(tk.Frame):

    def __init__(self, parent=0):
        Frame.__init__(self, parent, bg="peach puff")
        self.top_frameL = Frame(self, bg='peach puff', width=425, height=150)
        self.btm_frameL = Frame(self, bg='peach puff', width=425, height=150)
        self.top_frameR = Frame(self.btm_frameL, bg='peach puff', width=425, height=150)

        self.top_frameL.pack()
        self.top_frameR.pack()
        self.btm_frameL.pack(pady=(0, 10))

        # top_frameL is used here

        self.w = Label(self.top_frameL, text="Sniffer", font=("Helvetica", 18, "bold"), bg='peach puff')
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
                        padx=20, bg='peach puff', font=("Helvetica", 14)).pack()

        # btm_frameL is used here

        for val, language in enumerate(languages):
            self.R1 = Radiobutton(self.btm_frameL,
                                  text=language,
                                  padx=20,
                                  variable=self.v,
                                  value=val, bg='peach puff', font=("Helvetica", 14)).pack()

        self.L2 = Label(self.btm_frameL, text="Select TCP, UDP, or ICMP: ", font=("Helvetica", 14), bg='peach puff')
        self.L2.pack(pady=(20, 0))

        self.Ent = Entry(self.btm_frameL, width=15, font=("Helvetica", 14))
        self.Ent.pack(pady=(10, 10))

        self.btn = Button(self.btm_frameL, text='Begin Scan', command=self.ipdetails, borderwidth=5,
                          font=("Helvetica", 14))
        self.btn.pack(pady=(10, 10), anchor='s')

        self.scrollbar = Scrollbar(self.btm_frameL, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.S2 = Text(self.btm_frameL, height=14, width=60, borderwidth=5, font=("Helvetica", 14))
        self.S2.pack(padx=10, pady=(5, 0), fill=BOTH)
        self.S2.config(state=DISABLED)
        self.S2.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.S2.yview)

        OPTIONS = ["Packet: 1", "Packet: 2", "Packet: 3", "Packet: 4", "Packet: 5", "Packet: 6", "Packet: 7",
                   "Packet: 8", "Packet: 9", "Packet: 10", "Packet: 11", "Packet: 12", "Packet: 13", "Packet: 14",
                   "Packet: 15", "Packet: 16", "Packet: 17", "Packet: 18", "Packet: 19", "Packet: 20", "Packet: 21",
                   "Packet: 22", "Packet: 23", "Packet: 24", "Packet: 25"]

        self.variable = StringVar(self)
        self.variable.set(OPTIONS[0])

        self.w1 = OptionMenu(self, self.variable, *OPTIONS)
        self.w1.config(font=('Helvetica', 14), borderwidth=5)
        self.w1.pack(pady=(20, 10))
        self.tomenu = self.nametowidget(self.w1.menuname)
        self.tomenu.config(font=('Helvetica', 14))

        self.btn1 = Button(self, text='HexDump & Table', command=self.moreinfo, borderwidth=5, font=("Helvetica", 14))
        self.btn1.pack(pady=(15, 5), anchor='s')

        self.scrollbar1 = Scrollbar(self, orient="vertical")
        self.scrollbar1.pack(side=RIGHT, fill=Y)

        self.S3 = Text(self, height=12, width=60, borderwidth=5, font=("Helvetica", 14))
        self.S3.pack(padx=10, pady=10, fill=BOTH)
        self.S3.config(state=DISABLED)
        self.S3.config(yscrollcommand=self.scrollbar1.set)
        self.scrollbar1.config(command=self.S3.yview)

        sys.stdout = self
        self.pack()

    def custom_action(packet):
        # Create tuple of Src/Dst in sorted order
        key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
        packet_counts.update([key])
        return f"Packet #{sum(packet_counts.values())}: {packet[0][1].src} ==> {packet[0][1].dst}"

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
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", count=25,
                      prn=custom_action)
            print('\n')
            print(a)
            print()
            print(a.summary())
            self.S2.config(state=DISABLED)

    def moreinfo(self):
        self.S3.config(state=NORMAL)
        hi = self.variable.get().split(":")
        pos = int(hi[1])
        if pos > 25:
            print("Out of bounds")
            self.S3.config(state=DISABLED)
        else:
            neu = int(pos - 1)
            print(hexdump(a[neu]))
            print(data)
            self.S3.config(state=DISABLED)

    def flush(self):
        pass

    def write(self, txt):
        self.S2.insert(END, str(txt))
        self.S3.insert(END, str(txt))


if __name__ == '__main__':
    root = Tk()
    root.title("Sniffer")
    root.resizable(False, False)
    Application().mainloop()
