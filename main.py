import learn
import matplotlib.pyplot as plt

from functions import *
from my_libraries import *
from Constants import *

if __name__ == '__main__':

    test = [1, 2, 3, 4, 5]

print('ciao')

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

plt.bar(x, y)
plt.show()

print('NOW YOU CAN PULL!')
print('NOW YOU CAN PULL!')
print('NOW YOU CAN PULL!')
print('NOW YOU CAN PULL!')


















