a=int(input())
b=int(input())

respuesta= not(a==b or a<=b) and ((a%b)!=2)
respuesta=respuesta*1
print(respuesta)