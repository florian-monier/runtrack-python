def tri_croissant(liste):
    """
    Trie la liste passée en paramètre dans l'ordre croissant.
    """
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

ma_liste = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
tri_croissant(ma_liste)
print("Liste triée dans l'ordre croissant :", ma_liste)
