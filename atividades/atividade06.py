
valorProduto = float(input("Informe o valor do produto:"))
if (valorProduto <= 100):
    print("Produto sem desconto")
else: 
    ValorcomDesconto = valorProduto - valorProduto * 0.1
    print("Valor com desconto: ", ValorcomDesconto)

1