"""
Eric González, Izan Fernandez , Ayman dghoughi
08/11/2023
M03 UF1 A3
Descripció: Exercici 2

"""
nums = str(input("Introdueix una serie de 3 numeros:")).split()
if nums[1]>nums[0] and nums[1]<nums[2]:
    print("Estan en ordre creixent")
else:
    print("no estan en ordre creixent")