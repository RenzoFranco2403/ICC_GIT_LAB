print("Tercer ejercicio:")
print("48 decimal a sistema hexadecimal")
x = 48

bit1 = x % 16
cociente1 = x // 16

bit2 = cociente1 % 16
print("{} = {} {}".format(x, bit2, bit1))
print("")