xUm = int(input(""))
Yum = int(input(""))
xDois = int(input(""))
yDois = int(input(""))

meteoritos = int(input(""))

cordsMeteoritos = []
for i in range(0, meteoritos):
    auxCordX = int(input(""))
    auxCordy = int(input(""))
    cordsMeteoritos.append([auxCordX, auxCordy])

for i in range(len(cordsMeteoritos)):
    for j in range(0, 1):
        print(cordsMeteoritos[i][j])
    print("\n")
