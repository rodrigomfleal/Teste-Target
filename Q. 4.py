faturamento = { 
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.48,
    "ES" : 27165.48,
    "OUTROS" : 19849.53}

faturamento_total = sum(faturamento.values())

participacao = {estado: (faturamento / faturamento_total) * 100 for estado, faturamento in faturamento.items()}

for estado, participacao in participacao.items():
    print(f"A particição de {estado} é: {participacao:.2f}%")
