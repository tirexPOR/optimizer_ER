import pulp
from pulp import *

import Variables

def optimize(coeff, helmet_len, chest_len, gauntlets_len, legArmor_len):
    print(helmet_len)
    print(chest_len)
    print(gauntlets_len)
    print(legArmor_len)
    print(coeff.shape[0])
    size = coeff.shape[0]

    # Zdefiniowanie problemu
    prob = LpProblem("Maksymalizacja_negacji_obrażeń", LpMaximize)

    # Utworzenie zmiennych
    x = [LpVariable(f"x{i}", 0, 1, LpInteger) for i in range(size)]

    # Utworzenie funkcji celu
    prob += lpSum([(coeff[i][0] * Variables.rates[0] + coeff[i][1] * Variables.rates[1] +
                    coeff[i][2] * Variables.rates[2] + coeff[i][3] * Variables.rates[3] +
                    coeff[i][4] * Variables.rates[4] + coeff[i][5] * Variables.rates[5] +
                    coeff[i][6] * Variables.rates[6] + coeff[i][7] * Variables.rates[7] +
                    coeff[i][8] * Variables.rates[8] + coeff[i][9] * Variables.rates[9] +
                    coeff[i][10] * Variables.rates[10] + coeff[i][11] * Variables.rates[11] +
                    coeff[i][12] * Variables.rates[12]) * x[i] + Variables.constant for i in range(size)])

    # Utworzenie ograniczeń
    totalPieces = 0

    prob += lpSum([coeff[i][13] * x[i] for i in range(size)]) <= Variables.load, "Total weight piece"
    if Variables.chestplateSet == "":
        prob += lpSum([x[i] for i in range(chest_len)]) <= 1, "Chestplate"
        totalPieces += 1
    else:
        prob += lpSum([x[i] for i in range(chest_len)]) == 0, "Chestplate"

    if Variables.gauntletsSet == "":
        prob += lpSum([x[i] for i in range(chest_len, chest_len + gauntlets_len)]) <= 1, "Gauntlets"
        totalPieces += 1
    else:
        prob += lpSum([x[i] for i in range(chest_len, chest_len + gauntlets_len)]) == 0, "Gauntlets"

    if Variables.helmetSet == "":
        prob += lpSum([x[i] for i in range(chest_len + gauntlets_len,
                                           chest_len + gauntlets_len + helmet_len)]) <= 1, "Helmet"
        totalPieces += 1
    else:
        prob += lpSum([x[i] for i in range(chest_len + gauntlets_len,
                                           chest_len + gauntlets_len + helmet_len)]) == 0, "Helmet"

    if Variables.legArmorSet == "":
        prob += lpSum([x[i] for i in range(chest_len + gauntlets_len + helmet_len,
                                           chest_len + gauntlets_len + helmet_len + legArmor_len)]) <= 1, "Leg armor"
        totalPieces += 1
    else:
        prob += lpSum([x[i] for i in range(chest_len + gauntlets_len + helmet_len,
                                           chest_len + gauntlets_len + helmet_len + legArmor_len)]) == 0, "Leg armor"

    prob += lpSum([x[i] for i in range(size)]) <= totalPieces, "Total piece"

    # Chest
    # Gauntlets
    # Helmet
    # LegArmor

    # Rozwiązanie problemu
    prob.solve()
    weight_total = 0.0

    # Wypisanie wyniku
    wyniki = {}
    for variable in x:
        if variable.varValue == 1.0:
            number = int(variable.name[1:])

            weight_total += coeff[number][13]
            if number < chest_len:
                wyniki['chest'] = [number, Variables.armor_names[number]]
            elif number < chest_len + gauntlets_len:
                wyniki['gauntlets'] = [number, Variables.armor_names[number]]
            elif (number < chest_len + gauntlets_len + helmet_len):
                wyniki['helmet'] = [number, Variables.armor_names[number]]
            else:
                wyniki['legArmor'] = [number, Variables.armor_names[number]]

    if Variables.chestplateSet != "":
        wyniki['chest'] = [-1, Variables.chestplateSet]
        weight_total += Variables.chestplateSetRes[13]
    if Variables.gauntletsSet != "":
        wyniki['gauntlets'] = [-1, Variables.gauntletsSet]
        weight_total += Variables.gauntletsSetRes[13]
    if Variables.helmetSet != "":
        wyniki['helmet'] = [-1, Variables.helmetSet]
        weight_total += Variables.helmetSetRes[13]
    if Variables.legArmorSet != "":
        wyniki['legArmor'] = [-1, Variables.legArmorSet]
        weight_total += Variables.legArmorSetRes[13]

    print(f"Objective value: {value(prob.objective)}", '-', weight_total)
    # physical = round(100 * (100-coeff[wyniki['chest'][0]][0])/100 * (100-coeff[wyniki['gauntlets'][0]][0])/100 * \
    #            (100-coeff[wyniki['helmet'][0]][0])/100 * (100-coeff[wyniki['legArmor'][0]][0])/100, 4)
    # poise = coeff[wyniki['chest'][0]][12] + coeff[wyniki['gauntlets'][0]][12] + coeff[wyniki['helmet'][0]][12] + \
    #         coeff[wyniki['legArmor'][0]][12]
    # print('Physical: ' + str(100-physical))
    # print('Poise: ' + str(poise))
    return wyniki
