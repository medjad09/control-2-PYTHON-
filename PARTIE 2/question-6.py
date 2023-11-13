import re

def NbCMin(mot_de_passe):
    return sum(1 for char in mot_de_passe if char.islower())

def NbCMaj(mot_de_passe):
    return sum(1 for char in mot_de_passe if char.isupper())

def NbCAlpha(mot_de_passe):
    return sum(1 for char in mot_de_passe if not char.isalpha())

def LongMaj(mot_de_passe):
    majuscules = re.findall(r'[A-Z]+', mot_de_passe)
    return max((len(seq) for seq in majuscules), default=0)

def LongMin(mot_de_passe):
    minuscules = re.findall(r'[a-z]+', mot_de_passe)
    return max((len(seq) for seq in minuscules), default=0)

def score(mot_de_passe):
    total_caracteres = len(mot_de_passe)
    bonus = total_caracteres * 4 + (total_caracteres - NbCMaj(mot_de_passe)) * 2 + (total_caracteres - NbCMin(mot_de_passe)) * 3 + NbCAlpha(mot_de_passe) * 5
    malus = LongMaj(mot_de_passe) * 2 + LongMin(mot_de_passe) * 2
    score_final = bonus - malus

    if score_final < 20:
        return "très faible"
    elif 20 <= score_final < 40:
        return "faible"
    elif 40 <= score_final < 80:
        return "fort"
    else:
        return "très fort"

mot_de_passe_example = str(input("Entrez le mot de passe :"))
resultat = score(mot_de_passe_example)
print(f"Le mot de passe est considéré {resultat}.")
