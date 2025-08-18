def mostrar_menu():
    print("\n" + "=" * 30)
    print("CALCULADORA PYTHON".center(30))
    print("=" * 30)
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("=" * 30)

def calcular(opcao):
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == 1:
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"\nResultado: {num1} × {num2} = {resultado}")
        elif opcao == 4:
            if num2 == 0:
                print("\nErro: Divisão por zero!")
            else:
                resultado = num1 / num2
                print(f"\nResultado: {num1} ÷ {num2} = {resultado:.2f}")
    except ValueError:
        print("\nErro: Digite apenas números válidos!")

def main():
    while True:
        mostrar_menu()
        try:
            opcao = int(input("\nEscolha uma opção (1-5): "))
            
            if opcao == 5:
                print("\nCalculadora encerrada. Até logo!")
                break
            elif 1 <= opcao <= 4:
                calcular(opcao)
            else:
                print("\nOpção inválida! Digite um número entre 1 e 5.")
        except ValueError:
            print("\nErro: Digite apenas números de 1 a 5!")

if __name__ == "__main__":
    main()