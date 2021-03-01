class Carro():
    def __init__(self, velocidade=50):
        self.velocidade = velocidade
    
    
    def acelerar(self, delta=5, limite=220):
        self.delta = delta
        self.limite = limite
        if self.velocidade + self.delta <= self.limite:
            self.velocidade += self.delta
        elif self.delta + self.velocidade > self.limite:
            self.velocidade = self.limite
        
        return self.velocidade
    
    
    def frear(self, delta=5, minimo=0):
        self.delta = delta
        self.minimo = minimo
        if self.velocidade - self.delta >= self.minimo:
            self.velocidade -= self.delta
        elif self.delta - self.velocidade < self.minimo:
            self.velocidade = self.minimo
        
        return self.velocidade

if __name__ == '__main__':
    c1 = Carro(180)
    
    for _ in range(25):
        print(c1.acelerar(2), end=' ')
    
    print('\n')
    for _ in range(10):
        print(c1.frear(delta=20), end=' ')