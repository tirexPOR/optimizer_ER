import numpy as np

maxLoad=1.0
limitLoad=1.0
load=0.0

rates=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
constant = 0.0

regions=[False, "Ainsel River", False, "Altus Plateau", False, "Caelid", False, "Cathedral of the Forsaken",
         False, "Consecrated Snowfield", False, "Crumbling Farum Azula", False, "Deeproot Depths", False, "Lake of Rot",
         False, "Layndell, Ashen Capital", False, "Leyndell, Royal Capital", False, "Limgrave",
         False, "Liurnia of the Lakes", False, "Miquella's Haligtree", False, "Mohgwyn Dynasty Mausoleum",
         False, "Mountaintop of the Giants", False, "Nokron, Eternal City", False, "Nokstella, Eternal City",
         False, "Roundtable hold", False, "Siofra River", False, "Subterranean Shunning-Grounds",
         False, "Weeping peninsula"]

bosses=[False, "Commander Niall", False, "Elemer of the Briar", False, "Godfrey, First Elden Lord",
        False, "Loretta, Knight of the Haligtree", False, "Malenia, Blade of Miquella",
        False, "Maliketh, the Black Blade", False, "Mohg, Lord of Blood", False, "Morgott the Omen King",
        False, "Rennala, Queen of the Full Moon", False, "Starscourge Radahn", True, "None"]

classes={"Astrolog":"Astrologer", "Bandyta":"Bandit", "Bohater":"Hero", "Łajdak":"Wretch", "Prorok":"Prophet",
         "Samuraj":"Samurai", "Spowiednik":"Confessor", "Więzień":"Prisoner", "Włóczęga":"Vagabond",
         "Wojownik":"Warrior"}

roll=1.0
startClass=""

helmetSet=""
helmetSetRes=[]
chestplateSet=""
chestplateSetRes=[]
gauntletsSet=""
gauntletsSetRes=[]
legArmorSet=""
legArmorSetRes=[]

secondWindowFlag=0
thirdWindowFlag=0
resultWindowFlag=0

variables = np.array([])
helmet_len = 0
chest_len = 0
gauntlet_len = 0
legArmor_len = 0
armor_names = []