# 1. Funções
def converte_cpf(cpf):
    return [int(item) for item in cpf]

def verificar_elementos():
    

# 2. Entrada de dados
cpf = list(input('Digite seu CPF: '))

# 3. Processamento
cpf_convertido = converte_cpf(cpf)

if len(cpf_convertido) != 11:
    print('O CPF deve ter exatamente 11 dígitos.')
elif 