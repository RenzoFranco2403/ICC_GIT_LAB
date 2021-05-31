
print("Programación Imperativa")
print("="*40)
numeros = [1,2,5,10]
suma=0
for i in numeros:
    suma+=(i*2)
print(suma)

print("Programación Declarativa")
print("="*40)
suma = sum([i*2 for i in numeros])
print(suma)

print()
print("Programación Imperativa")
print("="*40)
nums=[]
n=int(input())
m=int(input())
nums.append(n)
nums.append(m)
print("Lista es: ",nums)

print()
print("Programación Declarativa")
print("="*40)
nums = [int(input()),int(input())]
print(nums)



print()
print("Programación Imperativa")
print("="*40)
nums=[]
n=int(input())
m=int(input())
n = n*3
m = m*3
nums.append(n)
nums.append(m)
print("Lista es: ",nums)


print()
print("Programación Declarativa")
print("="*40)
nums = [int(input())*3,int(input())*3]
print(nums)