class Jeton:
    """
    Cette classe représente un jeton.

    Attributes:
        lettre (str): La lettre écrite sur le jeton. Par convention toutes les lettres au scrabble sont en majuscules.
                      Dans ce travail nous ne considérons pas les jetons blancs (jokers) qui n'ont aucune lettre inscrite.
        valeur (int): Nombre de points associé au jeton (compris entre 0 et 20).
    """
    def __init__(self, lettre, valeur):
        """
        Constructeur de la classe.
        Permet de créer un Jeton à partir d'une lettre et d'un nombre de points

        Args:
            lettre (str): La lettre écrite sur le jeton (un caractère minuscule).
            valeur (int): Nombre de points associé au jeton (entier positif).

        Raises:
            AssertionError:
                - Si la valeur n'est pas comprise entre 0 et 20 (0 et 20 étant inclus).
                - Si la lettre n'est pas en majuscule.
        """
        # On valide les pré-conditions
        assert len(lettre) == 1 and lettre.isupper() and lettre.isalpha(), 'Lettre incorrecte.'
        assert 0 <= valeur <= 20, 'Valeur incorrecte.'

        # On initialise les différents attributs
        self.lettre = lettre
        self.valeur = valeur

    def __str__(self):
        """
        Formatage d'un jeton.
        Cette méthode est appelée lorsque vous faites str(v) où v est un objet Jeton.

        Returns:
            str: Chaîne de caractères représentant un jeton.
        """
        if self.valeur < 10:
            return '{}{}'.format(self.lettre, chr(0x2080 + self.valeur))
        else:
            return '{}{}{}'.format(self.lettre, chr(0x2080 + int(self.valeur / 10)), chr(0x2080 + int(self.valeur % 10)))
