#Função que simula um jogo de adivinhação (salve como atividade35)
#Objetivo: Criar uma função que gere um número aleatório e permita ao usuário tentar adivinhar.
#Desafio extra: Implementar níveis de dificuldade e contagem de tentativas.
import random 
def mostrar_menu():
    print("\n" + "=" * 30)
    print("Escolha o nível de dificuldade".center(30))
    print("=" * 30)
    print("1. Fácil [1-100] - Tentativas = 20 ")
    print("2. Médio [1-400] - Tentativas = 10 ")
    print("3. Dificíl [1-900] - Tentativas = 5 ")
    print("4. Sair")
    print("=" * 30)

def jogo_adivinhacao(opcao):
    tentativas = 0
    dificuldade = 0
    if opcao == 1:
        numero_secreto = random.randint(1, 100)
        dificuldade = 100
        tentativas = 20
    elif opcao == 2:
        numero_secreto = random.randint(1, 400)
        dificuldade = 400
        tentativas = 10
    elif opcao == 3:
        numero_secreto = random.randint(1,900)
        dificuldade = 900
        tentativas = 5
    else:
            print("Opção inválida para o jogo.")
            return

    while tentativas > 0:
        try:
            print(f"Você tem {tentativas} tentativas.")
            palpite = int(input(f"Digite seu palpite (1-{dificuldade}): "))
            
            if palpite < 1 or palpite > dificuldade:
                print(f"Por favor, digite um número entre 1 e {dificuldade}!")
                tentativas -= 1
                continue
            if palpite == numero_secreto:
                print(f"\nParabéns! Você acertou restando {tentativas} tentativas!")
                break
            elif palpite < numero_secreto:
                print("Tente um número MAIOR!")
            else:
                print("Tente um número MENOR!")

            tentativas -= 1
            
            if tentativas == 0:
                print("Acabou suas tentativas")
                break
                

                
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("\nEscolha uma opção (1-4): "))
            
            if opcao == 4:
                print("\nJogo encerrado. Até logo!")
                break
            elif 1 <= opcao <= 4:
                jogo_adivinhacao(opcao)
            else:
                print("\nOpção inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("\nErro: Digite apenas números de 1 a 4!")
        
if __name__ == "__main__":
    main()