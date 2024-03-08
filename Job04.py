def ajouter_mangue_a_fruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, "mangue")
    return fruits

resultat = ajouter_mangue_a_fruits()
print("Liste des fruits avec mangue ajoutée :", resultat)
