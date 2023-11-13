import re

def LongMin(mot_de_passe):
    minuscules = re.findall(r'[a-z]+', mot_de_passe)
    return max((len(seq) for seq in minuscules), default=0)

mot_de_passe_example = str(input("Entrez le mot de passe :"))
resultat = LongMin(mot_de_passe_example)
print("Longueur de la plus longue séquence de lettres minuscules :", resultat)
