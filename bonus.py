def est_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def type_triangle(a, b, c):
    if a == b == c:
        return "Equilatéral"
    elif a == b or b == c or c == a:
        return "Isocèle"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return "Rectangle"
    else:
        return "Quelconque"

a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

if est_triangle(a, b, c):
    print("Les longueurs peuvent former un triangle.")
    type_tri = type_triangle(a, b, c)
    print(f"Le triangle est de type {type_tri}.")
else:
    print("Les longueurs ne peuvent pas former un triangle.")
