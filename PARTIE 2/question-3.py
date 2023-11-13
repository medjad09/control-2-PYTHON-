def NbCAlpha(mot_de_passe):
    return sum(1 for char in mot_de_passe if not char.isalpha())

mot_de_passe_example = str(input("Entrez le mot de passe :"))
resultat = NbCAlpha(mot_de_passe_example)
print("Nombre de caractères non alphabétiques :", resultat)
