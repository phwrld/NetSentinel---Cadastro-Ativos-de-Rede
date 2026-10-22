ativos = [
    'WEB01',
    'DB01',
    'FW01'
]


criti = {
    'WEB01': 'CRITICIDADE GRAVE',
    'DB01': 'CRITICIDADE ALTA',
    'FW01': 'CRITICIDADE BAIXA',
}

cvss = {
     'WEB01' : 8.2,
     'DB01' : 6.4,
     'FW01' : 4.5

}

portas = [22, 80, 443, 23, 3389]

for nome in ativos:
    print(nome, '-', criti[nome], '|', 'NIVEL DE CVSS: -', cvss[nome] )

if cvss[nome] >= 7:
        print('ALERTA DE VULNERABILIDADE!')

print('=' * 40)

for porta in portas:

    if porta == 23 or porta == 3389:
        print('ALERTA! Porta', porta, 'precisa de atenção!')
    else:
        print('Porta', porta, '- Sem alerta')

print('=' * 40)