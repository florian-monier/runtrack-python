def echange_premiere_derniere(liste):
    """
    Échange les valeurs de la première et de la dernière case d'une liste.
    """
    if len(liste) < 2:
        print("La liste doit contenir au moins deux éléments.")
        return

    liste[0], liste[-1] = liste[-1], liste[0]

ma_liste = [1, 2, 3, 4, 5]
print("Liste avant échange :", ma_liste)
echange_premiere_derniere(ma_liste)
print("Liste après échange :", ma_liste)
