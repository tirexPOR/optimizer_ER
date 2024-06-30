from tkinter import *
from tkinter import ttk

import SecondWindow
import Variables

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("Elden Ring Optimizer")
frm.grid()

ttk.Label(frm, text="Podaj maksymalny udźwig postaci:").grid(column=0, row=0)
maxLoadSB = ttk.Spinbox(frm, from_=45.0, to=205.6, increment=0.1)
maxLoadSB.grid(column=1, row=0)
maxLoadSB.set(45.0)

ttk.Label(frm, text="Podaj wagę broni głównych:").grid(column=0, row=1, pady=10)
mwWgt1SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
mwWgt1SB.grid(column=1, row=1, pady=10, padx=5)
mwWgt1SB.set(0.0)
mwWgt2SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
mwWgt2SB.grid(column=2, row=1, pady=10)
mwWgt2SB.set(0.0)
mwWgt3SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
mwWgt3SB.grid(column=3, row=1, pady=10, padx=5)
mwWgt3SB.set(0.0)

ttk.Label(frm, text="Podaj wagę broni dodatkowych:").grid(column=0, row=2)
swWgt1SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
swWgt1SB.grid(column=1, row=2)
swWgt1SB.set(0.0)
swWgt2SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
swWgt2SB.grid(column=2, row=2)
swWgt2SB.set(0.0)
swWgt3SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
swWgt3SB.grid(column=3, row=2)
swWgt3SB.set(0.0)

ttk.Label(frm, text="Podaj wagę amuletów:").grid(column=0, row=3, pady=10)
aWgt1SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
aWgt1SB.grid(column=1, row=3, pady=10)
aWgt1SB.set(0.0)
aWgt2SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
aWgt2SB.grid(column=2, row=3, pady=10)
aWgt2SB.set(0.0)
aWgt3SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
aWgt3SB.grid(column=3, row=3, pady=10)
aWgt3SB.set(0.0)
aWgt4SB = ttk.Spinbox(frm, from_=0.0, to=999.9, increment=0.1)
aWgt4SB.grid(column=4, row=3, pady=10)
aWgt4SB.set(0.0)

ttk.Label(frm, text="Podaj współczynniki wagowe statystyk,\nktórych chcesz użyć w optymalizacji:") \
    .grid(column=0, rowspan=7)
ttk.Label(frm, text="Fizyczne").grid(column=1, row=4)
physicSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
physicSB.grid(column=2, row=4)
physicSB.set(0)
ttk.Label(frm, text="Vs uderzeniom").grid(column=3, row=4)
strikeSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
strikeSB.grid(column=4, row=4)
strikeSB.set(0)
ttk.Label(frm, text="Vs cięciom").grid(column=1, row=5)
slashSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
slashSB.grid(column=2, row=5)
slashSB.set(0)
ttk.Label(frm, text="Vs pchnięciom").grid(column=3, row=5)
pierceSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
pierceSB.grid(column=4, row=5)
pierceSB.set(0)
ttk.Label(frm, text="Magiczne").grid(column=1, row=6)
magicSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
magicSB.grid(column=2, row=6)
magicSB.set(0)
ttk.Label(frm, text="Ogniste").grid(column=3, row=6)
fireSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
fireSB.grid(column=4, row=6)
fireSB.set(0)
ttk.Label(frm, text="Elektryczne").grid(column=1, row=7)
electricSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
electricSB.grid(column=2, row=7)
electricSB.set(0)
ttk.Label(frm, text="Święte").grid(column=3, row=7)
holySB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
holySB.grid(column=4, row=7)
holySB.set(0)
ttk.Label(frm, text="Niewrażliwość").grid(column=1, row=8)
immSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
immSB.grid(column=2, row=8)
immSB.set(0)
ttk.Label(frm, text="Krzepa").grid(column=3, row=8)
robSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
robSB.grid(column=4, row=8)
robSB.set(0)
ttk.Label(frm, text="Skupienie").grid(column=1, row=9)
focusSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
focusSB.grid(column=2, row=9)
focusSB.set(0)
ttk.Label(frm, text="Wigor").grid(column=3, row=9)
vitSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
vitSB.grid(column=4, row=9)
vitSB.set(0)
ttk.Label(frm, text="Równowaga").grid(column=1, row=10)
poiseSB = ttk.Spinbox(frm, from_=0.0, to=99.0, increment=1.0)
poiseSB.grid(column=2, row=10)
poiseSB.set(0)

ttk.Label(frm, text="Zaznacz jaki typ uniki chcesz uzyskać:").grid(column=0, row=11, pady=10)
roll = IntVar()
ttk.Radiobutton(frm, text="Szybki", value=0, variable=roll).grid(column=1, row=11, pady=10)
ttk.Radiobutton(frm, text="Średni", value=1, variable=roll).grid(column=2, row=11, pady=10)
ttk.Radiobutton(frm, text="Ciężki", value=2, variable=roll).grid(column=3, row=11, pady=10)

ttk.Label(frm, text="Wybierz początkową klasę:").grid(column=0, row=12)
startClassCB = ttk.Combobox(frm, values=["Astrolog", "Bandyta", "Bohater", "Łajdak", "Prorok", "Samuraj", "Spowiednik",
                                         "Więzień", "Włóczęga", "Wojownik"])
startClassCB.grid(column=1, row=12)

def setParamethers():
    if Variables.secondWindowFlag == 0:
        Variables.maxLoad = float(maxLoadSB.get())
        if roll.get() == 0:
            Variables.roll = 0.2999
        if roll.get() == 1:
            Variables.roll = 0.6999
        if roll.get() == 2:
            Variables.roll = 0.9999
        Variables.limitLoad = round(Variables.maxLoad * Variables.roll, 4)
        Variables.load = Variables.limitLoad
        print(Variables.load)

        Variables.load -= float(mwWgt1SB.get())
        Variables.load -= float(mwWgt2SB.get())
        Variables.load -= float(mwWgt3SB.get())

        Variables.load -= float(swWgt1SB.get())
        Variables.load -= float(swWgt2SB.get())
        Variables.load -= float(swWgt3SB.get())

        Variables.load -= float(aWgt1SB.get())
        Variables.load -= float(aWgt2SB.get())
        Variables.load -= float(aWgt3SB.get())
        Variables.load -= float(aWgt4SB.get())
        print(Variables.load)

        if Variables.load <= 0.0:
            print("Error - load too low")
            return 0

        Variables.rates[0] = float(physicSB.get())
        Variables.rates[1] = float(strikeSB.get())
        Variables.rates[2] = float(slashSB.get())
        Variables.rates[3] = float(pierceSB.get())
        Variables.rates[4] = float(magicSB.get())
        Variables.rates[5] = float(fireSB.get())
        Variables.rates[6] = float(electricSB.get())
        Variables.rates[7] = float(holySB.get())
        Variables.rates[8] = float(immSB.get())
        Variables.rates[9] = float(robSB.get())
        Variables.rates[10] = float(focusSB.get())
        Variables.rates[11] = float(vitSB.get())
        Variables.rates[12] = float(poiseSB.get())

        i = 0
        for rate in Variables.rates:
            if rate > 0.0:
                i += 1
        for rate in Variables.rates:
            rate = round(rate / i, 4)

        Variables.startClass = startClassCB.get()

        SecondWindow.openSecondWindow()
    return 0

ttk.Button(frm, text="Wyjdź", command=root.destroy).grid(column=3, row=13)
ttk.Button(frm, text="Dalej", command=setParamethers).grid(column=4, row=13)
root.mainloop()