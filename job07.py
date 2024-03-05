chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur_chaine = len(chaine)
niveau_max = 10

for niveau in range(1, niveau_max + 1):
    nb_caracteres = 2 * niveau - 1
    caracteres_affiches = min(nb_caracteres, longueur_chaine)
    
    print(chaine[:caracteres_affiches].center(longueur_chaine))
    
    chaine = chaine[caracteres_affiches:]
    longueur_chaine -= caracteres_affiches
