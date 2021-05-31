#Programación declarativa
lista = [int(input()) for i in range(5)]
print(lista)


print()
print("Ejercicio 4")
print("-"*40)
numeros = [1,2,3,4,5]
pares = []
for i in numeros:
    if i%2 == 0:
        pares.append(i)
print(pares)