from tkinter import *
from tkinter import ttk
import numpy as np

import Variables
import ResultsWindow
import Connector
import Algorithm

def openThirdWindow():
    Variables.thirdWindowFlag = 1

    trdW = Toplevel()
    trdW.title("Elden Ring Optimizer")
    trdW.grid()

    ttk.Label(trdW, text="Wybierz elementy, które mają być zachowane:").grid(columnspan=2, row=0)
    ttk.Label(trdW, text="Hełm").grid(column=0, row=1, pady=5)
    helmetList = Connector.downloadList('Helmet')
    helmetCB = ttk.Combobox(trdW, values=helmetList)
    helmetCB.grid(column=1, row=1)
    ttk.Label(trdW, text="Napierśnik").grid(column=0, row=2)
    chestplateList = Connector.downloadList('Chestplate')
    chestplateCB = ttk.Combobox(trdW, values=chestplateList)
    chestplateCB.grid(column=1, row=2)
    ttk.Label(trdW, text="Rękawice").grid(column=0, row=3, pady=5)
    gauntletsList = Connector.downloadList('Gauntlets')
    gauntletsCB = ttk.Combobox(trdW, values=gauntletsList)
    gauntletsCB.grid(column=1, row=3)
    ttk.Label(trdW, text="Nakolanniki/Buty").grid(column=0, row=4)
    legArmorList = Connector.downloadList('Leg armor')
    legArmorCB = ttk.Combobox(trdW, values=legArmorList)
    legArmorCB.grid(column=1, row=4)

    def setParameters():
        if Variables.resultWindowFlag == 0:
            Variables.helmetSet = helmetCB.get()
            if Variables.helmetSet != "":
                Variables.helmetSetRes = Connector.downloadResSet(Variables.helmetSet)
                Variables.load -= Variables.helmetSetRes[13]
                for i in range(len(Variables.rates)):
                    Variables.constant += Variables.helmetSetRes[i] * Variables.rates[i]

            Variables.chestplateSet = chestplateCB.get()
            if Variables.chestplateSet != "":
                Variables.chestplateSetRes = Connector.downloadResSet(Variables.chestplateSet)
                Variables.load -= Variables.chestplateSetRes[13]
                for i in range(len(Variables.rates)):
                    Variables.constant += Variables.helmetSetRes[i] * Variables.rates[i]

            Variables.gauntletsSet = gauntletsCB.get()
            if Variables.gauntletsSet != "":
                Variables.gauntletsSetRes = Connector.downloadResSet(Variables.gauntletsSet)
                Variables.load -= Variables.gauntletsSetRes[13]
                for i in range(len(Variables.rates)):
                    Variables.constant += Variables.gauntletsSetRes[i] * Variables.rates[i]

            Variables.legArmorSet = legArmorCB.get()
            if Variables.legArmorSet != "":
                Variables.legArmorSetRes = Connector.downloadResSet(Variables.legArmorSet)
                Variables.load -= Variables.legArmorSetRes[13]
                for i in range(len(Variables.rates)):
                    Variables.constant += Variables.legArmorSetRes[i] * Variables.rates[i]

            if Variables.load <= 0.0:
                print("Nic nie założysz")
                return 0

            Variables.variables = np.array(Connector.downloadRes())
            Variables.helmet_len = Connector.downloadLen('Helmet')
            Variables.chest_len = Connector.downloadLen('Chestplate')
            Variables.gauntlet_len = Connector.downloadLen('Gauntlets')
            Variables.legArmor_len = Connector.downloadLen('Leg armor')
            Variables.armor_names = Connector.downloadNames()

            ResultsWindow.openResultsWindow(Algorithm.optimize(Variables.variables, Variables.helmet_len,
                                                               Variables.chest_len, Variables.gauntlet_len,
                                                               Variables.legArmor_len))
        return 0

    def closeWindow():
        if Variables.resultWindowFlag == 0:
            Variables.thirdWindowFlag = 0
            trdW.withdraw()
        return 0

    ttk.Button(trdW, text="Powrót", command=closeWindow).grid(column=0, row=5, pady=(5, 0))
    ttk.Button(trdW, text="Dalej", command=setParameters).grid(column=1, row=5)

    trdW.mainloop()
