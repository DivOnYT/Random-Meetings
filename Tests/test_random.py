import random

liste = ["a", "b", "c"]
for mots in liste:
    mot = random.choice(liste)
    print(mot)
    ind = int(liste.index(mot))
    del liste[ind]
    print(liste)