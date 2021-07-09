#######Ce programme n'est pas fini !!!! :/


from numpy import string_
from numpy.lib.npyio import load
import pandas as pd
import os, random, re
from colorama import Fore, Back, Style, init, deinit
from Loader import *

init()

path = os.getcwd()

class Base(object):
    def __init__(self, nb_groups):
        self.sheets_names = ["Avril 2021", "Mai 2021", "Juin 2021", "Juillet 2021"]
        self.path = os.getcwd()
        self.participants = []
        self.nb_groups = nb_groups
        self.nb_partici = get_size(fr'{self.path}\Liste_Part.xlsx', 'Liste participants')
        part = load_participants(fr'{self.path}\Liste_Part.xlsx', 'Liste participants')
        if self.nb_groups > self.nb_partici:
            print(f"{Fore.RED} ERROR !! Vous ne pouvez pas creer {self.nb_groups} groupes alors qu'il n'y a que {self.participants} personnes qui participent. {Fore.RESET}")
            return 0

        elif (self.nb_groups == 0) or (self.nb_groups < 0):
            print(f"{Fore.RED} ERREUR sur les groupes. Vérifiez de ne pas avoir entré une valeur IMPOSSIBLE !! {Fore.RESET}")
            return 0
        try:
            int(nb_groups)
        except Exception:
            return Exception
        
        for parti in part.values:
            self.participants.append(parti)
        # ----------->
        self.nb_p_group = self.nb_partici//self.nb_groups # donne le nombre de personnes pour un groupe de X taille
        self.nb_r_group = self.nb_partici%self.nb_groups #Donne les personnes restantes à des groupes de X taille
        # <-----------
        print(f"{Fore.BLUE} Vous pouvez créer {self.nb_p_group} groupes de {Fore.GREEN}{nb_groups}{Fore.BLUE} personnes.\n Il y aura une reste de {Fore.RED}{self.nb_r_group}{Fore.BLUE} personne. {Fore.RESET}")
        self.groups = load_groups(fr'{self.path}\Liste_Part.xlsx', self.sheets_names, self.nb_partici)  #Tous les Groupes assemblés
        self.run(self.nb_p_group)

        
    def verify_participant(self, to_verify, o_person, size): #Verifie si une personne a déjà été avec une autre si oui renvoie True
        path = self.path + "\Liste_Part.xlsx"
        groups = self.groups
        liste = self.participants
        sheets = self.sheets_names
        for name in sheets:
            file = pd.read_excel(path, sheet_name=name)
            fil = file.head(size)
            nb_rows = len(fil.axes[0])
            nb_columns = len(fil.columns[0]) - 1
            test_group = []
            compteur = 0
            for column in fil:
                if compteur != 5 or compteur < 5:
                    part = list(file[f"Participant {nb_columns-compteur}"])
                    test_group.append(part)
                    compteur = compteur + 1
            for groupe in test_group:
                try:
                    ind = int(groupe.index(to_verify))
                    print(str(ind) + f"{Fore.GREEN} Verified {Fore.RESET}" + str(to_verify))
                except:
                    pass

    def run(self, nb_p_groups):
        liste = self.participants
        groups = []
        for x in range(nb_p_groups):
            test = self.choose(liste, self.nb_groups)
            groups.append(test)
        for group in groups:
            for x in range(self.nb_groups):
                for man in group:
                    listes = group
                    ind = int(group.index(man))
                    del group[ind]
                    verif = self.verify_participant(man, self.groups, self.nb_partici)
                    group = listes

    def choose(self, liste, count):
        group = []
        for x in range(count):
            try:
                mot = random.choice(liste)
                group.append(mot)
                ind = int(liste.index(mot))
                del liste[ind]
            except:
                pass
        return group

if __name__ == "__main__":
    MaBAse = Base(5)