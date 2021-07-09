from numpy import string_
import numpy
from numpy.lib.npyio import load, save
import pandas as pd
import os, random, re, time
from colorama import Fore, Back, Style, init, deinit
from pandas.core.frame import DataFrame
from Loader import *
from updater import *

os.system("title Random Meetings - Argon and Co* -> Made By Côme d'Hérouville/Diversité infinie On YT")

titre = fr"""  {Fore.BLUE}{Style.BRIGHT}
 ____                    _                     __  __              _    _                    
|  _ \  __ _  _ __    __| |  ___   _ __ ___   |  \/  |  ___   ___ | |_ (_) _ __    __ _  ___ 
| |_) |/ _` || '_ \  / _` | / _ \ | '_ ` _ \  | |\/| | / _ \ / _ \| __|| || '_ \  / _` |/ __|
|  _ <| (_| || | | || (_| || (_) || | | | | | | |  | ||  __/|  __/| |_ | || | | || (_| |\__ \
|_| \_\\__,_||_| |_| \__,_| \___/ |_| |_| |_| |_|  |_| \___| \___| \__||_||_| |_| \__, ||___/
                                                                                   |___/    
                                                            {Fore.LIGHTRED_EX}{Style.DIM}By Côme d'Hérouville/ Diversité infinie On YT  {Fore.RESET}{Style.RESET_ALL}                      """

print(titre)

init()

path = os.getcwd()

class Base(object):
    def __init__(self, nb_groups):
        self.path = os.getcwd()
        xl = pd.ExcelFile(f"{self.path}\Liste_Part.xlsx")
        sheets = xl.sheet_names
        black_sheets = ["Liste participants", "Tirage_RM", "Grade_ancienneté"]
        self.sheets_names = []
        for sheet in sheets:
            if sheet in black_sheets:
                pass
            else:
                self.sheets_names.append(sheet)

        self.participants = []
        # ---- > Compteurs pour la barre de chargement
        self.compteur_d = 0 #compteur pour la fonction repecher
        # < ------
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
        self.nb_person = self.nb_partici//self.nb_p_group #donne le nombre de personnes par groupe
        self.nb_r_group = self.nb_partici%self.nb_groups #Donne les personnes restantes à des groupes de X taille
        # <-----------

        print(f"{Fore.BLUE} Vous pouvez créer {self.nb_p_group} groupes de {Fore.GREEN}{nb_groups}{Fore.BLUE} personnes.\n Il y aura une reste de {Fore.RED}{self.nb_r_group}{Fore.BLUE} personne. {Fore.RESET}")

        self.groups = load_groups(fr"{self.path}\Liste_Part.xlsx", self.sheets_names, self.nb_partici)  #Tous les Groupes assemblés

        self.dF = main(self.sheets_names)
        #self.dF = load_data(fr"{self.path}\Project_DF.xlsx", len(self.participants))
        #self.sheet_vierge()

        daf = [0]
        daf = int(len(self.participants)) * daf
        daf1 = []
        daf1.append(daf)
        daf1 = daf1 * self.nb_partici
        np = numpy.array(daf1)
        part = self.participants
        self.dF = pd.DataFrame(np, index=self.participants, columns=self.participants)

        groups = []
        rand = self.rand(self.participants)
        #rand = self.repecher(self.participants, self.participants)
        print(f"{Fore.GREEN}{Style.DIM} La liste des groupes(Premier Brassage) est : \n{Fore.RESET}")
        """for group in rand:
            print(Fore.BLUE + ", ".join(group) + Fore.RESET)"""
        print(f"{Fore.RED} Attention !! cette liste n'est pas définitive !! Laissez tourner le prgramme ... {Fore.RESET}{Style.RESET_ALL}")
        calc = self.nb_groups
        liste_participants = self.participants
        if self.nb_groups == len(rand):
            pass
        else:
            print(f"{Fore.RED}BUG dans le programme. Nous repechons la liste des personnes")
            try:
                for personne in self.list_part:
                    inde = liste_participants.index(personne)
                    del liste_participants[inde]
            except:
                pass
            #self.rand(liste_participants)
            for x in range(self.nb_groups):
                ap = self.repecher(self.list_part, self.participants)
                rand.append(ap)
            print(f"{Fore.GREEN}{Style.BRIGHT} Chargement Fini 100 % : Fin du 2ème brassage.{Style.RESET_ALL}{Fore.RESET}")
        if self.nb_r_group and self.nb_r_group > 1:
            for personne in self.list_part:
                choix = random.choice(rand)
                idx = rand.index(choix)
                rand[idx].append(personne)
        elif self.nb_r_group == 1:
            choix = random.choice(rand)
            idx = rand.index(choix)
            rand[idx].append(self.list_part[0])
        self.list_groups = rand
        #save_excel(self.dF)
        #save_gen_groups(self.list_groups, self.dF)
        self.save_as_txt(f"{self.path}\Output.txt", self.list_groups)
        #self.rand([random.choices(self.participants, k=4)])


    def save_excel(self, data):
        # ------------> Ecrire dans un fichier excel
        writer = pd.ExcelWriter('Project_DF.xlsx')
        data.to_excel(writer)
        writer.save()
        pathor = self.path + "\Liste_Part.xlsx"
        print(f"{Fore.GREEN} Fichier Excel enregistré en {pathor} . {Fore.RESET}")
        # <------------ Et Sauvegarder

    def repecher(self, liste_p_pris, liste_entiere):
        liste = liste_entiere
        try:
            for personne in liste_p_pris:
                inde = liste.index(personne)
                del liste[inde]
        except:
            pass

        lister = liste_entiere
        self.cote = []
        test = []
        final = []
        blck = []

        compteure = 0
        for personne in liste:
            if personne in blck:
                print("Blacklisted")
            else:
                inde = find(personne, self.participants)
                for x in range(len(self.participants)):
                    indice = self.dF.at[self.dF.index[x], personne]
                    #ch = f"{inde}:{x}:{indice}"   #Code index === Ordonnée, x === Abscisse, autre valeur === la valeur de la case
                    if indice == "x":
                        pass
                    else:
                        ch = [inde, x, indice]
                        test.append(ch)
                        blck.append(personne)
        self.cote = test
        del test
        liste_items = []
        items = []
        list_groups = []
        list_part = []
        entre_d = []
        black = []
        list_part = []
        chargement = []
        for personne in lister:
            if personne in black:
                print("Blacklisted")
            else:
                dic = self.get_person_b_name(personne)
                for cle, valeur in dic.items():
                    liste_items.append(valeur)
                while len(items) < self.nb_p_group:
                    for cle, valeur in dic.items():
                        mini = min(liste_items)
                        if valeur == mini:
                            items.append(cle)
                part = 0
                while part < self.nb_groups:
                    rd = random.choice(items)
                    ind = self.participants[rd]
                    if ind in black:
                        pass
                    else:
                        black.append(ind)
                        entre_d.append(ind)
                        list_part.append(ind)
                        part = part + 1
                        try:
                            calc = self.nb_p_group%compteure
                            if calc == 1:
                                self.compteur_d = self.compteur_d + 1
                                if self.compteur_d == 0 or self.compteur_d == 1 or self.compteur_d == 2:
                                    cla = self.compteur_d * self.nb_p_group
                                    print(f"{Fore.BLUE}{Style.BRIGHT} Chargement ... {cla} % avant la fin du premier brassage.{Style.RESET_ALL}{Fore.RESET}")
                                else:
                                    cla = compteure * self.nb_p_group
                                    print(f"{Fore.BLUE}{Style.BRIGHT} Chargement ... {cla} % avant la fin du premier brassage.{Style.RESET_ALL}{Fore.RESET}")
                        except:
                            pass
                        compteure = compteure + 1

                
                blck.append(personne)
                return entre_d

                """list_groups.append(entre_d)
                black.append(personne)
                time.sleep(1.5)
                
                del entre_d
                entre_d = []
        del liste_items

        for group in list_groups:
            list_groups.append(group)

        # prendre 1 groupe au hasard pour la/les dernières
        if self.nb_r_group:
            print(liste)

        #self.output()
        #self.save_as_txt(f"{path}\Output.txt", self.list_groups)
        return list_groups"""

    def rand(self, liste): # Retourne des groupes à partir de personnes / groupes  de nb_groups taille
        print(f"{Fore.RED}{Style.DIM} Si le programme a un 'freeze' sur un %, redemarrez le programme ...{Fore.RESET}{Style.RESET_ALL}")
        lister = liste
        self.cote = []
        test = []
        final = []
        for personne in liste:
            inde = find(personne, self.participants)
            for x in range(len(self.participants)):
                indice = self.dF.at[self.dF.index[x], personne]
                #ch = f"{inde}:{x}:{indice}"   #Code index === Ordonnée, x === Abscisse, autre valeur === la valeur de la case
                if indice == "x":
                    pass
                else:
                    ch = [inde, x, indice]
                    test.append(ch)
        self.cote = test
        del test
        liste_items = []
        items = []
        self.list_groups = []
        entre_d = []
        # ---- > Compteurs pour la barre de chargement
        self.compteur_u = 0 #compteur pour la fonction rand
        # < ------
        black = []
        self.list_part = []
        for personne in lister:
            if personne in black:
                pass
            else:
                dic = self.get_person_b_name(personne)
                for cle, valeur in dic.items():
                    liste_items.append(valeur)
                while len(items) < self.nb_p_group:
                    for cle, valeur in dic.items():
                        mini = min(liste_items)
                        if valeur == mini:
                            items.append(cle)
                part = 0
                while part < self.nb_groups:
                    rd = random.choice(items)
                    ind = self.participants[rd]
                    if ind in black:
                        pass
                    else:
                        if self.verify_p_by_p(personne, ind) == True:
                            black.append(ind)
                            entre_d.append(ind)
                            self.list_part.append(ind)
                            part = part + 1
                            print(f"{Fore.BLUE}{Style.BRIGHT} Chargement ... {self.compteur_u} % avant la fin du premier brassage.{Style.RESET_ALL}{Fore.RESET}")
                            self.compteur_u = self.compteur_u + 1
                        else:
                            run = False
                            while run != True:
                                rd = random.choice(items)
                                ind = self.participants[rd]
                                if self.verify_p_by_p(personne, ind) == True:
                                    black.append(ind)
                                    entre_d.append(ind)
                                    self.list_part.append(ind)
                                    part = part + 1
                                    run = True
                                
                self.list_groups.append(entre_d)
                black.append(personne)
                self.list_part.append(ind)
                time.sleep(0.25)
                
                del entre_d
                entre_d = []
        
        del liste_items
        #self.output()
        #self.save_as_txt(f"{path}\Output.txt", self.list_groups)
        print(f"{Fore.GREEN}{Style.BRIGHT} Chargement Fini 100 % avant la fin du premier brassage.{Style.RESET_ALL}{Fore.RESET}")
        return self.list_groups

        """test = []   # Code Inutile
        main = []

        for person in range(len(list_groups)):
            personne = list_groups[person]
            test.append(personne)
            try:
                calcul = person % self.nb_person
                calcul2 = person / self.nb_person
                if calcul == 0 and calcul2 != 0:
                    main.append(test)
                    del test
                    test = []
            except:
                pass
"""
    def verify_p_by_p(self, personne, o_person): #Vérifier une personne à partir d'une autre pour la faire entrer dans le groupe
        personne1 = dict(self.get_person_b_name(personne))
        personne2 = dict(self.get_person_b_name(o_person))
        ind1 = self.participants.index(personne)
        ind2 = self.participants.index(o_person)
        valeur1 = False
        valeur2 = False
        for cle, valeur in personne1.items():
            if cle == ind2:
               valeur1 = True
        for cle, valeur in personne2.items():
            if cle == ind1:
                valeur2 = True
        if valeur1 == valeur2:
            return True
        else:
            return False

    def save_as_txt(self, path, liste):
        f = open(path, "w+", encoding="Utf-8")
        for groupe in liste:
            f.write(", ".join(groupe) + "\n")
        f.close()
        print(f"{Fore.GREEN} Fichier Txt enregistré en '{path}' . {Fore.RESET}")

    def output(self):
        p_list = []
        for group in self.list_groups:
            for person in group:
                p_list = group
                idx = p_list.index(person)
                del p_list[idx]
                print(p_list)
                self.write_person_b_name(p_list)
        self.save_excel(self.dF)

    def write_person_b_name(self, groups):

        test_group = []

        for group in groups:
            for nom in group:
                print(nom)
                test_group = group
                idx = group.index(nom)
                del test_group[idx]
                for name in test_group:
                    try:
                        if self.dF.loc[nom, name] == "x":
                            pass
                        else:
                            self.dF.loc[nom, name] = self.dF.loc[nom, name] + 1
                    except:
                        pass
                del test_group
                test_group = []
        
    def get_person_b_name(self, name):
        dico = {}
        idx = self.participants.index(name)
        for personne in range(len(self.participants)):
            equal = self.cote[idx][2]
            dico[personne] = equal
        return dico

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
    
    def sheet_vierge(self):
        # Génération de la matrice de base
        daf = [0]
        daf = int(len(self.participants)) * daf
        daf1 = []
        daf1.append(daf)
        daf1 = daf1 * self.nb_partici
        np = numpy.array(daf1)
        part = self.participants
        self.dF = pd.DataFrame(np, index = self.participants, columns=self.participants)
        df = pd.DataFrame(np, index=self.participants, columns=self.participants)
        for personne in self.participants:
            self.dF.loc[personne, personne]= "x"
        print(self.dF.loc[self.participants[0], self.participants[0]])
        self.save_excel(self.dF)
        #Fin de Génération

if __name__ == "__main__":
    MaBAse = Base(4)
    #MaBAse.write_person_b_name("Thomas Samsoen", ["Kevin Perraud", "Amaury Lethu", "Manon Legros", "Pierre Wergens", "Justine Regniez"])
    #MaBAse.repecher(["Thomas Samsoen"], ["Kevin Perraud", "Amaury Lethu", "Manon Legros", "Thomas Samsoen", "Pierre Wergens", "Justine Regniez"])
