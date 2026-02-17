from datetime import datetime
data_string = datetime.now().strftime('%H:%M:%S')
print(data_string)



n = int(input())
horas = n // 3600
minutos = (n % 3600) // 60
segundos = n % 60 
print(f"{horas}:{minutos}:{segundos}")