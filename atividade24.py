# escreva("Digite um numero inteiro positivo: ")
# leia(numero)
# enquanto numero >= 0 faca
#    contador <- 0
#    para divisor de 1 ate numero faca
#        se (numero mod divisor = 0) entao
#            contador <- contador + 1
#         fimse
#    fimpara
#    se (contador = 2) entao
#       escreval("Numero primo")
#    senao
#         escreval("Numero não é primo")
#    fimse
#    escreva("Digite um numero inteiro positivo: ")
#    leia(numero)
# fimenquanto
def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        numero = int(input("Digite um número inteiro positivo (ou negativo para sair): "))
        
        if numero < 0:
            print("Programa encerrado.")
            break
            
        if is_prime(numero):
            print(f"{numero} é um número primo!")
        else:
            print(f"{numero} não é primo.")
            
    except ValueError:
        print("Por favor, digite um número inteiro válido.")