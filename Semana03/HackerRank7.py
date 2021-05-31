a = int(input())
b = int(input())

binario1 = bin(a)
binario11 = binario1[3:]

binario2 = bin(b)
binario21 = binario2[3:]

resultado = binario11 == binario21
resultado *= 1
print(resultado)