
"""
Ce script utilise une fonction décrivant un certain "chaos contrôlé". En modifiant certaines variables de cette
fonction, on peut obtenir différents niveaux de chaos. Voici un aperçu des variables à déterminer:

x : entre 0 et 1
r : plus haut = plus chaotique

Valeurs clé de r (à tester):
    # r = 2
    # r = 3
    # r = 3.5
    # r = 3.6 ==> Le chaos commence
    # r = 4

"""
# Importation du module nécessaire
import matplotlib.pyplot as plt

def fonction_chaotique(x=float(input('Entrez le pourcentage à évaluer (Entre 0 et 1): ')), r=float(input('Entrez le niveau de chaos désiré (valeurs clé suggérées: 2, 3, 3.5, 3.6, 4): '))):
    i=0
    while i < 1000:
        result = r*x*(1-x)
        x = result
        i += 1
        print(result)

        plt.scatter(i, result, color='r')
        plt.xlabel('Time (s)')
        plt.ylabel('Population')
        plt.title("Fonction chaotique de l'évolution d'une population")
        plt.pause(0.05)
        plt.grid()
    plt.show()

fonction_chaotique()

