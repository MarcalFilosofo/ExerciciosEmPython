from mysql.connector.errors import ProgrammingError
from db import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Lucas', '98765-4321'),
    ('claudin', '98765-4321'),
    ('peneira', '98765-4321'),
    ('paquera', '98765-4321'),
    ('gui', '98765-4321'),
    ('row', '98765-4321'),
    ('mises', '98765-4321'),
    ('hayek', '888-4321'),

    )

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros')