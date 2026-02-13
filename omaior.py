A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

maior = (A + B + abs(A - B)) / 2  
verdadeiro = (maior + C + abs(maior - C)) / 2
print (f"{verdadeiro:.0f} eh o maior")
