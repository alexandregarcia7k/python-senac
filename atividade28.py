def mostrar_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    print("-" * 15)
    for i in range(1, 11):
        print(f"{numero} x {i:2} = {numero * i:3}")
    print("-" * 15)

def gerar_tabuada():
    while True:
        try:
            numero = int(input("\nDigite um número para ver sua tabuada (1-10): "))
            if numero < 1 or numero > 10:
                print("Por favor, digite um número entre 1 e 10!")
                continue
                
            mostrar_tabuada(numero)
            
            continuar = input("\nDeseja ver outra tabuada? (S/N): ").strip().upper()
            if continuar != 'S':
                print("\nPrograma encerrado. Até mais!")
                break
                
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros.")

if __name__ == "__main__":
    print("\n=== GERADOR DE TABUADA ===")
    gerar_tabuada()