def NbCMin(mot_de_passe):
    return sum(1 for char in mot_de_passe if char.islower())

mot_de_passe_example = str(input("Entrez le mot de passe :"))
resultat = NbCMin(mot_de_passe_example)
print("Nombre de caractères minuscules :", resultat)
