"""
Eric González, Izan Fernandez , Ayman dghoughi
08/11/2023
M03 UF1 A3
Descripció: Exercici 4

"""
imp = float(input("Quin es l'import de la teva factura amb IVA inclòs?: "))
targ_cli = str(input("Tens targeta client si/no? ")).lower()
if targ_cli == "si" and imp >= 100:
    discount = 21 % imp
    price = imp - discount
    print("El preu final amb descompte es:", price)
else:
    print("No tens descompte el preu final és", imp)
