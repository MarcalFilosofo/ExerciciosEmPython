class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano        


    def __str__(self):
        return f'{self.dia} {self.mes} {self.ano}'


d1 = Data(7, 2, 2002)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)

