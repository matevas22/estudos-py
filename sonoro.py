# um visinho A quer saber se o som do seu carro é alto ou baixo, para isso ele mede a distância do carro até a sua casa e o tempo que o som demora para chegar até ele, com esses dados ele quer saber a velocidade do som, se for menor que 340 m/s o som é baixo, caso contrário é alto.

distancia = float(input("Digite a distância do carro até a casa do vizinho A (em metros): "))
tempo = float(input("Digite o tempo que o som demora para chegar até o vizinho A (em segundos): "))
velocidade_som = distancia / tempo
if velocidade_som < 340:
    print("O som do carro é baixo.")
else:
    print("O som do carro é alto.")
