cont = 0
media = 0
mediaDosPositivos = 0

for i in range(6):
    entrada = float(input())
    if entrada > 0:
        cont += 1
        media += entrada

if cont > 0:
    mediaDosPositivos = media / cont
    print(f"{cont} valores positivos")
    print("%.1f" %mediaDosPositivos)
else:
    print(f"0 valores positivos")
    print(0)
