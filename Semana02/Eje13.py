

# #Ejercicio 13

x13 = 3054

res1 = x13 % 8
coci = x13 // 8
res2 = coci % 8
coci = coci //8
res3 = coci % 8
coci = coci //8
res4 = coci % 8

print("el numero {} = {}{}{}{} en base 8".format(x13,res4,res3,res2,res1))
