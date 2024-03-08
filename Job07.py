L = [8, 24, 48, 2, 16]

nombre_multiples_de_3 = 0

for nombre in L:
    if nombre % 3 == 0:
        nombre_multiples_de_3 += 1

print("Nombre de multiples de 3 dans la liste L :", nombre_multiples_de_3)
