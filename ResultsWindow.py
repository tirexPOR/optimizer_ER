from tkinter import *
from tkinter import ttk
import numpy as np

import Variables
import Algorithm

def openResultsWindow(wyniki):
    Variables.resultWindowFlag = 1
    results = Toplevel()
    results.title("Elden Ring Optimizer")
    results.grid()

    ttk.Label(results, text="Hełm").grid(column=0, row=1)
    try:
        helmet_name = wyniki['helmet'][1]
    except:
        helmet_name = 'None'
    helmetLabel = ttk.Label(results, text=helmet_name)
    helmetLabel.grid(column=1, row=1)
    helmet = IntVar()
    helmetCB = ttk.Checkbutton(results, text="Wymień", offvalue=0, onvalue=1, variable=helmet)
    helmetCB.grid(column=2, row=1)
    if Variables.helmetSet != "":
        helmetCB["state"] = "disabled"

    ttk.Label(results, text="Napierśnik").grid(column=0, row=2)
    try:
        chest_name = wyniki['chest'][1]
    except:
        chest_name = 'None'
    chestplateLabel = ttk.Label(results, text=chest_name)
    chestplateLabel.grid(column=1, row=2)
    chestplate = IntVar()
    chestplateCB = ttk.Checkbutton(results, text="Wymień", offvalue=0, onvalue=1, variable=chestplate)
    chestplateCB.grid(column=2, row=2)
    if Variables.chestplateSet != "":
        chestplateCB["state"] = "disabled"

    ttk.Label(results, text="Rękawice").grid(column=0, row=3)
    try:
        gauntlets_name = wyniki['gauntlets'][1]
    except:
        gauntlets_name = 'None'
    gauntletsLabel = ttk.Label(results, text=gauntlets_name)
    gauntletsLabel.grid(column=1, row=3)
    gauntlets = IntVar()
    gauntletsCB = ttk.Checkbutton(results, text="Wymień", offvalue=0, onvalue=1, variable=gauntlets)
    gauntletsCB.grid(column=2, row=3)
    if Variables.gauntletsSet != "":
        gauntletsCB["state"] = "disabled"

    ttk.Label(results, text="Nakolanniki/\nButy").grid(column=0, row=4)
    try:
        legArmor_name = wyniki['legArmor'][1]
    except:
        legArmor_name = 'None'
    legArmorLabel = ttk.Label(results, text=legArmor_name)
    legArmorLabel.grid(column=1, row=4)
    legArmor = IntVar()
    legArmorCB = ttk.Checkbutton(results, text="Wymień", offvalue=0, onvalue=1, variable=legArmor)
    legArmorCB.grid(column=2, row=4)
    if Variables.legArmorSet != "":
        legArmorCB["state"] = "disabled"

    def closeWindow():
        Variables.resultWindowFlag = 0
        results.withdraw()
        return 0

    def change():
        if chestplate.get() == 1 or gauntlets.get() == 1 or helmet.get() == 1 or legArmor.get() == 1:
            if chestplate.get() == 1 and Variables.chest_len != 0:
                try:
                    Variables.variables = np.delete(Variables.variables, wyniki['chest'][0], axis=0)
                    Variables.chest_len -= 1
                    Variables.armor_names.pop(wyniki['chest'][0])
                    if helmet.get() == 1:
                        wyniki['helmet'][0] -= 1
                    if gauntlets.get() == 1:
                        wyniki['gauntlets'][0] -= 1
                    if legArmor.get() == 1:
                        wyniki['legArmor'][0] -= 1
                except:
                    print("error")
            elif Variables.chest_len == 0:
                Variables.chestplateSet = "None"
                Variables.chestplateSetRes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            if gauntlets.get() == 1 and Variables.gauntlet_len != 0:
                try:
                    Variables.variables = np.delete(Variables.variables, wyniki['gauntlets'][0], axis=0)
                    Variables.gauntlet_len -= 1
                    Variables.armor_names.pop(wyniki['gauntlets'][0])
                    if helmet.get() == 1:
                        wyniki['helmet'][0] -= 1
                    if legArmor.get() == 1:
                        wyniki['legArmor'][0] -= 1
                except:
                    print('error')
            elif Variables.gauntlet_len == 0:
                Variables.gauntletsSet = "None"
                Variables.gauntletsSetRes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            if helmet.get() == 1 and Variables.helmet_len != 0:
                try:
                    Variables.variables = np.delete(Variables.variables, wyniki['helmet'][0], axis=0)
                    Variables.helmet_len -= 1
                    Variables.armor_names.pop(wyniki['helmet'][0])
                    if legArmor.get() == 1:
                        wyniki['legArmor'][0] -= 1
                except:
                    print('error')
            elif Variables.helmet_len == 0:
                Variables.helmetSet = "None"
                Variables.helmetSetRes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            if legArmor.get() == 1 and Variables.legArmor_len != 0:
                try:
                    Variables.variables = np.delete(Variables.variables, wyniki['legArmor'][0], axis=0)
                    Variables.legArmor_len -= 1
                    Variables.armor_names.pop(wyniki['legArmor'][0])
                except:
                    print('error')
            elif Variables.legArmor_len == 0:
                Variables.legArmorSet = "None"
                Variables.legArmorSetRes = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            closeWindow()
            openResultsWindow(Algorithm.optimize(Variables.variables, Variables.helmet_len, Variables.chest_len,
                                                 Variables.gauntlet_len, Variables.legArmor_len))
            return 0
        else:
            return 0

    ttk.Button(results, text="Powrót", command=closeWindow).grid(column=0, row=5)
    ttk.Button(results, text="Wymień", command=change).grid(column=2, row=5)

    results.mainloop()
