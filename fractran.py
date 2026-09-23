class Fraction:

    def __init__(self, numérateur, dénominateur):

        self.numérateur = numérateur
        self.dénominateur = dénominateur

    def est_entier(self, n):
        return n % self.dénominateur == 0

    def valeur(self, n):
        return self.numérateur * (n // self.dénominateur)

    def __eq__(self, other):
        return (
            self.numérateur == other.numérateur
            and self.dénominateur == other.dénominateur
        )


class Facteur:

    def __init__(self, facteurs):
        self.facteurs = facteurs

    def nombre(self, exposants):
        nombre = 1
        for i in range(min(len(self.facteurs), len(exposants))):
            nombre = nombre * (self.facteurs[i] ** exposants[i])
        return nombre

    def décomposition(self, n):
        décomposition = list()
        for i in range(len(self.facteurs)):
            exp = 0
            while (((self.facteurs[i]) ** (exp + 1)) <= n) and (
                n % ((self.facteurs[i]) ** (exp + 1)) == 0
            ):
                exp = exp + 1
            décomposition.append(exp)
        return décomposition


class Fractran:
    def __init__(self, fractions):
        self.programme = fractions

    def run(self, n):
        i = 0
        while i < len(self.programme):
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                i = 0
            else:
                i += 1
        return n

    def suite(self, n, N):
        L = [n]
        i = 0
        while i < len(self.programme) and len(L) < N:
            if self.programme[i].est_entier(n):
                n = self.programme[i].valeur(n)
                L.append(n)
                i = 0
            else:
                i += 1
        return L
