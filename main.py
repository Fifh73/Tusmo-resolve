from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Fonction qui compte le nombre de lettres du mot
def nb_case():
    all_case = driver.find_elements(By.CSS_SELECTOR, ".cell-content")
    l_mot = len(all_case) / 6
    return int(l_mot)

#Instance chrome
driver = webdriver.Chrome()

#Ouvre le site web
driver.get("https://www.tusmo.xyz/sb88ac8f")

#Récupere la valeure de la lettre de départ
element = driver.find_element(By.CSS_SELECTOR, ".cell-content")
print(element.text)

#Récupère le nombre de lettre du mot
longueur_mot = nb_case()
print("nombre de lettres :", longueur_mot)

#Ferme l'instance chrome
#time.sleep(3)
driver.quit()