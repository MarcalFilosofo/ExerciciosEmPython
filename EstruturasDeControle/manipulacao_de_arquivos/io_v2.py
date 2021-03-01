arquivo = open('pessoas.cvs')
for registro in arquivo:
    print("Nome: {} Idade: {}".format(*registro.split(',')))
arquivo.close()