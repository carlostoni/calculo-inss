from datetime import datetime

def calcular_diferenca(data1, data2):
    data_inicial = datetime.strptime(data1, "%d/%m/%Y")
    data_final = datetime.strptime(data2, "%d/%m/%Y")
    diferenca = abs((data_final - data_inicial).days)
    
    anos = diferenca // 365
    meses = (diferenca % 365) // 30
    dias = (diferenca % 365) % 30
    
    return anos, meses, dias

total_dias = 0
periodos = []

while True:
    data1 = input("Digite a primeira data (DD/MM/YYYY) ou 'sair' para finalizar: ")
    if data1.lower() == 'sair':
        break
    data2 = input("Digite a segunda data (DD/MM/YYYY): ")
    
    anos, meses, dias = calcular_diferenca(data1, data2)
    diferenca_dias = anos * 365 + meses * 30 + dias
    total_dias += diferenca_dias
    periodos.append(f"Período: {anos} anos, {meses} meses, {dias} dias")

# Calcula o total acumulado
total_anos = total_dias // 365
total_meses = (total_dias % 365) // 30
total_dias_restantes = (total_dias % 365) % 30

print("\nResumo dos períodos:")
for periodo in periodos:
    print(periodo)

print(f"\nTotal acumulado: {total_anos} anos, {total_meses} meses, {total_dias_restantes} dias")

