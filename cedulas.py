"""Leia um valor inteiro.
A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
A seguir mostre o valor lido e a relação de notas necessárias."""

notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
print(valor)
for nota in notas:
    quantidade = valor // nota
    valor %= nota
    print(f"{quantidade} nota(s) de R$ {nota},00")