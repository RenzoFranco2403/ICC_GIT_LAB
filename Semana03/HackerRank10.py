a=str(input())
b=str(input())
c=str(input())

respuesta=(a > b) or (b > c and a > c)
respuesta=respuesta*1
print(respuesta)