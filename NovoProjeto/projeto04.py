#leitores = id, nome, telefone
#livros = isbn, titulo, autores, edicao, qtd_exemplar
#emprestimo = data_emprestimo, data_devolucao
#<leitor>
# - id: integer, nome: string, telefone:string
# + cadastrarLeitor(): void atualizarLeitor(): void
# + deleterLeitor(): void  consultarLeitor(): Leitor
#<Emprestimo>
# - dataEmprestimo: Date, dataDevolucao: Date,
# - livro: Livro, leitor: Leitor   
# + registrarEmprestimo(): void, registrarDevolucao(): void
#<Livro>
# - isbn: Integer, titulo: string, autores: string
# - edicao: integer, qtd_exemplate: integer
# + cadastrarLivro(): void, atualizarLivro(): void, deleterLivro(): void
# + consultarLivro(): Livro, verificarDisponibilidade(): Boolean
from dataclasses import dataclass, field
from datetime import date

leitores = {}
livros = {}
emprestimos = []

@dataclass
class Leitor:
  id: int
  nome: str
  telefone: str

@dataclass
class Livro:
  isbn: int
  titulo: str
  autores: str
  edicao: int
  qtd_exemplar: int

@dataclass
class Emprestimo:
  id: int
  leitor_id: int
  isbn: int
  data_emprestimo: date = field(default_factory=date.today)
  data_devolucao = None
  
  
#<leitor>
def cadastrarLeitor(leitor):
  if leitor.id in leitores:
    return (f"Leitor com o id {leitor.id} já existe.")
  leitores[leitor.id] = leitor

def atualizarLeitor(id, nome=None, telefone=None):
  if id not in leitores:
    return (f"Leitor {id} não encontrado.")
  if nome is not None:
    leitores[id].nome = nome
  if telefone is not None:
    leitores[id].telefone = telefone

def deletarLeitor(id):
  if id not in leitores:
    return(f"Leitor {id} não encontrado.") 
  ativos = [e for e in emprestimos if e.leitor_id == id and e.data_devolucao is None]
  if ativos:
    return("Leitor possui emprestimos ativos.")
  del leitores[id]
  
def consultarLeitor(id):
  if id not in leitores:
    return (f"Leitor {id} não encontrado.")
  return leitores[id]

#<Livro>
def cadastrarLivro(livro):
  if livro.isbn in livros:
    return(f"Livro com ISBN {livro.isbn} já existe.")
  livros[livro.isbn] = livro
  
def atualizarLivro(isbn, titulo=None, autores=None, edicao=None, qtd_exemplar=None):
  if isbn not in livros:
    return(f"Livro {isbn} não encontrado")
  l = livros[isbn]
  if titulo is not None:
    l.titulo = titulo
  if autores is not None:
    l.autores = autores
  if edicao is not None:
    l.edicao = edicao
  if qtd_exemplar is not None:
    l.qtd_exemplar = qtd_exemplar
  
def deletarLivro(isbn):
  if isbn not in livros:
    return (f"Livro {isbn} não encontrado.")
  ativos = [e for e in emprestimos if e.isbn == isbn and e.data_devolucao is None]
  if ativos:
    return("Livro possui exemplar(s) emprestado(s).")
  del livros[isbn]

def consultarLivro(isbn):
  if isbn not in livros:
    return (f"Livro {isbn} não encontrado.")
  return livros[isbn]

def verificarDisponibilidade(isbn):
  if isbn not in livros:
    return (f"Livro {id} não encontrado.")
  total = livros[isbn].qtd_exemplar
  emprestados = sum ( 1 for e in emprestimos if e.isbn == isbn and e.data_devolucao is None )
  return emprestados < total
  