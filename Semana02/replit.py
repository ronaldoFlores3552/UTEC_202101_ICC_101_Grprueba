
print("Sistema decimal")
print("="*40)
a = '10'
b = '20'

a = int(a)
b = int(b)

c = a + b
print(c)
print()
print("De Binario a decimal")
print("="*40)
num = '0b110'
decimal = int(num, 2)
print("{} en decimal es {}".format(num, decimal))
print()
print("De  Decimal a Binario")
print("="*40)
decimal = 6
enBinario = bin(decimal)
enBinario2 = enBinario[2:]
print("{} en binario es {}".format(decimal, enBinario))
print("{} en binario es {}".format(decimal, enBinario2))
print()
print("De Octal a decimal")
print("="*40)
num = '0o10'
decimal = int(num, 8)
print("{} en decimal es {}".format(num, decimal))
num = '0o22'
decimal = int(num, 8)
print("{} en decimal es {}".format(num, decimal))
print()
print("De Decimal a Octal")
print("="*40)
decimal = 18 
enOctal = oct(decimal)
enOctal2 = enOctal[2:]
print("{} en octal es {}".format(decimal, enOctal))
print("{} en octal es {}".format(decimal, enOctal2))
print()
print("De Hexadecimal a decimal")
print("="*40)
num = '0x12'
decimal = int(num, 16)
print("{} en decimal es {}".format(num, decimal))
print()
print("De Decimal a Hexadecimal")
print("="*40)
decimal = 18
enHexa = hex(decimal)
enHexa2 = enHexa[2:]
print("{} en hexadecimal es {}".format(decimal, enHexa))
print("{} en hexadecimal es {}".format(decimal, enHexa2))
num = '0x12'
print("num:",num)
print("num[2:3]:",num[2:3])
print("num[1:3]:", num[1:3])
print("num[:2]: ",num[:2])
print("num[2:]: ",num[2:])


x = 19 + 20 < 89 + 7
print("'19 + 20 < 89 + 7' es igual a {}".format(x))

x = 4|3 < 3|3
print("'4|3 < 3|3' es igual a {}".format(x))

x = 7&5 == 5|0
print("'7&5 == 5|0' es igual a {}".format(x))