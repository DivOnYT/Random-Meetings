import pandas as pd

def load_participants(path, sheet_name):
    file = pd.read_excel(path, sheet_name=sheet_name, usecols=list(range(11)))
    print(file['Adresse de messagerie'][1:10])
    file['column_i'].head(n) == file['column_i'][0:n]

load_participants(r'C:/Users/come.dherouville/Programmation/Projet-1/Liste_Part.xlsx', 'Liste participants')

