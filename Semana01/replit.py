x = 14

bit1 = x%2
cociente = x//2

bit2 = cociente%2
cociente = cociente//2

bit3 = cociente%2
bit4 = cociente//2

print("{} = {}{}{}{}".format(x,bit4,bit3,bit2, bit1))