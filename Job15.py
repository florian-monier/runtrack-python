def arrondir_et_trier(liste):
    """
    Arrondit les nombres de la liste et la retourne dans l'ordre croissant.
    """
    liste_arrondie = []

    for nombre in liste:
        nombre_arrondi = int(nombre)
        liste_arrondie.append(nombre_arrondi)

    n = len(liste_arrondie)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste_arrondie[j] > liste_arrondie[j + 1]:
                liste_arrondie[j], liste_arrondie[j + 1] = liste_arrondie[j + 1], liste_arrondie[j]

    return liste_arrondie

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = arrondir_et_trier(ma_liste)
print("Liste arrondie et triée :", resultat)
