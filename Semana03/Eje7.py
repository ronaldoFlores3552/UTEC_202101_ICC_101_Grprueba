#Ejercicio 7

a = int(input())
b = int(input())

ba = bin(a)
b1 = bin(a)[-3:]

bb = bin(b)
b2 = bin(b)[-3:]

r = b1 == b2
r *= 1
print(r)
