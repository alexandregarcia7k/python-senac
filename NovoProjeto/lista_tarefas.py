class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False
        
    def concluir(self):
        self.concluida = True
        
    def __str__(self):
        if self.concluida == False:
            return f'{self.descricao} - [Pendente]'
        else:
            return f'{self.descricao} - [Concluida]'
    
class ListaTarefas:
    def __init__(self, nome_lista):
        self.nome_lista = nome_lista
        self.tarefas = []
        
    def adicionar_tarefa(self, tarefa : Tarefa):
        self.tarefas.append(tarefa)
        

    def concluir_tarefa(self, descricao):
        for objeto_tarefa in self.tarefas:
            if descricao == objeto_tarefa.descricao:
                objeto_tarefa.concluir()
        
    def listar_tarefas(self):
        for objeto_tarefa in self.tarefas:
            print(objeto_tarefa)
    
    def listar_pendentes(self):
        for objeto_tarefa in self.tarefas:
            if objeto_tarefa.concluida == False:
                print(objeto_tarefa)

    def salvar_em_arquivo(self):
        nome_arquivo = f'{self.nome_lista}.txt'
        with open (nome_arquivo, 'w', encoding='utf-8') as arquivo:
            for objeto_tarefa in self.tarefas:
                arquivo.write(f'{objeto_tarefa}\n')

lista01 = ListaTarefas('Estudos')
lista01.adicionar_tarefa(Tarefa('Estudar Python'))
lista01.adicionar_tarefa(Tarefa('Estudar HTML'))
lista01.concluir_tarefa('Estudar HTML')
lista01.listar_tarefas()
lista01.listar_pendentes()
lista01.salvar_em_arquivo()
 