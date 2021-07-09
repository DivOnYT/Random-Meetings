import pandas as pd
import os
from numpy import string_
import numpy
from numpy.lib.npyio import load, save
from Loader import *
from colorama import Fore, Style, init, deinit

init()
path = os.getcwd()
liste_participants = load_participants(fr'{path}\Liste_Part.xlsx', 'Liste participants')

groups = []

daf = [0]
daf = int(len(liste_participants)) * daf
daf1 = []
daf1.append(daf)
daf1 = daf1 * len(liste_participants)
np = numpy.array(daf1)
part = liste_participants
dF = pd.DataFrame(np, index=liste_participants, columns=liste_participants)
for personne in liste_participants:
    dF.loc[personne, personne]= "x"

def save_excel(data):
        # ------------> Ecrire dans un fichier excel
    writer = pd.ExcelWriter('Project_DF.xlsx')
    data.to_excel(writer)
    writer.save()
    pathor = path + "\Liste_Part.xlsx"
    print(f"{Fore.GREEN} Fichier Excel enregistré en {pathor} . {Fore.RESET}")

def load_group_p_group(path, sheet, len_participants):
    group = []
    groups = []
    dframe = pd.read_excel(path, sheet_name=sheet, usecols="A:F")
    dframes = dframe.head(len_participants)

    nb_columns = len(dframes.columns[0]) - 1
    nb_rows = len(dframes.axes[0])
    test_group = []
    compteur = 0
    for ligne in dframes:
        if compteur != 5 or compteur < 5:
            part = list(dframes[f"Participant {nb_columns-compteur}"])
            test_group.append(part)
            compteur = compteur + 1
        group.append(test_group)

    for y in range(nb_rows):
        globals()[f"group_{y}"] = []

    for x in range(nb_rows):
        for i in range(len(test_group)):
            globals()[f"group_{x}"].append(test_group[i][x])
            #globals()[f"group_{x}"] = groups.append(test_group[i][x])
        groups.append(globals()[f"group_{x}"])   

    return groups

def write_group(path, groups, liste_partcipants):

    test_group = []

    for group in groups:
        for nom in group:
            test_group = group
            idx = test_group.index(nom)
            del test_group[idx]
            for name in test_group:
                try:
                    if dF.loc[nom, name] == "x":
                        pass
                    else:
                        dF.loc[nom, name] = dF.loc[nom, name] + 1
                except:
                    pass
            del test_group
            test_group = []
        
    
def main(sheets):
    path = os.getcwd()
    participants = []
    sheet_list = sheets
    part = load_participants(fr'{path}\Liste_Part.xlsx', 'Liste participants')
    for parti in part.values:
        participants.append(parti)
    for sheet in sheet_list:
        group = load_group_p_group(f"{path}\Liste_Part.xlsx", sheet, len(participants))
        write_group(f"{path}\Project_DF.xlsx", group, participants)
    return dF

def sheet_vierge():
    # Génération de la matrice de base
    daf = [0]
    daf = int(len(liste_participants)) * daf
    daf1 = []
    daf1.append(daf)
    daf1 = daf1 * len(liste_participants)
    np = numpy.array(daf1)
    part = liste_participants
    dF = pd.DataFrame(np, index = liste_participants, columns=liste_participants)
    for personne in liste_participants:
        dF.loc[personne, personne]= "x"
    save_excel(dF)

if __name__ == "__main__":
    main()