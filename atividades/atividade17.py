primeiro = float(input("O primeiro valor: "))
ultimo = float(input("O ultimo valor: "))
incremento = float(input("O incremento: "))
if (primeiro <= ultimo):
    while primeiro <= ultimo:
        print(primeiro)
        primeiro = primeiro + incremento
    else:
        while primeiro >= ultimo:
                print(primeiro)
                primeiro = primeiro - incremento
print("Acabou!")
