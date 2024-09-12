import json

arquivo = 'dados.json'

with open(arquivo, 'r') as file:
    dados = json.load(file)
    dia_valor = {}
    
    for i in dados:
        dia = i['dia']
        valor = i['valor']
        dia_valor[dia] = valor

    menor_valor = min(dia_valor.values())
    maior_valor = max(dia_valor.values())
    faturamento_mensal = sum(dia_valor.values())
    qtd_dias = len(dia_valor)
    media_mensal = faturamento_mensal / qtd_dias
    dias_acima_media = sum(1 for valor in dia_valor.values() if valor > media_mensal)

    print(f"O menor valor de faturamento ocorrido em um dia do mês é: {menor_valor}")
    print(f"O maior valor de faturamento ocorrido em um dia do mês é: {maior_valor}")
    print(f"A quantidade de dias no mês em que o valor foi superior à média mensal é de: {dias_acima_media}")
