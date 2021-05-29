#Ejercicio 1
print(3 or 2)
"""
2 = 0 1 0
    or
3 = 0 1 1 
----------
    0 1 1
"""
#Ejercicio 2
print(3 and 2)
"""
2 = 0 1 0
    or
3 = 0 1 1 
----------
    0 1 1
"""
#Ejercicio 3
print(14 >>1)
"""
pasos 
1100
0111
0011
0001 = 3
"""
#Ejercicio 4
print(12 >>1)
"""
pasos 
1100
0110 = 6
"""
#Ejercicio 5 
print(23 << 3)
"""
1011
10110
101100
1011000 = 184
"""
#Ejercicio 6
print(6 | 8)
"""
6 = 0 1 1 0
    or
8 = 1 0 0 0 
-----------
14= 1 1 1 0
"""
#Ejercicio 7
print(19 | 17)
"""
19 = 1 0 0 1 1 
    or
17 = 1 0 0 0 1
--------------
19 = 1 0 0 1 1
"""
# Ejercicio 8 
print(6 & 21)
"""
6 = 0 0 1 1 0
    and
21= 1 0 1 0 1
--------------
4 = 0 0 1 0 0
"""
# Ejercicio 9
print(12 & 7)
"""
12 = 1 1 0 0 
    and
7  = 0 1 1 1
--------------
4 = 0 0 1 0 0
""" 

#operadores relacionales

#Ejemplo 1
print(19+20 < 89 +7)
"""
39 < 96 
True
"""
#Ejemplo 2
print(4|3 < 3|3)
"""
4 = 100  |  3 = 011
    or   |      or
3 = 011  |  3 = 011
-------- |  --------
7 = 111  |  3 = 011
7 < 3
False
"""

#Ejemplo 3

print(7&5 == 5|0)
"""
7 = 111  |  5 = 101
    or   |      or
5 = 101  |  0 = 000
-------- |  --------
5 = 101  |  5 = 101
5 == 5
True
"""