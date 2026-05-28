# =============================================================
# FIAP - Data Science | Data Driven Application & Data Science
# Professora: Patrícia Angelini
# Avaliação: 2026 1ª Global Solutions
# Integrantes (ordem alfabética):
#   - Luana Ramos Rabelo RM 570351
#   - Lucas Luna Pimentel RM 573538
#   - Mariana Ishikawa Mota RM 572886
# =============================================================

# -------------------------------------------------------
# LISTAS DE ARMAZENAMENTO
# -------------------------------------------------------
tipos_eventos = []
paises        = []
regioes       = []
cidades       = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []

# -------------------------------------------------------
# 1. ENTRADA DE DADOS
# -------------------------------------------------------

# Solicita a quantidade de eventos
while True:
    try:
        qt_eventos = int(input("Insira a quantidade de eventos: "))
        if qt_eventos > 0:
            break
        else:
            print("A quantidade deve ser maior que zero.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

# Aqui coletamos os dados de cada evento
for i in range(qt_eventos):
    print(f"\n--- Evento {i + 1} ---")

    # Tipo de evento
    tipo = input("Tipo: ")
    tipos_eventos.append(tipo)

    # País do evento
    pais = input("País: ")
    paises.append(pais)

    # Região do evento 
    regiao = input("Região: ")
    regioes.append(regiao)

    # Cidade do evento 
    cidade = input("Cidade: ")
    cidades.append(cidade)

    # Área afetada — deve ser maior que zero
    while True:
        try:
            area = float(input("Área (km²): "))
            if area > 0:
                areas_afetadas.append(area)
                break
            else:
                print("A área deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número.")

    # Intensidade — deve estar entre 1 e 10
    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if 1 <= intensidade <= 10:
                intensidades.append(intensidade)
                break
            else:
                print("A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    # Número de ocorrências
    while True:
        try:
            oc = int(input("Ocorrências: "))
            if oc >= 0:
                ocorrencias.append(oc)
                break
            else:
                print("O número de ocorrências não pode ser negativo.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

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

# h) Evento mais crítico (maior intensidade; em empate, maior área)
idx_critico = 0
for i in range(1, total_eventos):
    if intensidades[i] > intensidades[idx_critico]:
        idx_critico = i
    elif intensidades[i150] == intensidades[idx_critico]:
        if areas_afetadas[i] > areas_afetadas[idx_critico]:
            idx_critico = i

# -------------------------------------------------------
# 4. RELATÓRIO DE RESULTADOS
# -------------------------------------------------------

print("\n========================================")
print("         RELATÓRIO DE ANÁLISE          ")
print("========================================")
print(f"Total de eventos registrados: {total_eventos}")
print("----------------------------------------")
print("Resumo Geral")
print("----------------------------------------")
print(f"Área total afetada: {soma_areas:.0f} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")
print("----------------------------------------")
print("Análises")
print("----------------------------------------")
print(f"Região com maior número de ocorrências: {regiao_mais_oc}")
print(f"Quantidade de eventos acima da média de intensidade: {eventos_acima_media}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")
print("----------------------------------------")
print("Evento Mais Crítico")
print("----------------------------------------")
print(f"Tipo: {tipos_eventos[idx_critico]}")
print(f"Local: {cidades[idx_critico]}, {regioes[idx_critico]}, {paises[idx_critico]}")
print(f"Intensidade: {intensidades[idx_critico]}")
print(f"Área afetada: {areas_afetadas[idx_critico]:.0f} km²")
print("========================================")
print(f"Total de desastres registrados: {total_eventos}")