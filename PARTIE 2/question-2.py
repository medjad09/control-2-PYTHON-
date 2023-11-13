def NbCMaj(mot_de_passe):
    return sum(1 for char in mot_de_passe if char.isupper())

mot_de_passe_example = str(input("Entrez le mot de passe :"))
resultat = NbCMaj(mot_de_passe_example)
print("Nombre de caractères majuscules :", resultat)
