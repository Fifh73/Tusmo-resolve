from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as pg
import json
import time

#Fonction qui compte le nombre de lettres du mot
def nb_case():
    all_case = driver.find_elements(By.CSS_SELECTOR, ".cell-content")
    l_mot = len(all_case) / 6
    return int(l_mot)

#Fonction qui permet d'analyser un resultat et prévoir le prochain mot
def resolve(list, red, yellow):
    a = 0



#Fonction qui permet de sortir un resultat
def result():
    red_l = []
    yellow_l = []
    
    try:
        red = driver.find_elements(By.CSS_SELECTOR, ".r")
        for element_r in red:
            red_l.append(element_r.text)
    except:
        print("Pas de cases rouges")

    try:
        yellow = driver.find_elements(By.CSS_SELECTOR, ".y")
        for element_y in yellow:
            yellow_l.append(element_y.text)
    except:
        print("Pas de cases jaunes")
    
    return red_l, yellow_l



#Instance chrome
driver = webdriver.Chrome()

#Ouvre le site web, crée la variable local storage locale pour passer le site en français et recharge la page
partie = "s451e3a1"
driver.get("https://www.tusmo.xyz/" + partie)
driver.execute_script("window.localStorage.setItem('locale', 'fr')")
driver.get("https://www.tusmo.xyz/" + partie)

#Récupere la valeure de la lettre de départ
lettre = driver.find_element(By.CSS_SELECTOR, ".cell-content")
l1 = lettre.text

#Récupère le nombre de lettre du mot
longueur_mot = nb_case()
print("nombre de lettres :", longueur_mot)

#Trie la liste de mots en fontcion du nombre de lettres et les enregistre dans la liste liste_long
liste_long = []
with open('./mots-stat.json', 'r') as f:
    data = json.load(f)
for mot in data:
    if len(mot) == longueur_mot:
        liste_long.append(mot)

#Trie la liste de mot en fonction de la premiere lettre
lettre_liste = []
for t_mot in liste_long:
    if t_mot[0] == l1.lower():
        lettre_liste.append(t_mot)



#Inscrit le premier mot de la liste dans le jeu
pg.write(lettre_liste[5])
pg.press('enter')

# Appelle la fonction result qui permet de donner un resultat avec la position des rouges et des oranges
#r,y = result()

#Ajoute la permière lettre du mot au début de la liste
#r.insert(l1)

#resolve(lettre_liste, r, y)

#Ferme l'instance chrome
time.sleep(3)
driver.quit()