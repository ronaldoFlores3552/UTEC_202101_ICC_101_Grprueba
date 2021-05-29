# #Ejercicio 8
x8 = 305

res1 = x8 % 16
coci = x8 // 16
res2 = coci % 16
coci = coci //16

print("el numero {} = {}{}{} en base 16".format(x8,coci,res2,res1))