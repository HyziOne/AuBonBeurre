from random import *

class values:
    "definition des valeurs aléatoire"
v = values()
li=[]
v.temps_cuve = round(uniform(2.5,4),1)
v.temps_ext = round(uniform(8,14),1)
v.pds_lait = randint(3512,4607)
v.ph = round(uniform(6.8,7.2),1)
v.k_plus = randint(35,47)
v.conc_nacl = round(uniform(1,1.7),1)
v.niv_salmonelle = randint(17,37)
v.niv_ecoli = randint(35,49)
v.niv_listeria = randint(28,54)
li.append(v.temps_cuve)
li.append(v.temps_ext)
li.append(v.pds_lait)
li.append(v.ph)
li.append(v.k_plus)
li.append(v.conc_nacl)
li.append(v.niv_salmonelle)
li.append(v.niv_ecoli)
li.append(v.niv_listeria)

print(li)
