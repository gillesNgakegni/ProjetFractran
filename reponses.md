# Projet interpréteur-fractran : réponses aux questions

## Question 1 : créez un dossier *interpréteur-fractran* qui sera le projet vscode où vous placerez vos différents fichiers. 

C'est fait.

## Implémentez la classe la classe **Fraction** dans le fichier *fractran.py* et ses tests dans le fichier *test_fractran.py*.

Voir les fichiers *fractran.py* et *test_fractran.py*.


## Question 3 : Implémentez la classe **Facteur** dans le fichier *fractran.py* et ses tests dans le fichier *test_fractran.py*.

Voir les fichiers *fractran.py* et *test_fractran.py*.

## Question 4 : ajoutez le code de la classe dans le fichier *fractran.py* et implémentez des tests de celle-ci dans le fichier *test_fractran.py*.

Voir les fichiers *fractran.py* et *test_fractran.py*.

## Question 5 : créez un fichier *main.py* où vous calculerez les sommes ``i+j`` de tous les entiers `1<=i,j<=10`.

Voir les fichiers *main.py* et *fonctions_utilisées_dans_le_main.py*.



## Question 6 : ajoutez au fichier *main.py* une partie où vous calculerez les produits `i*j` de tous les entiers `1<=i,j<=10`.

Voir les fichiers *main.py* et *fonctions_utilisées_dans_le_main.py*.

## Question 7 : ajoutez au fichier *main.py* une partie où vous calculerez les produits `i*j` de tous les entiers `1<=i,j<=10`.

Voir les fichiers *fractran.py* et *test_fractran.py*.


## Question 8 : ajoutez dans le programme principal le code de la suite de Fibonacci et explicitez comment il fonctionne (je ne veux pas de preuve, juste une explication du code python).

Voir le fichier *main.py*

Explicitation du code ``python`` : ce programme utilise le programme `fractran`  de la suite de Fibonacci à savoir ```fibonacci = [Fraction(23, 95), Fraction(57, 23), Fraction(17, 39), Fraction(130, 17), Fraction(11, 14), 
          Fraction(35, 11), Fraction(19, 13), Fraction(1, 19), Fraction(35, 2), Fraction(13, 7), 
          Fraction(7, 1)]```.

En l'appliquant à l'entier 3 (```sortie_brute = Fractran(fibonacci).suite(3, 1000) ```), on obtient une suite de nombres telle que : *a et b sont des termes consécutifs de la suite de Fibonacci si et seulement si* ```n=(2**a)(3**b)``` *appartient à la suite de nombres générées par notre programme fractran*.

La suite du code python consiste à extraire les exposants *a* et *b* des nombres *n* qui s'écrivent sous la forme ```n=(2**a)(3**b)```.

## Question 9 : ajoutez dans le programme principal le code permettant de rendre tous les nombres premiers trouvés pour 100000 nobres rendu par le programme.

Voir le fichier *main.py*.


