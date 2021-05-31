a = int(input())
b = int(input())

respuesta = ((a!=b) or (a>=b)) and (a%b==1)
respuesta *= 1
print(respuesta)