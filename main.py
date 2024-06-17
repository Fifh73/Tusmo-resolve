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

#Instance chrome
driver = webdriver.Chrome()

#Ouvre le site web
driver.get("https://www.tusmo.xyz/s411f0c5")

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

pg.write(lettre_liste[1])
pg.press('enter')

#Ferme l'instance chrome
time.sleep(3)
driver.quit()