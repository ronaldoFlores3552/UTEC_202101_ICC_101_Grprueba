# #Ejercicio 9

x9 = 587

res1 = x9 % 8
coci = x9 // 8
res2 = coci % 8
coci = coci //8
res3 = coci % 8
coci = coci //8


print("el numero {} = {}{}{}{} en base 8".format(x9,coci,res3,res2,res1))