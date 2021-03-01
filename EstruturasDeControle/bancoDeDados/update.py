from db import nova_conexao
from mysql.connector import ProgrammingError

sql = 'UPDATE contatos SET nome = "Alterado" WHERE id % 2 = 0'


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except ProgrammingError as e:
        print(f'ERRO: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) alterado(s)')