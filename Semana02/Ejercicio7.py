print("Séptimo ejercicio:")
print("Pasar 254 decimal a sistema binario")

x = 254

bit1 = x % 2
cociente = x // 2

bit2 = cociente % 2
cociente = cociente // 2

bit3 = cociente % 2
cociente = cociente // 2

bit4 = cociente % 2
cociente = cociente // 2

bit5 = cociente % 2
cociente = cociente // 2

bit6 = cociente % 2
cociente = cociente // 2

bit7 = cociente % 2
cociente = cociente // 2

bit8 = cociente % 2
cociente = cociente // 2

print("{} = {} {} {} {} {} {} {} {}".format(x, bit8, bit7, bit6, bit5, bit4,
                                            bit3, bit2, bit1))
print("")