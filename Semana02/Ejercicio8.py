print("Octavo Ejercicio:")
print("305 decimal a sistema hexadecimal")
x = 305

bit1 = x % 16
cociente1 = x // 16

bit2 = cociente1 % 16
cociente2 = cociente1 // 16

bit3 = cociente2 % 16

print("305 decimal =", bit3, bit2, bit1)
print("")