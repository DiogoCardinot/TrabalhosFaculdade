import math
import numpy as np

# Abre o arquivo e retorna uma lista com as linhas do arquivo.
def abrirInstancia(instancia):
    arquivo = open("./instancias/" + instancia + '.txt', "r")  # Abre o arquivo
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
    arquivo.close()  # Fecha o arquivo

    for linha in range(0, len(linhas)):
        linhas[linha] = linhas[linha].strip()  # Remove os espaços em branco e quebras de linha

    return linhas

def dadosInstancia(instancia):
    linhas = abrirInstancia(instancia)
    encontrado = False  # Variável para identificar se a linha desejada foi encontrada ou não
    i = 0  # Começando do índice 0

    while i < len(linhas) and not encontrado:
        if linhas[i][0:len(instancia)] == instancia:
            encontrado = True
        else:
            i = i + 1

    if encontrado and i + 1 < len(linhas):  # Verifica se a linha foi encontrada e se há espaço suficiente para acessar a próxima linha
        valor = int(linhas[i + 1].split()[1])  # Assume que o valor está na próxima linha após a linha encontrada
        return valor
    else:
        print(f"Linha com prefixo {instancia} não encontrada ou dados insuficientes.")
        return None  # Ou algum valor padrão ou um indicador de que a linha não foi encontrada


# Lê o arquivo e retorna uma matriz com a demanda de cada nó.
def demandaNo(instancia):
    linhas = abrirInstancia(instancia)
    i, j = 0, 0
    # A demanda de cada nó é fornecida na parte do arquivo entre onde está escrito 'demand section' e 'depot section'.
    for x in range(0, len(linhas)):
        if linhas[x] == "DEMAND_SECTION":
            i = x
        if linhas[x] == "DEPOT_SECTION":
            j = x

    demanda = np.zeros((j - i - 1, 2), dtype=int)
    for z in range(i + 1, j):
        colunas = linhas[z].split()
        demanda[z - i - 1, 0] = colunas[0]
        demanda[z - i - 1, 1] = colunas[1]
    return demanda

# Retorna a capacidade do veículo a partir do arquivo.
def capacidadeVeiculo(instancia):
    linhas = abrirInstancia(instancia)
    for linha in linhas:
        if 'CAPACITY :' in linha:
            capacidade = int(linha[10:len(linha)])
    return capacidade

# Retorna uma matriz com as coordenadas dos nós.
def coordenadasNos(instancia, dimensao):
    # Cria uma lista que conterá as coordenadas dos nós.
    coordenadas = np.zeros((dimensao, 3), dtype=int)
    linhas = abrirInstancia(instancia)
    # As coordenadas começam da 8ª linha.
    for i in range(7, 7 + dimensao):
        colunas = linhas[i].split()
        coordenadas[i - 7, 0] = colunas[0]
        coordenadas[i - 7, 1] = colunas[1]
        coordenadas[i - 7, 2] = colunas[2]
    return coordenadas

# Calcula a distância euclidiana entre dois pontos (x1, y1) e (x2, y2).
def distanciaEuclidiana(x1, y1, x2, y2):
    # Calcula as diferenças nas coordenadas x e y.
    (diff_x, diff_y) = (x1 - x2, y1 - y2)

    # Calcula a distância euclidiana usando o teorema de Pitágoras.
    distancia = math.sqrt(diff_x * diff_x + diff_y * diff_y) + 0.5

    # Arredonda para baixo para obter um valor inteiro.
    return math.floor(distancia)


# Retorna uma matriz de distâncias entre os nós.
def matrizDistancia(instancia, dimensao):
    # Abre o arquivo e lê as linhas.
    linhas = abrirInstancia(instancia)
    
    # Inicializa uma matriz de distâncias com zeros.
    dm = np.zeros((dimensao, dimensao), dtype=int)
    
    # Verifica se o arquivo contém distâncias explícitas ou coordenadas euclidianas.
    if "EXPLICIT" in linhas[4]:
        # Se o tipo de distância for "EXPLICIT", as distâncias são fornecidas no formato explicit low diagonal row.
        
        # Calcula o número total de elementos abaixo da diagonal principal na matriz de distâncias.
        n = math.floor((dimensao * (dimensao - 1)) / 2)
        
        # Inicializa um vetor para armazenar as distâncias.
        c = np.zeros((n,), dtype=int)
        
        # Calcula quantas linhas do arquivo contêm as distâncias (10 elementos por linha).
        b = math.floor(n / 10)
        
        # Lê as linhas do arquivo que contêm as distâncias.
        for x in range(9, 9 + b + 1):
            colunas = linhas[x].split()
            if isinstance(colunas, np.ndarray):
                # Se for um array numpy, converte para lista
                colunas.tolist()
            c = np.concatenate((c, colunas), axis=None)
        
        # Preenche a matriz de distâncias com os valores abaixo da diagonal principal.
        m = 0
        for i in range(0, dimensao):
            for j in range(0, dimensao):
                if i > j:
                    dm[i][j] = c[m]
                    m = m + 1
        # Imprime a matriz de distâncias e a retorna.
        print(dm)
        return dm

    elif "EUC_2D" in linhas[4]:
        # Se o tipo de distância for "EUC_2D", as distâncias são calculadas a partir das coordenadas euclidianas.
        
        # Obtém as coordenadas dos nós a partir da função coordenadasNos.
        coord = coordenadasNos(instancia, dimensao)
        
        # Preenche a matriz de distâncias com as distâncias euclidianas calculadas.
        for i in range(0, dimensao):
            for j in range(0, dimensao):
                if i > j:
                    dm[i][j] = distanciaEuclidiana(coord[i][1], coord[i][2], coord[j][1], coord[j][2])
        # Imprime a matriz de distâncias e a retorna.
        print(dm)
        return dm
    else:
        # Se o tipo de distância não for reconhecido, retorna None.
        return