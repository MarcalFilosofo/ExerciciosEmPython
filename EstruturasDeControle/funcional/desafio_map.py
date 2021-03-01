lista_um = [
    {'nome': 'Joao', 'idade': 31},
    {'nome': 'Carlos', 'idade': 24},
    {'nome': 'Daniel', 'idade': 55}
]

so_nomes = map(lambda n: f"{n['nome']} tem  {n['idade']}", lista_um)
print(list(so_nomes))