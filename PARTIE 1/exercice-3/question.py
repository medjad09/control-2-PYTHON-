def somme_max_sous_tableau(tableau):
    if not tableau:
        return 0

    max_somme_globale = max_somme_locale = tableau[0]

    for nombre in tableau[1:]:
        max_somme_locale = max(nombre, max_somme_locale + nombre)
        max_somme_globale = max(max_somme_globale, max_somme_locale)

    return max_somme_globale

tableau_str = input("Entrez les éléments du tableau séparés par des espaces : ")
tableau_example = [int(nombre) for nombre in tableau_str.split()]

resultat = somme_max_sous_tableau(tableau_example)
print("La somme maximale d'un sous-tableau continu est :", resultat)
