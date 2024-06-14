import json

#crée un dictionnaire qui associe chque lettre de l'alphabet à sa frequence d'apparition dans la langue française
frequences = {}

frequences['a'] = 8.15
frequences['b'] = 0.97
frequences['c'] = 3.15
frequences['d'] = 3.73
frequences['e'] = 17.39
frequences['f'] = 1.12
frequences['g'] = 0.97
frequences['h'] = 0.85
frequences['i'] = 7.31
frequences['j'] = 0.45
frequences['k'] = 0.02
frequences['l'] = 5.69
frequences['m'] = 2.87
frequences['n'] = 7.12
frequences['o'] = 5.28
frequences['p'] = 2.80
frequences['q'] = 1.21
frequences['r'] = 6.64
frequences['s'] = 8.14
frequences['t'] = 7.22
frequences['u'] = 6.38
frequences['v'] = 1.64
frequences['w'] = 0.03
frequences['x'] = 0.41
frequences['y'] = 0.28
frequences['z'] = 0.15


#Ouvre le fichier mots.json qui contient des mot de la langue française
with open('./mots.json', 'r') as f:
    data = json.load(f)

#Sépare les mots avec -, des espacese et qui font moins de 3 lettres, des mots entiers
null_mot = []
ok_mot = []
for mot in data:
    if ' ' in mot :
       null_mot.append(mot)
    elif '-' in mot :
        null_mot.append(mot)
    elif len(mot) < 3:
        null_mot.append(mot)
    else:
        ok_mot.append(mot)

#Additionne la probabilité d'un mot en fonction de ses lettres
poids_mot = {}

for each_mot in ok_mot:
    val = 0
    for lettres in each_mot:
        val = val + frequences[lettres]
    poids_mot[each_mot] = val

ord_mots = dict(sorted(poids_mot.items(), key=lambda item: item[1], reverse=True))

#Enregistre en json le dictionnaire avec les mots triés
with open('mots-stat.json', 'w') as f:
    json.dump(ord_mots, f)