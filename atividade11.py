salario = float(input('Salário? R$'))
if salario <= 1900:
    print("Isento")
elif salario <= 2800:
    imposto = salario * 0.075
    print(f'O imposto é: R${imposto}')
elif salario <= 3700:
    imposto = salario * 0.15
    print(f'O imposto é: R${imposto}')
else:
    imposto = salario * 0.225
    print(f'O imposto é: R${imposto}')