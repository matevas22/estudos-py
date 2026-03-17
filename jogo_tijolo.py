"""A entrada começa com um número inteiro T (T ≤ 100), representando o número de casos de teste. Cada uma das próximas T linhas irá começar com um número inteiro N (1 < N < 11), número de membros da equipe, seguido por N inteiros separados por espaço representando as idades de todos os membros de uma equipe. Cada um destes N inteiros será entre 11 e 20(inclusive). Nota-se que, as idades serão dadas estritamente em ordem crescente ou estritamente em ordem decrescente. Nós não vamos mencionar qual está aumentando e qual está diminuindo, 
você tem que ser cuidadoso o suficiente para lidar com ambas as situações."""
T = int(input())
for case in range(1, T + 1):
    input_data = input().split()
    N = int(input_data[0])
    meio = N // 2
    ages = list(map(int, input_data[1:]))

    if ages == sorted(ages):
        print(f"Case {case}: INCREASING")
    else:
        print(f"Case {case}: DECREASING")
    
    

