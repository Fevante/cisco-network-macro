import pyautogui
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
import time
from configparser import ConfigParser
from pathlib import Path
import pygame


# other stuff


def deiconify(x):
    x.deiconify()


def destroy(x):
    x.destroy()


def root_destroy(*args):
    root.destroy()


def conft():
    for i in range(0, 4):
        ex()
        enter()
    pyautogui.typewrite("en")
    enter()
    pyautogui.typewrite("conf t")
    enter()


def ex():
    pyautogui.typewrite("exit")
    enter()


def enter():
    pyautogui.press("enter")


def center_window(rt, width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    rt.geometry('%dx%d+%d+%d' % (width, height, x, y))


# <------------------------------------------------------------------------------------------------>
# dhcp start
def dhcp_op(*args):
    root.withdraw()
    dhcpWindow = Toplevel(root)
    dhcpWindow.attributes("-topmost", True)
    center_window(dhcpWindow, 525, 380)

    # back button
    backBtn = Button(dhcpWindow, text="Back to menu",
                     command=lambda: [uwuFc(), deiconify(root), destroy(dhcpWindow)])
    backBtn.grid(row=0, column=0, padx=10)

    # Exit button
    exitButton = Button(dhcpWindow, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    # Input column
    kitoltes = Label(dhcpWindow, text="Input", font=15)
    kitoltes.grid(row=0, column=1)

    # port input
    portLabel = Label(dhcpWindow, text="Interface:")
    portLabel.place(x=132, y=68)

    portInput = Text(dhcpWindow, height=1, width=15)
    portInput.grid(row=2, column=1, padx=30, pady=15)

    # ip 1 input
    ip1Label = Label(dhcpWindow, text="Ip:")
    ip1Label.place(x=132, y=118)

    ip1Input = Text(dhcpWindow, height=1, width=15)
    ip1Input.grid(row=3, column=1, padx=30, pady=15)

    # mask input
    maskLabel = Label(dhcpWindow, text="Mask:")
    maskLabel.place(x=132, y=168)

    maskInput = Text(dhcpWindow, height=1, width=15)
    maskInput.grid(row=5, column=1, padx=30, pady=15)

    # name input
    nameLabel = Label(dhcpWindow, text="Pool name: ")
    nameLabel.place(x=132, y=218)

    nameInput = Text(dhcpWindow, height=1, width=15)
    nameInput.grid(row=6, column=1, padx=30, pady=15)

    # done button
    doneButton = Button(dhcpWindow, text="Done", fg="green", border=1,
                        command=lambda: [uwuFc(), cd_dhcp(dhcpWindow), dhcp_getinfo(portInput.get("0.0", END),
                                                                                    ip1Input.get("0.0", END),
                                                                                    maskInput.get("0.0", END),
                                                                                    nameInput.get("0.0", END)
                                                                                    )])
    doneButton.grid(row=7, column=1)

    # Example Column
    example = Label(dhcpWindow, text="Example", font=15)
    example.grid(row=0, column=2, padx=20)
    portExample = Label(dhcpWindow, text="gig0/0", font=10)
    portExample.place(x=320, y=84)
    ip1Example = Label(dhcpWindow, text="192.168.1.1", font=10)
    ip1Example.place(x=300, y=134)
    maskExample = Label(dhcpWindow, text="255.255.255.0", font=10)
    maskExample.place(x=290, y=184)
    nameExample = Label(dhcpWindow, text="terem1", font=10)
    nameExample.place(x=320, y=234)


def help_win():
    txt = "Ha a példák alapján sem megy kérdezd meg Antit"
    showinfo(
        title="Help window",
        message=txt
    )


# countdown window
def cd_dhcp(rt):
    global dhcpPort, dhcpIp1, dhcpIp2, dhcpMask, dhcpName
    rt.withdraw()
    dhcpMessage = Toplevel(root)
    dhcpMessage.attributes("-topmost", True)
    dhcpMessage.title("Dhcp countdown")
    dhcpLabel = Label(dhcpMessage, font=50, pady=15)
    dhcpLabel.pack(padx=40)

    def countdown(count):
        dhcpLabel['text'] = f"Wait {count}s"

        if count > 0:
            dhcpMessage.after(1000, countdown, count - 1)
        elif count == 0:
            destroy(dhcpMessage)
            dhcpAU()

    countdown(5)


def dhcp_getinfo(a, b, c, d):
    global dhcpPort, dhcpIp1, dhcpIp2, dhcpMask, dhcpName
    dhcpPort = a[:-1]
    dhcpIp1 = b[:-1]
    if b[-5] == '.':
        dhcpIp2 = dhcpIp1[:-3] + '0'
    elif b[-4] == '.':
        dhcpIp2 = dhcpIp1[:-2] + '0'
    else:
        dhcpIp2 = dhcpIp1[:-1] + '0'
    dhcpMask = c[:-1]
    dhcpName = d[:-1]


# half automated dhcp
def dhcpAU():
    global dhcpPort, dhcpIp1, dhcpIp2, dhcpMask, dhcpName
    conft()
    pyautogui.typewrite(f"int {dhcpPort}")
    enter()
    pyautogui.typewrite(f"ip address {dhcpIp1} {dhcpMask}")
    time.sleep(0.1)
    enter()
    pyautogui.typewrite("no shutdown")
    enter()
    ex()
    pyautogui.typewrite(f"ip dhcp pool {dhcpName}")
    enter()
    pyautogui.typewrite(f"default {dhcpIp1}")
    enter()
    pyautogui.typewrite(f"net {dhcpIp2} {dhcpMask}")
    enter()
    ex()
    ex()
    pyautogui.typewrite("copy run start")
    enter()
    enter()
    time.sleep(1)
    deiconify(root)


# dhcp variables
dhcpPort = None
dhcpIp1 = None
dhcpIp2 = None
dhcpName = None
dhcpMask = None


# dhcp end
# <------------------------------------------------------------------------------------------------>


# <------------------------------------------------------------------------------------------------>
# ripV2 start
def rip_op(*args):
    root.withdraw()
    ripWindow = Toplevel(root)
    center_window(ripWindow, 335, 200)
    ripWindow.attributes("-topmost", True)
    cableLabel = Label(ripWindow, text="Mennyi kábel van?")
    cableLabel.grid(row=0, column=1)

    # back button
    backBtn = Button(ripWindow, text="Back to menu",
                     command=lambda: [uwuFc(), deiconify(root), destroy(ripWindow)])
    backBtn.grid(row=0, column=0, padx=10)

    # Exit button
    exitButton = Button(ripWindow, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    cableInput = Entry(ripWindow)
    cableInput.grid(row=1, column=1)
    cDoneButton = Button(ripWindow, text="Done", fg="green",
                         command=lambda: [
                             uwuFc(), input_to_variable(cableInput.get(), ripWindow),
                         ])
    cDoneButton.grid(row=3, column=1)
    ripWindow.mainloop()


def input_to_variable(c, d):
    global cable
    cable = int(c)
    network_count(d)


def network_count(rt):
    global cable, rip_runs
    rt.withdraw()
    if rip_runs != cable:
        rip_runs += 1
        network_input()
    else:
        cd_rip()


def cd_rip():
    ripMessage = Toplevel(root)
    ripMessage.attributes("-topmost", True)
    ripMessage.title("Rip countdown")
    ripLabel = Label(ripMessage, font=50, pady=15)
    ripLabel.pack(padx=40)

    def countdown(count):
        ripLabel['text'] = f"Wait {count}s"

        if count > 0:
            ripMessage.after(1000, countdown, count - 1)
        elif count == 0:
            destroy(ripMessage)
            rip()

    countdown(5)


def network_input():
    global rip_runs
    nInputWindow = Toplevel(root)
    center_window(nInputWindow, 330, 200)
    nInputWindow.attributes("-topmost", True)

    backBtn = Button(nInputWindow, text="Back", width=10,
                     command=lambda: [uwuFc(), nInputWindow.destroy(), clear(), rip_op()])
    backBtn.grid(row=0, column=0, padx=10)
    label = Label(nInputWindow, text=f"{rip_runs}. ip")
    label.grid(row=0, column=1)
    ipInput = Entry(nInputWindow)
    ipInput.grid(row=1, column=1)
    doneButton = Button(nInputWindow, text="Done", command=lambda: [uwuFc(), ip_add(ipInput.get()),
                                                                    network_count(nInputWindow)])
    doneButton.grid(row=2, column=1)
    # Exit button
    exitButton = Button(nInputWindow, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    nInputWindow.mainloop()


def ip_add(ip):
    global ipList
    ipList.append(ip)


def clear():
    global ipList, cable, rip_runs
    cable = 0
    rip_runs = 0
    ipList = []


def rip():
    global ipList
    print("rip bozo")
    conft()
    pyautogui.typewrite("router rip")
    enter()
    pyautogui.typewrite("version 2")
    enter()
    for i in ipList:
        pyautogui.typewrite(f"network {i}")
        enter()
    clear()
    root.deiconify()


# rip variables
cable = 0
rip_runs = 0
ipList = []


# ripV2 end
# <------------------------------------------------------------------------------------------------>


# <------------------------------------------------------------------------------------------------>
# telnet start
def telnet_op(*args):
    root.withdraw()
    telnetWindow = Toplevel(root)
    center_window(telnetWindow, 490, 200)
    telnetWindow.attributes("-topmost", True)

    # back button
    backBtn = Button(telnetWindow, text="Back to menu",
                     command=lambda: [uwuFc(), deiconify(root), destroy(telnetWindow), mode_sw()])
    backBtn.grid(row=0, column=0, padx=10)

    # Exit button
    exitButton = Button(telnetWindow, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    krdsLabel = Label(telnetWindow, text="Mibe kell telnet?", font=15)
    krdsLabel.place(x=178, y=10)
    switchButton = Button(telnetWindow, text="Switch", font=45, pady=10, padx=35,
                          command=lambda: [uwuFc(), mode_sw(), telnet_op_switch_and_router(), telnetWindow.destroy()])
    switchButton.grid(row=1, column=1, padx=10)
    routerButton = Button(telnetWindow, text="Router", font=45, pady=10, padx=35,
                          command=lambda: [uwuFc(), mode_rt(), telnet_op_switch_and_router(), telnetWindow.destroy()])
    routerButton.grid(row=1, column=2)

    telnetWindow.mainloop()


def mode_sw():
    global telnetMode
    telnetMode = 0


def mode_rt():
    global telnetMode
    telnetMode = 1


def telnet_op_switch_and_router():
    global telnetMode
    root.withdraw()
    telnetWin = Toplevel(root)
    telnetWin.attributes("-topmost", True)
    center_window(telnetWin, 525, 500)

    # back button
    backBtn = Button(telnetWin, text="Back", padx=20,
                     command=lambda: [uwuFc(), telnetWin.destroy(), telnet_op()])
    backBtn.grid(row=0, column=0, padx=10)

    # Exit button
    exitButton = Button(telnetWin, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    # Input column
    kitoltes = Label(telnetWin, text="Input", font=15)
    kitoltes.grid(row=0, column=1)

    interfaceLabel = Label(telnetWin, text="Interface:")
    interfaceLabel.place(x=122, y=68)
    interfaceInput = Text(telnetWin, height=1, width=15)
    interfaceInput.grid(row=2, column=1, padx=30, pady=15)

    ipLabel = Label(telnetWin, text="Ip:")
    ipLabel.place(x=122, y=118)
    ipInput = Text(telnetWin, height=1, width=15)
    ipInput.grid(row=3, column=1, padx=30, pady=15)

    maskLabel = Label(telnetWin, text="Mask:")
    maskLabel.place(x=122, y=168)
    maskInput = Text(telnetWin, height=1, width=15)
    maskInput.grid(row=4, column=1, padx=30, pady=15)

    passwordLabel = Label(telnetWin, text="Password:")
    passwordLabel.place(x=122, y=218)
    passwordInput = Text(telnetWin, height=1, width=15)
    passwordInput.grid(row=5, column=1, padx=30, pady=15)

    # done button
    doneButton = Button(telnetWin, text="Done", fg="green", border=1,
                        command=lambda: [uwuFc(), telnet_getinfo(interfaceInput.get("1.0", END),
                                                                 ipInput.get("1.0", END),
                                                                 maskInput.get("1.0", END),
                                                                 passwordInput.get("1.0", END)),
                                         destroy(telnetWin)])
    doneButton.grid(row=7, column=1)

    # Example column
    example = Label(telnetWin, text="Example", font=15)
    example.grid(row=0, column=2, padx=20)
    if telnetMode == 0:
        interfaceExample = Label(telnetWin, text="vlan 1", font=10)
        interfaceExample.place(x=310, y=84)
    else:
        interfaceExample = Label(telnetWin, text="gig0/0", font=10)
        interfaceExample.place(x=310, y=84)
    if telnetMode == 0:
        ipExample = Label(telnetWin, text="192.168.1.2", font=10)
        ipExample.place(x=288, y=134)
    else:
        ipExample = Label(telnetWin, text="192.168.1.1", font=10)
        ipExample.place(x=288, y=134)
    maskExample = Label(telnetWin, text="255.255.255.0", font=10)
    maskExample.place(x=280, y=184)
    passwordExample = Label(telnetWin, text="Józsika123", font=10)
    passwordExample.place(x=290, y=234)


def telnet_getinfo(a, b, c, d):
    global telnetInterface, telnetIp, telnetMask, telnetPassword
    telnetInterface = a[:-1]
    telnetIp = b[:-1]
    telnetMask = c[:-1]
    telnetPassword = d[:-1]
    cd_telnet()


def cd_telnet():
    telnetMessage = Toplevel(root)
    telnetMessage.attributes("-topmost", True)
    telnetMessage.title("Telnet countdown")
    telnetLabel = Label(telnetMessage, font=50, pady=15)
    telnetLabel.pack(padx=40)

    def countdown(count):
        telnetLabel['text'] = f"Wait {count}s"

        if count > 0:
            telnetMessage.after(1000, countdown, count - 1)
        elif count == 0:
            destroy(telnetMessage)
            telnet()

    countdown(5)


def telnet():
    global telnetIp, telnetMask, telnetPassword
    conft()
    pyautogui.typewrite(f"int {telnetInterface}")
    enter()
    pyautogui.typewrite(f"ip add {telnetIp} {telnetMask}")
    enter()
    pyautogui.typewrite("no shutdown")
    enter()
    pyautogui.typewrite("line vty 0 15")
    enter()
    pyautogui.typewrite(f"password {telnetPassword}")
    enter()
    pyautogui.typewrite("login")
    enter()
    ex()
    ex()
    pyautogui.typewrite("copy run start")
    enter()
    enter()


# telnet variables
telnetMode = 0
telnetInterface = None
telnetIp = None
telnetMask = None
telnetPassword = None


# telnet end
# <------------------------------------------------------------------------------------------------>

# <------------------------------------------------------------------------------------------------>
# s nat start
def snat_op(*args):
    root.withdraw()
    snatWindow = Toplevel(root)
    center_window(snatWindow, 500, 400)
    snatWindow.attributes("-topmost", True)

    backBtn = Button(snatWindow, text="Back to menu",
                     command=lambda: [uwuFc(), deiconify(root), destroy(snatWindow)])
    backBtn.grid(row=0, column=0, padx=10)

    exitButton = Button(snatWindow, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    kitoltes = Label(snatWindow, text="Input", font=15)
    kitoltes.grid(row=0, column=1)

    inIpLabel = Label(snatWindow, text="Fordítani kívánt ip:")
    inIpLabel.place(x=132, y=68)
    inIpInput = Text(snatWindow, height=1, width=15)
    inIpInput.grid(row=2, column=1, padx=30, pady=15)

    outIpLabel = Label(snatWindow, text="Fordított ip:")
    outIpLabel.place(x=132, y=118)
    outIpInput = Text(snatWindow, height=1, width=15)
    outIpInput.grid(row=3, column=1, padx=30, pady=15)

    insideInterfaceLabel = Label(snatWindow, text="Inside interface:")
    insideInterfaceLabel.place(x=132, y=168)
    insideInterfaceInput = Text(snatWindow, height=1, width=15)
    insideInterfaceInput.grid(row=4, column=1, padx=30, pady=15)

    outsideInterfaceLabel = Label(snatWindow, text="Outside interface:")
    outsideInterfaceLabel.place(x=132, y=218)
    outsideInterfaceInput = Text(snatWindow, height=1, width=15)
    outsideInterfaceInput.grid(row=5, column=1, padx=30, pady=15)

    doneButton = Button(snatWindow, text="Done", fg="green", border=1,
                        command=lambda: [uwuFc(), cd_snat(),
                                         snat_getinfo(inIpInput.get("1.0", END),
                                                      outIpInput.get("1.0", END),
                                                      insideInterfaceInput.get("1.0", END),
                                                      outsideInterfaceInput.get("1.0", END)), destroy(snatWindow)])
    doneButton.grid(row=7, column=1)

    # Example column
    example = Label(snatWindow, text="Example", font=15)
    example.grid(row=0, column=2, padx=20)

    inIpExample = Label(snatWindow, text="192.168.1.1", font=10)
    inIpExample.place(x=300, y=84)
    outIpExample = Label(snatWindow, text="50.0.0.3", font=10)
    outIpExample.place(x=310, y=134)
    insideInterfaceExample = Label(snatWindow, text="gig0/0", font=10)
    insideInterfaceExample.place(x=320, y=184)
    outsideInterfaceExample = Label(snatWindow, text="gig0/1", font=10)
    outsideInterfaceExample.place(x=320, y=234)

    snatWindow.mainloop()


def snat_getinfo(a, b, c, d):
    global inIp, outIp, sInsideInterface, sOutsideInterface
    inIp = a[:-1]
    outIp = b[:-1]
    sInsideInterface = c[:-1]
    sOutsideInterface = d[:-1]


def cd_snat():
    snatMessage = Toplevel(root)
    snatMessage.attributes("-topmost", True)
    snatMessage.title("Snat countdown")
    snatLabel = Label(snatMessage, font=50, pady=15)
    snatLabel.pack(padx=40)

    def countdown(count):
        snatLabel['text'] = f"Wait {count}s"

        if count > 0:
            snatMessage.after(1000, countdown, count - 1)
        elif count == 0:
            destroy(snatMessage)
            snat()

    countdown(5)


def snat():
    global inIp, outIp, sInsideInterface, sOutsideInterface
    conft()
    pyautogui.typewrite(f"ip nat inside source static {inIp} {outIp}")
    enter()
    pyautogui.typewrite(f"int {sInsideInterface}")
    enter()
    pyautogui.typewrite("ip nat inside")
    enter()
    ex()
    pyautogui.typewrite(f"int {sOutsideInterface}")
    enter()
    pyautogui.typewrite("ip nat outside")
    enter()
    ex()
    time.sleep(1)
    root.deiconify()


# static nat variables
inIp = None
outIp = None
sInsideInterface = None
sOutsideInterface = None


# static nat end
# <------------------------------------------------------------------------------------------------>


# <------------------------------------------------------------------------------------------------>
# dynamic nat start
def dnat_op(*args):
    root.withdraw()
    dnatWindow = Toplevel(root)
    dnatWindow.attributes("-topmost", True)
    center_window(dnatWindow, 525, 500)

    # back button
    backBtn = Button(dnatWindow, text="Back to menu",
                     command=lambda: [uwuFc(), deiconify(root), destroy(dnatWindow), mode_sw()])
    backBtn.grid(row=0, column=0, padx=10)

    # Exit button
    exitButton = Button(dnatWindow, text="EXIT!!!4!!!!!4!", height=2, width=10, background="red",
                        command=lambda: [uwuFc(), save_exit()])
    exitButton.grid(row=0, column=3, padx=15, pady=15)

    # Input column
    kitoltes = Label(dnatWindow, text="Input", font=15)
    kitoltes.grid(row=0, column=1)

    startIpLabel = Label(dnatWindow, text="Start ip")
    startIpLabel.place(x=132, y=68)
    startIpInput = Text(dnatWindow, height=1, width=15)
    startIpInput.grid(row=2, column=1, padx=30, pady=15)

    endIpLabel = Label(dnatWindow, text="End ip:")
    endIpLabel.place(x=132, y=118)
    endIpInput = Text(dnatWindow, height=1, width=15)
    endIpInput.grid(row=3, column=1, padx=30, pady=15)

    nMaskLabel = Label(dnatWindow, text="Mask:")
    nMaskLabel.place(x=132, y=168)
    nMaskInput = Text(dnatWindow, height=1, width=15)
    nMaskInput.grid(row=4, column=1, padx=30, pady=15)

    permitIpLabel = Label(dnatWindow, text="Permit ip:")
    permitIpLabel.place(x=132, y=218)
    permitIpInput = Text(dnatWindow, height=1, width=15)
    permitIpInput.grid(row=5, column=1, padx=30, pady=15)

    permitMaskLabel = Label(dnatWindow, text="Permit mask:")
    permitMaskLabel.place(x=132, y=268)
    permitMaskInput = Text(dnatWindow, height=1, width=15)
    permitMaskInput.grid(row=6, column=1, padx=30, pady=15)

    dInsideInterfaceLabel = Label(dnatWindow, text="Inside interface:")
    dInsideInterfaceLabel.place(x=132, y=318)
    dInsideInterfaceInput = Text(dnatWindow, height=1, width=15)
    dInsideInterfaceInput.grid(row=7, column=1, padx=30, pady=15)

    dOutsideInterfaceLabel = Label(dnatWindow, text="Outside Interface:")
    dOutsideInterfaceLabel.place(x=132, y=368)
    dOutsideInterfaceInput = Text(dnatWindow, height=1, width=15)
    dOutsideInterfaceInput.grid(row=8, column=1, padx=30, pady=15)

    doneButton = Button(dnatWindow, text="Done", fg="green", border=1,
                        command=lambda: [uwuFc(), cd_dnat(), dnat_getinfo(startIpInput.get('1.0', END),
                                                                          endIpInput.get('1.0', END),
                                                                          nMaskInput.get('1.0', END),
                                                                          permitIpInput.get('1.0', END),
                                                                          permitMaskInput.get('1.0', END),
                                                                          dInsideInterfaceInput.get('1.0', END),
                                                                          dOutsideInterfaceInput.get('1.0', END)),
                                         destroy(dnatWindow)])
    doneButton.grid(row=10, column=1)

    # Example Column
    example = Label(dnatWindow, text="Example", font=15)
    example.grid(row=0, column=2, padx=20)

    startIpExample = Label(dnatWindow, text="40.0.0.2", font=10)
    startIpExample.place(x=310, y=84)
    endIpExample = Label(dnatWindow, text="40.0.0.4", font=10)
    endIpExample.place(x=310, y=134)
    nMaskExample = Label(dnatWindow, text="255.255.255.0", font=10)
    nMaskExample.place(x=290, y=184)
    permitIpExample = Label(dnatWindow, text="192.168.1.0", font=10)
    permitIpExample.place(x=295, y=234)
    permitMaskExample = Label(dnatWindow, text="0.0.0.255", font=10)
    permitMaskExample.place(x=305, y=284)
    dInsideInterfaceExample = Label(dnatWindow, text="gig0/0", font=10)
    dInsideInterfaceExample.place(x=315, y=334)
    dOutsideInterfaceExample = Label(dnatWindow, text="gig0/1", font=10)
    dOutsideInterfaceExample.place(x=315, y=384)


def dnat_getinfo(a, b, c, d, e, f, g):
    global startIp, endIp, nMask, permitIp, permitMask, dInsideInterface, dOutsideInterface
    startIp = a[:-1]
    endIp = b[:-1]
    nMask = c[:-1]
    permitIp = d[:-1]
    permitMask = e[:-1]
    dInsideInterface = f[:-1]
    dOutsideInterface = g[:-1]


def cd_dnat():
    dnatMessage = Toplevel(root)
    dnatMessage.attributes("-topmost", True)
    dnatMessage.title("Dnat countdown")
    dnatLabel = Label(dnatMessage, font=50, pady=15)
    dnatLabel.pack(padx=40)

    def countdown(count):
        dnatLabel['text'] = f"Wait {count}s"

        if count > 0:
            dnatMessage.after(1000, countdown, count - 1)
        elif count == 0:
            destroy(dnatMessage)
            dnat()

    countdown(5)


def dnat():
    global startIp, endIp, nMask, permitIp, permitMask, dInsideInterface, dOutsideInterface
    conft()
    pyautogui.typewrite(f"ip nat pool DNAT {startIp} {endIp} netmask {nMask}")
    enter()
    pyautogui.typewrite(f"access-list 1 permit {permitIp} {permitMask}")
    enter()
    pyautogui.typewrite(f"ip nat inside source list 1 pool DNAT")
    enter()
    pyautogui.typewrite(f"int {dInsideInterface}")
    enter()
    pyautogui.typewrite("ip nat inside")
    enter()
    ex()
    pyautogui.typewrite(f"int {dOutsideInterface}")
    enter()
    pyautogui.typewrite("ip nat outside")
    enter()
    time.sleep(1)
    root.deiconify()


# dnat variables
startIp = None
endIp = None
nMask = None
permitIp = None
permitMask = None
dInsideInterface = None
dOutsideInterface = None
# dynamic nat end
# <------------------------------------------------------------------------------------------------>

# config stuff
config = ConfigParser()
config.read("config.ini")
pygame.mixer.init()


def save_exit():
    global byll, aszi
    config.set('voice', 'byll', str(byll.get()))
    config.set('voice', 'baszi', str(aszi.get()))
    root.destroy()
    with open('config.ini', 'w') as f:
        config.write(f)


def sound_path(filename):
    return str(Path(__file__).resolve().parent / 'Sounds' / filename)

def billOn():
    global byll, aszi
    if byll.get() == True and aszi.get() == byll.get():
        aszi.set(False)


def asziOn():
    global byll, aszi
    if aszi.get() == True and byll.get() == aszi.get():
        byll.set(False)


def sound_path(filename):
    return str(Path(__file__).resolve().parent / 'Sounds' / filename)

def byll_sound():
    pygame.mixer.music.load(sound_path('Bill_voice.mp3'))
    pygame.mixer.music.play()

def uwu_sound():
    pygame.mixer.music.load(sound_path('uwu.wav'))
    pygame.mixer.music.play()

def nyan_sound():
    pygame.mixer.music.load(sound_path('nyan.wav'))
    pygame.mixer.music.play()

def aszi_sound():
    pygame.mixer.music.load(sound_path('Aszi_voice.wav'))
    pygame.mixer.music.play()


def easterEgg(*args):
    help_menu.add_checkbutton(label="uwu", onvalue=1, offvalue=0, variable=uwu)


def uwuFc(*args):
    global uwu, byll
    if uwu.get() == True and byll.get() == True:
        uwu_sound()


def nyan(*args):
    if byll.get():
        nyan_sound()


def sound():
    if byll.get():
        byll_sound()
    elif aszi.get():
        aszi_sound()


# <------------------------------------------------------------------------------------------------>


# root start
root = tk.Tk()
center_window(root, 400, 425)

# variables
aszi = tk.BooleanVar()
byll = tk.BooleanVar()
uwu = tk.BooleanVar()
aszi.set(config.get("voice", "baszi"))
byll.set(config.get("voice", "byll"))

krds = Label(root, text="Mi kell báttya?", font=("Arial", 20)).pack()

# menuBar
menuBar = Menu(root)

help_menu = Menu(menuBar, tearoff=0)
help_menu.add_separator()
help_menu.add_command(label="Help", command=help_win)

voice_menu = Menu(help_menu, tearoff=0)
voice_menu.add_checkbutton(label="Byll", onvalue=1, offvalue=0, variable=byll, command=billOn)
voice_menu.add_checkbutton(label="Aszi", onvalue=1, offvalue=0, variable=aszi, command=asziOn)

help_menu.add_cascade(label="Voice Assistant", menu=voice_menu)

menuBar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menuBar)

# buttons
dhcpButton = Button(root,
                    text="Dhcp", padx=74, pady=10, cursor="dot", background="#e1e1e1",
                    command=lambda: [uwuFc(), dhcp_op()]).pack(pady=10)
ripButton = Button(root, text="Rip v2", padx=72, pady=10, cursor="dot", background="#e1e1e1",
                   command=lambda: [uwuFc(), rip_op()]).pack(pady=10)
telnetButton = Button(root, text="Telnet", padx=72, pady=10, cursor="dot", background="#e1e1e1",
                      command=lambda: [uwuFc(), telnet_op()]).pack(pady=10)
sNat = Button(root, text="Static Nat", padx=62, pady=10, cursor="dot", background="#e1e1e1",
              command=lambda: [uwuFc(), snat_op()]).pack(pady=10)
dNat = Button(root, text="Dynamic Nat", padx=53, pady=10, cursor="dot", background="#e1e1e1",
              command=lambda: [uwuFc(), dnat_op()]).pack(pady=10)
exitButton = Button(root, text="Exit", bg="red", padx=53, pady=10, cursor="dot", command=save_exit).pack(pady=10)

# root binds
root.bind("1", dhcp_op)
root.bind("2", rip_op)
root.bind("3", telnet_op)
root.bind("4", snat_op)
root.bind('5', dnat_op)
root.bind("9", root_destroy)
root.bind("0", easterEgg)
root.bind('n', nyan)

# root settings
root.title("Hálpy v2.0")
root.attributes("-topmost", True)
root.after(100, sound)
root.mainloop()
# <------------------------------------------------------------------------------------------------>
