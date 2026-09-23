from fractran import Fraction, Facteur, Fractran


def somme(n, m):
    somme = [Fraction(3, 2)]
    facteurs = Facteur([2, 3, 5])
    v = Fractran(somme).run(facteurs.nombre([n, m]))
    exp_max = 1
    n = v / (3 ** (exp_max))
    while n > 1:
        exp_max = exp_max + 1
        n = v / (3 ** (exp_max))

    return exp_max


def produit(n, m):
    produit = [
        Fraction(455, 33),
        Fraction(11, 13),
        Fraction(1, 11),
        Fraction(3, 7),
        Fraction(11, 2),
        Fraction(1, 3),
    ]
    facteurs = Facteur([2, 3, 5])
    v = Fractran(produit).run(facteurs.nombre([n, m]))
    exp_max = 1
    n = v / (5 ** (exp_max))
    while n > 1:
        exp_max = exp_max + 1
        n = v / (5 ** (exp_max))

    return exp_max
