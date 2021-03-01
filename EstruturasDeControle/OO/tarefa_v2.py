#! python
from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))
    
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes))'




class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
    
    def concluir(self):
        self.feito = True
    
    def __str__(self):
        return self.descricao + ('{Concluido}' if self.feito else '')


def main():
    casa = Projeto('Casa')
    casa.add('Passar roupa')
    casa.add(Tarefa('Passar roupa'))
    casa.add(Tarefa('Lavar prato'))
    casa.add(Tarefa('Lavar Roupa'))
    print(casa)
    
    casa.procurar('Lavar prato').concluir()
    #[tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')

main()