import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite seu palpite (1-100): "))
            tentativas += 1
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100!")
                continue
                
            if palpite == numero_secreto:
                print(f"\nParabéns! Você acertou em {tentativas} tentativas!")
                break
            elif palpite < numero_secreto:
                print("Tente um número MAIOR!")
            else:
                print("Tente um número MENOR!")
                
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

if __name__ == "__main__":
    jogo_adivinhacao()