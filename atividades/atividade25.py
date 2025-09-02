# escreva("Informe N termo de Fibonacci: ")
# leia(numero)
# fa <- 1
# para x de 1 ate numero faca
#      fb <- fa
#      fa <- fn
#      fn <- fa + fb
#      escreval(fn)
# fimpara
n = int(input("Informe N termos de Fibonacci: "))

a, b = 0, 1

print("Sequência de Fibonacci:")
for _ in range(n):
    print(a, end=' → ')
    a, b = b, a + b

print("FIM")