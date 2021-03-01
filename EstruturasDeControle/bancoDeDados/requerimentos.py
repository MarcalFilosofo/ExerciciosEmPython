#! python3
try:
    from mysql import connector
except:
    print('MySql Connector nao instalado')
else:
    print('MySql instalado')