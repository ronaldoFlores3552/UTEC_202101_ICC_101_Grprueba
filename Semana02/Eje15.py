# #Ejercicio 15

x15 = 15850

res1 = x15%16
coci = x15//16

res2 = coci%16
coci = coci//16

res3 = coci%16
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
print("El numero {} = {}{}{}{}".format(x15,letra(coci) ,letra(res3),letra(res2),letra(res1)))
