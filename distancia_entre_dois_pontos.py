x1, y1 = input().split()
x1 = float(x1)
y1 = float(y1)
x2, y2 = input().split()
x2 = float(x2)
y2 = float(y2)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"{distancia:.4f}")



# MAIS facil e melhor para fazer, o "map" é opcional

# x1, y1 = map(float, input().split())
# x2, y2 = map(float, input().split())

# distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# print(f"{distancia:.4f}")