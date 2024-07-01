import learn
import matplotlib.pyplot as plt
import pandas as pd

from functions import *
from my_libraries import *
from Constants import *
from functions import *

if __name__ == '__main__':
    testing =[1, 2, 3, 4]

DESTINATION_FOLDER = os.path.join(BASE, FOLDER)
# pd.read_csv(f"{data_files}{csv_name}")
titanic = 'mytitanic.xlsx'
# ci-dessous = mettre le chemin en dur (Marco )
data = pd.read_excel(os.path.join(DESTINATION_FOLDER, titanic), index_col=0)
print(data)

#Focus Survivants
not_survived = data[data['Survived'] == 1]
print(not_survived)

class_not_surviveb = not_survived.groupby("Pclass").count().rename(columns = {"Survived": "Count"}).reset_index()
print(class_not_surviveb)

class_not_surviveb = class_not_surviveb[["Pclass","Count"]]
print(class_not_surviveb)

x = class_not_surviveb["Pclass"]
y = class_not_surviveb["Count"]
plt.plot(x, y, color = "blue", linewidth = "4")
plt.title("Titanic suvivors")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.hist(y, range = (0, 5), bins = 5, color = 'yellow', edgecolor = 'red')
plt.grid("true")
#plt.show()

#plt.bar(x, y)
#plt.show()

# coucou Myriam je vois ton code! Mathys fait caca dans ton jardin

#list_var_class = ['Pclass'].
#print(list_var_class.sort())

#list_var_class = ['Fare'].unique()
#print(list_var_class.sort())
#back to Python training"
#prix_classe_sex = [('Pclass' == 1) & ('Sex' == 'Female')].groupby["Survived",'Fare'.mean().rename(columns={'Fare':'Ticket_moyen'})]
#print(prix_classe_sex) ??????
#df.groupby(['Name'])[('Revenue', 'Margin', 'Quanity')].agg(['sum'])


Bonjour = "Bonjour, je m'appelle Myriam"
#print('Bonjour')

#Comment enchainer la requête aprèe avoir saisi la valeur ?#
nombre = input("Entrer un chiffre : ")
print(nombre)
print((type(nombre)))
#Comment corriger l'erreur ci-dessous ?????"

a = input("Saisir chiffre 1 : ")
b = input("Saisir chiffre 2 : ")
c = int(a)+int(b)
print(c)






