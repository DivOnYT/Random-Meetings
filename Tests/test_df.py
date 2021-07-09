import pandas as pd
import random, numpy
liste = ['Thomas Samsoen', 'Kevin Perraud', 'Pierre Wergens', 'Grégoire Berthelon', 'Louise Mercier', 'André Farah', 'Isabelle Hautant', 'Eric De Chambine', 'Etienne De Saint Germain', 'Mickail Voyiatzis', 'Jessica Bismuth', 'Manon Henric', 'Aniis Koodoruth', 'Amaury Lethu', 'Justine Barbi', 'Louis Dubois', 'Manon Legros', 'Lucie Vanderdoodt', 'Etienne Vauquelin', 'Jean-Loup Ezvan', 'Chloé Barbier', 'Pierre Verinaud', 'Adeline Simon', 'Antoine Cruard', 'Louis Laplace', 'Cyril Capello', 'Audrey Malzieu', 'Thomas Bovier', 'Inès Sghaier', 'Chaima Adjif', 'Elise Blanc', 'Noëllie Renaudin', 'Clara Fourquier', 'Bertrand Fouace', 'Emile Kern', 'Donatien Mathias', 'Romain Weigel', 'Marion Henry', 'Arthur de la Taille', 'Luigi Cirillo', 'Christian Kobayashi', 'Salomé Bonnet', 'Ibtissam El Kairouh', 'Hippolyte Favreau', 'Adrien Signolet', 'Célian Chazal', 'Pierre Matoussowsky', 'Jihen Mairech', 'Chloé Bru', 'Bertrand Desmottes', 'Justine Portier', 'Florian Richetta', 'Aldric Dimitri Diximus', 'Pierre-Yves Hachemin', 'Hang Xu', 'Hortense Remy', 'Leo Garcia', 'Nicolas Durantel', 'Alice le Texier', 'Aymeric Nguyen', 'Marine Bernasconi', 'Marie Delville', 'Mattéo Grolleau', 'Quentin Moreschetti', 'Lisa Lamiable', 'Jonas Lefort', 'Clovis Ravion', 'Fabrice Corbiere', 'Julie Rabier', 'Mohamed Ben Rejeb', 'Chloé Philidet', 'Ahmed Lamarti', 'Elie Dumond', 'Jonathan Barcat', 'Gabriel Longou', 'Silvère-Yann Ngouela', 'Marie Chaffard-Lucon', 'Maxime de Maindreville', 'Julian Rodriguez', 'Selima  Drira', 'Bettina Devines', 'Claire Duan', 'Lorraine Lepers', 'Marina Bounechada', 'Oussama Samim', 'Nizar Akiki', 'Louis Perrot', 'Yazid Aberkane', 'Baptiste André', 'Anatole Chevtchik', 'Justine Regniez']
daf = [1]
daf = int(len(liste)) * daf
dataFrame = pd.DataFrame([daf], index=liste,
                   columns=liste)
df = [3]
df = int(len(liste)) * df
data = pd.DataFrame([df], index=liste, columns=liste)
dataf = data + dataFrame
#dat = dataf.loc[].at[]   # Acceder à une donnée
#print(dat)