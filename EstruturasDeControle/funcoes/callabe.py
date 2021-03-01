def exercutar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom dia')
    

def boa_tarde():
    print('Boa tarde')


if __name__ == '__main__':
    exercutar(bom_dia)
    exercutar(boa_tarde)
    exercutar(1)