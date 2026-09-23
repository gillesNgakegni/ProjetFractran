import numpy

from fractran import Fraction, Facteur, Fractran

from fonctions_utilisées_dans_le_main import somme, produit

# Calcul les sommes i+j de tous les entiers 1<=i,j<=10

les_sommes_des_entiers_i_j = numpy.zeros((10, 10))

for i in range(10):
    for j in range(10):
        les_sommes_des_entiers_i_j[i][j] = somme(i + 1, j + 1)


print("les sommes i+j de tous les entiers 1<=i,j<=10 : ")
print(les_sommes_des_entiers_i_j)

# Calcul les produits i*j de tous les entiers 1<=i,j<=10

les_produits_des_entiers_i_j = numpy.zeros((10, 10))

for i in range(10):
    for j in range(10):
        les_produits_des_entiers_i_j[i][j] = produit(i + 1, j + 1)


print("les produits i*j de tous les entiers 1<=i,j<=10 : ")
print(les_produits_des_entiers_i_j)

# Code de la suite de Fibonacci

print("Fibonacci rend les couples (F(n), F(n+1)) :")
fibonacci = [
    Fraction(23, 95),
    Fraction(57, 23),
    Fraction(17, 39),
    Fraction(130, 17),
    Fraction(11, 14),
    Fraction(35, 11),
    Fraction(19, 13),
    Fraction(1, 19),
    Fraction(35, 2),
    Fraction(13, 7),
    Fraction(7, 1),
]

sortie_brute = Fractran(fibonacci).suite(3, 1000)
sortie = []
for n in sortie_brute:
    if n == Facteur([2, 3]).nombre(Facteur([2, 3]).décomposition(n)):
        sortie.append(Facteur([2, 3]).décomposition(n))

print(sortie)

# Code nombres premiers


print("Les nombres premiers :")
nombres_premiers = [
    Fraction(17, 91),
    Fraction(78, 85),
    Fraction(19, 51),
    Fraction(23, 38),
    Fraction(29, 33),
    Fraction(77, 29),
    Fraction(95, 23),
    Fraction(77, 19),
    Fraction(1, 17),
    Fraction(11, 13),
    Fraction(13, 11),
    Fraction(15, 14),
    Fraction(15, 2),
    Fraction(55, 1),
]

sortie_brute2 = Fractran(nombres_premiers).suite(2, 100000)
sortie2 = []
for n in sortie_brute2:
    if n == Facteur([2]).nombre(Facteur([2]).décomposition(n)) and (
        Facteur([2]).décomposition(n) != [1]
    ):
        sortie2.append(Facteur([2]).décomposition(n))

print(sortie2)
