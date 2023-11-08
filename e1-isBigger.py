"""
Eric González, Izan Fernandez , Ayman dghoughi
08/11/2023
M03 UF1 A3
Descripció: Exercici 1

"""

num1 = int(input("Introueix el primer numero:"))
num2 = int(input("Introueix el segon numero:"))
if num1 >= num2:
    num1 , num2 = num2 , num1
    print(num1)
    print(num2)
else:
    print("EL primer nombre no es mes gran ni igual que el segon")
