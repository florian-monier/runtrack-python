def verifier_pair_impair(nombre):
    try:
        nombre = int(nombre)  
        if nombre < 0:
            print("Le nombre doit être positif.")
        elif nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

verifier_pair_impair(10)
verifier_pair_impair(7)
verifier_pair_impair(15.5)  
verifier_pair_impair(-3)    
verifier_pair_impair("abc")  
