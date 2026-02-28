notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
valor = float(input())

valor_centavos = int(valor * 100 + 0.5)


print("NOTAS:")
for nota in notas:
    nota_centavos = int(nota * 100)
    quantidade = valor_centavos // nota_centavos
    valor_centavos %= nota_centavos
    print(f"{quantidade:.0f} nota(s) de R$ {nota:.2f}")
print("MOEDAS:")
for moeda in moedas:
    moeda_centavos = int(moeda * 100)
    quantidades = valor_centavos // moeda_centavos
    valor_centavos %= moeda_centavos
    print(f'{quantidades:.0f} moeda(s) de R$ {moeda:.2f}')

nota_centavos = int(nota * 100)
quantidade = valor_centavos // nota_centavos   

