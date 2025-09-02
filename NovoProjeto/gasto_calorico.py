#Objetivo: Criar uma função que receba o tipo de atividade física, duração (em minutos) e peso do usuário, e calcule o gasto calórico estimado.
#Desafio extra: Permitir diferentes atividades (ex: caminhada, corrida, ciclismo) com fatores de multiplicação diferentes e retornar uma tabela com os resultados.


def gasto_calorico():
    print("\n" + "=" * 30)
    try:
        peso = float(input('Informe o seu peso em Kg: '))
        duracao = float(input('Informe a duração da atividade em MINUTOS: '))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        return

    atividades_mets = {
        'Dormindo': 0.9,
        'Caminhada': 8.3,
        'Bicicleta': 6.0,
        'Pular Corda': 12.3,
        'Musculação': 6.0
    }

    print("\n" + "Escolha as Atividades".center(30))
    print("=" * 30)


    atividades_selecionadas = {}
    for atividade, mets in atividades_mets.items():
        escolha = input(f'Deseja incluir {atividade}? (S/N) ').lower()
        if escolha == 's':
            atividades_selecionadas[atividade] = mets


    resultados = []
    for atividade, mets in atividades_selecionadas.items():
        gasto = (mets * 3.5 * peso) / 200 * duracao
        resultados.append((atividade, gasto))

    print("\n" + "Tabela de Gasto Calórico".center(30))
    print("=" * 30)
    print(f'{"Atividade":<15} | {"Calorias Gastas":>15}')
    print("-" * 32)
    for atividade, calorias in resultados:
        print(f'{atividade:<15} | {calorias:>14.2f}')
    print("=" * 32)


gasto_calorico()
