from random import randint


def sortearNumero ():
    return randint(1, 6)


if __name__ == '__main__':
    for i in range(1, 7):
        numeroEscolhido = sortearNumero()
        if i % 2 == 1 :
            continue
        
        if sortearNumero() == i:
            print("Acertou!", i)
            break
    else:
        print('Nao acertou o numero')
    
