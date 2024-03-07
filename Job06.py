def check_positivity(nombre):
    if nombre > 0:
        print("Positif")
    elif nombre < 0:
        print("Négatif")
    else:
        print("Le nombre est égal à zéro")

check_positivity(5)
check_positivity(-3)
check_positivity(0)
