dias = int(input())
ano = dias // 365
mes = (dias % 365) // 30 or (dias % 365) // 30 + 1
dia = (dias % 365) % 30 
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
