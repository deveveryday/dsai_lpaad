'''
Problema 3 — Monitoramento de Produção Industrial
Situação: Uma indústria possui uma linha com capacidade planejada de 500 unidades por turno. Nos
últimos seis turnos, foram registradas as seguintes produções: 485, 510, 472, 498, 455 e 520 unidades.
A equipe utiliza a produção média para avaliar o desempenho geral do período, ver Tabela.
Além da classificação geral, existe uma regra de segurança operacional: Se pelo menos um turno
apresentar produção inferior a 460 unidades, deverá ser emitido um alerta operacional,
independentemente da classificação obtida pela média.
Desenvolva um programa que apresente:
• armazene as produções em uma lista;
• determine a quantidade de turnos analisados;
• calcule a produção total do período;
• calcule a produção média por turno;
• identifique a maior e a menor produção registrada;
• classifique o desempenho geral do período;
• verifique se deve ser emitido um alerta operacional.
'''

units = [485, 510, 472, 498, 455, 520]
low_production = 460
alert = ""

if  units[0] < low_production or units[1] < low_production or units[2] < low_production or units[3] < low_production or units[4] < low_production or units[5] < low_production:
    alert = "Operational Alert"
else:
    alert = ""

number_of_shifts = len(units)
total = sum(units)
mean = sum(units) / len(units)
low = min(units)
high = max(units)

if total >= 500:
    classification = "goal reached"
elif total > 480 and total >= 499.99:
    classification = "attention"
elif total < 480:
    classification = "lower than the goal"


print("total", total)
print("mean", mean)
print("low", low)
print("high", high)
print(alert)
print(classification)