def get_dia_semana(dia):
    dias = {
        1: 'FDS',
        2: 'SEMANA',
        3: 'SEMANA',
        4: 'SEMANA',
        5: 'SEMANA',
        6: 'SEMANA',
        7: 'FDS',
    }
    return dias.get(dia, '** Invalido **')


if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
    print(f'{get_dia_semana(100)}')