import ipcalc
from tkinter import *
import tkinter as tk
from scapy.all import *

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
        self.w.pack(pady=(20, 10), side=LEFT, padx=(200, 0))

        self.btn2 = Button(self.top_frameL, text="IP Calc", command=self.create_window, borderwidth=5,
                           font=("Helvetica", 14))
        self.btn2.pack(side=RIGHT, pady=(20, 10), padx=(100, 0))

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

        self.S2 = Text(self.btm_frameL, height=8, width=60, borderwidth=5, font=("Helvetica", 14))
        self.S2.pack(padx=10, pady=(5, 0), fill=BOTH)
        self.S2.config(state=DISABLED)
        self.S2.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.S2.yview)

        self.w1 = Label(self, text="Which packet do you want more information on: ", font=("Helvetica", 14),
                        bg='peach puff')
        self.w1.pack(pady=(20, 10))

        self.entry1 = Entry(self, width=15)
        self.entry1.config(font=("Helvetica", 14))
        self.entry1.pack()

        self.btn1 = Button(self, text='Get Info', command=self.moreinfo, borderwidth=5, font=("Helvetica", 14))
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
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 0 and fill == "udp":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", filter="udp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 0 and fill == "icmp":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", filter="icmp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 0 and fill == "":
            a = sniff(iface="Killer E2500 Gigabit Ethernet Controller", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)

        if Val == 1 and fill == "tcp":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", filter="tcp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 1 and fill == "udp":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", filter="udp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 1 and fill == "icmp":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", filter="icmp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 1 and fill == "":
            a = sniff(iface="TAP-NordVPN Windows Adapter V9", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)

        if Val == 2 and fill == "tcp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", filter="tcp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 2 and fill == "udp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", filter="udp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 2 and fill == "icmp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", filter="icmp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 2 and fill == "":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)

        if Val == 3 and fill == "tcp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", filter="tcp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 3 and fill == "udp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", filter="udp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 3 and fill == "icmp":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", filter="icmp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 3 and fill == "":
            a = sniff(iface="Microsoft Wi-Fi Direct Virtual Adapter #2", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)

        if Val == 4 and fill == "tcp":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", filter="tcp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 4 and fill == "udp":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", filter="udp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 4 and fill == "icmp":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", filter="icmp", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
            self.S2.config(state=DISABLED)
        if Val == 4 and fill == "":
            a = sniff(iface="Killer(R) Wireless-AC 1550 Wireless Network Adapter (9260NGW) 160MHz", count=25)
            print(a)
            print('\n')
            print(a.nsummary())
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

    def create_window(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("IP Calculator")
        newWindow.config(bg='peach puff')
        newWindow.geometry('{}x{}'.format(750, 700))
        newWindow.resizable(False, False)
        self.top = tk.Frame(newWindow, bg='peach puff')
        self.top.pack()
        self.top1 = tk.Frame(newWindow, bg='peach puff')
        self.top1.pack()
        self.mid1 = tk.Frame(newWindow, bg='peach puff')
        self.mid1.pack()
        self.mid2 = tk.Frame(newWindow, bg='peach puff')
        self.mid2.pack()
        self.bot = tk.Frame(newWindow, bg='peach puff')
        self.bot.pack()

        self.Label4 = tk.Label(self.top, text="IP Calculator", font=("Helvetica", 18, "bold"), bg='peach puff')
        self.Label4.pack(anchor='nw', pady=(10, 0))

        self.Label1 = tk.Label(self.top1, text="Enter Host/Network: ", font=("Helvetica", 14), bg='peach puff')
        self.Label1.pack(side=LEFT, anchor='nw', pady=(10, 0))

        self.Ent1 = tk.Entry(self.top1, width=15)
        self.Ent1.config(font=("Helvetica", 14))
        self.Ent1.pack(side=LEFT, anchor='ne', pady=(15, 0))

        self.Label2 = tk.Label(self.mid1, text="Enter Netmask: ", font=("Helvetica", 14), bg='peach puff')
        self.Label2.pack(side=LEFT, anchor='w', pady=(10, 0))

        self.Ent2 = tk.Entry(self.mid1, width=15)
        self.Ent2.config(font=("Helvetica", 14))
        self.Ent2.pack(side=LEFT, anchor='e', pady=(15, 0))

        self.btn3 = tk.Button(self.mid2, text="Calculate", font=("Helvetica", 14), command=self.ipfig)
        self.btn3.pack(pady=(15, 0))

        self.Label3 = tk.Label(self.bot, text="Results: ", font=("Helvetica", 18, 'bold'), bg='peach puff')
        self.Label3.pack(anchor='n', pady=(10, 0))

        self.S1 = tk.Text(self.bot, height=18, width=21, font=("Helvetica", 14), borderwidth=5)
        self.S1.tag_configure("left", justify="left")
        self.S1.tag_add("left", 1.0, "end")
        self.S1.pack(side=LEFT, padx=(0, 10), pady=(15, 0), fill=BOTH, anchor='w')
        self.S1.config(state=DISABLED)

        self.S4 = tk.Text(self.bot, height=18, width=42, font=("Helvetica", 14), borderwidth=5)
        self.S4.tag_configure("right", justify="right")
        self.S4.tag_add("right", 1.0, "end")
        self.S4.pack(side=LEFT, padx=(0, 0), pady=(15, 0), fill=BOTH, anchor='w')
        self.S4.config(state=DISABLED)

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
        print("Address: " + str(ip.bin()) + '\n')
        print("Netmask: " + str(ipnm.bin()) + '\n')
        print("Network: " + str(ipn.bin()) + '\n')
        print("Broadcast: " + str(ipbc.bin()) + '\n')
        print("HostMin: " + str(iphf.bin()) + '\n')
        print("HostMax: " + str(iphl.bin()))
        self.S4.config(state=DISABLED)

    def flush(self):
        pass

    def write(self, txt):
        self.S2.insert(END, str(txt))
        self.S3.insert(END, str(txt))
        self.S1.insert(END, str(txt))
        self.S4.insert(END, str(txt))


if __name__ == '__main__':
    root = Tk()
    root.title("Sniffer")
    root.resizable(False, False)
    Application().mainloop()
