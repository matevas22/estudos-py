numeros_com_virgula_arrays = input("Digite números separados por vírgula: ")
numeros = numeros_com_virgula_arrays.join(",")
numeros_inteiro = []
numeros_invalidos = []

for n in numeros:
    try:
        numeros_inteiro.append(int(n.strip()))
    except ValueError:
        numeros_invalidos.append(n.strip())

if numeros_invalidos:
    print(f"Erro: Digite só numeros, aqui não tem só numeros: {','.join(numeros_com_virgula_arrays)}")

else:
    separar_numeros_par = [n for n in numeros_inteiro if n % 2 == 0]
    print(f"Numeros Válidos", numeros_inteiro)
    print("Numeros pares", separar_numeros_par)