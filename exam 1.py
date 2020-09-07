vals = [0x6c71d92f, 0x47051050, 0x727c866e, 0x08004570,
        0x003460f5, 0x4000ed06, 0x61100de2, 0xfb81c0a8,
        0x014201bb, 0xfb6ac339, 0xba124031, 0x73878010,
        0x007b1859, 0x00000101, 0x050a4031, 0x73864031, 0x7387]

print()
version = vals[3]
v1 = hex(vals[3]).lstrip("0x")
ver = str(v1)
version = version >> 12
print("The version is: " + str((version & 255)))
print("The header length is: " + ver[4:5])
print("Differentiated Services Field: " + "0x" + ver[5:7])
print()

version = vals[4]
v1 = hex(vals[4]).lstrip("0x")
ver = str(v1)
version = version >> 12
print("Total Length is: " + str((version & 255)))
num = int((ver[2:]), 16)
print("Identification: " + "0x" + str((ver[2:])) + ' ' + '(' + str(num) + ')')
print()

version = vals[5]
v1 = hex(vals[5]).lstrip("0x")
ver = str(v1)
version = version >> 12
if ver[:2] == '80':
    print("Flags: " + "0x" + ver[:4] + ", reserved (evil bit)")
elif ver[:2] == '40':
    print("Flags: " + "0x" + ver[:4] + ", Do Not Fragment")
elif ver[:2] == '20':
    print("Flags: " + "0x" + ver[:4] + ", More Fragments follow")
print("Fragment offset: " + ver[3:4])
tmp = (ver[4:6])
print("Time to live: " + str(int(tmp, 16)))
tmp = (ver[6:])
i = int(tmp, 16)
if i == 1:
    print("Protocol: ICMP " + "(" + str(i) + ")")
elif i == 2:
    print("Protocol: IGMP " + "(" + str(i) + ")")
elif i == 6:
    print("Protocol: TCP " + "(" + str(i) + ")")
elif i == 9:
    print("Protocol: IGRP " + "(" + str(i) + ")")
elif i == 17:
    print("Protocol: UDP " + "(" + str(i) + ")")
elif i == 47:
    print("Protocol: GRE " + "(" + str(i) + ")")
elif i == 50:
    print("Protocol: ESP " + "(" + str(i) + ")")
elif i == 51:
    print("Protocol: AH " + "(" + str(i) + ")")
elif i == 57:
    print("Protocol: SKIP " + "(" + str(i) + ")")
elif i == 88:
    print("Protocol: EIGRP " + "(" + str(i) + ")")
elif i == 89:
    print("Protocol: OSPF " + "(" + str(i) + ")")
elif i == 115:
    print("Protocol: L2TP " + "(" + str(i) + ")")
print()

version = vals[6]
v1 = hex(vals[6]).lstrip("0x")
ver = str(v1)
version = version >> 12
print("Header checksum: " + "0x" + str(ver[:4]) + " [" + "validation disabled" + "]")
print("[" + "Header checksum status: Unverified" + "]")
print()

version1 = vals[7]
v1 = hex(vals[7]).lstrip("0x")
ver1 = str(v1)
version1 = version1 >> 12
tmp = str(ver[4:] + ver1[:4])
print("Source: " + str(int(tmp[:2], 16)) + "." + str(int(tmp[2:4], 16)) + "." + str(int(tmp[4:6], 16)) + "." + str(
    int(tmp[6:], 16)))
print()

version = vals[8]
v = hex(vals[8]).lstrip("0x")
ver = str('0' + v)
version = version >> 12
tmp = str(ver1[4:] + ver[:4])
print("Destination: " + str(int(tmp[:2], 16)) + "." + str(int(tmp[2:4], 16)) + "." + str(int(tmp[4:6], 16)) + "." + str(
    int(tmp[6:], 16)))
print("Source port: " + str(int(ver[3:], 16)))
print()

version = vals[9]
v1 = hex(vals[9]).lstrip("0x")
ver = str(v1)
version = version >> 12
print("Destination port: " + str(int(ver[:4], 16)))
print()

version1 = vals[10]
v1 = hex(vals[10]).lstrip("0x")
ver1 = str(v1)
version1 = version1 >> 12
tmp = str(ver[4:] + ver1[:4])
print("Sequence number (raw): " + str(int(tmp, 16)))
print()

version = vals[11]
v1 = hex(vals[11]).lstrip("0x")
ver = str(v1)
version = version >> 12
tmp = str(ver1[4:] + ver[:4])
print("Acknowledgement number (raw): " + str(int(tmp, 16)))
