class Carro:
    def __init(self, velocidadeMaxima):
        self.velocidadeMaxima = velocidadeMaxima
        self.velocidadeAtual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidadeMaxima
        nova = self.velocidadeAtual + delta
        self.velocidadeAtual = nova if nova <= maxima else maxima
        return self.velocidadeAtual

    def frear(self, delta=5):
        nova = self.velocidadeAtual - delta
        self.velocidadeAtual = nova if nova >= 0 else 0
        return self.velocidadeAtual



if __name__ == '__main__':
    c1 = Carro(180)
    
    for _ in range(25):
        print(c1.acelerar(25), end=' ')
    
    print('\n')
    for _ in range(10):
        print(c1.frear(delta=20), end=' ')