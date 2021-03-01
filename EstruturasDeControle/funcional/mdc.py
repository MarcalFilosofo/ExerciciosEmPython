#! python
def mdc(numeros):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)
    
    return calc(min(numeros))


if __name__ == "__main__":
    print(mdc([24, 12, 48, 96]))