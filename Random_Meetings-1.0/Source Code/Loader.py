import pandas as pd

def load_participants(path, sheet_name):
    file = pd.read_excel(path, sheet_name=sheet_name, usecols=list(range(11)))
    return file['Nom'][1:103]

def load_groups(path, sheet_names, size):
    groups = []
    for sheet_name in sheet_names:
        file = pd.read_excel(path, sheet_name=sheet_name, usecols="A:F")
        fil = file.head(size)
        nb_columns = len(fil.columns[0]) - 1
        nb_rows = len(fil.axes[0])
        #globals()["test"] = [] #Je fais des test
        #test.append("test")
        #print(test)
        test_group = []
        compteur = 0
        for column in fil:
            if compteur != 5 or compteur < 5:
                part = list(file[f"Participant {nb_columns-compteur}"])
                test_group.append(part)
                compteur = compteur + 1
        for y in range(nb_rows):
            globals()[f"group_{y}"] = []

        for x in range(nb_rows):
            for i in range(len(test_group)):
                
                globals()[f"group_{x}"].append(test_group[i][x])
                #globals()[f"group_{x}"] = groups.append(test_group[i][x])
            groups.append(globals()[f"group_{x}"])
    return groups

def get_rows_len(path, sheet_name):
    file = pd.read_excel(path, sheet_name=sheet_name, usecols="A:F")
    fil = file.head(size)
    return len(fil.axes[0])

def get_column_len(path, sheet_name):
    file = pd.read_excel(path, sheet_name=sheet_name, usecols="A:F")
    fil = file.head(size)
    return len(fil.axes[0])

def get_size(path, sheet_name):
    return len(load_participants(path, sheet_name))

def find(to_find, liste):
    try:
        ind = int(liste.index(to_find))
        return ind
    except:
        return "ERREUR"
    
def load_data(path, size):
    file = pd.read_excel(path, sheet_name="Sheet1")
    fil = file.head(size)
    return fil

