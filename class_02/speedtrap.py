'''
Problema 2 — Controle de Velocidade
Situação: Um radar registrou a velocidade de um veículo em uma via cujo limite é de 70 km/h.
Desenvolva um programa que:
• Leia a velocidade do veículo;
• Verifique se ele ultrapassou 70 km/h;
• Informe se o veículo está dentro do limite ou se o motorista foi multado;
• Calcule a multa considerando R$ 9,00 por km/h excedente;
• Exiba o valor total da multa.
• Calcule o percentual de excesso de velocidade em relação ao limite.
    ((velocidade - limite) / limite) x 100

'''

car_speed = 105
speed_trap = 120
difference = 0
percentual = 0.0

if car_speed > speed_trap:
    message = "you got a ticket"
    difference = car_speed - speed_trap
    percentual = ((car_speed - speed_trap) / speed_trap) * 100
else:
    message = ":) you are driving under the limits"

ticket_value = difference * 9

print(ticket_value, percentual)
