from my_libraries import *

from functions import *
from Constants import *


def wrapper_product(a, b):
    return product(a, b)


if __name__ == '__main__':
    FILE = 'titanic3.xls'
    datanic = pd.read_excel(os.path.join(CHEMIN, FILE), index_col=0)
    print(datanic)

    '''Les variables et les fonctions sont en MIN
    Les constantes en MAJ
    Les classes en (Nom)'''

    a, b = 2, 4
    c = product(a, b)
    print (c)


# Myriam test
print('a/n b')









