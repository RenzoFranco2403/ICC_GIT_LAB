#Programación declarativa
nombres = ["JUAN", "KARLA", "MANUEL", "FIORELLA"]
nombres_minus = [nom.lower() for nom in nombres]
print(nombres_minus)

print()
print("Ejercicio 3")
print("-"*40)
#lee 5 números enteros
# desde teclado y almacénalos en una lista
lista = []
for i in range(5):
    n = int(input("ingrese un numero: "))
    lista.append(n)
print(lista)