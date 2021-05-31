print("Primer ejercicio:")
print("Pasar 13 decimal a sistema octal")
x = 13

bit1 = x % 8
cociente = x // 8

bit2 = cociente % 8
cociente = cociente // 8
print("{} = {} {}".format(x, bit2, bit1))

print("")