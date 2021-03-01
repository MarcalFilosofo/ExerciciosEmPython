def todos_params(*args, **kwargs):
    print(f'Ards: {args}')
    print(f'Kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params('1', '2', '3', legal=True, valor=1.22)
