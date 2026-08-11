'''
Problema 1 — Desempenho de uma Rede de
Supermercados
Situação: Uma rede de supermercados registrou o faturamento diário de uma de suas unidades durante cinco dias úteis,
ver Tabela.
A direção estabeleceu que uma unidade apresenta:
• Bom desempenho: média diária igual ou superior a R$ 22.000;
• Desempenho regular: média entre R$ 19.000 e R$ 21.999,99;
• Desempenho crítico: média inferior a R$ 19.000.
Desenvolva um programa que permita analisar os dados da unidade e apresente:
• quantidade de dias analisados;
• faturamento total;
• faturamento médio diário;
• maior faturamento registrado;
• menor faturamento registrado;
• classificação do desempenho da unidade conforme os critérios da direção.


Dia Faturamento
Segunda R$ 18.500
Terça R$ 21.300
Quarta R$ 17.800
Quinta R$ 24.600
Sexta R$ 27.400

'''

sells = [18500, 21300, 17800, 24600, 27400]

total = sum(sells)
mean = sum(sells) / len(sells)
bigger = max(sells)
smaller = min(sells)

if mean >= 22000:
    performance = "Good performance"
elif mean >= 19000 and mean <= 21999:
    performance = "Normal performance"
else:
    performance = "Critical performance"

print(f"total: {total} - média: {mean} - maior: {bigger} - menor {smaller} \n performance: {performance}")