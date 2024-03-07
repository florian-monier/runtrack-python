def afficher_aliments(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire, fraise, cassis")
        else:
            print("Saison non reconnue pour le type 'fruits'")
    elif type == "légume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "été":
            print("Artichaut, aubergine, navet")
        else:
            print("Saison non reconnue pour le type 'légume'")
    else:
        print("Type non reconnu")

afficher_aliments("fruits", "hiver")
afficher_aliments("fruits", "été")
afficher_aliments("légume", "hiver")
afficher_aliments("légume", "été")
