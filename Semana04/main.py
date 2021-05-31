print("Bienvenidos a programar en Python")
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
opc = int(input("Ingrese opcion: "))
if opc == 1:
    c = a + b
    print("{} + {} = {}".format(a, b, c))
else:
    c = a - b
    print("{} - {} = {}".format(a, b, c))