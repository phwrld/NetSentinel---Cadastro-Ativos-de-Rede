print('=' * 50)
print('   SEJA BEM VINDO/A! 👨‍💻')
print('   NETSENTINEL - CADASTRO ATIVOS DE REDES')
print('=' * 50)
#Início de Interface
# ------------------------------------------------------------------------------------------------------------------------------------

#Aqui criamos as váriaveis e atribuímos valores a ela
# ------------------------------------------------------------------------------------------------------------------------------------
nome_host = 'WEB-SRV-01'
endereco_ip = '192.168.1.10'
porta = 443
criticidade = 5
firewall_ativo = True
host_ativo = False 

#Set de informações
# ------------------------------------------------------------------------------------------------------------------------------------
nome_host = input("Digite o nome do Host (Hostname): ")
endereco_ip = input("Digite o Endereço IP do host (ex: 192.168.1.10):")
endereco_mac = input("Digite o Endereço MAC (ex: 00:1B:44:11:3A:B7):")
sistema_operacional = input("Digite o Sistema Operacional (ex: Linux, Windows, Mac...):")

#Set de Gravidade e Criticidade
# ------------------------------------------------------------------------------------------------------------------------------------
porta_critica = int(input('Principal porta aberta: (Ex: 22, 80)'))
nivel_criticidade = int(input('Nível de criticidade: (Ex - 1 BAIXO - 5 CRÍTICO) '))

#Informações de CVSS e PING
# ------------------------------------------------------------------------------------------------------------------------------------
tempo_resposta_ping = float(input(' Digite o Tempo médio do Ping: '))
score_cvss = float(input('Escale o nível de CVSS: (0.0 a 10.0:): ' ))

#Boolean Working
# ------------------------------------------------------------------------------------------------------------------------------------
firewall_ativo_input = input('Firewall ativo? (s/n): ').strip().lower()
firewall_ativo = firewall_ativo_input == 's'   

status_ativo_input = input('O host está acessível no momento?: (s/n)').strip().lower()
status_ativo = status_ativo_input == 's'

#Geração de Relatórios
#------------------------------------------------------------------------------------------------------------------------------------

print('=' * 50)
print('   RELATÓRIO DO HOST CADASTRADO ❗')
print('=' * 50)

print(f'Hostname: {nome_host} (Tipo: {type(nome_host).__name__})')
print(f'Porta Alvo: {porta_critica} (Tipo: {type(porta_critica).__name__})')