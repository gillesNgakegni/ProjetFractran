from fonctions_utilisées_dans_le_main import somme, produit


def test_somme():
    assert somme(10, 3) == 13


def test_produit():
    assert produit(1, 2) == 2
