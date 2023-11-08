"""
Eric González, Izan Fernandez , Ayman dghoughi
08/11/2023
M03 UF1 A3
Descripció: Exercici 3

"""

velinicial = float(input("Introdueix la velocitat inicial en m/s: "))
acceleracio = float(input("Introdueix l'acceleració en m/s²: "))
temps = float(input("Introdueix el temps: "))
velinst = (velinicial + acceleracio) * temps
print(velinst)
if velinst <= 0:
    print("Esta parat i no puc calcular la mitjana")
else:
    velmitj = (velinicial + velinst)/2
    print("La velocitat mitjana es", velmitj)
