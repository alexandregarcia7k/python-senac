def calcular_media():
    print("\n=== CALCULADORA DE MÉDIA ===")
    print("(Digite valores entre 0 e 10)\n")
    
    notas = []
    while len(notas) < 4:
        try:
            nota = float(input(f"Digite a {len(notas)+1}ª nota: "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Erro: Nota deve ser entre 0 e 10!")
        except ValueError:
            print("Erro: Digite apenas números!")

    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 6 else "Reprovado"

    print("\n" + "=" * 30)
    print(f"NOTAS: {notas}")
    print(f"MÉDIA: {media:.1f}")
    print(f"STATUS: {status}")
    print("=" * 30)

if __name__ == "__main__":
    while True:
        calcular_media()
        continuar = input("\nCalcular outra média? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nPrograma encerrado.")
            break