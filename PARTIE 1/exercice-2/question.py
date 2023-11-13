def remplir_matrice(N, P):
    if N <= 0 or P <= 0 or N > 10 or P > 10:
        print("Veuillez entrer des valeurs valides pour N et P (entre 1 et 10 inclus).")
        return

    matrice = [[0] * P for _ in range(N)]
    valeur = 1

    for i in range(N):
        for j in range(P):
            matrice[i][j] = valeur
            valeur += 1

    print("Matrice normale :")
    for ligne in matrice:
        print(" ".join(map(str, ligne)))

    print("\nMatrice alternativement de gauche à droite puis de droite à gauche :")
    for i in range(N):
        if i % 2 == 0:
            print(" ".join(map(str, matrice[i])))
        else:
            print(" ".join(map(str, matrice[i][::-1])))

N = int(input("Entrez un entier N (entre 1 et 10) : "))
P = int(input("Entrez un entier P (entre 1 et 10) : "))

remplir_matrice(N, P)
