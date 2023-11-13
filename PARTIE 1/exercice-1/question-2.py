def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

def annees_bissextiles(siecle):
    annees = [annee for annee in range((siecle - 1) * 100 + 1, siecle * 100) if est_bissextile(annee)]
    return annees

siecle = int(input("Entrez le numéro du siècle : "))

resultat = annees_bissextiles(siecle)
print(f"Les années bissextiles du siècle {siecle} sont : {resultat}")
