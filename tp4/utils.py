

def coordonnees_case(ligne, colonne, nb_pixels_par_case):
    """
    Détermine les coordonnées en pixel d'une case.

    Args:
        ligne (int): L'index de la ligne de la case.
        colonne (int): L'index de la colonne de la case.
        nb_pixels_par_case (int): Nombre de pixels qu'occupe la représentation graphique d'une case.

    Returns:
        (int, int, int, int): Les coodonnées en pixel des quatre coins d'une case.
    """
    debut_ligne = ligne * nb_pixels_par_case
    fin_ligne = debut_ligne + nb_pixels_par_case
    debut_colonne = colonne * nb_pixels_par_case
    fin_colonne = debut_colonne + nb_pixels_par_case
    return debut_ligne, debut_colonne, fin_ligne, fin_colonne


def dessiner_jeton(canvas, jeton, ligne, colonne, nb_pixels_par_case, selection=False, tag='lettre'):
    """
    Dessine une jeton sur l'interface graphique.

    Args:
        canvas (tkinter.Canvas): Un Widget Canvas où dessiner le jeton
        jeton (Jeton): Le jeton à dessiner
        ligne (int): L'index de la ligne de la case où dessiner le jeton.
        colonne (int): L,index de la colonne de la case où dessiner le jeton.
        nb_pixels_par_case (int): Nombre de pixels qu'occupe la représentation graphique d'une case (ou d'un jeton).
        selection (bool): True si le jeton est sélectionné par le joueur (False par défaut).
        tag (str): Étiquette à affubler au dessin du jeton ("lettre" par défaut)
    """
    debut_ligne, debut_colonne, fin_ligne, fin_colonne = coordonnees_case(ligne, colonne, nb_pixels_par_case)
    centre = (debut_colonne + nb_pixels_par_case // 2, debut_ligne + nb_pixels_par_case // 2)

    if selection:
        couleur = 'orange'
    else:
        couleur = '#b9936c'

    canvas.create_rectangle(debut_colonne, debut_ligne, fin_colonne, fin_ligne, fill=couleur, tags=tag)
    canvas.create_text(centre, font=('Times', '31'), text=str(jeton), tags=tag)
