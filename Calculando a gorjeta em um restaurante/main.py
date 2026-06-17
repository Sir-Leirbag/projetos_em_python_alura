conta = float(input('Digite o valor total da conta: '))
porcentagem = float(input('Digite a porcentagem de gorjeta: '))

def calcular_gorjeta (porcentagem, conta):
    valor_da_gorjeta = conta * (porcentagem / 100)
    return valor_da_gorjeta

def calcular_total (conta, porcentagem):
    total = conta + calcular_gorjeta(porcentagem, conta)
    return total

print(f'Valor da gorjeta: R$ {calcular_gorjeta(porcentagem, conta)}')
print(f'Total a pagar: R$ {calcular_total(conta, porcentagem)}')
