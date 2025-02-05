from datetime import datetime

def calcular_diferenca_datas(lista_datas):
    total_dias = 0
    for i in range(len(lista_datas) - 1):
        data_inicial = datetime.strptime(lista_datas[i], "%d/%m/%Y")
        data_final = datetime.strptime(lista_datas[i + 1], "%d/%m/%Y")
        total_dias += abs((data_final - data_inicial).days)
    
    # Converte total de dias para anos, meses e dias
    anos = total_dias // 365
    meses = (total_dias % 365) // 30  # Aproximação de meses
    dias = (total_dias % 365) % 30  # Dias restantes
    
    return f"{anos} anos, {meses} meses, {dias} dias"

# Pergunta ao usuário as datas
lista_de_datas = []
while True:
    entrada = input("Digite uma data no formato DD/MM/YYYY (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    lista_de_datas.append(entrada)

if len(lista_de_datas) < 2:
    print("É necessário inserir pelo menos duas datas para calcular a diferença.")
else:
    resultado = calcular_diferenca_datas(lista_de_datas)
    print("Diferença total:", resultado)
