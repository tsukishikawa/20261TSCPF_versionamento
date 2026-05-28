# =============================================================
# FIAP - Data Science | Data Driven Application & Data Science
# Professora: Patrícia Angelini
# Avaliação: 2026 1ª Global Solutions
# Integrantes (ordem alfabética):
#   - Lucas (Representante)
#   - Luana
#   - Mariana
# Projeto: PAYNE — Sistema de Monitoramento de Tempestades Solares
# =============================================================

# -------------------------------------------------------
# CORES ANSI
# -------------------------------------------------------
RESET    = "\033[0m"
NEGRITO  = "\033[1m"
VERDE    = "\033[92m"
AMARELO  = "\033[93m"
AZUL     = "\033[94m"
CIANO    = "\033[96m"
VERMELHO = "\033[91m"
BRANCO   = "\033[97m"
MAGENTA  = "\033[95m"

# -------------------------------------------------------
# BANNER DE ABERTURA
# -------------------------------------------------------
print(f"""
{AMARELO}{NEGRITO}
 ██████╗  █████╗ ██╗   ██╗███╗   ██╗███████╗
 ██╔══██╗██╔══██╗╚██╗ ██╔╝████╗  ██║██╔════╝
 ██████╔╝███████║ ╚████╔╝ ██╔██╗ ██║█████╗
 ██╔═══╝ ██╔══██║  ╚██╔╝  ██║╚██╗██║██╔══╝
 ██║     ██║  ██║   ██║   ██║ ╚████║███████╗
 ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝
{RESET}
{CIANO}  Sistema de Monitoramento de Tempestades Solares{RESET}
{MAGENTA}  Powered by Dados Espaciais — FIAP 2026{RESET}
""")

# -------------------------------------------------------
# TIPOS DE EVENTO VÁLIDOS
# -------------------------------------------------------
tipos_validos = [
    "tempestade solar",
    "ejeção de massa coronal",
    "flare solar",
    "vento solar",
    "partículas energéticas solares"
]

# -------------------------------------------------------
# LISTAS DE ARMAZENAMENTO
# -------------------------------------------------------
tipos_eventos  = []
paises         = []
regioes        = []
cidades        = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []

# -------------------------------------------------------
# 1. ENTRADA DE DADOS
# -------------------------------------------------------
print(f"{CIANO}{'='*50}{RESET}")
print(f"{NEGRITO}{BRANCO}  REGISTRO DE EVENTOS SOLARES{RESET}")
print(f"{CIANO}{'='*50}{RESET}\n")

# Solicita a quantidade de eventos
while True:
    try:
        qt_eventos = int(input(f"{CIANO}Insira a quantidade de eventos: {RESET}"))
        if qt_eventos > 0:
            break
        else:
            print(f"{VERMELHO}  ⚠ A quantidade deve ser maior que zero.{RESET}")
    except ValueError:
        print(f"{VERMELHO}  ⚠ Valor inválido. Digite um número inteiro.{RESET}")

# Exibe tipos válidos antes de iniciar
print(f"\n{MAGENTA}Tipos de evento disponíveis:{RESET}")
for i, t in enumerate(tipos_validos, 1):
    print(f"  {AMARELO}{i}.{RESET} {t}")

# Coleta os dados de cada evento
for i in range(qt_eventos):
    print(f"\n{NEGRITO}{AMARELO}--- Evento {i + 1} ---{RESET}")

    # Tipo de evento — aceita número (1-5) ou nome completo
    while True:
        entrada = input(f"{AZUL}Tipo (número ou nome): {RESET}").strip().lower()
        if entrada.isdigit() and 1 <= int(entrada) <= len(tipos_validos):
            tipo = tipos_validos[int(entrada) - 1]
            tipos_eventos.append(tipo)
            break
        elif entrada in tipos_validos:
            tipos_eventos.append(entrada)
            break
        else:
            print(f"{VERMELHO}  ⚠ Tipo inválido. Digite o número (1-5) ou o nome completo.{RESET}")

    # País afetado
    pais = input(f"{AZUL}País: {RESET}").strip()
    paises.append(pais)

    # Região
    regiao = input(f"{AZUL}Região: {RESET}").strip()
    regioes.append(regiao)

    # Base de monitoramento / cidade
    cidade = input(f"{AZUL}Cidade: {RESET}").strip()
    cidades.append(cidade)

    # Área de impacto geomagnético
    while True:
        try:
            area = float(input(f"{AZUL}Área: {RESET}"))
            if area > 0:
                areas_afetadas.append(area)
                break
            else:
                print(f"{VERMELHO}  ⚠ A área deve ser maior que zero.{RESET}")
        except ValueError:
            print(f"{VERMELHO}  ⚠ Valor inválido. Digite um número.{RESET}")

    # Intensidade geomagnética (1–10)
    print(f"{MAGENTA}  Escala: 1 = fraco  |  5 = moderado  |  10 = extremo (Carrington){RESET}")
    while True:
        try:
            intensidade = int(input(f"{AZUL}Intensidade: {RESET}"))
            if 1 <= intensidade <= 10:
                intensidades.append(intensidade)
                break
            else:
                print(f"{VERMELHO}  ⚠ A intensidade deve estar entre 1 e 10.{RESET}")
        except ValueError:
            print(f"{VERMELHO}  ⚠ Valor inválido. Digite um número inteiro.{RESET}")

    # Número de ocorrências detectadas
    while True:
        try:
            oc = int(input(f"{AZUL}Ocorrências: {RESET}"))
            if oc >= 0:
                ocorrencias.append(oc)
                break
            else:
                print(f"{VERMELHO}  ⚠ O número de ocorrências não pode ser negativo.{RESET}")
        except ValueError:
            print(f"{VERMELHO}  ⚠ Valor inválido. Digite um número inteiro.{RESET}")

# -------------------------------------------------------
# 3. ANÁLISE DE DADOS
# -------------------------------------------------------

# a) Total de eventos registrados
total_eventos = len(tipos_eventos)

# b) Soma total das áreas afetadas
soma_areas = sum(areas_afetadas)

# c) Média das intensidades
media_intensidade = sum(intensidades) / total_eventos

# d) Evento com maior área afetada
idx_maior_area = areas_afetadas.index(max(areas_afetadas))

# e) Região com maior número de ocorrências
idx_maior_oc = ocorrencias.index(max(ocorrencias))
regiao_mais_oc = regioes[idx_maior_oc]

# f) Densidade média (ocorrências ÷ área)
densidade_media = sum(ocorrencias) / soma_areas

# g) Quantidade de eventos acima da média de intensidade
eventos_acima_media = 0
for intens in intensidades:
    if intens > media_intensidade:
        eventos_acima_media += 1

# h) Evento mais crítico (maior intensidade; empate: maior área)
idx_critico = 0
for i in range(1, total_eventos):
    if intensidades[i] > intensidades[idx_critico]:
        idx_critico = i
    elif intensidades[i] == intensidades[idx_critico]:
        if areas_afetadas[i] > areas_afetadas[idx_critico]:
            idx_critico = i

# -------------------------------------------------------
# 4. RELATÓRIO DE RESULTADOS
# -------------------------------------------------------

print(f"\n{VERDE}{NEGRITO}========================================{RESET}")
print(f"{VERDE}{NEGRITO}RELATÓRIO DE ANÁLISE{RESET}")
print(f"{VERDE}{NEGRITO}========================================{RESET}")
print(f"{BRANCO}Total de eventos registrados: {AMARELO}{total_eventos}{RESET}")
print(f"{VERDE}----------------------------------------{RESET}")
print(f"{NEGRITO}{CIANO}Resumo Geral{RESET}")
print(f"{VERDE}----------------------------------------{RESET}")
print(f"{BRANCO}Área total afetada: {AMARELO}{soma_areas:.0f} km²{RESET}")
print(f"{BRANCO}Média de intensidade: {AMARELO}{media_intensidade:.1f}{RESET}")
print(f"{VERDE}----------------------------------------{RESET}")
print(f"{NEGRITO}{CIANO}Análises{RESET}")
print(f"{VERDE}----------------------------------------{RESET}")
print(f"{BRANCO}Região com maior número de ocorrências: {AMARELO}{regiao_mais_oc}{RESET}")
print(f"{BRANCO}Quantidade de eventos acima da média de intensidade: {AMARELO}{eventos_acima_media}{RESET}")
print(f"{BRANCO}Densidade média de ocorrências: {AMARELO}{densidade_media:.2f} ocorrências/km²{RESET}")
print(f"{VERDE}----------------------------------------{RESET}")
print(f"{NEGRITO}{VERMELHO}Evento Mais Crítico{RESET}")
print(f"{VERDE}----------------------------------------{RESET}")
print(f"{BRANCO}Tipo: {VERMELHO}{tipos_eventos[idx_critico]}{RESET}")
print(f"{BRANCO}Local: {VERMELHO}{cidades[idx_critico]}, {regioes[idx_critico]}, {paises[idx_critico]}{RESET}")
print(f"{BRANCO}Intensidade: {VERMELHO}{intensidades[idx_critico]}{RESET}")
print(f"{BRANCO}Área afetada: {VERMELHO}{areas_afetadas[idx_critico]:.0f} km²{RESET}")
print(f"{VERDE}{NEGRITO}========================================{RESET}")
print(f"{BRANCO}Total de desastres registrados: {AMARELO}{total_eventos}{RESET}")