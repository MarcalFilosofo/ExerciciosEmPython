a = "arara"
#print(a[::-1])
tamanhoA = len(a)
ehPalindromo = 1


for i in range(tamanhoA):
    if a[i] == a[-i-1]:
        pass
    else:
        ehPalindromo = 0
    #print(f"{a[i]} {a[-i-1]}")
print(ehPalindromo)
