print("Sexto ejercicio:")
print("104 decimal a sistema binario")

x = 104
bit1 = x % 2
cociente1 = x // 2

bit2 = cociente1 % 2
cociente2 = cociente1 // 2

bit3 = cociente2 % 2
cociente3 = cociente2 // 2

bit4 = cociente3 % 2
cociente4 = cociente3 // 2

bit5 = cociente4 % 2
cociente5 = cociente4 // 2

bit6 = cociente5 % 2
cociente6 = cociente5 // 2

bit7 = cociente6 % 2

print("104 =", bit7, bit6, bit5, bit4, bit3, bit2, bit1)
print("")