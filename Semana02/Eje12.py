

# #Ejercicio 12

x12 = 1054

res1 = x12%16
coci = x12//16

res2 = coci%16
coci = coci//16

def letra(res):
    res = str(res) 
    if res == "10":
        return "A"
    elif res == "11":
        return "B"
    elif res == "12":
        return "C"
    elif res == "13":
        return "D"
    elif res == "14":
        return "E"
    elif res == "15":
        return "F"
    else :
        return res
print("El numero {} = {}{}{}".format(x12, letra(coci),letra(res2),letra(res1)))