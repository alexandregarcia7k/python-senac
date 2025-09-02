#Objetivo: Criar uma função que receba a idade do usuário e retorne a faixa de frequência cardíaca ideal para atividades físicas (usando a fórmula: 220 - idade).
#Desafio extra: Retornar também a zona de queima de gordura (50% a 70% da frequência máxima) e a zona de cardio (70% a 85%).

def frequencia_cardiaca():
   idade = int(input("Digite sua idade: "))
   FMC = 220 - idade
   queima_gordura_min = FMC * 0.5
   queima_gordura_max = FMC * 0.7
   cardio_min = FMC * 0.7
   cardio_max = FMC * 0.85
   print(f'A sua faixa de frequência cardíaca ideal para atividade físicas é de: [{FMC}]')
   print(f'A sua zona de queima de gordura é de:\n Max: [{queima_gordura_max:.0f}]\n Min: [{queima_gordura_min:.0f}]')
   print(f'A sua zona de cardio é de:\n Max: [{cardio_max:.0f}]\n Min:[{cardio_min:.0f}]')
   
frequencia_cardiaca()