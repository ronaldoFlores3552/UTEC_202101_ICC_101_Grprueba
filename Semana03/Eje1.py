#Ejercicio 1

a = input()
b = input()
a = int(a)
b = int(b)

respuesta = ((a!=b) or (a>=b)) and (a%b==1)
respuesta *= 1
print(respuesta)

