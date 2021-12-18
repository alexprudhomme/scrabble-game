class Case:
    """
    Cette classe représente une case sur un tableau de scrabble.

    Attributes:
        multiplicateur (int) : vaut 1 si la case n'est pas spéciale;
                               vaut 2 dans le cas d'une case compte double;
                               vaut 3 dans le cas d'une case compte triple.
        effet (str): vaut 'M' si la case est spéciale et affecte le pointage des mots;
                     vaut 'L' si la case est spéciale et affecte le pointage des lettres;
                     vaut None si la case n'est pas spéciale.
        jeton_occupant (Jeton): Le jeton contenu sur la case (None si aucun jeton).
    """
    def __init__(self, multiplicateur=1, effet=None):
        """
        Constructeur de la classe.
        Notez qu'une case nouvellement créée est vide, c'est-à-dire le jeton occupant est None.

        Args:
            multiplicateur (int, optionnel): Multiplicateur de la case (vaut 1, 2 ou 3).
            effet: (str, optionnel): Effet de la case (vaut None, 'M', ou 'L').

        Raises:
            AssertionError:
                - Si le multiplicateur n'est pas compris entre 1 et 3 (1 et 3 étant inclus).
                - Si l'effet est égal à None ou si l'effet n'est ni 'M' ou 'L'.
        """
        # On valide les pré-conditions
        assert 1 <= multiplicateur <= 3, 'Multiplicateur incorrect.'
        assert effet is None or effet in 'ML', 'Type incorrect.'

        # On initialise les différents attributs
        self.multiplicateur = multiplicateur
        self.effet = effet
        self.jeton_occupant = None

    def est_vide(self):
        """
        Vérifie si une case est vide ou pas (jeton_occupant est None ou pas).

        Returns:
            bool: True si la case est vide, False sinon.
        """
        return self.jeton_occupant is None

    def placer_jeton(self, jeton_a_placer):
        """
        Place un jeton dans la case.

        Args:
            jeton_a_placer (Jeton): Objet à placer dans la case.

        Returns:
           bool: True si le jeton a été placé avec succès;
                 False sinon (si la case est déjà occupée).
        """
        if self.est_vide():
            self.jeton_occupant = jeton_a_placer
            return True
        else:
            return False

    def retirer_jeton(self):
        """
        Retire le jeton de la case.

        Returns:
            Jeton: Le jeton retiré, ou None si la case est vide.
        """
        jeton = self.jeton_occupant
        self.jeton_occupant = None
        return jeton

    def valeur_jeton(self):
        """
        Permet de trouver la valeur du jeton dans la case.

        Returns:
            int: Valeur du jeton occupant, ou None si la case est vide.
        """
        return None if self.est_vide() else self.jeton_occupant.valeur

    def lettre_jeton(self):
        """
        Permet de trouver la lettre inscrite sur le jeton dans la case.

        Returns:
            str: Lettre du jeton occupant, ou None si la case est vide.
        """
        return None if self.est_vide() else self.jeton_occupant.lettre

    def code_couleur(self):
        """
        Méthode permettant de trouver la couleur associée à une case.

        Returns:
            str: Code de couleur de la case.
        """
        if self.effet == 'M' and self.multiplicateur == 2:
            return '#ffaccb'
        elif self.effet == 'M' and self.multiplicateur == 3:
            return '#ff0000'
        elif self.effet == 'L' and self.multiplicateur == 2:
            return '#00c9ff'
        elif self.effet == 'L' and self.multiplicateur == 3:
            return '#0051ff'
        else:
            return '#f5ebdc'

    def texte_case(self):
        """
        Méthode permettant de trouver le libellé associé à une case.

        Returns:
            str: Libellé de la case.
        """
        if self.effet == 'M' and self.multiplicateur == 2:
            return 'Mot\nDouble'
        elif self.effet == 'M' and self.multiplicateur == 3:
            return 'Mot\nTriple'
        elif self.effet == 'L' and self.multiplicateur == 2:
            return 'Lettre\nDouble'
        elif self.effet == 'L' and self.multiplicateur == 3:
            return 'Lettre\nTriple'
        else:
            return ''

    def __str__(self):
        """
        Formatage d'une case.
        Cette méthode est appelée lorsque vous faites str(v) où v est un objet Case.

        Returns:
            str: Chaîne de caractères représentant une case.
        """
        s = '' if self.est_vide() else str(self.jeton_occupant)
        return '\x1b[0;30;{}m{:^4s}\x1b[0m'.format(self.code_couleur(), s)
