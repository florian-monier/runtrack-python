def my_long_word(n, phrase):
    """
    Retourne les mots plus longs que n dans la phrase donnée.
    """
    mots = phrase.split()  
    mots_plus_longs = []

    for mot in mots:
        mot_sans_ponctuation = mot.strip(",.!?;:'\"")

        if len(mot_sans_ponctuation) > n:
            mots_plus_longs.append(mot_sans_ponctuation)

    return " ".join(mots_plus_longs)  

phrase_exemple = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
resultat = my_long_word(3, phrase_exemple)
print("Output :", resultat)
