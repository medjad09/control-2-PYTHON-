def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

annee_utilisateur = int(input("Entrez une année : "))

if est_bissextile(annee_utilisateur):
    print("Oui, l'année", annee_utilisateur, "est bissextile.")
else:
    print("Non, l'année", annee_utilisateur, "n'est pas bissextile.")
