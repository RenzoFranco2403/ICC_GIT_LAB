print("Treceavo Ejercicio:")
print("3054 decimal a sistema octal")
x = 3054

bit1 = x % 8
cociente1 = x // 8

bit2 = cociente1 % 8
cociente2 = cociente1 // 8

bit3 = cociente2 % 8
cociente3 = cociente2 // 8

bit4 = cociente3 % 8
cociente4 = cociente3 // 8

print("3054 =", bit4, bit3, bit2, bit1)
print("")