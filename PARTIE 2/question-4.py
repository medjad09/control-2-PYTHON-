import re

def LongMaj(mot_de_passe):
    majuscules = re.findall(r'[A-Z]+', mot_de_passe)
    return max((len(seq) for seq in majuscules), default=0)

mot_de_passe_example = str(input("Entrez le mot de passe :"))
resultat = LongMaj(mot_de_passe_example)
print("Longueur de la plus longue séquence de lettres majuscules :", resultat)
