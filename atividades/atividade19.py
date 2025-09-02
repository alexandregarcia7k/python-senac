capital = float(input("Informe o capital Inicial: R$"))
taxa = float(input("Informe a taxa de juros a.m: (%): "))
mesFinal = int(input("Informe a quantidade de meses: "))

taxa = taxa / 100

for mes in range(1, mesFinal + 1):
    montante = capital * (1 + taxa) ** mes
    print(f"Mes {mes}: R${montante:.2f}")