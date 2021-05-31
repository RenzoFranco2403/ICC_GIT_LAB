print("Cuarto ejercicio:")
print("Pasar 99 decimal a sistema hexadecimal")

x = 99

bit1 = x % 16
cociente = x // 16

bit2 = cociente % 16
cociente = cociente // 16

print("{} = {} {}".format(x, bit2, bit1))
print("")